user_input = str(input("Enter a Phase: "))
text = user_input.splict()
a = "  "
for i in text:
    a = a+str(i[0]).upper()
    print(a)
