def print_pattern(n):
    if n == 1:
        print("*")
        return

    print_pattern(n - 1)

    print("* " * n)


n = int(input("Enter a number: "))

print_pattern(n)