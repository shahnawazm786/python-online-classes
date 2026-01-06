book_name={
            "serial_no":1,
            "NameOfBook":'Python',
            "WriterName":'James',
            "Price":800,
            "No_of_page":110
           } 

print(book_name['No_of_page'])
print(book_name['NameOfBook']) # dictinary
print(book_name['WriterName'])
#Modification assignment operator used - '='
book_name['WriterName']='Thompson'
print('After update WriterName')
print(book_name)

#insertion and updation 
#insertion
print('Adding publisher')
book_name['publisher']="ORally"
print(book_name)
# if key present into the dictionary then 'modification will be taken place'
# else insertion will be taken place




