#!/usr/bin/env python3
#Author: Liam Waterman
#Author ID: 123151235
#Date Created: 2025/01/24 


import sys

def main():
    # Assign default value to timer
    timer = 3 if len(sys.argv) < 2 else int(sys.argv[1])

    # While loop to count down the timer
    while timer > 0:
        print(timer)
        timer -= 1

    print("blast off!")

if __name__ == "__main__":
    main()
