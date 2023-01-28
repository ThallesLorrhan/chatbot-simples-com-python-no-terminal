import os 
def processar_resposta(resposta,nome):
   if resposta == '1':
      print(f"{ os.linesep}{nome} este chat funciona 100% em python através de uma pequena capitassão de seus dados e com resposta já programadas{ os.linesep}")
   elif resposta == '2':
      print(f"{ os.linesep}{nome} nós podemos fazer que você saiba tudo sobre nosso chat :) { os.linesep}")
   else:
       print("digite apenas 1 e 2")
  
def start():
         #apresentar o chatbot
         print("ola bem vindo a central do chtabot")
         #pedir seu nome
         nome = input("Digite seu nome: ")
         #pedir o email
         email = input("Digite seu email: ")
         while True:
            #oferecer uma menu de opções
            resposta = input(
               f'Oque gostaria de saber hoje?{os.linesep}[1] - como funciona o nosso chat?{os.linesep}[2] - Oque a gente pode fazer por você?{os.linesep}'
               ) 
               #precessar a resposta enviada
            processar_resposta(resposta,nome)
    
# criando um ambiente
if __name__ == '__main__':
 start()