| Grupos | Minutos por grupo | Resultado esperado | Saída obtida |
| --- | --- | --- | --- |
| 10 | 5.0 | Análise dentro do prazo | 2.0 |
| 12 | 5.0 | Análise dentro do prazo | 2.4 |
| 13 | 5.0 | Análise dentro do prazo | 2.6|
| 0 | 5.0 | Essa quantidade de símbolos é inválida. | |
| 10 | -1.0 | Esse tempo é inválido. | |

| Tempo disponível | Tempo necessário | Risco | Pista | Resultado esperado | Saída obtida |
| --- | --- | --- | --- | --- | --- |
| 60 | 60 | sim | sim | Prioridade Máxima | 0.0 |
| 60 | 61 | sim | sim | Solicitar apoio: tempo insuficiente. | -1.0 |
| 60 | 30 | nao | sim | Prioridade alta | 30.0 |
| 60 | 30 | nao | nao | Prioridade normal. | 30.0 |
| 60 | 30 | sim | nao | Prioridade máxima | 30.0 |
| 0 | 30 | nao | nao | Tempo inválido! | -30.0 |
| 60 | 30 | talvez | nao | Resposta inválida. | 30.0 |
| -1 | 30 | talvez | nao | Tempo inválido, resposta inválida. | 29.0 |

# Caso da atividade 1:
# Colocamos em grupos: 15; em tempo estimado, 12 minutos. Resultou em: Análise dentro do prazo, 1.25. Primeiramente, a principal coisa a ser verificada no código é se a quantidade de grupos é maior que zero e um número positivo, e depois, se o tempo é válido e menor que 60, se for maior que 60, é necessário reorganizar o trabalho. Mas nesse caso, está tudo certo.


# Caso da atividade 2:
# Já nesse, testei um caso de prioridade máxima. Resultado:
# Identifique a mensagem. msd
# Quanto tempo há disponível, em minutos? 14
# Quanto tempo é necessário, em minutos? 12
# A mensagem indica risco imediato? (sim/nao) sim
# A mensagem contém uma pista recorrente? (sim/nao) nao
# Prioridade máxima.
# Minutos que restarão após a análise: 2.0