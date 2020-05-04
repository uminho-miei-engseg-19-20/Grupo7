# TPC8 - Aula10

## Pergunta P1.1

### 1. Qual a vulnerabilidade que existe na função *vulneravel()* e quais os efeitos da mesma?

A vulnerabilidade consiste na declaração de `i` e `j` como inteiros, sendo depois utilizados num ciclo em que são comparados com um `size_t`, sendo que este é um unsigned integer cujo tamanho depende do compilador utilizado (mas é garantido ser grande o suficiente para conter o maior objeto que o sistema suporta).

Ao verificar os tamanhos máximos de `int` e `size_t` obtemos os seguintes resultados:
  - Max int size: 2147483647
  - SIZE_MAX (tamanho máximo de `size_t`): 18446744073709551615
  
Assim, se o tamanho das variáveis `x` e  `y` for grande o suficiente é possível que, nos ciclos *for* de *vulneravel()*, ocorra um overflow dos inteiros `i` e `j` o que resulta em ciclos infinitos. No entanto, tentar executar `matriz[i*y+j] = valor;` depois de ocorrer o overflow resultará num segmentation fault.

### 2. Complete o *main()* de modo a demonstrar essa vulnerabilidade.

```
int main() {
  char *matriz;
  vulneravel(matriz, 2147483647, 2147483647, 1);
}
```

### 3. Ao executar dá algum erro? Qual?

Ao executar ocorre um segmentation fault.

## Pergunta P1.2

### 1. Qual a vulnerabilidade que existe na função *vulneravel()* e quais os efeitos da mesma?

Na função vulnerável não é feita nenhuma verificação do tamanho da variàvel `tamanho` (que é do tipo `size_t`) para garantir que este não é 0 antes de entrar na condição *if*. Se `tamanho` for 0, ocorrerá underflow quando a este valor for subraída uma unidade (`tamanho_real = tamanho - 1;`) para criar `tamanho_real` (que também é `size_t`), passando esta nova a ter o tamanho máximo permitido (pois `size_t` é um unsigned integer).

Neste caso, o resultado de `destino = (char *) malloc(tamanho_real);` será NULL, o que significa que `memcpy(destino, origem, tamanho_real);` não terá sucesso e resultará em segmentation fault.

### 2. Complete o *main()* de modo a demonstrar essa vulnerabilidade.

```
int main() {
  char *origem = 'talco';
  vulneravel(origem, 0);
}
```

### 3. Ao executar dá algum erro? Qual?

Ao executar ocorre um segmentation fault.

### 4. Utilize as várias técnicas de programação defensiva introduzidas na aula teórica para mitigar as vulnerabilidades. Explique as alterações que fez.

```
void vulneravel (char *origem, size_t tamanho) {
        size_t tamanho_real;
        char *destino;
        if (tamanho < MAX_SIZE && tamanho > 0) {
                tamanho_real = tamanho - 1; // Não copiar \0 de origem para destino
                destino = (char *) malloc(tamanho_real);
                memcpy(destino, origem, tamanho_real);
        }
}
```
