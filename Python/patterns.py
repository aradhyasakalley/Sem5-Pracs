def pattern1(n):
    # Upper part of the pattern
    for i in range(1, n + 1):
        print(str(i) * i)

    # Lower part of the pattern
    for i in range(n - 1, 0, -1):
        print(str(i) * i)

pattern1(5)

def pattern2(n):
    start_char = ord('A')
    for i in range(n):
        char = chr(start_char+i)
        print(char*(i+1))
pattern2(5)

def pattern3(n):
    start_char = ord('A')
    for i in range(n):
        char = chr(start_char+i)
        print(char*(i+1))