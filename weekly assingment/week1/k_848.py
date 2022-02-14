class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        word = [ord(i)%97 for i in s]
        index = -1
        temp = shifts
        tempval = 0
        while index + len(temp) != -1:
            tempval += temp[index]%26
            temp[index] = tempval%26
            index -= 1

        return "".join([chr((word[i]+(temp[i]))%26+97) for i in range(len(word))])