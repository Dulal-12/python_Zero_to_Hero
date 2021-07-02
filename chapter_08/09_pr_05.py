def remove_and_strip(string , word):
    return string.replace(word , '').strip()
string = '        Dulal is a good boy'
word = "Dulal"
print(remove_and_strip(string , word))