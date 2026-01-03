try:
    x = int(input("Enter the number : "))
    ans = 10 / x
except  ZeroDivisionError:
    print(f"Divide by 0 is not allowed")
except:
    print("Invalid Input")
else:
    print(f"ans = {ans}")
finally:
    print("End of Program")