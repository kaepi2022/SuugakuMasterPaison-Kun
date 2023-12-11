print("計算マスター！ぱいそんくん")
print("")

while True:
 
 Math = input("+、-、×、÷、のどれかを入力してください。") #Math Type
 One = input("1桁目を入力してください。")
 Two = input("2桁目を入力してください。")

 anw = -9999999999

 #Calculation Program
 if Math == "+":
  anw = float(One) + float(Two) 
 elif Math == "-":
  anw = float(One) - float(Two)
 elif Math == "*" or Math == "×":
  anw =float(One) * float(Two)
 elif Math == "/" or Math == "÷":
  anw =float(One) / float(Two)
 else:
  print("ちゃんと記号を入れろカス")
  
 if not anw == -9999999999:
  print("答えは", str(anw), " です。")
  print("")