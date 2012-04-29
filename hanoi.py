###############################################
# Solution for hanoi towers                   #
# Created by Donat Csikos <csdonat@gmail.com> #
# At 29/04/2012.                              #
###############################################

# imports
import sys

# num of items on the first rod
K = raw_input("Number of disks on the left rod:")
try:
    K = int(K)
    if K <= 0:
	raise Exception
    K = K - 1
except:
    print "Rerun the script and enter a positive integer!"
    exit(1)

# rods
A = range(K + 1)[::-1]
B = []
C = []

def display():
    """ Display the current state of the towers. """
    print A
    print B
    print C
    print '-----------------'

def move(num, source, dest):
    """ Move one disk. """
    if source[-1] != num:
        raise Exception('invalid')
    del(source[-1])
    dest.append(num)
    display()
    check()


def check():
    """ check if the tower is in an invalid state. """
    check_tower(A)
    check_tower(B)
    check_tower(C)

def check_tower(T):
    """ Check if a state is valid (there is no bigger disk in a smaller one).. """
    for i in range(len(T) - 1):
        if T[i] <= T[i + 1]:
            raise Exception('invalid state')
    

def hanoi(disk, source, dest, spare):
    """ Solves hanoi towers. """
    if disk == 0:
        move(disk, source, dest)
    else:
        hanoi(disk - 1, source, spare, dest)
        move(disk, source, dest)
        hanoi(disk - 1, spare, dest, source)

# display initial state
display()

# start solver
hanoi(K, A, B, C)
