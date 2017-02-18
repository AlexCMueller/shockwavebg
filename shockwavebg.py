# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
# 
# For more information, please refer to <http://unlicense.org/>

import colorama
import random
import shutil
import time

# this function prints the colors out to the terminal
def printTape(tape):
    string = "\n"
    for item in tape:
        string += colors[item]

    print(string, end="")

# this function runs a cycle of shockwave, a cellular automata rule invented
# by lock.
# the rules are as follows:
# A becomes B
# B becomes A, unless next to A, then it becomes 0
# 0 becomes 0, unless next to A, then it becomes A
def doCycle(tape):
    newTape = []

    for i in range(len(tape)):

        # A becomes B
        if tape[i] == 1:
            newTape.append(2)

        # B becomes A, unless next to A
        # then it becomes 0
        if tape[i] == 2:
            if (tape[(i - 1) % len(tape)] == 1 or
                tape[(i + 1) % len(tape)] == 1):

                newTape.append(0)
            else:
                newTape.append(1)
        
        # 0 becomes 0, unless next to A, then it becomes A
        if tape[i] == 0:
            if (tape[(i - 1) % len(tape)] == 1 or
                tape[(i + 1) % len(tape)] == 1):

                newTape.append(1)
            else:
                newTape.append(0)

    return newTape

# get terminal size
width, height = shutil.get_terminal_size((80, 20))

# magic numbers to make colors happen
colorama.init()
colors = [colorama.Back.BLACK + " ",
          colorama.Back.WHITE + " ",
          colorama.Back.GREEN + " "]

# initialize the tape
tape = []
for i in range(width):
    tape.append(random.randint(0,2))

# change the number to change the speed
sleepTime = 1/30

# start printing the automata
while True:
    printTape(tape)
    tape = doCycle(tape)
    time.sleep(sleepTime)
