//rascunho exercicio mc
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

typedef struct {
    int64_t mantissa;
    int64_t expoente;
}ieee;

ieee bin;

int64_t separa_mantissa(int64_t binario, int64_t mantissa){
    //printf("Entrou na funcao da mantissa");
    if(binario == 0){
        printf("\nO valor da mantissa é 0\n");
        return 0;
    }else{
        int64_t value = mantissa;
        value = value &9007199300000000;
        printf("\n valor da mantissa = %ld\n", value);
        return value;
    }
}

int64_t separa_expoente(int64_t binario){
    //printf("Entrou na funcao do expoente");
    if(binario == 0){
        printf("\nO valor do expoente é 0\n");
        return 0;
    }else{
        int64_t value = binario;
        value = value >> 52 &2047;
        printf("\n valor do expoente = %ld\n", value);
        return value;
    }
}

int main(){
    char entrada[64];
    printf("\nInsira o binario do numero que deseja descobrir a mantissa e o valor do expoente OBS:64 bits\n");
    fgets(entrada, 64, stdin);
    char mantissa[64];
    //printf("Chegou aqui");
    for(int i = 0; i < 64; i++){
        if (i<11){
            mantissa[i] = '0';
        }
        else if(i==11){
            mantissa[i] = '1';
        }else{
            mantissa[i] = entrada[i];
        }
    }
    //printf("Chegou aqui 2");
    int64_t binario;
    int64_t mantissaint;
    binario = atoll(entrada);
    printf("%ld, entrada\n", binario);
    mantissaint = atoll(mantissa);
    printf("%ld, mantissa\n", mantissaint);
    bin.mantissa = separa_mantissa(binario, mantissaint);
    bin.expoente = separa_expoente(binario);
}