import json
f = open("txt.txt", "r")

fn = open("txt2.json", "w")
# # print(f.readlines())
# bigline = ""
# with open("txt.txt", "r") as f:
#     line = f.read()
#     if line != "\n":
#         bigline += line
#         # for l in line:
#         #     if l != '\n':
#         #         bigline += l
bigline = """

По студентам 1 г.о.:
Главный менеджер - Кусаинова Алия Ериковна +7 727 357 43 36


fit_1course@kbtu.kz
a.kussainova@kbtu.kz


Менеджер - Есенбекқызы Ақбота +7 727 357 43 39 a.yessenbekkyzy@kbtu.kz

По студентам 2 г.о.
Главный менеджер
Ахметжан Дана Муратбекқызы +7 727 357 43 44 fit_2course@kbtu.kz
d.akhmetzhan@kbtu.kz

По студентам 3 г.о.:
Главный менеджер
Қайназар Мадина Нұратқызы +7 727 357 43 47 fit_3course@kbtu.kz
m.kainazar@kbtu.kz

Менеджер
Айтахун Толғанай Бауыржанқызы +7 727 357 43 49 t.aitakhun@kbtu.kz

По студентам 4,5–7 г.о:
Главный менеджер
Нұрсадықова Адия Ұланқызы +7 727 357 43 43 fit_4course@kbtu.kz
a.nursadykova@kbtu.kz

Менеджер - Ермакова Алтынай Кенжебекқызы +7 727 357 43 42 fit_5-7courses@kbtu.kz
a.yermakova@kbtu.kz
"""
# data = json.loads(bigline)
json.dump(f.read(), fn)

# fn.write(data)
# print(bigline.strip())
# fn.write(bigline.strip())
#     # print(line)
# print("goodbye")