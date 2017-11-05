# -*- coding: UTF-8 -*-.
import re


def word_count(fin_path):
    with open(fin_path, 'r') as fin:
        all_words = re.split(r'[\s\.,:]', fin.read().strip())

    result = {}
    for x in all_words:
        if x:
            result[x] = result.get(x, 0) + 1
    result = sorted(result.items(), key=lambda item:item[1], reverse=True)

    return result


if __name__ == '__main__':
    result = word_count('textEN.txt')
    with open('result.txt', 'w') as fout:
        for line in result:
            fout.write(line[0] + '\t' + str(line[1]) + '\n')
    print('结果保留在当前目录result.txt文件中.')

