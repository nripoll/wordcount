happy = input("Enter a statement to word count: ")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

    
print("The word frecuency of your input is: ")
print(counts)
