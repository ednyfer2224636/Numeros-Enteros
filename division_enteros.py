"""División de números enteros
Problema No. 2"""

#input
A= input("Digite el valor de A: ")
A= int(A)
B= input("Digite el valor de B: ")
B= int(B)

#processing - storage
C = A/B
D = A%B
E = A//B

#output
print ("La división de " + str (A) + " y " + str (B) + " es " + str (C))
print ("El módulo de " + str (A) + " y " + str (B) + " es " + str (D))
print ("El cociente de " + str (A) + " y " + str (B) +  " es " + str (E))