def bayes_theorem(P_A, P_B, P_B_given_A):
    # Aplicação do Teorema de Bayes
    P_A_given_B = (P_B_given_A * P_A) / P_B
    
    return P_A_given_B

# Probabilidades
P_D = 1/1000   # Probabilidade da doença (A)
P_TP = (0.99 * P_D) + (0.02 * (1-P_D)) # Probabilidade de teste positivo (B)
P_TP_given_D = 0.99 # Probabilidade de teste positivo se a pessoa tem a doença (B|A)

# Calculando a probabilidade de ter a doença dado um teste positivo (A|B)
P_D_given_TP = bayes_theorem(P_D, P_TP, P_TP_given_D)

print(f"A probabilidade de ter a doença dado um teste positivo é {P_D_given_TP*100:.2f}%")
