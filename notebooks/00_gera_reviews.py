import pandas as pd
import numpy as np

np.random.seed(42)
clientes = [f"Cliente_{i:03d}" for i in range(1, 201)]
servicos = ["Internet", "Telefone", "TV", "Nuvem", "Streaming", "Fibra Óptica"]

# Exemplos de textos para sortear, cobrindo todos os tipos de sentimento
textos_positivos = [
    "Ótimo serviço, estou muito satisfeito.",
    "Atendimento rápido e eficiente.",
    "Fui muito bem atendido, recomendo!",
    "Estou gostando bastante do serviço.",
    "Resolveu meu problema na hora, parabéns!",
    "Muito bom! Surpreendeu minhas expectativas.",
    "Funcionou perfeitamente durante a viagem.",
    "Atendimento cordial e sem enrolação.",
    "Nota 10! Melhor experiência que já tive.",
    "Equipe super preparada e educada."
]
textos_neutros = [
    "Serviço razoável, mas melhorou ultimamente.",
    "Nada a reclamar, tudo dentro do esperado.",
    "É um serviço ok, cumpre o que promete.",
    "Funciona na maior parte do tempo.",
    "Ainda estou avaliando o serviço.",
    "Cobrança correta, sem surpresas.",
    "Experiência comum, igual a outras empresas.",
    "O app poderia ser mais rápido.",
    "Poderiam oferecer mais opções.",
    "Serviço comum, nem bom nem ruim."
]
textos_negativos = [
    "O atendimento poderia ser melhor.",
    "Muito lento, sempre com problemas.",
    "Não resolve meu problema nunca.",
    "Péssimo! Nunca mais contrato.",
    "O sinal cai toda hora, não gosto.",
    "Péssimo suporte ao cliente.",
    "Estou muito insatisfeito com o serviço.",
    "Atendimento demorado e ineficiente.",
    "Nunca consigo falar com o suporte.",
    "Quero cancelar, só dor de cabeça."
]
all_reviews = textos_positivos*10 + textos_neutros*7 + textos_negativos*10  # Mais negativos e positivos para balancear

# Gera 10000 reviews aleatórios
n = 10000
df = pd.DataFrame({
    "cliente": np.random.choice(clientes, n),
    "servico": np.random.choice(servicos, n),
    "review": np.random.choice(all_reviews, n)
})

df.to_csv("data/reviews.csv", index=False)
