# --- Calculadora de Média Escolar ---

print("=== Calculadora de Média Escolar ===")

# Recebe as notas do usuário (usando float para aceitar números quebrados)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética das três notas
media = (nota1 + nota2 + nota3) / 3

# Exibe a média formatada com 2 casas decimais
print(f"\nA sua média final é: {media:.2f}")

# Estrutura de decisão para verificar a situação do aluno
if media >= 7.0:
    print("Situação: 🟢 Aprovado! Parabéns pelo esforço!")
elif media >= 5.0:
    print("Situação: 🟡 Em Recuperação. Ainda dá tempo de virar o jogo!")
else:
    print("Situação: 🔴 Reprovado. Não desanime, revise o conteúdo e tente de novo!")