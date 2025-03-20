from  inherit import Square
from  inherit import Quadrilateral  
def main():
    
    square = Square(color='blue', border_width=2, filled=True, side_size_a=5)
    print(square.info())  
    square.draw()  


    quadrilateral = Quadrilateral(color='red', border_width=3, filled=False, 
                                   side_size_a=6, side_size_b=4, side_size_c=6, side_size_d=4)
    print(quadrilateral.info())  
    quadrilateral.draw()  
    
if __name__ == "__main__":
    main()
