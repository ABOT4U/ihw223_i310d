def compute_area_of_circle(radius):
	pi = 3.1415926
	area = pi * radius * radius
	return area

radius1 = 2
area1 = compute_area_of_circle(radius1)
print(f"The area of circle with radius {radius1} is: {area1}")

radius2 = 1
area2 = compute_area_of_circle(radius2)
print(f"The area of circle with radius {radius2} is: {area2}")
