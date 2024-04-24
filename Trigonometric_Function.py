import math

print("距離と高さから角度を求める")

print("距離：", end='')
kyori = input()  # 距離を入力

print("高さ：", end='')
takasa = input()  # 高さを入力

if kyori == "0":
    print("値が不正です")  # 0が入力された場合の処理
else:
    kyori = float(kyori)  # 距離を浮動小数点数に変換
    takasa = float(takasa)  # 高さを浮動小数点数に変換

    kyori = float(abs(kyori))  # 距離を絶対値に変換
    takasa = float(abs(takasa))  # 高さを絶対値に変換

    kakudo = math.asin(float(takasa/kyori))  # 逆関数から角度を算出

    kakudo = float(kakudo*(180/math.pi))  # 角度をラジアン(rad)から度(deg)に変換

    kakudo = round(kakudo, 1)  # 角度を四捨五入して少数第一位までの値とする

    print("角度：", end='')
    print(kakudo)
