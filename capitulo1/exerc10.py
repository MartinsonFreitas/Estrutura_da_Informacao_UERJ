from EstruturasSimplificadas import *

def exerc10(string):
    # Uma string casada é uma sequência de caracteres {, }, (, ), [, e ] que
    # estejam casados corretamente. Por exemplo, {{()[]}} é uma string
    # casada, porém {{()]} não é, pois o segundo { casa com um ]. Mostre
    # que uma pilha pode ser usada para isso de tal modo que dada uma string
    # de tamanho n, você possa determinar se ela é uma string casada no tempo O(n).
    
    # Escreva aqui sua resposta para o exercício 10. Sua resposta deve retornar 
    # True ou False de acordo com o resultado do casamento da string.
   # Crie uma pilha vazia
    pilha = Pilha()
    correspondentes = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in correspondentes.values():  # Empilha aberturas
            pilha.push(char)
        elif char in correspondentes.keys():  # Processa fechamentos
            try:
                if pilha.pop() != correspondentes[char]:
                    return False
            except IndexError:  # Pilha vazia = fechamento sem abertura
                raise IndexError("Fechamento sem abertura correspondente")
        else:  # Caractere inválido
            return False
    
    return pilha.size() == 0  # True se a pilha estiver vazia

    

if __name__ == "__main__":
    exerc10("{{()[]}") # Não é uma string casada
    exerc10("{{()[]}}") # É uma string casada
    exerc10("{{()]}") # Não é uma string casada
    exerc10("{{()[]}}{") # Não é uma string casada
    exerc10("{{()[]}}{}") # É uma string casada
    exerc10("{{()[]}}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{}{") # Não é uma string casada
    exerc10("") # É uma string casada
