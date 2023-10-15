# TODO Найдите количество книг, которое можно разместить на дискете

ch = 4
ch_in_str = 25
str_in_page = 50
pages_in_book = 100

byte_size_of_book = ch * ch_in_str * str_in_page * pages_in_book
byte_size_of_disk = 1.44 * 1024 * 1024

books_in_disk = int(byte_size_of_disk//byte_size_of_book)
print("Количество книг, помещающихся на дискету:", books_in_disk)
