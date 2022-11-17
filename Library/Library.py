import os
from pandas import DataFrame, read_csv

status = True
#Menggunakan file csv untuk menyimpan data
#Membaca data dari csv lalu diubah ke bentuk list
#"*args" >> argument untuk mempersingkat parameter 
def current_book_data(*args):
    global current_data,list_data
    current_data = read_csv("data_library.csv")
    list_data = current_data.values.tolist()

    new_list = [args[0],args[1],args[2],args[3]]#Memasukkan item dari setiap parameter sesuai urutannya
    list_data.append(new_list)
    saved_data(list_data) #Memanggil prosedur saved data untuk menyimpan perubahan pada list

#Membuat data baru
def create_data_book():
    try :
        new_Title = input("Title of the book : ")
        new_Author = input("Author of the book : ")
        new_Publisher = input("Publisher of the book : ")
        new_ReleaseYear = int(input("Release date with YYYY format : "))
        print("Data berhasil ditambahkan!")
        current_book_data(new_Title, new_Author, new_Publisher, new_ReleaseYear)#Memanggil prosedur 
    except ValueError:
        print("Kesalahan input pada <ReleaseYear>")
        input("Enter untuk mengulang!")
        os.system("cls")
        create_data_book()


#Melihat semua isi data
def show_data_book():
    #Jika belum ada data maka akan me-return value "EmptyData"
    current_data = read_csv("data_library.csv")  
    list_data = current_data.values.tolist()
    if list_data == []:
        print("Data is Empty")
        return "EmptyData"
    else:
        print()
        print("-"*57)
        print("|{:^3}|{:^12}|{:^12}|{:^12}|{:^12}|".format("No","Title","Author","Publisher","ReleaseYear"))
        print("-"*57)
        for i in range(len(list_data)):
            print("|{:^3}|{:^12}|{:^12}|{:^12}|{:^12}|".format(i, 
            list_data[i][0], list_data[i][1], list_data[i][2], list_data[i][3]))
        print("-"*57)

#untuk mencari buku
def search_book():
    current_data = read_csv("data_library.csv")
    list_data = current_data.values.tolist()
    list_Title = current_data.Title.values.tolist()
    search_title = input("Title of the book : ")
    if search_title in list_Title:
        index = list_Title.index(search_title)#Mencari index buku yang dicari pada file csv
        print(f"There's a book with title [ {search_title} ] with index {index}\n")
        print("-"*57)
        print("|{:^3}|{:^12}|{:^12}|{:^12}|{:^12}|".format("No","Title","Author","Publisher","ReleaseYear"))
        print("-"*57)
        print("|{:^3}|{:^12}|{:^12}|{:^12}|{:^12}|".format(index, 
            list_data[index][0], list_data[index][1], list_data[index][2], list_data[index][3]))
        print("-"*57)
    else:
        print(f"We can't find book with title [ {search_title} ]  in our database")

#update data
def update_book():
    #Untuk cek apakah ada data atau tidak
    if show_data_book() == "EmptyData":
        print("Oow, You can't update data. Create at least 1 data")
    #Jika ada blok else akan dieksekusi
    else:
        current_data = read_csv("data_library.csv")
        list_data = current_data.values.tolist()
        try:
            choose = int(input("Select data you want to update : "))
            index = choose

            update_title = input("Input new title : ")
            update_author = input("Input new author : ")
            update_publisher = input("Input new publisher : ")
            update_releaseyear = int(input("Input new releaseyear : "))

            list_data[index] = [update_title, update_author,update_publisher, update_releaseyear]
            saved_data(list_data)
        #Jika blok program except di eksekusi akan memanggil prosedur update_book kembali untuk input ulang
        except IndexError:
            print("Oops! Input greater than index of list, please try again!")
            update_book()

# Untuk delete data berdasarkan index yang diinput
def delete_book():
    show_data_book()
    try:
        current_data = read_csv("data_library.csv")
        list_data = current_data.values.tolist()
        choose = int(input("select the data you want to delete => "))
        list_data.pop(choose)

        print("Data Successfully Deleted")

        saved_data(list_data)

    except IndexError:
        print("Input must be number!")
        delete_book()

#Menghapus data secara keseluruhan
def reset_data():
    current_data = read_csv("data_library.csv")
    list_data = current_data.values.tolist()
    list_data.clear()
    print("Reset Data Succesful")
    saved_data(list_data)

#Save data
#Semua perubahan yang dilakukan akan disave menggunakan prosedur ini, maka prosedur ini harus dipanggil terus
def saved_data(list_data):
    saved_data = DataFrame(list_data, columns=["Title", "Author", "Publisher", "ReleaseYear"])
    saved_data.to_csv("data_library.csv", index=False)

#Untuk pilihan menu
def menu():
    os.system('cls')
    print("="*12)
    print("What you want to do?")
    print("[1] Create data")
    print("[2] Show data")
    print("[3] Search Book")
    print("[4] Update Book")
    print("[5] Delete Book")
    print("[6] Reset Data")
    print("[0] Exit")
    menu_input = int(input("Choose menu above (type the number) == "))
    if menu_input == 1:
        create_data_book()
    elif menu_input == 2:
        show_data_book()
    elif menu_input == 3:
        search_book()
    elif menu_input == 4:
        update_book()
    elif menu_input == 5:
        delete_book()
    elif menu_input == 6:
        reset_data()
    elif menu_input == 0:
        print("thank you for using this program!!!")
        exit()
    else:
        input("Oops wrong number. Press any key to return")
        menu()

#agar program melakukan pengulangan
while status == True:
    menu()
    check_status = input("Next process?[Y/N] => ")
    if (check_status == "Y") or (check_status == "y"):
        status = True
    else:
        status = False
print("Good Bye!!!")
#Mungkin program ini belum sesuai harapan
#Masih memerlukan perbaikan