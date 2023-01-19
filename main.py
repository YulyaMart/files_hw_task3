
with open('1.txt', 'r', encoding = 'utf-8') as f1, open('2.txt', 'r', encoding = 'utf-8') as f2, open('3.txt', 'r', encoding = 'utf-8') as f3, open('4.txt', 'w', encoding = 'utf-8') as f4:
    lines_amount = {}
    file_content = {}
    lines_amount['1.txt'] = sum(1 for _ in f1)
    lines_amount['2.txt'] = sum(1 for _ in f2)
    lines_amount['3.txt'] = sum(1 for _ in f3)
    f1.seek(0)
    f2.seek(0)
    f3.seek(0)
    file_content['1.txt'] = f1.read()
    file_content['2.txt'] = f2.read()
    file_content['3.txt'] = f3.read()
    sorted_tuples = sorted(lines_amount.items(), key=lambda item: item[1])
    sorted_lines_amount = {k: v for k, v in sorted_tuples}
    for k, v in sorted_lines_amount.items():
        for key, value in file_content.items():
            if k == key:
                f4.write('%s\n%s\n%s\n' % (k, v, value))
