import chardet
encoding = chardet.detect('r�xirfg')['encoding'] 
unicode_string = unicode('r�xirfg', encoding)
my_ascii = unicode_string.encode('ascii', 'ignore')
my_uni_string = my_ascii.decode('utf8')
print(my_uni_string)