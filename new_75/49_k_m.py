class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = [[strs[0]]]
        record = [sorted(list(strs[0]))]
        for i in range(1,len(strs)):
            temp = sorted(list(strs[i]))
            if temp not in record:
                record.append(temp)
                result.append([strs[i]])
            else:
                for r in result:
                    if sorted(list(r[0])) == sorted(list(strs[i])):
                        r.append(strs[i])
                        break
        return result
        
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         grp = defaultdict(list)
#         for s in strs:
#             k = "".join(sorted(s))
#             grp[k].append(s)
#         s = grp.values()
#         return s
    
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         d=defaultdict(list)
#         for i in strs:
#             d[tuple(sorted(i))].append(i)
#         return [d[i] for i in d]
