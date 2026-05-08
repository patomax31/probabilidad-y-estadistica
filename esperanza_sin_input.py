         # 0, 1 , 2
bidi = [[1, 2, 3],       # 0
        [0.3, 0.4, 0.3]] #1

esperanza = 0
varianza = 0

rows = 2
cols = 3

print(bidi)

for j in range (cols):
    esp = (bidi[0][j] * bidi[1][j])
    print(f"esp_{j}: {esp}")
    esperanza += esp

    
print("esperanza:", esperanza)
