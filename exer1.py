input1, input2, input3 = input().split()
if input1 == 'A':
    result = int(input2) + int(input3)
    print(result)
elif input1 == '%':
    result = int(input2) % int(input3)
    print(result)
elif input1 == 'S':
    result = int(input2) - int(input3)
    print(result)
elif input1 == '>':
    result = int(input2) > int(input3)
    if result == True:
         print("1")
    else:
         print("0")
elif input1 == '<':
    result = int(input2) < int(input3)
    if result == True:
         print("1")
    else:
         print("0")
else:
    print('Invalid operation!')
