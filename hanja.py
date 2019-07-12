import sys
import random


settingfile = 'hanja.dat'
filename = ''
errfilename = ''
erraddfmt = '오답 단어장에 {}(을)를 추가했습니다.\n'

def setting():
    if not os.path.exists(settingfile):
        pass
    with open(settingfile, 'rt') as rf:
        pass


def main():
    with open(filesrc, 'rt', encoding='utf-8', errors='ignore') as rf:
        database = rf.readlines()
        random.shuffle(database)

    filename = ''.join(filesrc.split('.')[:-1])
    errfilename = filename + '-errors.txt'
    index = 1
    prevline = ''
    for line in database:
        question, answer = line.split('/')
        print(str(index) + '/' + str(len(database)))
        print(question, end='')

        if input() and index > 1:
            addError(errfilename, prevline)

        print(answer)

        prevline = line
        index += 1

    print('테스트 종료! 수고했습니다.')
    if input():
        addError(errfilename, prevline)


def writeError(filename, errline):
    with open(filename, 'at', encoding='utf-8') as ef:
        ef.write(errline)

def addError(filename, errline):
    writeError(filename, errline)
    print(erraddfmt.format(errline))


if(__name__ == '__main__'):
    try:
        filesrc = sys.argv[1]
    except IndexError: # 사용자가 파일을 지정하지 않은 경우
        setting()
    else:# 데이터 파일을 지정한 경우
        main()
