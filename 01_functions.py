def perf (m):
    return ((m[0]+m[1]+m[2]+m[3])/400)*100



marks = [45,75,86,77]

per = perf (marks)


marks2 = [75,98,88,78]

per2 = (sum(marks2)/400)*100


print(per,per2)
