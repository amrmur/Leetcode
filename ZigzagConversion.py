class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        letters = []
        n = len(s)
        index = 0
        while(index < n):
            letters.append(s[index])
            index += (numRows - 1) * 2
        for j in range(1, numRows - 1):
            index = j
            while(True):
                if(index >= n):
                    break
                letters.append(s[index])
                if(index + ((numRows - 1 - j) * 2) >= n):
                    break
                letters.append(s[index + ((numRows - 1 - j) * 2)])
                index += (numRows - 1) * 2
        index = numRows - 1
        while(index < n):
            letters.append(s[index])
            index += (numRows - 1) * 2
        return "".join(letters)

        # Time Complexity: O(n)
        # Space Complexity: O(n)
