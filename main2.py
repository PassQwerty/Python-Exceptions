def sum(*, number1: int, number2: int):  # Объявление функции sum() с получением двух именованных аргументов. 
    return number1 + number2             # Аргументы number1 и number2 должны быть целочисленными.
    


def test1():  # Объявление функции test1().
    newArray = [1, 2, 3, 4]  # Создание списка newArray с четырьмя элементами.
    try:  # Начало блока try-except. 
          # Здесь мы ожидаем возникновение ошибки при выполнении следующей строки.
        element = newArray[5]  # Получение пятого элемента списка, которого не существует, 
                               # и вызовет исключение IndexError.
        print(element)
    except:  # Обычное исключение без обработки.
        resultSum = sum(number1=newArray[1], number2=newArray[3])  # Вызов функции sum() с передачей в нее второго 
                                                                   # и четвертого элемента списка как именованных аргументов. 
                                                                   # Результат будет равен сумме 2 и 4.
        print(resultSum)  # Вывод результата выполнения функции на экран.


def test2():  # Объявление функции test2().
    newArray = [1, 2, 3, 4]  # Создание списка newArray с четырьмя элементами.
    try:  # Начало блока try-except.
          # Здесь мы ожидаем возникновение ошибки при выполнении следующих строк.
        element = newArray[5]  # IndexError
        element = rrr  # NameError
    except IndexError:  # Обработка исключения IndexError.
        print("Ошибка индекса")
    except NameError:  # Обработка исключения NameError.
        print("Ошибка имени")
    except Exception:  # Обработка любого другого исключения. 
                       # Если мы не уверены, какое именно исключение может возникнуть, 
                       # мы можем использовать этот общий блок для обработки любых ошибок.
        resultSum = sum(number1=newArray[1], number2=newArray[3])  # Вызов функции sum() с передачей в нее второго 
                                                                   # и четвертого элемента списка как именованных аргументов. 
                                                                   # Результат будет равен сумме 2 и 4.
        print(resultSum)
    finally:  # Блок finally. 
              # Он выполнится в любом случае, даже если исключение не возникнет.
              # Он используется, когда нужно освободить ресурсы или выполнить какие-то действия 
              # в любом случае после выполнения блока try-except.
        print("Проверка прошла")


def test3():  # Объявление функции test3().
    data = {1: "google", 2: "apple", 3: "amazon"}  # Создание словаря data.
    try:  # Начало блока try-except.
          # Здесь мы ожидаем возникновение ошибки при выполнении следующей строки.
        nameCompany = data[2]  # Получение значения словаря.
    except Exception:  # Обработка любого исключения. 
                       # Если мы не уверены, какое именно исключение может возникнуть, 
                       # мы можем использовать этот общий блок для обработки любых ошибок.
        nameCompany = "microsoft"  # Назначение значения по умолчанию в случае ошибки.
    else:  # Блок else выполняется, если в блоке try не было исключений.
        nameCompany = nameCompany.upper()  # Изменение регистра букв в названии компании.

    print(nameCompany)  # Вывод значения на экран.
    print("Проверка завершена")



if __name__ == '__main__':
    test1()
    # test2()
    # test3()
