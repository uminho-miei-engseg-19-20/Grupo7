## Resolução TPC2 - Aula 3

#### Pergunta 1.1

De seguida encontram-se os ficheiros relativos à resolução desta pergunta.

- [init-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/Blind%20signatures/init-app.py)
- [blindSignature-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/Blind%20signatures/blindSignature-app.py)
- [ofusca-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/Blind%20signatures/ofusca-app.py)
- [desofusca-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/Blind%20signatures/desofusca-app.py)
- [verify-app.py](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/Blind%20signatures/verify-app.py)

#### Pergunta 2.1

Nesta pergunta, foi pedido ao grupo que escolhesse dois sitíos de Câmaras Municipais Portuguesas e que se efetuasse o *SSL Server Test* para cada um desses sitíos. As Câmaras Municipais escolhidas foram a de [Barcelos](https://www.cm-barcelos.pt/) e a de [Lisboa](https://www.lisboa.pt/).

- ##### Resultados dos *SSL Server Test*

De seguida encontram-se os ficheiros pdf com os resultados dos testes.
- [CM Barcelos](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/sslTestBarcelos.pdf)
- [CM Lisboa](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/sslTestLisboa.pdf)

- ##### Análise do sítio com pior _rating_

Apesar de ambos os sítios terem obtido um _rating_ B, o da CM Barcelos é pior comparativamente ao da CM Lisboa, como se pode observar nas imagens em baixo.

- [Rating CM Barcelos](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/sslTestBarcelos.jpg)
- [Rating CM Lisboa](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/sslTestLisboa.jpg)

Tal como podemos observar no [ficheiro pdf](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/sslTestBarcelos.pdf) com o resultado do teste, o sítio além de não suportar TLS 1.3, suporta ainda versões _legacy_, tais como TLS 1.1 e TLS 1.0, que já não são completamente seguras. Além disto, a maioria das _Cipher suites_ utilizadas são consideradas fracas, o que levanta sérios problemas de segurança nas comunicações.

- ##### **POODLE (TLS)**

**POODLE (Padding Oracle On Downgraded Legacy Encryption)** é um ataque que explora falhas na implementação do modo CBC nos protocolos TLS 1.0 a TlS 1.2. O problema está na verificação do _padding_, onde algumas implementações não o fazem corretamente, o que pode colocar os servidores em risco mesmo que não tenham SSL 3.0 ativo.
Como se pode observar no resultado da análise, o sítio da CM Barcelos não se encontra ameaçado por este _exploit_.

#### Pergunta 3.1

Para a resolução deste exercício, o grupo escolheu dois servidores de empresas comerciais em Madrid, [Vodafone Espanha (77.226.197.217)](https://www.shodan.io/host/77.226.197.217) e [Belcloud LTD (88.80.148.127)](https://www.shodan.io/host/88.80.148.127).

- Resultados *SSH-Audit*
  - [Vodafone Espanha](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/ssh-audit-77.226.197.217.txt)
  - [Belcloud LTD](https://github.com/uminho-miei-engseg-19-20/Grupo7/blob/master/TPraticas/TPC2/ssh-audit-88.80.148.127.txt)

- Versões do *Software*

````
# general - 77.226.197.217
(gen) banner: SSH-2.0-HUAWEI-1.5
(gen) compatibility: OpenSSH 5.9-6.0, Dropbear SSH 2013.56+ (some functionality from 0.52)
(gen) compression: disabled
`````

````
# general - 88.80.148.127
(gen) banner: SSH-2.0-OpenSSH_7.4
(gen) software: OpenSSH 7.4
(gen) compatibility: OpenSSH 7.3+ (some functionality from 6.6), Dropbear SSH 2016.73+ (some functionality from 0.52)
(gen) compression: enabled (zlib@openssh.com)
````
- Versão com mais vulnerabilidades

Após a análise dos resultados do *SSH-Audit* e do *Shodan*, foi possível perceber que para o servidor da Vodafone Espanha não foram encontradas quaisquer vulnerabilidades, o que não significa que não possam existir, apenas que estes *scans* não identificaram nenhuma. Já para o servidor da Belcloud LTD, o *Shodan* encontrou duas vulnerabilidades, [
CVE-2018-15919](https://www.cvedetails.com/cve/CVE-2018-15919/) e [CVE-2017-15906](https://www.cvedetails.com/cve/CVE-2017-15906).

Segundo o CVE-Details ambas as vulnerabilidades possuem um *CVSS score* de 5.0. Apesar da dificuldade da exploração dessas vulnerabilidades ser baixa, as mesmas não podem ser consideradas graves.
