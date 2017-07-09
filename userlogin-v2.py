#!/usr/bin/python

import shelve


def newuser():
    db = shelve.open('userinfo.dat', writeback=True)

    nname = raw_input('please input new user name:>')
    while True:
        if db.has_key(nname):
            print('the user name has taken, please try another!')
            continue
        else:
            break
    npwd = raw_input('please intput the user password:>')
    db[nname] = npwd
    db.close()

def olduser():
    db = shelve.open('userinfo.dat')

    oname = raw_input('please input old user name:>')
    opwd = raw_input('please input the user password:>')
    if db[oname] == opwd:
        print('welcome back %s' % oname)
    else:
        print('login incorrect')

    db.close()

def showuser():
    db = shelve.open('userinfo.dat')
    print db
    db.close()

def login():
    info = '''
(N)ew User Login
(O)ld User Login
(P)rint User Info
(Q)uit 

Enter choice:->'''
    while True:
        try:
            choice = raw_input(info).strip().lower()
        except (EOFError, KeyboardInterrupt):
            choice = 'q'
        if choice in 'noqp':
            print('you choice %s' % choice)
        else:
            print('invalid option, try agagin!')
            continue

        if choice == 'q':
            break
        elif choice == 'n':
            newuser()
        elif choice == 'o':
            olduser()
        else:
            showuser()

if __name__ == '__main__':
    login()
