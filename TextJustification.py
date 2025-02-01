class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        index = 0
        n = len(words)
        while(index < n):
            # add 1st word on line
            space = maxWidth - len(words[index])
            numWords = 1

            # add more words if it can fit
            while(index + numWords < n and len(words[index + numWords]) + 1 <= space - numWords + 1):
                space -= len(words[index + numWords])
                numWords += 1

            line = []

            # add the first word
            line.append(words[index])

            if(numWords == 1 or index + numWords == n): # one word/last line is left-aligned
                for j in range(index + 1, index + numWords):
                    line.append(' ')
                    line.append(words[j])
                line.append(' ' * (space - numWords + 1))
            else: # left and right justiied
                # space per word and leftover space
                spw = space // (1 if numWords == 1 else numWords - 1)
                ls = space % (1 if numWords == 1 else numWords - 1)

                for j in range(index + 1, index + numWords):
                    line.append(' ' * (spw + (1 if ls > 0 else 0)))
                    ls -= 1
                    line.append(words[j])

            lines.append(''.join(line))
            index += numWords
        return lines
# Time Complexity: O(n)
# Space Complexity: O(n)
