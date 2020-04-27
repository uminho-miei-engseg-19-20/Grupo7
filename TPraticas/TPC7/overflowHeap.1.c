#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) {
	if (argc != 2){
		printf("Faltam argumentos\n");
		return 0;
	}
	int tamanhoArgv = strlen(argv[1]); //Tamanho do argv1

    char *dummy = (char *) malloc (sizeof(char) * (tamanhoArgv + 1)); //Alocar espaço para o argv1 e \0
    char *readonly = (char *) malloc (sizeof(char) * 9); //Alocar espaço para "laranjas" + \0
    
    strncpy(readonly, "laranjas",8);
    strncpy(dummy, argv[1],tamanhoArgv);
    
    readonly[8]='\0';
    dummy[tamanhoArgv]='\0';

    printf("%s\n", readonly);
    printf("%s\n", dummy);

    return 1;
}
