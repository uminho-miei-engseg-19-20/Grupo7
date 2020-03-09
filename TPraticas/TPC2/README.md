## Resolução TPC2 - Aula 3

#### Pergunta 1.1

De seguida encontram-se os ficheiros relativos à resolução desta pergunta.

- [init-app.py]()
- [blindSignature-app.py]()
- [ofusca-app.py]()
- [desofusca-app.py]()
- [verify-app.py]()

#### Pergunta 2.1

Nesta pergunta, foi pedido ao grupo que escolhesse dois sitíos de Câmaras Municipais Portuguesas e que se efetuasse o *SSL Server Test* para cada um desses sitíos. As Câmaras Municipais escolhidas foram a de [Barcelos](https://www.cm-barcelos.pt/) e a de [Lisboa](https://www.lisboa.pt/).

##### Resultados dos *SSL Server Test*

De seguida encontram-se os ficheiros pdf com os resultados dos testes.

- [CM Barcelos]()
- [CM Lisboa]()

##### Análise do sítio com pior -rating-

Apesar de ambos os sítios terem obtido um -rating- B, o da CM Barcelos é pior comparativamente ao da CM Lisboa.

Tal como podemos observar no [ficheiro pdf]() com o resultado do teste, o sítio além de não suportar TLS 1.3, suporta ainda versões --legacy--, tais como TLS 1.1 e TLS 1.0, que já não são completamente seguras. Além disto, a maioria das -Cipher suites- utilizadas são consideradas fracas, o que levanta sérios problemas de segurança nas comunicações.

##### **POODLE (TLS)**

**POODLE (Padding Oracle On Downgraded Legacy Encryption)** é um ataque que explora falhas na implementação do modo CBC nos protocolos TLS 1.0 a TlS 1.2. O problema está na verificação do -padding-, onde algumas implementações não o fazem corretamente, o que pode colocar os servidores em risco mesmo que não tenham SSL 3.0 ativo.

Como se pode observar no resultado da análise, o sítio da CM Barcelos não se encontra ameaçado por este -exploit-
