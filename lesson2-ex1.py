import csv


def get_data(filestoread):
    n = 0
    for eachfile in filestoread:
        with open(eachfile, encoding='utf-8') as fileiread:

            for mystring in fileiread:
                mystring = mystring.strip()
                if n == 0:
                    os_prod_list.append(mystring)
                    print(mystring)
                if n == 1:
                    os_name_list.append(mystring)
                    print(mystring)
                if n == 2:
                    os_code_list.append(mystring)
                    print(mystring)
                if n == 3:
                    os_type_list.append(mystring)
                    print(mystring)
        n = n+1
    return 0
def write_to_csv(filetowrite):
    get_data(columnfilesarray)
    with open(filetowrite, 'w') as f_n:
        f_n_writer = csv.writer(f_n, delimiter=',')
        n = 0
        for eachID in os_code_list:
            row = []
            row.append(os_prod_list[n])
            row.append(os_name_list[n])
            row.append(os_code_list[n])
            row.append(os_type_list[n])
            n = n + 1
            print(row)
            f_n_writer.writerow(row)
            print(n)
    return 0

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

columnfilesarray = ['info_1.txt', 'info_2.txt', 'info_3.txt', 'info_4.txt']
write_to_csv('test.csv')
print(len(os_type_list))