class Solution:
    def intToRoman(self, num: int) -> str:
        words = []
        while(num >= 1000):
            words.append('M')
            num -= 1000

        if(num >= 900):
            words.append("CM")
            num -= 900
        elif(num >= 500):
            words.append('D')
            num -= 500
        elif(num >= 400):
            words.append("CD")
            num -= 400
        while(num >= 100):
            words.append('C')
            num -= 100
        
        if(num >= 90):
            words.append("XC")
            num -= 90
        elif(num >= 50):
            words.append('L')
            num -= 50
        elif(num >= 40):
            words.append("XL")
            num -= 40
        while(num >= 10):
            words.append('X')
            num -= 10
        
        if(num >= 9):
            words.append("IX")
            num -= 9
        elif(num >= 5):
            words.append('V')
            num -= 5
        elif(num >= 4):
            words.append("IV")
            num -= 4
        while(num >= 1):
            words.append('I')
            num -= 1

        return "".join(words)

        # TIME COMPLEXITY: O(1)
        # SPACE COMPLEXITY: O(1)
