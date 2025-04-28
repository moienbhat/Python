try:
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print("Divided by Zero!")
except ValueError:
    print("Invalid input!")