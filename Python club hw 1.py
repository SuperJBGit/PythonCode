numbers=input("The numbers seperated by commas: ")
numbers=list(numbers.split(", "))
for i in range (len(numbers)):
    numbers[i]=int(numbers[i])
sumed=sum(numbers)
print(sumed)
