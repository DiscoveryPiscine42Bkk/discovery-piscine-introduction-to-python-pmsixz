try:
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))

    result = list(range(start, end + 1))
    print(result)

except ValueError:
    print("none")