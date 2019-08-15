from openpyscad import *
import math
import random
import sys

unit_size = 4

# start_degree = 0 is east
# Always think of your arc in ccw for the start_degree.
# Then add the is_clockwise boolean.
def generate_quarter_circle(radius, start_degree, circle_x, circle_y, is_clockwise=False):
  # use cosine/sine to generate x and y
  quarter_circle_degrees = 90
  degree_spacing = 5
  qc_points = []
  for degree in range(start_degree, start_degree + quarter_circle_degrees + degree_spacing, degree_spacing):
    qc_points.append(
      [math.cos(math.radians(degree)) * radius, 
       math.sin(math.radians(degree)) * radius])
  for qc_point in qc_points:
    qc_point[0] = qc_point[0] + circle_x
    qc_point[1] = qc_point[1] + circle_y
  if is_clockwise:
    qc_points.reverse()
  return qc_points

letterA_list = []
letterA_list += [[0,0]]
letterA_list += generate_quarter_circle(1, 90, 1, 3, True)
letterA_list += generate_quarter_circle(1, 0, 3, 3, True)
letterA_list += [[4,0], [3,0], [3,1.5], [1,1.5], [1,0]]
letterA_len = len(letterA_list)
letterA_list += generate_quarter_circle(0.5, 90, 1.5, 2.5, True)
letterA_list += generate_quarter_circle(0.5, 0, 2.5, 2.5, True)
letterA = Polygon(letterA_list, 
                  [list(range(letterA_len)), list(range(letterA_len, len(letterA_list)))])

letterB_list = []
letterB_list += [[0,0], [0,4]]
letterB_list += generate_quarter_circle(1, 0, 3, 3, True)
letterB_list += generate_quarter_circle(1, 270, 3, 3, True)
letterB_list += generate_quarter_circle(1, 0, 3, 1, True)
letterB_list += generate_quarter_circle(1, 270, 3, 1, True)
letterB_len = len(letterB_list)
letterB_list += [[1,2.75], [1,3.25]]
letterB_list += generate_quarter_circle(0.25, 0, 3, 3, True)
letterB_list += generate_quarter_circle(0.25, 270, 3, 3, True)
letterB_list += [[1,2.75]]
letterB_list += [[1,0.75], [1,1.25]]
letterB_list += generate_quarter_circle(0.25, 0, 3, 1, True)
letterB_list += generate_quarter_circle(0.25, 270, 3, 1, True)
letterB_list += [[1,0.75]]
letterB = Polygon(letterB_list,
                  [list(range(letterB_len)), list(range(letterB_len, len(letterB_list)))])

letterC_list = []
letterC_list += generate_quarter_circle(1, 90, 1, 3, True)
letterC_list += [[4,4], [4,3]]
letterC_list += generate_quarter_circle(1, 90, 2, 2)
letterC_list += generate_quarter_circle(1, 180, 2, 2)
letterC_list += [[4,1], [4,0]]
letterC_list += generate_quarter_circle(1, 180, 1, 1, True)
letterC = Polygon(letterC_list)

letterD_list = []
letterD_list += [[0,0], [0,4]]
letterD_list += generate_quarter_circle(1, 0, 3, 3, True)
letterD_list += generate_quarter_circle(1, 270, 3, 1, True)
letterD_len = len(letterD_list)
letterD_list += [[1,1], [1,3]]
letterD_list += generate_quarter_circle(0.5, 0, 2.5, 2.5, True)
letterD_list += generate_quarter_circle(0.5, 270, 2.5, 1.5, True)
letterD = Polygon(letterD_list, 
                  [list(range(letterD_len)), list(range(letterD_len, len(letterD_list)))])

letterE = Polygon([[0,0], [0,4], [4,4], [4,3],
                   [1,3], [1,2.5], [3,2.5], [3,1.5], 
                   [1,1.5], [1,1], [4,1], [4,0]])

letterF = Polygon([[0,0], [0,4], [4,4], [4,3], 
                   [1,3], [1,2.5], [3,2.5], [3,1.5], 
                   [1,1.5], [1,0]])

letterG_list = []
letterG_list += generate_quarter_circle(1, 90, 1, 3, True)
letterG_list += generate_quarter_circle(1, 0, 3, 3, True)
letterG_list += generate_quarter_circle(0.5, 90, 1.5, 2.5)
letterG_list += generate_quarter_circle(0.5, 180, 1.5, 1.5)
letterG_list += generate_quarter_circle(0.5, 270, 2, 1.5)
letterG_list += [[2,1.5], [2,2.5]]
letterG_list += generate_quarter_circle(1, 0, 3, 1.5, True)
letterG_list += [[4,0], [3,0]]
letterG_list += generate_quarter_circle(1, 270, 2, 1, True)
letterG_list += generate_quarter_circle(1, 180, 1, 1, True)
letterG = Polygon(letterG_list)

letterH = Polygon([[0,0], [0,4], [1,4], [1,2.5], 
                   [3,2.5], [3,4], [4,4], [4,0], 
                   [3,0], [3,1.5], [1,1.5], [1,0]])

letterI = Polygon([[0,0], [0,1], [1.5,1], [1.5,3], 
                   [0,3], [0,4], [4,4], [4,3], 
                   [2.5,3], [2.5,1], [4,1], [4,0]])

letterJ_list = [[0, 1.5]]
letterJ_list += generate_quarter_circle(0.5, 180, 1.5, 1.5)
letterJ_list += generate_quarter_circle(0.5, 270, 2.5, 1.5)
letterJ_list += [[3,4], [4,4]]
letterJ_list += generate_quarter_circle(1, 270, 3, 1, True)
letterJ_list += generate_quarter_circle(1, 180, 1, 1, True)
# Used in JSM to remove 2 manifold error
# letterJ_list[0][1] = letterJ_list[0][1] - 0.02
# letterJ_list[1][1] = letterJ_list[1][1] - 0.02
letterJ = Polygon(letterJ_list)

letterK = Polygon([[0,0], [0,4], [1,4], [1,3], 
                   [1.25,2.75], [2.5,4], [4,4], [2,2], 
                   [4,0], [2.5,0], [1,1.5], [1,0]])

letterL = Polygon([[0,0], [0,4], [1,4], [1,1], [4,1], [4,0]])

letterM = Polygon([[0,0], [0,4], [1.25,4], [2,2], 
                   [2.75,4], [4,4], [4,0], [3,0], 
                   [3,2], [2.5,0.5], [1.5,0.5], [1,2], 
                   [1,0]])

letterN = Polygon([[0,0], [0,4], [1.5,4], [3,1.5], 
                   [3,4], [4,4], [4,0], [2.5,0], 
                   [1,2.5], [1,0]])

letterO_list = []
letterO_list += generate_quarter_circle(1, 90, 1, 3, True)
letterO_list += generate_quarter_circle(1, 0, 3, 3, True)
letterO_list += generate_quarter_circle(1, 270, 3, 1, True)
letterO_list += generate_quarter_circle(1, 180, 1, 1, True)
letterO_len = len(letterO_list)
letterO_list += generate_quarter_circle(0.5, 90, 1.5, 2.5, True)
letterO_list += generate_quarter_circle(0.5, 0, 2.5, 2.5, True)
letterO_list += generate_quarter_circle(0.5, 270, 2.5, 1.5, True)
letterO_list += generate_quarter_circle(0.5, 180, 1.5, 1.5, True)
letterO = Polygon(letterO_list, 
                  [list(range(letterO_len)), list(range(letterO_len, len(letterO_list)))])

letterP_list = []
letterP_list += [[0,0], [0,4]]
letterP_list += generate_quarter_circle(1, 0, 3, 3, True)
letterP_list += generate_quarter_circle(1, 270, 3, 2.5, True)
letterP_list += [[1,1.5], [1,0]]
letterP_len = len(letterP_list)
letterP_list += [[1,2.5], [1,3]]
letterP_list += generate_quarter_circle(0.25, 0, 2.75, 2.75, True)
letterP_list += generate_quarter_circle(0.25, 270, 2.75, 2.75, True)
letterP = Polygon(letterP_list, 
                  [list(range(letterP_len)), list(range(letterP_len, len(letterP_list)))])

letterQ_list = []
letterQ_list += generate_quarter_circle(1, 90, 1, 3, True)
letterQ_list += generate_quarter_circle(1, 0, 3, 3, True)
letterQ_list += [[4,0], [3,0]]
letterQ_list += generate_quarter_circle(0.5, 270, 2.5, 0.5, True)
letterQ_list += generate_quarter_circle(1, 180, 1, 1, True)
letterQ_len = len(letterQ_list)
letterQ_list += generate_quarter_circle(0.5, 90, 1.5, 2.5, True)
letterQ_list += generate_quarter_circle(0.5, 0, 2.5, 2.5, True)
letterQ_list += generate_quarter_circle(0.5, 270, 2.5, 1.5, True)
letterQ_list += generate_quarter_circle(0.5, 180, 1.5, 1.5, True)
letterQ = Polygon(letterQ_list, 
                  [list(range(letterQ_len)), list(range(letterQ_len, len(letterQ_list)))])

letterR_list = []
letterR_list += [[0,0], [0,4]]
letterR_list += generate_quarter_circle(1, 0, 3, 3, True)
letterR_list += generate_quarter_circle(1, 270, 3, 2.5, True)
letterR_list += [[2.5,1.5], [4,0], [2.5,0], [1,1.5], [1,0]]
letterR_len = len(letterR_list)
letterR_list += [[1,2.5], [1,3]]
letterR_list += generate_quarter_circle(0.25, 0, 2.75, 2.75, True)
letterR_list += generate_quarter_circle(0.25, 270, 2.75, 2.75, True)
letterR = Polygon(letterR_list, 
                  [list(range(letterR_len)), list(range(letterR_len, len(letterR_list)))])

letterS_list = []
letterS_list += [[0,0], [0,1]]
letterS_list += generate_quarter_circle(0.25, 270, 2.75, 1.25)
letterS_list += generate_quarter_circle(0.25, 0, 2.75, 1.25)
letterS_list += generate_quarter_circle(1, 180, 1, 2.5, True)
letterS_list += generate_quarter_circle(1, 90, 1, 3, True)
letterS_list += [[4,4], [4,3]]
letterS_list += generate_quarter_circle(0.25, 90, 1.25, 2.75)
letterS_list += generate_quarter_circle(0.25, 180, 1.25, 2.75)
letterS_list += generate_quarter_circle(1, 0, 3, 1.5, True)
letterS_list += generate_quarter_circle(1, 270, 3, 1, True)
letterS = Polygon(letterS_list)

letterT = Polygon([[0,4], [4,4], [4,3], [2.5,3], 
                  [2.5,0], [1.5,0], [1.5,3], [0,3]])

letterU_list = []
letterU_list += [[0,4], [1,4]]
letterU_list += generate_quarter_circle(0.5, 180, 1.5, 1.5)
letterU_list += generate_quarter_circle(0.5, 270, 2.5, 1.5)
letterU_list += [[3,4], [4,4]]
letterU_list += generate_quarter_circle(1, 270, 3, 1, True)
letterU_list += generate_quarter_circle(1, 180, 1, 1, True)
letterU = Polygon(letterU_list)

letterV = Polygon([[0,4], [1,4], [2,2], [3,4], [4,4], [2.5,0], [1.5,0]])

letterW = Polygon([[0,4], [1.25,4], [1.5,2], [2,2.5], 
                   [2.5,2], [2.75,4], [4,4], [3.5,0], 
                   [2.5,0], [2,1], [1.5,0], [0.5,0]])

letterX = Polygon([[0,0], [1,2], [0,4], [1.25,4], 
                   [2,2.5], [2.75,4], [4,4], [3,2], 
                   [4,0], [2.75,0], [2,1.5], [1.25,0]])

letterY = Polygon([[0,4], [1.25,4], [2,3], [2.75,4], 
                   [4,4], [2.5,2], [2.5,0], [1.5,0],
                   [1.5,2]])

letterZ = Polygon([[0,0], [0,1], [2.5,3], [0,3], 
                   [0,4], [4,4], [4,3], [1.5,1], 
                   [4,1], [4,0]])

letters = {'A': letterA, 'B': letterB, 'C': letterC, 'D': letterD,
           'E': letterE, 'F': letterF, 'G': letterG, 'H': letterH,
           'I': letterI, 'J': letterJ, 'K': letterK, 'L': letterL,
           'M': letterM, 'N': letterN, 'O': letterO, 'P': letterP,
           'Q': letterQ, 'R': letterR, 'S': letterS, 'T': letterT,
           'U': letterU, 'V': letterV, 'W': letterW, 'X': letterX,
           'Y': letterY, 'Z': letterZ}

# Rotation functions in the same plane.
def r0(pgon):
  return pgon

def r90(pgon):
  return pgon.rotate([0,0,90]).translate([unit_size,0,0])

def r180(pgon):
  return pgon.rotate([0,0,180]).translate([unit_size,unit_size,0])

def r270(pgon):
  return pgon.rotate([0,0,270]).translate([0,unit_size,0])

# Rotation function in the same plane.
# The num argument indicates the number of times this is rotated by 90 degrees.
# To rotate something 180 degrees, set num=2.
def rotate2d(pgon, num=1):
  for i in range(num):
    pgon = pgon.rotate([0,0,90]).translate([unit_size,0,0])
  return pgon

# Functions to rotate the polyhedron to another plane.
def xy(phedron):
  return phedron

def yz(phedron):
  return phedron.rotate([90,0,90])

def zx(phedron):
  return phedron.rotate([270,180,0]).translate([unit_size,0,0])

# Takes 3 letters and returns the boolean
def manualGEBify(letter1, letter2, letter3):
  return (xy(r0(letters[letter1]).linear_extrude(unit_size)) &
          yz(r0(letters[letter2]).linear_extrude(unit_size)) &
          zx(r0(letters[letter3]).linear_extrude(unit_size)))

# Takes 3 letters, randomizes the orientations
# Returns the intersection of the letters and the orientations as an array.
def GEBify(letter1, letter2, letter3):
  orientations = [r0, r90, r180, r270]
  numOrientations = len(orientations)
  pickOrientations = [random.randrange(numOrientations), random.randrange(numOrientations), random.randrange(numOrientations)]
  return [
          (xy(orientations[pickOrientations[0]](letters[letter1]).linear_extrude(unit_size)) &
          yz(orientations[pickOrientations[1]](letters[letter2]).linear_extrude(unit_size)) &
          zx(orientations[pickOrientations[2]](letters[letter3]).linear_extrude(unit_size))) , pickOrientations ]

#manualGEBify('J', 'S', 'M').write('geb.scad') # 0, 90, 0
#manualGEBify('J', 'S', 'A').write('geb.scad') # 0, 90, 0
#manualGEBify('P', 'S', 'E').write('geb.scad') # 180, 90, 0
#manualGEBify('B', 'G', 'E').write('geb.scad') # 0, 0, 180
#manualGEBify('B', 'G', 'E').write('geb.scad') # 90, 0, 0

# Returns 3 random letters of the alphabet
def randomPickThree():
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabetLen = len(alphabet)
  return alphabet[random.randrange(alphabetLen)] + alphabet[random.randrange(alphabetLen)] + alphabet[random.randrange(alphabetLen)]

# Takes a string. If the string is longer than 3 letters,
# use only the first 3. If it's less than 3, randomly pick some
# to fill the rest.
# Shuffle and uppercase before returning.
def parseAndShuffleLetters(input):
  if len(input) < 3:
    input = input + randomPickThree()
	
  threeLetters = list(input[:3].upper())
  random.shuffle(threeLetters)
  return ''.join(threeLetters)


if __name__ == '__main__':
  input = parseAndShuffleLetters('ADA')
  if len(sys.argv) > 1:
    input = parseAndShuffleLetters(str(sys.argv[1]))

#gebbed = GEBify(input[0], input[1], input[2])
#gebbed[0].write('geb.scad')
#print(gebbed[1])
