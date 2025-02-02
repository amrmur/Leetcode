class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())

        left, right = 0, len(s) - 1
        while(left < right):
            if(s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

        # Time/Space Complexity: O(n)
        # Bottom solution is technically more efficient but I like this one more

        # start, end = 0, len(s) - 1
        # while(start < end):
        #     if(not s[start].isalnum()):
        #         end += 1
        #     elif(not s[end].isalnum()):
        #         start -= 1
        #     elif(s[start].lower() != s[end].lower()):
        #         return False
        #     start += 1
        #     end -= 1
        # return True

        # start = 0
        # end = len(s) - 1
        # while(start <= end):
        #     charStart = s[start]
        #     charEnd = s[end]

        #     if(ord(charStart) >= 65 and ord(charStart) <= 90):
        #         charStart = chr(ord(charStart) + 32)
        #     elif(not((ord(charStart) >= 48 and ord(charStart) <= 57) or(ord(charStart) >= 97 and ord(charStart) <= 122))):
        #         start += 1
        #         continue

        #     if(ord(charEnd) >= 65 and ord(charEnd) <= 90):
        #         charEnd = chr(ord(charEnd) + 32)
        #     elif(not((ord(charEnd) >= 48 and ord(charEnd) <= 57) or (ord(charEnd) >= 97 and ord(charEnd) <= 122))):
        #         end -= 1
        #         continue

        #     if(charStart != charEnd):
        #         return False
            
        #     start += 1
        #     end -= 1

        # return True
