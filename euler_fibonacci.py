def main ():
    fib_seq = [1,2]

    while(True):
        fib_new = fib_seq[-1] + fib_seq[-2]
        if fib_new > 4000000:
            break
        fib_seq.append(fib_new)
        
    total = 0 
    
    for i in fib_seq:
        if i % 2 == 0:
            total += i
    print (total)

main()
        
    