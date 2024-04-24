print("1つ目の数値：", end='')
a = int(input())

print("2つ目の数値：", end='')
b = int(input())

try:
    print(a/b)
except:
    ZeroDivisionError
    print("０以外の数字を入れる事")

while True:
    print("1つ目の数値：", end='')
    a = input()

    print("2つ目の数値：", end='')
    b = input()

    if a == "end" or b == "end":
        print("終了します")
        break

    try:
        a = int(a)
        b = int(b)
    except:
        ValueError
        print("正しい値を入力してください")
        continue

    try:
        print(a/b, end="\n")
    except:
        ZeroDivisionError
        print("０以外の数字を入れる事")
