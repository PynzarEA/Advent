
def find_floor(stroka):
    sum = 0
    for symbol in list(stroka):
        if symbol == ('('):
            sum += 1
        if symbol == (')'):
            sum -= 1
    return sum
def main():
    print(find_floor(input()))
if __name__ == '__main__':
    main()