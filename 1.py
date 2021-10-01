print ("Введите имя студента")
name = input()
print ("Введите фамилию студента")
surname = input()
print ("Введите год рождения студента")
birthyear = int(input())
print (name, surname, birthyear,sep="_")
name,surname = surname, name
birthyear+=60
print (name,surname,birthyear,sep="_")