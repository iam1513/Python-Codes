num_terms = 10
first_term, second_term = 0, 1

for _ in range(num_terms):
    print(first_term, end=" ")
    first_term, second_term = second_term, first_term + second_term
