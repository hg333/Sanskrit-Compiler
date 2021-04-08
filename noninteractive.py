import basic
code = open("sample.txt",'r')

# basic.run(code.read())

import codecs
with codecs.open('sample.txt', encoding='utf-8') as f:
    i = f.read().encode('utf-8')
    basic.run(i.decode('utf-8'))
