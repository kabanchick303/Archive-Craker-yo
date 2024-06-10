import zipfile

def crack_password(password_list, archive):
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    archive.extractall(pwd=word)
                    print("пароль был найден на стороке", idx)
                    print("Пароль -", word.decode())
                    return True
                except:
                    print(word.decode(),"не подходит")
                    continue
    return False

password_list = "rockyou.txt"
archive = input("Введите название архива, добавленного в папку")

obj = zipfile.ZipFile(archive)

cnt = len(list(open(password_list, 'rb')))

crack_password(password_list, obj)

if crack_password(password_list, obj) == False:
    print("В файле", password_list, "Не найдено необходимого пароля")










