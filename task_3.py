import os


def file_sorted(path):
    with open(path, 'r', encoding='utf-8') as fr:
        file = fr.readlines()
        len_file = len(file)
    return {len_file: [os.path.basename(path), file]}


sort_dict = file_sorted("sorted/1.txt")
sort_dict.update(file_sorted("sorted/2.txt"))
sort_dict.update(file_sorted("sorted/3.txt"))


with open('result.txt', 'w', encoding='utf-8') as fw:
    for i in dict(sorted(sort_dict.items())):
        fw.write(sort_dict[i][0] + '\n')
        fw.write(str(i) + '\n')
        for j in sort_dict[i][1]:
            fw.write(j)
        fw.write('\n')
