import math_lib as mathfunctions
import argparse



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='take input from terminal')    
    parser.add_argument('first_value', type=int, help='first integer to be added')    
    parser.add_argument('second_value', type=int, help='second integer to be added')
    
    args = parser.parse_args()
    a= args.first_value
    b= args.second_value
    
    answer1 = mathfunctions.add(a,b)
    answer2 = mathfunctions.div(answer1,3)

    print(answer1)
    print(answer2)