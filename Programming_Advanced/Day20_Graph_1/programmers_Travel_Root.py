# from collections import deque
# def solution(tickets):
#     airport={}
#     for st, des in tickets:
#         if st in airport: airport[st].append(des)
#         else: airport[st]=[des]
#     for key, value in airport.items():
#         airport[key].sort()
#         airport[key]=deque(value)
#     start="ICN"
#     result=[start]
#     while airport:
#         start=airport[start].popleft()
#         result.append(start)
#         if start in airport:
#             if len(airport[start]):
#                 print(airport[start], start)
#                 print(airport)
#                 continue
#             return result
#         else:
#             print(airport)
#             return result
# from collections import deque


def solution(tickets):
    N = len(tickets)+1
    airport = {}
    for st, des in tickets:
        if st in airport:
            airport[st].append(des)
        else:
            airport[st] = [des]
    # for key, value in airport.items():
    #     airport[key].sort()
    #     airport[key] = deque(value)

    def f(airports, result, start):
        global re
        if len(result) == N:
            if not re:
                re = result
            else:
                re = min(re, result)
            return

        if start not in airports: return
        if len(airports[start])==0:return
        for idx, key in enumerate(airports[start]):
            airports[start].remove(key)
            f(airports, result + [key], key)
            airports[start].insert(idx,key)

    f(airport, ["ICN"], "ICN")

    return re
arr=input().split()
ticket=[]
for i in range(0,len(arr),2):
    ticket.append([arr[i],arr[i+1]])
re = ['z']*(len(ticket)+1)
r=solution(ticket)
print(r)
# ICN JFK HND IAD JFK HND
# ICN SFO ICN ATL SFO ATL ATL ICN ATL SFO