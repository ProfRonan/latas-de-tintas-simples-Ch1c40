print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa
import math
litros = metros_quadrados / 3
latas = litros / 18

qtd_de_latas = math.ceil(latas)
valor_total = qtd_de_latas*80

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.
qtd_de_latas = qtd_de_latas
valor_total = valor_total

print(f"Serão necessárias {qtd_de_latas} latas totalizando R$ {valor_total}")
