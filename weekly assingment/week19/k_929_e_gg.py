class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        rec = set()
        for i in emails:
            temp = i.split("@")
            temp[0]= ('').join(temp[0].split("."))
            if "+" in temp[0]: temp[0] = temp[0][:temp[0].index("+")]
            rec.add(('@').join(temp))
        return len(rec)
