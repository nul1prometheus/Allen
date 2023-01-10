import os
import dbm
import pickle
import shelve
import wc
import anagram_sets
import hashlib

# from __future__ import print_function, division
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
#
# def walk(dirname):
#     for name in os.listdir(dirname):
#         path = os.path.join(dirname, name)
#         if os.path.isfile(path):
#             print(path)
#         else:
#             walk(path)
#
#
# # walk(os.getcwd())
#
# # try:
# #     fin = open("E:\\1.txt")
# # except:
# #     print('Что-то пошло не так.')
#
# db = dbm.open('captions', 'c')
# db['cl.png'] = 'Photo'
# # print(db['cl.png'])
# # for key in db:
# #     print(key, db[key])
# db.close()
# t = [1, 2, 3]
# s = pickle.dumps(t)
# print(s)
# t1 = pickle.loads(s)
# print(t1)
# print(t1 is t)
# d = shelve.open('1.1', 'c')
# with shelve.open('1.1') as states:
#     states['1'] = '1'
#     states['2'] = '2'
#
# with shelve.open('1.1') as states:
#     for key in states:
#         print(key, " - ", states[key])
#
# # city = shelve.open('1.1').keys()
# # print(city)
# with shelve.open('1.1') as states:
#     for city in states.keys():
#         print(city, end=" ")
# print()
# with shelve.open('1.1') as states:
#     for state in states.items():
#         print(state)

# filename = "D:/f12.txt"
# cmd = 'certutil -hashfile' + ' ' + filename
# fp = os.popen(cmd)
# res = fp.read()
# stat = fp.close()
# # print(res)
# wc.linecount('wc.py')


def sed(file1, exchangestr, samplestr):
    try:
        f2 = open("file2", "w")
    except:
        print('Smth wrong, check filename or smth')
    try:
        f1 = open(file1, "r")
    except:
        print('Smth wrong, check filename or smth')
    while True:
        line = f1.readline()
        if not line:
            break
        if line.strip() == samplestr:
            f2.write(exchangestr + '\n')
        else:
            f2.write(line)
    f1.close()
    f2.close()


file1 = 'file1'
# print(sed(file1, "fff", "asd"))

def store_anagrams(sometxtfile):
    return anagram_sets.all_anagrams(sometxtfile)


def read_anagrams(sometxtfile, someword):
    a = anagram_sets.all_anagrams(sometxtfile)
    try:
        b = anagram_sets.signature(someword)
        c = a[b]
    except:
        print('No such word')
        raise SystemExit()
    return c


# print(store_anagrams('words.txt'))
# print(read_anagrams('words.txt', 'asd'))

def obxodFile(path, level=1, d=[]):
    # print('Level=', level, 'Content:', os.listdir(path))
    try:
        for i in os.listdir(path):
            os.chdir(path)
            if (os.path.abspath(i) not in d) and os.path.isfile(i):
                d.append(os.path.abspath(i))
            if os.path.isdir(path + '\\' + i):
                    # print('Спускаемся', path + '\\' + i)
                obxodFile(path + '\\' + i, level + 1)
                    # print('Возвращаемся в', path)
    except:
        pass
    return d

pathsoffiles = obxodFile("""E:\\""")

def md5sumsofsmth(d):
    hashs = []
    repeats = []
    for i in d:
        with open(i) as file_to_check:
            # read contents of the file
            data = file_to_check.read()
            # pipe contents of the file through
            if hashlib.md5(data).hexdigest() not in hashs:
                hashs.append(hashlib.md5(data).hexdigest())
            else:
                repeats.append(i)
        #Словарь с повторами????

print(obxodFile("""E:\\"""))


