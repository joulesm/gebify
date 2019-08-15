from flask import Flask, request  
import subprocess
import time
import json

import urllib
import urllib2
#import urllib.request
#import urllib.parse

from geb import *

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def gebifyFromTweet():
  #multi_dict = request.args
  #for key in multi_dict:
  #  print 'key:' + multi_dict.get(key)
  #  print 'val:' + multi_dict.getlist(key)
  print request
  filename = str(int(time.time()))
  print "filename: " + filename
  print json.dumps(request.json)
  print "the tweet text is: " + request.json['gebtext']
  splittext = request.json['gebtext'].split(' ')
  final_word = None
  for word in splittext:
    if word.isalpha():
      final_word = word
      break
  if final_word == None:
    print 'no word to parse'
    return 'fail'
  
  print final_word 
  input = parseAndShuffleLetters(final_word)
  geb_response = GEBify(input[0], input[1], input[2])
  geb_response[0].write('scad/' + filename + '.scad')
  print geb_response[1]
  subprocess.call(['/usr/bin/openscad',
                  'scad/' + filename + '.scad',
                  '--o',
                  '/home/person/code/gebify/gebify-node/public/stl/' + filename + '.stl'])
  #params = urllib.parse.urlencode({'filename': filename + '.stl'})
  #url = "localhost:3002/stl_ready" % params
  #with urllib.request.urlopen(url) as f:
  #  print(f.read().decode('utf-8'))
  url = 'http://localhost:3002/stl_ready'
  values = {'filename': filename + '.stl', 
            'link': request.json['geblink'],
            'user': request.json['gebuser'] }
  #          'tweet': request.json['gebtweet'] }
  data = urllib.urlencode(values)
  response = urllib2.urlopen(url + '?' + data)
  res_content = response.read()
  print res_content
  return filename

if __name__ == "__main__":
  #gebifyFromTweet()
  app.run(host="0.0.0.0", port="3001")
