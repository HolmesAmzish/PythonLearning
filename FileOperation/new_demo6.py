filename = 'demo6.py'                                                                             #0
with open(filename, 'r') as fp:                                                                   #1
    lines = fp.readlines()                                                                        #2
max_length = len(max(lines, key=len))                                                             #3
lines = [line.rstrip().ljust(max_length)+'#'+str(index)+'\n' for index, line in enumerate(lines)] #4
with open('new_' + filename, 'w') as fp:                                                          #5
    fp.writelines(lines)                                                                          #6
