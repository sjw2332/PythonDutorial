#애완동물을 소개해주세요

animal = "고양이"
color = "흰색"
age = 2
is_adult = age >= 3

print("우리집" +animal+ "는" + color + "입니다")
# print(animal+ "는" +str(age)+ "살이고 혼자 잘놉니다")
print(animal, "는" ,age, "살이고 혼자 잘놉니다")   # , 를 사용하면 str 타입으로 안바꿔줘도 되지만 space가 하나 들어감.
print( animal+ "는 어른일까요? " + str(is_adult))