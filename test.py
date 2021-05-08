from itertools import product
from zipfile import ZipFile
from passGen import PassGen


filename = 'dummy.zip'
zip = ZipFile(filename)
passgen = PassGen(_shuffle=True)
cnt = 0
for pw in passgen.bank:
    try:
        zip.extractall( pwd=bytes(pw, encoding='ansi'))
        print(pw)
    except Exception:
        cnt += 1
        if not cnt % 10000:
            print('Tried', cnt)
    


