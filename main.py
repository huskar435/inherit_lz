from  inherit import Square
from  inherit import Quadrilateral  
def main():
    
    square = Square(color='black', border_width=4, filled=True, side_size_a=5)
    print(square.info())  
    square.draw()  


    quadrilateral = Quadrilateral(color='green', border_width=3, filled=False,  side_size_a=6, side_size_b=5, side_size_c=4, side_size_d=3)
    print(quadrilateral.info())  
    quadrilateral.draw()  
    
if __name__ == "__main__":
    main()

