counter = 0
string = 'hello'
values = [0,2,4,6,8,10]
while counter != 10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    string = memory
    counter+=1
memory = ' world'
print(string + memory)
