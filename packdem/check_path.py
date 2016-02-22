# coding: utf8
import os.path
def check_file():
    ur=raw_input('Enter path (/home/askar/Desktop): ')
    if os.path.exists(ur):
        fl=raw_input('Enter file/folder (qw.jpg): ')
        if os.path.exists(ur+'/'+fl):
            print 'Последний доступ (в сек): ', os.path.getatime(ur)
            print 'Последний изменение (в сек): ',os.path.getmtime(ur+'/'+fl)
            print 'Время создания (в сек): ',os.path.getctime(ur+'/'+fl)
            print 'Размер', os.path.getsize(ur)
        else:
            print 'Нет такого файла/папки!!!'
    else:
        print 'Error 404!!!'
