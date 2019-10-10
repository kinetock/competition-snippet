
def Levenshtein(s1, s2):
    dist = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    for i in range(len(s1)+1):
        dist[i][0] = i
    for i in range(len(s2)+1):
        dist[0][i] = i
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            dist[i][j] = min(dist[i-1][j]+1, dist[i][j-1]+1, dist[i-1][j-1] + cost)
    
    # for i in range(len(s1)+1):
    #     print(dist[i])

s1 = input()
s2 = input()

print(Levenshtein(s1, s2))
