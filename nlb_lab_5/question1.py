def bayes_theorem(P_A, P_B_given_A, P_B):
    return (P_B_given_A * P_A) / P_B

P_A = 0.5
P_B_given_A = 0.7
P_B = 0.6

posterior = bayes_theorem(P_A, P_B_given_A, P_B)
print("P(A|B) =", posterior)