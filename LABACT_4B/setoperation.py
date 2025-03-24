A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'j', 'i', 'k'}

elements_in_A_and_B = A & B
print(f"Elements in both A and B: {elements_in_A_and_B}")
print(f"Number of elements in both A and B: {len(elements_in_A_and_B)}")

elements_in_B_not_in_A_and_C = B - (A | C)
print(f"Elements in B that are not in A and C: {elements_in_B_not_in_A_and_C}")
print(f"Number of elements in B that are not in A and C: {len(elements_in_B_not_in_A_and_C)}")

print(f"i. {A | B | C}")
print(f"ii. {A & B & C}")
print(f"iii. {B & C}")
print(f"iv. {A & C}")
print(f"v. {C - (A | B)}")
print(f"vi. {B - (A | C)}")