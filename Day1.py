
def find_floor(stroka):
    for line in stroka.split('\n'):
        sum = 0
        for symbol in list(line):
            if symbol == ('('):
                sum += 1
            if symbol == (')'):
                sum -= 1
        print(sum)
def main():
    find_floor(input())
if __name__ == '__main__':
    main()