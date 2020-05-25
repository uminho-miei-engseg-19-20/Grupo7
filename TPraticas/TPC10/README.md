# TPC10 - Aula12

## Pergunta P1.1

#### Concept (1)

Na primeira janela é explicado o que se pretende fazer, não sendo necessário completar nenhuma ação.

#### What is SQL? (2)

Na segunda janela é pedido que se escreva uma *query* que nos permita saber o departamento no qual o empregado 'Bob Franco' trabalha. Para tal foi inserida a seguinte *query*: `SELECT department FROM employees WHERE first_name = 'Bob' AND last_name = 'Franco';`.

#### Data Manipulation Language (DML) (3)

Aqui é pedido que se modifique o valor de *department* para o empregado 'Tobi Barnett'. Isto é feito através da *query* `UPDATE employees SET department = 'Sales' WHERE first_name = 'Tobi' AND last_name = 'Barnett';`.

#### Data Definition Language (DDL) (4)

É pedido que se adicione uma coluna chamada "phone" á tabela. Para tal insere-se a *query* `ALTER TABLE employees ADD phone varchar(20);`.

#### Data Control Language (DCL) (5)

É pedido que criemos uma *query* que dê ao grupo "UnauthorizedUsers" permissão para alterar tabelas. Isso pode ser feito da seguinte maneira: `GRANT ALTER TABLE TO UnauthorizedUser;`.

#### What is SQL injection? (6)

Não é feito nenhum pedido.

#### Consequences of SQL injection (7)

Não é feito nenhum pedido.

#### Severity of SQL injection (8)

Não é feito nenhum pedido.

#### Try It! String SQL injection (9)

Nesta janela é pedido que se complete a *query* apresentada de modo a que sejam mostrados todos os utilizadores da tabela. A *query* completa é: `SELECT * FROM user_data WHERE first_name = 'John' and last_name = 'Smith' or '1' = '1'`.

#### Try It! Numeric SQL injection (10)

Aqui é pedido que coloquemos o *input* necessário em "Login_Count" e "User_ID" de maneira a que a seguinte *query* devolva toda a informação da tabela. A query que deve ser completada é `SELECT * FROM user_data WHERE login_count = " + Login_Count + " AND userid = "  + User_ID;`.

Esta tarefa pode ser completa ao colocar o input que resulte na seguinte *query*: `SELECT * From user_data WHERE Login_Count = 1 and userid= 1 OR '1' = '1';`.

#### Compromising confidentiality with String SQL injection (11)

É pedido que se inisira *input* de modo a que a partir da *query* mostrada de seguida seja possível ver toda a informação da tabela
```
"SELECT * FROM employees WHERE last_name = '" + name + "' AND auth_tan = '" + auth_tan + "';
```
Existem várias formas de completar o pedido, mas que utilizámos neste caso foi `SELECT * FROM employees WHERE last_name = 'das' OR '1' = '1';--" + name + "' AND auth_tan = '" + auth_tan + "';`.

#### Compromising Integrity with Query chaining (12)

Nesta janela é pedido que se altere o valor do nosso salário, sendo que neste caso somos o empregado "John **Smith**" cujo TAN é "3SL99A". Tendo em conta que na janela anterior já tivemos acesso a toda a informação da tabela podemos utilizar o seguinte *input* para o parâmetro "last_name" de modo cumprir o nosso objetivo: `dasda'; UPDATE employees SET salary = 100000 WHERE last_name = 'Smith' AND auth_tan = '3SL99A';--`. 

Assim sendo a *query* completa fica algo deste género: `"SELECT * FROM employees WHERE last_name = 'dasda'; UPDATE employees SET salary = 100000 WHERE last_name = 'Smith' AND auth_tan = '3SL99A';--" + name + "' AND auth_tan = '" + auth_tan + "';`.

#### Compromising Availability (13)

Aqui é pedido que se insira uma *search string* de modo a conseguir apagar a tabela *access_log*. Para o fazer podemos inserir `asad'; DROP TABLE access_log;--`.

## Pergunta 2.1

Apenas são demonstrados os passos com questões. Todos os passos não referidos serviam apenas para fornecer conhecimento.

#### Passo 2

Depois de aberta a consola em dois separadores diferentes, e executado o comando `alert(document.cookie);` é possível observar que as cookies em ambas as tabs são a mesma.

#### Passo 7

Neste passo, o objetivo era perceber quais os inputs que não faziam a validação correta de injeção de scripts. Para tal foi inserido o comando `<script>alert('Vulnerável')</script>` em ambas as caixas, sendo possível perceber que a caixa do número do cartão é vulnerável a ataques de injeção, pois surgiu um alerta 'Vulneravél' aquando da submissão. Na caixa do código de acesso aquando a submissão do script, o mesmo foi rejeitado surgindo a mensagem ` Seems like  you tried to compromise our shop with a reflected XSS attack. We do ...our "best"... to prevent such attacks. Try again!`.

#### Passo 10

Foi analisado o ficheiro `GoatRouter.js` com o objetivo de descobrir as rotas existentes, sendo descoberta a linha `'test/:param':'testRoute`. Assim sendo, foi possível descobrir que a rota para o test code era `start.mvc#test/`.

#### Passo 11

Depois de descoberto a rota para o test code, e sabendo que queriamos executar a ação `webgoat.customjs.phoneHome()` foi inserido o seguinte URL `http://localhost:8080/WebGoat/start.mvc#test/<script>webgoat.customjs.phoneHome()<%2Fscript>`. De notar que é utilizado `%2F` ao invés da barra de fecho do script, para evitar confusões com a barra de separadores de routes. Depois de introduzido este URL, fomos à consola onde estava esta mensagem `phone home said {"lessonCompleted":true,"feedback":"Congratulations. You have successfully completed the assignment.","output":"phoneHome Response is -563512430","assignment":"DOMCrossSiteScripting","attemptWasMade":true}`. Assim sendo, foi possível concluír que a resposta era -563512430.

#### Passo 12

As respostas às questões são as seguintes:
- P1->4
- P2->3
- P3->1
- P4->2
- P5->4

## Pergunta P3.1

#### Passo 2

É-nos pedido que fazer *reset* da password e depois login para verificar se conseguimos ler e-mails com o WebWolf. 

Primeiro acede-se à página de *reset* da password onde se coloca o e-mail do utilizador que registámos no WebGoat (\<user\>@webgoat.org) e fazemos o pedido de uma nova password.

Depois disso acede-se ao WebWolf e faz-se login com os dados da conta que registámos no WebGoat. Aí abre-se o e-mail com a nova password e usa-se esta para fazer o login que era pedido no início.

#### Passo 4

É pedido que se descubra a password de um outro utilizador através da pergunta secreta, o que implica dar a resposta certa à pergunta. 

Neste caso, através de força bruta é possível descobrir a resposta à pergunta de segurança de cada utilizador, visto que não há mecanismo de lock-out. 

Como exemplo, resposta à pergunta de segurança do utilizador 'admin' é 'green'.

#### Passo 5

Para completar este passo basta verificar as razões pelas quais 2 pergutas de segurança comuns não são assim tão seguras.

#### Passo 6

O objetivo neste passo é fazer o *reset* da password do Tom e depois fazer login na sua conta.

Para isso vamos usar o burp para intercetar o tráfego (para que o Tom não receba o e-mail e torne o link inútil para os nossos propósitos).

Antes de utilizar o burp devemos pô-lo à escuta numa porta, que no nosso caso será a porta 8080 e mudar o proxy do browser para o mesmo do burp. Para além disso é necessário importar o certificados para o browser, que podem ser gerados no burp.

Quando é feito um novo pedido de *reset* de password para o utilizador Tom vemos que o pedido é intercetado no burp. Assim, basta mudar o parâmetro "Host" para redirecionar-lo para o WebWolf (no nosso caso é alterar a porta para a 9090).

No WebWolf basta ir a "Incoming requests" e teremos acesso ao link original para fazer o *reset* da password do Tom. Assim sendo, para alterar a password basta pegar no link e trocar a porta 9090 pela porta 8080.

Assim o link de *reset* http://localhost:9090/WebGoat/PasswordReset/reset/reset-password/83ad89c9-5821-47aa-bc24-c9c4224609ab passa a ser http://localhost:8080/WebGoat/PasswordReset/reset/reset-password/83ad89c9-5821-47aa-bc24-c9c4224609ab.

Acedendo ao link é possível trocar a password da conta do Tom e assim ganhar acesso à sua conta.

## Pergunta 4.1

Apenas são demonstrados os passos com questões. Todos os passos não referidos serviam apenas para fornecer conhecimento.

#### Passo 5

Neste passo, o objetivo é executar o mesmo código fonte `<script>alert('XSS')</script>`, mas utilizando versões diferentes do `jquery-ui`. Na versão mais antiga, `jquery-ui:1.10.4`, é possível observar que o script é executado. Na versão mais recente, `jquery-ui:1.12.0`, o script já não executa.

#### Passo 12

Para este passo o objetivo era introduzir a nossa própria versão de XML de um contacto. Foi introduzido 
```xml
    <contact>
        <java.lang.Integer>1</java.lang.Integer>
        <firstName>Bruce</firstName>
        <lastName>Mayhew</lastName>
        <email>webgoat@owasp.org</email>  
    </contact>
``` 
onde `<id>1</id>` foi substituído por `<java.lang.Integer>1</java.lang.Integer>`.

