from time import sleep
from zipfile import ZipFile
from passGen import PassGen
import multiprocessing
from termutils import *



def crackBrut(lock:multiprocessing.Lock, num):
    import random
    import string
    from itertools import product
    filename = 'dummy.zip'
    zip = ZipFile(filename)
    cnt = 0
    cont = True
    BABA = string.ascii_letters + string.digits + string.punctuation
    # BOOEY = [ch for ch in BABA]
    while cont:
        for pwd in product(BABA, repeat=4+num):
            pw = "".join(pwd)

            try:
                zip.extractall( pwd=bytes(pw, encoding='utf-8'))
                cont = False
                cont = False
                with lock:
                    moveTo(20+num, 2)
                    cprint(f'Found {pw}', 'green', end='')
                    print(flush=True, end='')
                    with open('foundpassw', 'a+') as f:
                        f.write(pw + '\n')
            except Exception:
                cnt += 1
                if not cnt % 10000:
                    # with lock:
                    moveTo(2+num, 2)
                    cprint(f'Tries {str(cnt):<20}:- {pw[:20]}                        ', 'cyan', end='')
                    print(flush=True, end='')

def crackRT(lock:multiprocessing.Lock, num, pwds):
    import shutil
    filename = 'dummy.zip'
    nfn = f'tmp/{num}{filename}'
    shutil.copyfile(filename, nfn)
    zip = ZipFile(nfn)
    cnt = 0
    cont = True
    while cont:
        for pw in pwds:
            try:
                pas = bytes(pw, encoding='utf-8')
                zip.extractall(pwd=pas)
                cont = False
                with lock:
                    moveTo(25+num, 2)
                    cprint(f'Found {pw}', 'green', end='')
                    print(flush=True, end='')
                    with open('foundpassw', 'a+') as f:
                        f.write(pw + '\n')
            except Exception:
                cnt += 1
                if not cnt % 1000:
                    # with lock:
                    moveTo(2+num, 2)
                    cprint(f'Tries {str(cnt):<20}:- {pw[:20]}                        ', 'cyan', end='')
                    print(flush=True, end='')


if __name__=="__main__":
    
    passgen = PassGen()
    xxx = passgen.split(24)
    clear()
    threads = []
    lock = multiprocessing.Lock()
    for num, pwds in enumerate(xxx):
        args = (lock, num, pwds, )
        thread = multiprocessing.Process(target=crackRT, args=args, daemon=True)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
