## Resolução TPC4 - Aula 5

#### Pergunta 1.1

A resolução para esta pergunta encontra-se no ficheiro main.experiencia2.1.js.

#### Pergunta 2.1

De seguida são apresentados os resultados de minerar com dificuldades.

* Tempo de mineração com dificuldade 2

  * ''' node main.experiencia2.1.js  0,11s user 0,07s system 66% cpu 0,271 total '''

* Tempo de mineração com dificuldade 3

  * ''' node main.experiencia2.1.js  0,37s user 0,04s system 105% cpu 0,389 total '''

* Tempo de mineração com dificuldade 4

  * ''' node main.experiencia2.1.js  1,66s user 0,06s system 102% cpu 1,683 total '''
  
* Tempo de mineração com dificuldade 5

  * ''' node main.experiencia2.1.js  23,44s user 0,70s system 78% cpu 30,867 total '''
  
Como se pode observar pelos resultados obtidos, quanto maior a dificuldade, maior o tempo de execução, pois a dificuldade influencia o número de zeros existentes no inicio da hash, o que torna mais complicado gerar uma hash que cumpra os requisitos para minerar uma *coin*. É também necessário referir, que o poder computacional do computador onde a mineração acontece influencia o resultado final.

#### Pergunta 2.2

O algoritmo de *proof of work* consiste em incrementar 1 ao cumprimento da *blockchain*, e sempre que se obtém um múltiplo de 9 é minerada uma *coin*.

Não é um algoritmo adequado para minerar pois é bastante simples obter um múltiplo de 9, o que desvaloriza o valor da moeda.
