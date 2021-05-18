#Program header goes here

#ADD ANY NECESSARY IMPORT STATEMENTS HERE

import shape 
import circle 
import square
import triangle

#Define main function
def main():

    #CREATE A SHAPE: red, border (1), name: Generic Shape
    my_shape = shape.Shape( 1, 'generic shape')

    #CREATE A CIRCLE: blue, border (2), name: Circle
    my_circle = circle.Circle( 2, 'Carl the Cirle')
    #CREATE A SQUARE: yellow, border (3), name: Square
    my_square = square.Square( 3, 'Sanndy the Square')
    #CREATE A TRIANGLE: orange, border (4), name: Triangle
    my_triangle = triangle.Triangle( 4, 'Terry the Triangle')

    #ADD CODE TO SET THE APPROPRIATE ATTRIBUTES OF EACH SUBCLASS:
    #CIRCLE: RADIUS = 4
    my_circle.set_radius(4)
    #SQUARE: SIDE = 5
    my_square.set_side(5)
    #TRIANGLE: BASE = 4, HEIGHT = 10
    my_triangle.set_base(4)
    my_triangle.set_height(10)
    
    #ADD CODE TO PRINT THE VALUES OF EACH SHAPE, INCLUDING SHAPE
    print(my_shape)
    print(my_circle)
    print(my_triangle)
    print(my_square)

    #ADD CODE TO PRINT THE AREA OF THE CIRCLE, SQUARE, AND TRIANGLE
    circle_area = my_circle.calc_area()
    print(circle_area)
    square_area = my_square.calc_area()
    print(square_area)
    triangle_area = my_triangle.calc_area()
    print(triangle_area)


#Call main function
main()
