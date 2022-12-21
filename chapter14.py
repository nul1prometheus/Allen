import os
# fout = open('D:\pyfiles\output.txt', 'w')
# line1 = "Я ждал это время, и вот это время пришло,\n"
# fout.write(line1)
# line2 = "Те, кто молчал, перестали молчать.\n"
# fout.write(line2)
# x = 52
# fout.write(str(x))
# fout.close()
#
#
# camels = 45
# str1 = 'I have %d camels' % camels
# print(str1)
# print('In %g years I bought %d %s' % (3.5, 7, 'camels'))
# str2 = 'The sum of {0} and {1} is {2}'
# x = input('Введите 1 чило:')
# x = int(x)
# y = input('Введите 1 чило:')
# y = int(y)
# z = x+y
# print(str2.format(x, y, z))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk(os.getcwd())
