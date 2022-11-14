import os
import numpy as np


def openCOW(file):
    commands = []
    with open(file, "r") as f:
        for line in f.readlines():
            for obj in line.split():
                if obj == "MoO" or obj == "MOo" or obj == "moO" or \
                        obj == "mOo" or obj == "moo" or obj == "MOO" or \
                        obj == "OOM" or obj == "oom" or obj == "mOO" or \
                        obj == "Moo" or obj == "OOO":
                    commands.append(obj)
    return commands


def mooAndMOO(commands):
    stack = []
    dic = {}
    ind = 0
    for command in commands:
        if command == 'MOO':
            stack.append(ind)
        if command == 'moo':
            dic[ind] = stack[len(stack) - 1]
            dic[stack.pop()] = ind
        ind += 1
    return dic


def processingCommands(commands, dic):
    res = np.zeros(len(commands))
    index = 0
    i = 0
    while i != len(commands):
        if commands[i] == "MoO":
            res[index] += 1
        elif commands[i] == "MOo":
            res[index] -= 1
        elif commands[i] == "moO":
            index += 1
        elif commands[i] == "mOo":
            index -= 1
        elif commands[i] == "moo":
            i = dic[i] - 1
        elif commands[i] == 'MOO':
            if res[index] == 0:
                i = dic[i]
        elif commands[i] == "OOM":
            if res[index] == 32 or res[index] == 44:
                print(f"{chr(int(res[index]))}", end="")
            else:
                print(f"{int(res[index])}", end="")
        elif commands[i] == "oom":
            res[index] = input()
        elif commands[i] == "mOO":
            res[index] = i
        elif commands[i] == "Moo":
            if res[index] == 0:
                res[index] = input()
            else:
                print(f"{chr(int(res[index]))}", end="")
        elif commands[i] == "OOO":
            res[index] = 0

        i += 1


directory = 'cow_examples'
files = os.listdir(directory)
cow = filter(lambda x: x.endswith('.cow'), files)
for file in cow:
    print("\n",directory + '/' + file,end=":")
    commands = openCOW(directory + '/' + file)
    dic = mooAndMOO(commands)
    processingCommands(commands, dic)

