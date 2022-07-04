"""#Using Slice
s="QuestGlobal"
print(s[::-1])"""

#Using While Loop
s="QuestGlobal"
s1=""
i=len(s)-1
while i>=0:
    s1=s1+s[i]
    i=i-1
print(s1)

#Using For Loop
"""s="QuestGlobal"
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")"""
