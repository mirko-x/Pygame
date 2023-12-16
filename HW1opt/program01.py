# -*- coding: utf-8 -*-

if 'profile' not in __builtins__:
    print("installing dummy profile")
    def profile(x): return x
'''
abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_


'''


@profile
def ex1(int_seq, subtotal):
    tot = 0
    int_seq = list(map(int, int_seq.split(",")))
    n = len(int_seq)
    zerobool, unobool, valbool = True, True, True

    for x in int_seq:
        if x != 0:
            zerobool = False
            break
    for x in int_seq:
        if x != 1:
            unobool = False
            break
    for x in int_seq:
        if  x != int_seq[0]:
            valbool = False
            break

    if valbool and subtotal%x != 0:
        return 0
    if (zerobool  and  subtotal != 0) or ( n<=1 and subtotal != int_seq):
        return 0
    if (unobool and subtotal > n):
        return 0
    if (unobool  and subtotal == n):
        return subtotal
    if unobool and subtotal > 1:
        return n-subtotal+1

    for i in range (n):
        somma = 0
        for j in range (i, n):
            if (int_seq[i] or int_seq[j] ) > subtotal:
                break
            somma += int_seq[j]
            
            if somma == subtotal:
                tot += 1
            elif somma > subtotal:
                break
            
            

    return tot
    pass


if __name__ == '__main__':

    pass
