#!/usr/bin/env python3

"""
A script to demonstrate adding two numbers using a function in Python.
"""

import argparse

def add(a, b):
    """
    Returns the sum of a and b.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def main():
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="The first number")
    parser.add_argument("b", type=float, help="The second number")
    args = parser.parse_args()
    
    result = add(args.a, args.b)
    print(f"The sum of {args.a} and {args.b} is {result}")

if __name__ == "__main__":
    main()
