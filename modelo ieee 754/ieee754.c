//rascunho exercicio mc
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

typedef struct {
    __int64 mantissa;
    __int64 expoente;
}ieee;

ieee bin;

__int64 separa_mantissa(__int64 binario, __int64 mantissa){
    if(binario == 0){
        return 0;
    }else{
        __int64 value = mantissa;
        value = value &9.0071993e+15;
        printf("\n valor da mantissa = %d\n", value);
        return value;
    }
}

__int64 separa_expoente(__int64 binario){
    if(binario == 0){
        return 0;
    }else{
        __int64 value = binario;
        value = value >> 52 &2047
        printf("\n valor do expoente = %d\n", value);
        return value;
    }
}

int main(){
    char entrada[64];
    printf("\nInsira o binario do numero que deseja descobrir a mantissa e o valor do expoente OBS:64 bits\n");
    fgets(entrada, 64, stdin);
    char mantissa[64];
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
    __int64 binario;
    __int64 mantissaint;
    binario = _atoi64(entrada);
    mantissaint = _atoi64(mantissa);
    ieee.mantissa = separa_mantissa(binario, mantissaint);
    ieee.expoente = separa_expoente(binario);
}