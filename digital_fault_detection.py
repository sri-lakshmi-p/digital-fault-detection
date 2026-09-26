# Digital Fault Detection Using Boolean Algebra and Coding Theory
# Hamming (7,4) Code
import numpy as np
# ---------------------------------------------------------
# STEP 1: Boolean Algebra
# F = AB + C
# ---------------------------------------------------------
A = int(input("Enter A (0 or 1): "))
B = int(input("Enter B (0 or 1): "))
C = int(input("Enter C (0 or 1): "))
# Boolean function
F = (A & B) | C
print("\nBoolean Function:")
print("F = AB + C")
print("A =", A, " B =", B, " C =", C)
print("F =", F)
# Information vector
u = np.array([A, B, C, F])
print("\nInformation Vector:")
print("u =", ''.join(map(str, u)))
# ---------------------------------------------------------
# STEP 2: Hamming (7,4) Encoding
# ---------------------------------------------------------
G = np.array([
    [1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1]
])
# Encoding: c = uG (mod 2)
codeword = np.dot(u, G) % 2
print("\nGenerator Matrix G:")
print(G)
print("\nEncoded Codeword:")
print("c =", ''.join(map(str, codeword)))
# ---------------------------------------------------------
# STEP 3: Introduce an Error
# ---------------------------------------------------------
error_position = int(
    input("\nEnter error position (1-7, enter 0 for no error): ")
)
received = codeword.copy()
if error_position != 0:
    received[error_position - 1] ^= 1
print("\nReceived Word:")
print("r =", ''.join(map(str, received)))
# ---------------------------------------------------------
# STEP 4: Syndrome Calculation
# ---------------------------------------------------------
H = np.array([
    [1, 1, 1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1]
])
syndrome = np.dot(H, received) % 2
print("\nParity Check Matrix H:")
print(H)
print("\nSyndrome:")
print("S =", ''.join(map(str, syndrome)))
# ---------------------------------------------------------
# STEP 5: Detect and Correct Error
# ---------------------------------------------------------
corrected = received.copy()
if np.all(syndrome == 0):
    print("\nNo error detected.")
else:
    error_found = False
    for i in range(7):
        column = H[:, i]
        if np.array_equal(syndrome, column):
            print("\nError detected at position:", i + 1)
            corrected[i] ^= 1
            print("Error corrected.")
            error_found = True
            break
    if not error_found:
        print("\nError pattern could not be corrected.")
# ---------------------------------------------------------
# STEP 6: Display Corrected Codeword
# ---------------------------------------------------------
print("\nCorrected Codeword:")
print("c =", ''.join(map(str, corrected)))
# ---------------------------------------------------------
# STEP 7: Recover Original Information
# ---------------------------------------------------------
original_data = corrected[:4]
print("\nRecovered Information Vector:")
print("u =", ''.join(map(str, original_data)))
# ---------------------------------------------------------
# FINAL RESULT
# ---------------------------------------------------------
print("\n-----------------------------------")
print("FINAL RESULT")
print("-----------------------------------")
if np.array_equal(original_data, u):
    print("Original data recovered successfully.")
    print("Digital fault/error was detected and corrected.")
else:
    print("Data could not be recovered.")

