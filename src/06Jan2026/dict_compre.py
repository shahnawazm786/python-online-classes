book_name={
            "serial_no":1,
            "NameOfBook":'Python',
            "WriterName":'James',
            "Price":800,
            "No_of_page":110
           }

for key in book_name.keys():
    print(key)

for val in book_name.values():
    print(val)

for k,v in book_name.items():
    print(f'Key is -> {k} and Value is -> {v}')