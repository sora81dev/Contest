N = input()
n_int = int(N)

let=[]
for i in range(n_int):
    if i==0:
        let.append("1")
    let.append("0")
    if not n_int == 0:
        let.append("1")

test="".join(let)
print(test)