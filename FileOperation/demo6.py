filename = 'demo6.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
max_length = len(max(lines, key=len))
lines = [line.rstrip().ljust(max_length)+'#'+str(index)+'\n' for index, line in enumerate(lines)]
with open('new_' + filename, 'w') as fp:
    fp.writelines(lines)