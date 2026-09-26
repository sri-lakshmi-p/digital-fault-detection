# Digital Fault Detection Using Boolean Algebra and Coding Theory
## About the Project
This mini-project combines Boolean Algebra and Coding Theory to study
a simple digital fault detection system.

Boolean Algebra is used to find the expected output of the system.
A Hamming (7,4) code is then used to detect and correct a single-bit
error in the transmitted binary data.

## Concepts Used
- Boolean Algebra
- Boolean Function
- Generator Matrix
- Parity-Check Matrix
- Hamming (7,4) Code
- Syndrome
- Single-bit Error Detection and Correction

## Working
The program follows these steps:
1. Takes the values of A, B and C.
2. Calculates the Boolean function F = AB + C.
3. Forms the information vector.
4. Encodes the information using the generator matrix.
5. Introduces a single-bit error.
6. Calculates the syndrome using the parity-check matrix.
7. Finds the error position.
8. Corrects the error.
9. Recovers the original information.

## Example

Information vector:

1011

Encoded codeword:

1011001

After introducing an error:

1011101

Error position:

5

Corrected codeword:

1011001

Recovered information:

1011

## Requirements
Python 3 and NumPy are required.
Install NumPy using: pip install numpy
