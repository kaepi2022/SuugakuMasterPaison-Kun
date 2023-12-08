#Math Master Paison-Kun
def ask(): #関数
    temp = input("+,-,×(乗法),÷(除法)のどれかを入力してください")
    return temp

while True: #永遠に
    print("") #改行
    print("計算マスターぱいそんくん") # title bar
    one = input("1文字を入力してください。") #一文字目
    two = input("2文字を入力してください。") #二文字目

    temp = ask()

    ans = 0
    
    if temp == "+": #もし記号が+なら
        ans = int(one) + int(two)
    elif temp == "-":
        ans = int(one) - int(two)
    elif temp == "*" or temp == "×":
        ans = int(one) * int(two)
    elif temp == "/" or temp == "÷":
        ans = int(one) / int(two)
    else: #それ以外であれば
        print("有効な記号を入力してください")

    if not ans == 0:
        print("答えは" + str(ans) + "です")