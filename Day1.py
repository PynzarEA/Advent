
def find_floor(stroka):
    sum = 0
    for symbol in list(stroka):
        if symbol == ('('):
            sum += 1
        if symbol == (')'):
            sum -= 1
    if sum == 0:
        return 0
    else:
        return sum + 1
def main():
    print(find_floor(input()))
if __name__ == '__main__':
    main()