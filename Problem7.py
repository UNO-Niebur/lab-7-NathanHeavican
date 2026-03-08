#Problem7.py
#Name: Nathan Heavican
#Date: 3/7/26
#Assignment: Lab 7
#Purpose: Practice breaking large problems into smaller parts, writing reusable helper functions, composing functions together, and using incremental development to build correct solutions.

#Project Euler problem 7
#Approach: Check numbers one at a time and use isPrime to see if they are prime, and keep checking until the 10001st prime number is found.
#Runtime notes: This program takes less than a second to get the answer because isPrime only checks up to the square root of the number.

from NumberTests import isPrime

def main():
    count = 0
    num = 1
    while count < 10001:
        num = num + 1
        if isPrime(num):
            count = count + 1

    print(num)

if __name__ == '__main__':
  main()
