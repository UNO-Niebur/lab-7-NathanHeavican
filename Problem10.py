#Problem10.py
#Name: Nathan Heavican
#Date: 3/7/26
#Assignment: Lab 7
#Purpose: Practice breaking large problems into smaller parts, writing reusable helper functions, composing functions together, and using incremental development to build correct solutions.

#Project Euler problem 10
#Approach: Check each number below 2,000,000 using isPrime; if the number is prime, add it to the running total.
#Runtime notes: This program takes about 5 seconds to run because each number below 2,000,000 is tested and is added if it is prime.

from NumberTests import isPrime

def main():
    total = 0
    for num in range(2, 2000000):
        if isPrime(num):
            total = total + num
    
    print(total)

if __name__ == '__main__':
    main()
