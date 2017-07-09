#!/usr/bin/python

import cPickle as pickle
import os.path

def init():
    if os.path.exists('userinfo.pkl'):
        pass
    else:
        db = {}
        userinfo = open('userinfo.pkl', 'wb')
        pickle.dump(db, userinfo)
        userinfo.close()

def newuser():
    userinfo = open('userinfo.pkl', 'rb')
    db = pickle.load(userinfo)
    userinfo.close()

    nname = raw_input('please input new user name:>')
    while True:
        if db.has_key(nname):
            print('the user name has taken, please try another!')
            continue
        else:
            break
    npwd = raw_input('please intput the user password:>')
    db[nname] = npwd
    userinfo = open('userinfo.pkl', 'wb')
    pickle.dump(db, userinfo, True)
    userinfo.close()

def olduser():
    userinfo = open('userinfo.pkl', 'rb')
    db = pickle.load(userinfo)
    userinfo.close()

    oname = raw_input('please input old user name:>')
    opwd = raw_input('please input the user password:>')
    if db[oname] == opwd:
        print('welcome back %s' % oname)
    else:
        print('login incorrect')

def showuser():
    userinfo = open('userinfo.pkl', 'rb')
    db = pickle.load(userinfo)
    print db

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
    init()
    login()
