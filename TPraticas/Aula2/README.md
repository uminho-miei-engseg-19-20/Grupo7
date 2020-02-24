## Pergunta P1.1
Conclusões: 
  - `head -c **n** /dev/random | openssl enc -base64` --> Com base no **n** fornecido será gerado um número (pseudo-)aleatório com esse tamanho, em bytes, e em base64;
  - É utilizado o algoritmo de Yarrow na geração dos números (pseudo-)aleatórios que está implementado em `/dev/random` e `/dev/urandom`, sendo que a diferença entre *random* e *urandom* é que o primeiro bloqueia quando não tem entropia suficiente para satisfazer o pedido, enquanto o *urandom* nunca bloqueia (mas pode produzir resultados com menor qualidade).

## Pergunta P1.2
  Desta vez, quando se recorre ao /dev/random para gerar um número (pseudo-)aleatório, este já não bloqueia devido ao pacote `haveged`, que utiliza o algoritmo HAVEGE para gerar entropia a partir de eventos na máquina, resolvendo assim o problema de falta de entropia.
 
 
## Pergunta P2.1 (alíneas A e B juntas)  
**Para dividir** o segredo foi necessário correr o seguinte código: `python createSharedSecret-app.py 8 5 1 mykey.pem`, no qual o 8 é o número de componentes em que se "dividirá" o segredo, 5 o número mínimo de componentes necessários para reconstruir o segredo, 1 o usage id (que deve ser único) e mykey.pem é a chave privada para assinar cada componente resultante da divisão (é necessário criar o par de chaves pública e privada usando o comando que está nas notas do problema). Ao executar este código é-nos pedido para digitar a password da chave-privada dada como argumento e o segredo que queremos dividir. Depois disto são imprimidos os 8 componentes (porque 8 foi o pedido).

**Para recuperar** o segredo é possível usar `recoverSecretFromComponents-app.py` ou `recoverSecretFromAllComponents-app.py`.

O programa **`recoverSecretFromAllComponents-app.py`** necessita de todos os componentes originais (neste caso 8) para reconstruir o segredo, e pode ser executado com o seguinte código: `python recoverSecretFromAllComponents-app.py 8 1 mykey.crt`, em que 8 é o número total de componentes, 1 é o usage id que foi dado aquando da divisão do segredo e mykey.crt é o certificado da chave privada usada para assinar os componentes (o certificado tem de ser criado antes da execução usando o comando que está nas notas do problema). Durante a execução é-nos pedido para inserir todos os 8 componentes, um a um, e no final, se tudo tiver sido feito corretamente, o segredo é impresso no terminal.

O programa **`recoverSecretFromComponents-app.py`** é capaz de reconstruir o segredo sem ter todos os componentes, desde que o número de componentes fornecido seja maior ou igual ao quorum dado inicialmente (neste caso 5). Este programa pode ser executado da seguinte maneira: `python recoverSecretFromComponents-app.py 5 1 mykey.crt`, em que 5 é o número de componentes que se vai dar ao programa (neste caso podia ser qualquer número entre 5, o quorum, e 8, o número total de componentes), 1 é o usage id que foi dado aquando da divisão do segredo e mykey.crt é o certificado da chave privada usada para assinar os componentes. Durante a execução é-nos pedido para inserir, um a um, 5 quaisquer componentes (neste caso, é pedido o número de componentes explicitado na escrita do comando). No final, se tudo tiver sido feito corretamente, o segredo é impresso no terminal.

## Pergunta 4.1
```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            77:96:d5:5e:29:6d:01:cc:f5:0c:ed:b3:70:7b:0d:d8:42:69:55:35
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = NL, O = Staat der Nederlanden, CN = Staat der Nederlanden Burger CA - G3
        Validity
            Not Before: Apr 17 09:46:43 2019 GMT
            Not After : Nov 12 00:00:00 2028 GMT
        Subject: C = NL, O = Cleverbase ID B.V., 2.5.4.97 = NTRNL-67419925, CN = Cleverbase ID PKIoverheid Burger CA - G3
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (4096 bit)
                Modulus:
                    00:b5:78:c8:71:c2:e3:74:c2:e3:87:67:80:4a:5e:
                    8f:f5:25:aa:ff:d5:c7:a9:88:81:5c:39:8b:75:1a:
                    ce:6c:e4:a2:f2:50:39:cc:f9:d6:00:06:15:33:d1:
                    62:1f:ee:f6:ae:56:f3:dc:8f:1b:3c:35:df:be:66:
                    29:9f:83:bb:22:1b:0b:be:d5:b2:26:bd:16:06:a4:
                    8b:36:88:5b:46:a2:69:d0:2b:69:ff:98:dd:d6:8a:
                    ec:f0:6d:cf:4a:a9:53:81:be:44:0f:0b:b5:ff:4d:
                    a3:6b:2b:39:88:25:eb:41:b1:b4:2d:98:82:ec:0a:
                    0b:fd:d6:f3:9b:8d:1a:10:66:52:ae:97:6e:74:8d:
                    98:80:69:60:2e:c9:c0:b8:15:c3:d8:0d:dd:2d:4e:
                    4d:72:53:1d:2a:ff:5f:ae:47:57:cd:05:53:11:6b:
                    d4:de:47:eb:a8:bf:2d:97:1d:99:ab:c4:d0:f4:33:
                    5c:38:29:9d:84:a1:a4:d3:fd:73:fa:6c:dc:4a:f4:
                    ad:fd:d3:b2:cf:ca:d9:1d:51:0f:33:0b:23:95:eb:
                    f9:89:60:bc:a8:ca:d2:cf:4d:3e:25:52:ab:69:63:
                    f8:a3:ef:2b:c4:37:40:ed:42:67:ae:92:65:52:bb:
                    09:da:54:b6:0f:1c:44:c3:2a:5a:73:6d:f6:57:cb:
                    e6:35:3d:3d:71:cf:3f:7d:62:2d:0b:89:7e:3d:b9:
                    46:63:f8:6d:ed:f5:2a:e8:70:bd:cd:24:87:1a:d8:
                    aa:18:c4:b3:3b:25:03:9a:a8:49:19:79:35:b0:0f:
                    78:9e:1c:ca:7a:3a:f1:24:8f:8c:3e:ee:a5:0d:d2:
                    14:d9:ef:3c:e4:5b:a9:92:74:ef:20:29:19:92:39:
                    f0:af:c8:2f:b4:37:7b:c6:41:c4:a0:ae:04:bc:ac:
                    e0:7e:16:ea:0b:82:a3:16:9a:bb:30:66:1c:42:c6:
                    2d:df:f9:58:ed:ee:ee:64:72:36:ff:45:39:29:25:
                    fe:11:90:12:8c:55:e1:01:e7:61:1a:05:97:29:50:
                    e8:67:22:47:8e:f1:76:61:fa:cc:b0:65:5d:9b:5a:
                    c7:37:9a:9b:97:02:79:3b:7e:48:3e:51:02:f3:5e:
                    32:f2:71:02:29:45:6b:e3:fc:cd:0f:60:cc:5e:9c:
                    15:9f:ec:d0:18:08:cb:05:90:1b:28:cf:d4:15:82:
                    ec:40:8c:51:ce:36:9b:9e:d1:9f:72:fb:ff:3f:3e:
                    1b:67:6f:dc:3c:5c:1f:66:12:27:a6:79:2e:70:aa:
                    8a:c2:56:22:9f:57:df:7d:23:70:20:55:91:f1:7a:
                    7a:de:6e:c1:6c:e9:c9:99:3c:4b:92:bc:45:9f:22:
                    19:32:b7
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            Authority Information Access: 
                CA Issuers - URI:http://cert.pkioverheid.nl/DomBurgerCA-G3.cer

            X509v3 Subject Key Identifier: 
                F1:8E:69:8E:3E:4E:61:54:1A:CE:D6:92:94:D2:82:85:7D:FA:B9:40
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Authority Key Identifier: 
                keyid:FF:68:75:42:7D:FA:6F:C7:5A:93:38:9F:35:44:D0:AA:2D:00:B2:89

            qcStatements: 
                0.0...+.......0.......I..
            X509v3 Certificate Policies: 
                Policy: 2.16.528.1.1003.1.2.3.1
                Policy: 2.16.528.1.1003.1.2.3.2
                Policy: 2.16.528.1.1003.1.2.3.3
                  CPS: https://cps.pkioverheid.nl

            X509v3 CRL Distribution Points: 

                Full Name:
                  URI:http://crl.pkioverheid.nl/DomBurgerLatestCRL-G3.crl

            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 Extended Key Usage: 
                TLS Web Client Authentication, E-mail Protection, 1.3.6.1.4.1.311.10.3.12, Microsoft Encrypted File System, OCSP Signing
    Signature Algorithm: sha256WithRSAEncryption
         07:ed:f9:bd:6e:41:dd:72:19:03:c9:ae:b5:91:e3:36:e3:a3:
         19:5e:a7:01:55:98:75:b8:e1:00:23:77:14:20:08:19:c1:ca:
         86:c0:35:ca:9f:1e:cc:cd:03:5e:6d:11:db:b3:9d:45:e4:1e:
         58:14:51:5f:61:4f:62:d4:93:3f:e8:ce:cb:9a:24:1e:31:f7:
         ad:f9:a6:3a:b4:77:68:65:13:b3:f0:53:42:56:f0:41:6a:b1:
         ce:e7:a9:d4:17:20:9d:92:62:a4:52:cf:16:c9:f3:9d:57:c1:
         2c:17:fb:01:be:fe:87:7a:b9:5c:5d:5b:5a:5a:aa:4f:96:5f:
         ac:4a:43:3a:4c:d9:b4:29:47:a5:ae:77:10:41:39:bd:00:3b:
         6e:7b:99:50:79:db:ea:27:fe:b2:06:4b:4e:86:ab:01:84:83:
         a9:6d:41:6e:7b:b7:c7:e4:30:6e:9e:1b:94:69:44:a4:dd:e2:
         29:5d:d1:8d:5f:9d:87:2a:83:c3:91:2c:a5:0d:54:36:64:f0:
         0d:09:b7:63:66:a8:57:81:fb:4d:b0:5c:5c:4d:9d:a4:5a:5c:
         73:33:6f:92:7e:2e:b5:71:27:fa:7f:c7:ed:a5:16:63:dd:35:
         ac:4a:f5:c9:e9:65:f0:e5:05:3a:18:96:9a:23:7a:3d:4a:5e:
         64:7f:77:a8:21:5b:53:85:24:72:e1:4d:6e:21:82:e4:8e:88:
         01:8e:33:80:1e:40:43:15:3a:15:49:76:a3:f2:c3:61:4b:2e:
         a0:76:60:26:9f:7c:e6:c6:e5:60:86:df:17:20:1f:18:fe:ec:
         08:9b:8a:2d:c0:33:25:53:84:fd:3c:4a:ca:a6:e2:19:46:f9:
         9d:8c:0f:bd:f5:c0:d6:88:57:fe:dd:d2:12:ea:ab:ac:d7:ed:
         28:2c:ad:1d:50:59:ce:6f:cf:62:c5:5f:ca:8f:f6:d3:c3:6a:
         8b:6a:ba:08:fa:af:95:8f:0a:15:07:a0:21:dc:bb:ab:ca:f1:
         e8:82:f9:94:ce:99:68:57:25:3d:58:b0:16:04:1f:5f:fb:38:
         c8:5b:dd:ac:ee:a6:b7:6a:42:92:e4:b9:3c:4c:ce:a3:76:c5:
         07:3c:75:49:d2:8e:39:df:4d:51:78:87:ff:b0:d0:cc:f7:00:
         b8:67:39:45:1a:c0:b7:92:df:d3:8c:99:c2:3b:76:c8:c4:0d:
         3e:15:b1:1a:11:a9:49:9f:4f:88:21:9e:b5:87:21:78:52:26:
         fe:c2:29:37:fa:1b:00:0e:8f:6d:f2:63:77:e3:86:cb:71:fa:
         91:f2:cb:9e:29:e1:da:b7:84:b5:0f:3c:a1:f9:77:3b:f6:bb:
         8c:3b:7c:7f:8c:f7:28:d6

 ```
 
 **Algoritmo de assinatura:** SHA256 com RSA
 
 De acordo com as recomendações do [NIST de 2016](https://www.keylength.com/en/4/) o *hash* SHA256 permanecerá adequado até para além do ano 2030.
 
 **Algoritmo de Chave-Pública:** RSA
 **Tamanho da chave:** 4096 bits
 
Para a chave-pública ser considerado segura depois de 2030 a chave utilizada terá de ter, segundo o NIST, pelo menos, 3072 bits. Esta chave é de 4096 bits, e visto que tem validade até 2028 consideramos que 4096 bits é um tamanho adequado.
 
 
