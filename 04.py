pop_a = 80000
pop_b = 200000

taxa_a = 0.03
taxa_b = 0.015 

anos = 0

while pop_a < pop_b:
    pop_a = pop_a + (pop_a * taxa_a)
    pop_b = pop_b + (pop_b * taxa_b)
    anos = anos + 1

print("Número de anos para a população de A ultrapassar ou igualar a de B:", anos)
print("População de A:", int(pop_a))
print("População de B:", int(pop_b))