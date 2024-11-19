import Pessoa
import os
def limpar():os.system('cls')

res = 0
limpar()
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÂO: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("Digite o nome da pessoa: "))
    idade = int(input("Digite a idade da pessoa: "))
    cargo = str(input("Digite o cargo da pessoa: "))
    salario = float(input("Digite o salario da pessoa: "))
    
    cadastro.append(Pessoa.Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("Nº","Nome","Idade","Cargo","Salário"))
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format(y,
                  x.get_nome(),
                  x.get_idade(),
                  x.get_cargo(),
                  x.get_salario()
              ))
        y =+1
def alterar(x,y,z):
    if(y==0): cadastro[x].set_nome(z)
    if(y==1): cadastro[x].set_idade(z)
    if(y==2): cadastro[x].set_cargo(z)
    if(y==3): cadastro[x].set_salario(z)

alterar(0,0,"Caique")
mostrar()
