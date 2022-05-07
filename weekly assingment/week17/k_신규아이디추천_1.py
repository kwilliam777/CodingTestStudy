def solution(new_id):
    id = ('').join([i for i in new_id.lower() if i.isalnum() or i=="." or i=="-" or i=="_"])
    while ".." in id: id = id.replace("..",".")
    if id[0]==".": id = id[1:]
    if len(id)==0: id = "a"
    if id[-1]==".": id = id[:-1]
    if len(id)==0: id = "a"
    if len(id)>=16:
        id = id[:15]
        if id[-1]==".": id = id[:-1]
    while len(id)<3: id+=id[-1]

    return id


# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st
