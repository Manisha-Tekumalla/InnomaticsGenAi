names = [" Alice ", "bob", " CHARLIE "]
cleaned_names=[]
for name in names:
    cleaned_names.append(name.strip().lower())
print(cleaned_names)