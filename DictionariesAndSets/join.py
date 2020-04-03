myList = ["a", "b", "c", "d"]
print(", ".join(myList)) #It prints "a, b, c, d"

letters = ["ABCDEFGHIJKLMNOPQRSTUVWWXYZ"]

for c in letters:
    print(", ".join(c)) #It prints "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, W, X, Y, Z"

numbers = ["0123456789"]
for n in numbers:
    print(" number, ".join(n))