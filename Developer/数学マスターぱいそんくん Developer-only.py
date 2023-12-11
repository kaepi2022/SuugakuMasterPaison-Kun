print("計算マスター！ぱいそんくん")
print("")

while True:
 
 UN = input("小数まで計算するには,Yes少数を含まないものは,Noを入力してください。>>>>　")
 Math = input("+、-、×、÷、のどれかを入力してください。") #Math Type
 One = input("1桁目を入力してください。")
 Two = input("2桁目を入力してください。")

 anw = -9999999999

 # if Yes
 if UN == "Yes":
  if Math == "+":
   anw = float(One) + float(Two) 
  elif Math == "-":
   anw = float(One) - float(Two)
  elif Math == "*" or Math == "×":
   anw =float(One) * float(Two)
  elif Math == "/" or Math == "÷":
   anw =float(One) / float(Two)
 else:
  print("正しい記号を入力してください。")

# if No
  
 if UN == "No":
  if Math == "+":
   anw = int(One) + int(Two) 
  elif Math == "-":
   anw = int(One) - int(Two)
  elif Math == "*" or Math == "×":
   anw = int(One) * int(Two)
  elif Math == "/" or Math == "÷":
   anw = int(One) / int(Two)
 else:
  print("正しい記号を入力してください。")  

 if not anw == -9999999999:
  print("答えは", str(anw), "です。")
  print("")