def right_angled_triangle(n):
    for i in range(1, n+1):
        print('*' * i)

def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

def pyramid(n):
    for i in range(n):
        print(' ' * (n-i-1) + '*' * (2*i+1))

def inverted_pyramid(n):
    for i in range(n):
        print(' ' * i + '*' * (2*(n-i)-1))

def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

def repeated_number_triangle(n):
    for i in range(1, n+1):
        print((str(i) + ' ') * i)

def number_pyramid(n):
    for i in range(1, n+1):
        print(' ' * (n-i), end='')
        print(' '.join(str(j) for j in range(1, i+1)))

def floyd_triangle(n):
    num = 1
    for i in range(1, n+1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()

def alphabet_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65 + j), end=' ')
        print()

def repeated_alphabet_triangle(n):
    for i in range(n):
        print((chr(65+i) + ' ') * (i+1))

def diamond(n):
    for i in range(n):
        print(' ' * (n-i-1) + '*' * (2*i+1))
    for i in range(n-2, -1, -1):
        print(' ' * (n-i-1) + '*' * (2*i+1))

def hourglass(n):
    for i in range(n):
        print(' ' * i + '*' * (2*(n-i)-1))
    for i in range(1, n):
        print(' ' * (n-i-1) + '*' * (2*i+1))

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def factorial(x):
    return 1 if x == 0 else x * factorial(x-1)

def pascal_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        for j in range(i + 1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=' ')
        print()

# -------- Menu System --------
def main():
    while True:
        print("\nChoose a pattern to display:")
        print("1. Right-Angled Triangle")
        print("2. Inverted Right-Angled Triangle")
        print("3. Pyramid")
        print("4. Inverted Pyramid")
        print("5. Increasing Number Triangle")
        print("6. Repeated Number Triangle")
        print("7. Number Pyramid")
        print("8. Floyd's Triangle")
        print("9. Alphabet Triangle")
        print("10. Repeated Alphabet Triangle")
        print("11. Diamond")
        print("12. Hourglass")
        print("13. Hollow Square")
        print("14. Pascal’s Triangle")
        print("0. Exit")

        choice = int(input("\nEnter your choice: "))
        if choice == 0:
            print("Exiting. Goodbye!")
            break

        size = int(input("Enter size (recommended 5-10): "))

        if choice == 1:
            right_angled_triangle(size)
        elif choice == 2:
            inverted_right_triangle(size)
        elif choice == 3:
            pyramid(size)
        elif choice == 4:
            inverted_pyramid(size)
        elif choice == 5:
            number_triangle(size)
        elif choice == 6:
            repeated_number_triangle(size)
        elif choice == 7:
            number_pyramid(size)
        elif choice == 8:
            floyd_triangle(size)
        elif choice == 9:
            alphabet_triangle(size)
        elif choice == 10:
            repeated_alphabet_triangle(size)
        elif choice == 11:
            diamond(size)
        elif choice == 12:
            hourglass(size)
        elif choice == 13:
            hollow_square(size)
        elif choice == 14:
            pascal_triangle(size)
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
