class Solution:
    def interpret(self, command: str) -> str:
        temp = command
        result = ""
        
        while len(temp) != 0:
            if temp[:1] == "G":
                result += "G"
                temp = temp[1:]
            if temp[:2] == "()":
                result += "o"
                temp = temp[2:]
            if temp[:4] == "(al)":
                result += "al"
                temp = temp[4:]

        return result
        