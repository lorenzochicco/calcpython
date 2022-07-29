cycle = "yes"
while True:
    result = float(0)
    n1 = (float(input("Insert a number: ")))
    operator = input("Insert one of the following operators: + - * / ** ")
    n2 = (float(input("Insert a number: ")))
    if cycle == "yes":
        if operator == "+":
            result = n1 + n2
            print(result)
        elif operator == "-":
            result = n1 - n2
            print(result)
        elif operator == "*":
            result = n1 * n2
            print(result)
        elif operator == "/":
            result = n1 / n2
            print(result)
        elif operator == "**":
            result = n1 ** n2
            print(result)
        cycle = input("Do you want to calculate one more time? Type 'yes' or 'no' ")
        cycle = cycle.lower()
        if cycle == "no":
            break


