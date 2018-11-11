# Project_5
# Maxim Zolotykh

# "Все, о чем здесь идет речь, случилось в нашем уездном городишке, который в давние времена,
# быть может, и назывался городом, но теперь, когда в нем живет не более двух тысяч захудалых обывателей,
# кличется, по непонятной игре русского языка, — городищем,  что более подходило бы, конечно, какой-нибудь столице.
# Тинная речка, Лягушка, не спеша, пологим изгибом, течет по городу."
# И вот наш Егорушка замечает лягушек, и людей на соседнем берегу речки, подумал он, а смогут ли эти пресмыкающиеся
# заполонить всех прохожих, и смогут ли допрыгнуть, ведь маленькие совсем еще боятся народ, и только и могут, что громко
# квакать...
# Если вдруг Егорушка совсем не заметит лягушек или людей, то он отправится домой!
# Рассказать об этом Егорушка может только с помощью файла input.txt!
# Сначала Егорушка сообщает количество людей, которых он увидел на соседнем берегу. Затем количество лягушек, если он их
# заметил. И рассказывает были ли малыши. Далее он высчитывет расстояние от лягушек до людей. И по размеру лягушек
# определяет дальность их прыжка. Все данные Егорушка представляет в виде чисел. Создайте файл input.txt и представьте
# себя на месте Егорушки, проделав его действия.
file = input('Enter name of file: ')
while True:
    try:
        input_file = open (file,'r')
    except FileNotFoundError:
            print('File {} not faund.'.format(file))
            file_str = input('Enter name of file: ')
    else:
        with open('input.txt', 'r') as f_in:
            with open('output.txt', 'w') as f_out:
                information = ""
                for line in f_in:
                    information += line
                people, frogs, little, S, jump = information.split()
                try:
                    int(people) / int(frogs - little)
                except ZeroDivisionError:
                    print("Egor went home!", file=f_out)
                except ValueError:
                    print("Enter the number!", file=f_out)
                else:
                    if int(S) > int(jump):
                        print("Frogs doesn't jump!", file=f_out)
                    elif int(S) <= int(jump):
                        if int(frogs) >= int(people):
                            print("Frogs will be enough for everyone", file=f_out)
                        else:
                            print("Frogs enough for", int(people), "people")

