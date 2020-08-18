#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define TAM 100

void inicio (char word[TAM], size_t size);
void q0(size_t cont, char word[TAM], size_t size);
void q1(size_t cont, char word[TAM], size_t size);
void q2(size_t cont, char word[TAM], size_t size);
void q3(size_t cont, char word[TAM], size_t size);
void q4(size_t cont, char word[TAM], size_t size);
void q5(size_t cont, char word[TAM], size_t size);
void qFim();
void qErro();

int main (){
    char word[TAM];
    char flag[] = "exit";
    size_t size = 0;
    while(1){
        printf("Informe uma palavra: \n");
        gets(word);
        fflush(stdin);
        if(strcmp(word, flag)==0){
            printf("Finalizando...\n");
            break;
        }else{
            while(word[size] != '\0'){
                size++;
            }
            inicio(word, size);
        }
    }   
  return 0;
}
void inicio (char word[TAM], size_t size){
    size_t cont = 0;
    q0 (cont, word, size);
}
void q0(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q1( cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q2(cont, word, size);
        }else if((word[cont] == 'E') || (cont == size)){
            qFim();
        }else{
            qErro();
        }
    }
}
void q1(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q0(cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q1(cont, word, size);
        }else{
            qErro();
        }
    }
}
void q2(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q5(cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q4(cont, word, size);
        }else{
            qErro();
        }
    }
}
void q3(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q4(cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q5(cont, word, size);
        }else{
            qErro();
        }
    }
}
void q4(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q2(cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q3(cont, word, size);
        }else if(cont == size){
            qFim();
        }else{
            qErro();
        }
    }
}
void q5(size_t cont, char word[TAM], size_t size){
    if(cont < TAM){
        if (word[cont] == 'b'){
            cont ++;
            q3(cont, word, size);
        }else if(word[cont] == 'a'){
            cont ++;
            q2(cont, word, size);
        }else if(cont == size){
            qFim();
        }else{
            qErro();
        }
    }
}
void qErro(){
    printf("Palavra rejeitada pelo autmato programado\n");
}
void qFim(){
    printf("Palavra aceita pelo automato programado\n");
}

