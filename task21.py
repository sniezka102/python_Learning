
"""
Question 21 - Level 3
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
	UP 5
	DOWN 3
	LEFT 3
	RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after
a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
	UP 5
	DOWN 3
	LEFT 3
	RIGHT 2
Then, the output of the program should be:
	2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


def distanceCompute(position):
    startedPoint = [0,0]
    calc = round(math.sqrt((position[0] - startedPoint[0]**2)+(position[1]-startedPoint[1])**2)#wzór na obliczanie
                                                                                               # odległości punktu od środka
return calc
"""

import math
print("please write the robot steps, up, down, left, right, please separate them by the comma")

pointPosition = []
while True:
    userInput = input()
    pointPosition.append(userInput.split(","))
    if not userInput:
        break
movements = pointPosition[0]
movementPosition = {'UP' : movements[0],'DOWN' : movements[1], 'LEFT' : movements[2], 'RIGHT' : movements[3]}

startedPoint = [0,0]
step = [0,0]
for key in movementPosition:
    if key == 'UP':
        point = [0,movementPosition[key]]
        step[1] += int(point[1])
    elif key == 'DOWN':
        point = [0, movementPosition[key]]
        step[1] -= int(point[1])
    elif key == 'LEFT':
        point = [movementPosition[key],0]
        step[0] -= int(point[0])
    elif key == 'RIGHT':
        point = [movementPosition[key], 0]
        step[0] += int(point[0])
    else:
        pass

calculation = math.sqrt((step[0])**2 + (step[1])**2)
print(round(calculation))


"""
ogólnie miałam problem żeby zrozumieć treść zadania :(
w ostateczności stwierdziłam że chodzi aby zliczyć kroki i obliczyć ile przeszedł robocik w osi x i y 
hmm, najgorsze to załapać o co może chodzić w danym zadaniu ;(
"""