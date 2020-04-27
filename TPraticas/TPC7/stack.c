#include <stdlib.h>
#include <stdio.h>
#include <string.h>
int bof(char *str)
{
	int tamanho = strlen(str);

	char *buffer = (char *) malloc (sizeof(char) * (tamanho + 1));//Alocar espaço para str + \0

	strncpy(buffer, str, tamanho);
	buffer[tamanho] = '\0';

	return 1;
}

int main(int argc, char **argv)
{
	int tamanho = 517;
	char str[tamanho];
	FILE *badfile;
	badfile = fopen("badfile", "r");
	if (badfile != NULL){ //Verificar se foi possível abrir o ficheiro badfile
		fread(str, sizeof(char), tamanho, badfile);
		bof(str);
		printf("Returned Properly\n");
		return 1;
	}
	printf("Erro ao abrir o ficheiro\n");
	return 0;
}
