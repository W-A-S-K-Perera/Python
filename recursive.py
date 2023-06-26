def recursive_sequence(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sequence(n-1)

while True:
    num = int(input("Enter number: "))
    if num == -1:
        print("Output: Finished")
        break
    else:
        print("Output:", recursive_sequence(num))
