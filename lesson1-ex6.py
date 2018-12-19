import locale
def_encoding = locale.getpreferredencoding()
print(def_encoding)

myarray = ['сетевое программирование','сокет','декоратор']
myfile = open('test.txt', 'w')
for val in myarray:
    myfile.write(val+'\n')
myfile.close()
print(myfile)

#will rise an error, because in Windows 10 with Russian locale
#default encoding will be cp1251
with open('test.txt', encoding='utf-8') as fileiread:
#with open('test.txt', encoding='cp1251') as fileiread:
    for mystring in fileiread:
        print(mystring)