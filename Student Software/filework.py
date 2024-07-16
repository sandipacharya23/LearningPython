## File Handling
# r- read, a- append(pahila ko data + new data lyauna help garxa), w- write, x-Create

#read file
f= open('binod.csv', 'r')
print(f.read())

# Write 
f= open('contact.csv','a')
f.write('\nbabina, 77987')
f.close()