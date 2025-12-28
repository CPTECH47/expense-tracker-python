# -------- Sum of Array --------
a=[10,20,30]
sum=0
for i in range(0,3):
   sum=sum+a[i]
print(f"sum of the arrays is {sum}")

# -------- Largest Element --------

a = [10, 20, 30]

b = a[0]       

for i in range(1, len(a)):
    if a[i] > b:
        b= a[i]

print("the greatest number is",b)
