# Ryan Lugo: RJL 10/12/21

x_point_one = int(input("What is the first X Coordinate?: "))
y_point_one = int(input("Whatis the first Y Coordinate?:"))

x_point_two = int(input("What is the second X Coordinate?: "))
y_point_two = int(input("What is the second Y Coordinate?: "))

distance_formula = ( ((x_point_two **2) - (x_point_one **2)) + ((y_point_two **2) - (y_point_one **2)) ) ** 0.5

print("This is the distance between the two points:",distance_formula)