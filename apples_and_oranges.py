# Following the idea from 
# https://github.com/kdungs/codecon/blob/master/src/apples.cc
# But TLE for python :(

import sys
from fractions import gcd

def find_solution(max_money, price, other):
    while max_money >= 0 and (max_money % price) != 0:
        max_money -= other
    if max_money < 0:
        return -1
    return max_money / price

def main():
    data = sys.stdin.read().splitlines()
    
    A0,O0,M0,x,y,Mf = 0,0,0,0,0,0
    data = data[0].split()
    data = list( map(int, data) )
    A0 = data[0]
    O0 = data[1]
    M0 = data[2]
    x  = data[3]
    y  = data[4]
    Mf = data[5]
    
    max_money = A0*x + O0*y + M0 - Mf
    # g = gcd(x,y)
    # if max_money % g != 0:
    #     print('Impossible')
    #     return
    
    a = find_solution(max_money, x, y)
    if a == -1:
        print('Impossible')
        return
    
    o = find_solution(max_money, y, x)
    if o == -1:    
        print('Impossible')
        return
    print('%d %d' % (a, o))
            
main()
   
