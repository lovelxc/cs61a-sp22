#!/usr/bin/env python

import os, sys

nlab, nhw = 15, 10
# add proj names you want
proj_list = ['hog', 'cats', 'ants', 'lambdaing']


def bash_shell(bash_command):
    try:
        return os.popen(bash_command).read().strip()
    except:
        return None


def delete_all():
    if input("Please enter 'Yes': ") == 'Yes':
        bash_shell('rm -rf Lab')
        bash_shell('rm -rf zipfile')
        bash_shell('rm -rf Homework')
        bash_shell('rm -rf Project')


def download():
    if not os.path.exists('zipfile'):
        os.mkdir('zipfile')
    os.chdir('zipfile')
    for i in range(nlab):
        if not os.path.exists('lab%02d.zip'%(i)):
            bash_shell("wget --no-check-certificate https://www-inst.eecs.berkeley.edu/~cs61a/sp22/lab/lab%02d/lab%02d.zip"%(i,i))
    for i in range(nhw):
        if not os.path.exists('hw%02d.zip'%(i)):
            bash_shell("wget --no-check-certificate https://www-inst.eecs.berkeley.edu/~cs61a/sp22/hw/hw%02d/hw%02d.zip"%(i,i))
    for i in proj_list:
        if not os.path.exists('%s.zip' % (i)):
            bash_shell(
                "wget --no-check-certificate https://www-inst.eecs.berkeley.edu/~cs61a/sp22/proj/%s/%s.zip"
                % (i, i))
    os.chdir('..')


def unzip():
    outpath = 'Homework'
    if not os.path.exists(outpath): os.mkdir(outpath)
    for i in range(nhw):
        bash_shell("unzip -n zipfile/hw%02d -d "%(i) + outpath)

    outpath = 'Lab'
    if not os.path.exists(outpath): os.mkdir(outpath)
    for i in range(nlab):
        bash_shell("unzip -n zipfile/lab%02d -d "%(i) + outpath)

    outpath = 'Project'
    if not os.path.exists(outpath):
        os.mkdir(outpath)
    for i in proj_list:
        bash_shell("unzip -n zipfile/%s -d " % (i) + outpath)


def remove_zipfile():
    bash_shell("rm -rf zipfile")


if __name__ == '__main__':
    # download *.zip
    print('-' * 20 + 'start' + '-' * 20)
    download()
    unzip()
    remove_zipfile()
