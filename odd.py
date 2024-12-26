num=int(input("entwr the value of num : "))
print("odd numbers from 1 to ",num,":")
for i in range(1,num+1):
    if(i%2!=0):
        print(i,end=' ')
