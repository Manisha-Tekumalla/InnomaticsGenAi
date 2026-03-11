marks=[45,78,90,33,60]
p=0
fail=0
for i in marks:
    if i>=50:
        p+=1
    else:
        fail+=1
print("No of students passed:",p)
print("No of students failed:",fail)

