"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #9 - License Plate (licenseplate.py)


Author: Wonjun Lee

Difficulty Level: 5/10

Prompt: Jon was speeding on the highway with his RACECAR, and the highway camera has taken a picture 
of the RACECAR’s number plate. However, some characters on the plate are blurry. Please write a function 
that returns the number of possible combinations of the number plate. The number plate for his RACECAR
consists of 7 distinct characters, starting with 3 distinct alphabets and ending with 4 distinct numbers. 
The input will be passed as a string and any blurred characters will be written as ‘.’

Test Cases: 
Input: “ABC123.” ; Output: 7
Input: “.ON0123” ; Output: 24
Input: “.BC.234” ; Output: 168
"""

class Solution:
    def licensePlate(self,str):
        # type str: string
        # return: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        a = 0

        for i in range(3):
            if str[i] == '.':
                a += 1

        n = 0

        for i in range(3, 7):
            if str[i] == '.':
                n += 1

        result = 1

        if a == 1:
            result *= 24
        elif a == 2:
            result *= 25 * 24
        elif a == 3:
            result *= 26 * 24 * 25

        for i in range(7, 7 + n):
            result *= i
        
        return result


def main():
    string1 = input()
    tc1 = Solution()
    ans = tc1.licensePlate(string1)
    print(ans)

if __name__ == "__main__":
    main()