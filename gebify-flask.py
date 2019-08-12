from flask import Flask, request  
import subprocess
import time
import urllib.request
import urllib.parse

from geb import *

app = Flask(__name__)
 
@app.route('/', methods=['GET', 'POST'])
def gebifyFromTweet():
  filename = int(time.time())
  text = request.args.get('text')
  input = parseAndShuffleLetters(text)
  GEBify(input[0], input[1], input[2]).write(filename + '.scad')
  subprocess.run(['/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD',
                  filename + '.scad',
                  '--o',
                  filename + '.stl]'])
  params = urllib.parse.urlencode({'filename': filename + '.stl'})
  url = "localhost:3000/stl_ready" % params
  with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))

if __name__ == "__main__":
  gebifyFromTweet()
#  app.run(host="0.0.0.0", port="5000")