class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        temp = students
        count = 0
        while len(temp) != 0:
            if count > len(temp):
                break
            if temp[0] == sandwiches[0]:
                temp.pop(0)
                sandwiches.pop(0)
                count = 0
            else:
                temp.append(temp.pop(0))
                count += 1
        return len(temp)