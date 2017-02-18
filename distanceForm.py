import sys
import math

def distance(x1, x2, y1, y2):
	dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
	return dist

def main():
	x1 = int(input("Enter x1: "))
	y1 = int(input("Enter y1: "))
	x2 = int(input("Enter x2: "))
	y2 = int(input("Enter y2: "))

	print("Distance between points: "distance(x1, x2, y1, y2))

main()