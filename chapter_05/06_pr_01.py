myDict = {
    'booi' : 'Book',
    'kolom': 'Pen',
    'botol' : 'Bottle'
}
print('Options are : ',list(myDict.keys()))
a = input('Enter The Bangla Name : ')
print('The meaning of word is : ',myDict.get(a , 'NotFound'))