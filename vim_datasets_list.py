with open('./train.txt', encoding='utf-8') as f:
    paths = f.readlines()

with open('./train_' + '.txt', 'a', encoding='utf-8') as g:
    for line in paths:
        g.write(line[12:23]+'\n')
f.close()

with open('./val.txt', encoding='utf-8') as h:
    paths_val = h.readlines()

with open('./val_' + '.txt', 'a', encoding='utf-8') as k:
    for line in paths_val:
        k.write(line[12:23]+'\n')
h.close()