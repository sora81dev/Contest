class main():
    def __init__():
        N=input()
        P=list(map(int,input().split()))
        Max=max(P)
        Pnt=(Max+1)-P[0]
        P_new = [i for i in P if i == Max]
        if P[0]==Max:
            if len(P_new)==1:
                print(0)
            else:
                print(Pnt)
        else: 
            (print(Pnt))
main.__init__()