Framework utilizado = PyTest
Matrícula: 212006737
Nome: Caetano Korilo Fleury de Amorim

Como rodar o programa:
    - Não é necessário compilar o projeto
    - Para o rodar o arquivo de teste é necessário digitar 'pytest testa_oito_rainhas.py' no terminal
    - Para o arquivo com o código, o teste usado no PDF no trabalho está escrito em formato 'linha linha linha...'
    em uma variável no início do código. A segunda linha apenas transforma as linhas em uma lista de listas

Funções e seus significados:
test_check_table_column_size() e test_check_table_row_size() e test_check_true_table():
    - Checa se o tabuleiro tem a formatação 8x8.
    - Passar nesse teste significa que com o tabuleiro 8x8 podemos utilizar
    utilizar as outras funções que necessariamente já assumem um tabuleiro 8x8.
    - Além disso esse teste já prova que não há rainhas na mesma coluna então já há
    embutida uma função de checagem horizontal

test_vertical_loss() e test_vertical_win():
    - Checa se o tabuleiro tem duas ou mais rainhas na mesma coluna ou na vertical.
    - Passar nesse teste significa que na situação de perda (duas ou mais rainhas na vertical) a função provou que 
    o jogo não é uma solução ou que na situação de vitória (sem rainhas na vertical de outras) a função provou que 
    o jogo é uma solução.

test_diagonal_loss_01(), test_diagonal_loss_02() e test_diagonal_win():
    - Checa se o tabuleiro tem duas ou mais rainhas na diagonal.
    - Passar nesse teste significa que na situação de perda (duas ou mais rainhas na diagonal) a função provou que 
    o jogo não é uma solução ou que na situação de vitória (sem rainhas na diagonal de outras) a função provou que 
    o jogo é uma solução.

test_check_game_win(), test_check_game_loss_01() e test_check_game_loss_02():
    - Checa se o tabuleiro é uma solução(1), não é uma solução(0) ou se é válida(-1).
    - Passar nesse teste significa que todas as outras funções funcionam e que o programa funciona



