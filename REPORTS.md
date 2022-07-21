# 1º Relatóio: Etapa AI-a (Analisador Léxico e Sintático)

1. Qual é o nome do relator?

    > Mateus Leal Gonçalves

2. A etapa foi completamente ou parcialmente concluída?

    > Parcialmente concluído

3. No caso de parcialmente concluída, o que não foi concluído?

    > O tratamento de erros do Parser não está contemplando todos os erros das gramática, porém os erros presentes nos exemplos foram capturados.

4. O programa passa nos testes automatizados?
    
    > Não passou nos testes automatizados, devido a duas falhas

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?
    
    > Foram executados 46 testes e 2 falhas foram encontradas, uma referente à quantidade de tokens e outra à quantidade de token MINUS

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    
    > - Compreender o funcionamento da biblioteca SLY
        - Remoção de ambiguidades da gramática da linguagem minijava, sendo necessário repensar a gramática, devido ao fato que ela é apresentada como uma expressão regular.
        - Identificar os erros de sintaxe fornecidos pelo SLY e fazer o tratamento no parser.

7. Qual a participação de cada membro da equipe na etapa de execução?
    
    > O trabalho foi realizado em conjunto por todos os integrantes, as reuniões foram realizadas por meio de conferências online (Discord) com o intuito de debater sobre a implementação e implementar. Todos os integrantes participaram ativamente da construção do Parser e do Lexer.


# 2º Relatório: Etapa AI-b (Árvores Sintática Abstrata e Análise Semântica)

1. Qual é o nome do relator?

    > Gabriel Marques Maranhão

2. A etapa foi completamente ou parcialmente concluída?

    > Parcialmente concluído

3. No caso de parcialmente concluída, o que não foi concluído?

    > Alguns erros de semântica não foram identificados.

4. O programa passa nos testes automatizados?
    
    > Não passou nos testes automatizados dos seguintes arquivos de análise semântica:
       -  SemanticFaultyReturnTypeAndArgTypeUsage.java

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?

    > Foram executados 73 testes e 1 falha foi encontrada:
        - SemanticFaultyReturnTypeAndArgTypeUsage.java
          - Falha: 
                File "D:\semestre 7\Compiladores\Trabalho 2\PyMJCG07\tests\test_semantic.py", line 188, in 
                    test_number_of_return_type_mismatch self.assertEqual(actual, expected, test_file_name) AssertionError: 2 != 1 : SemanticFaultyReturnTypeAndArgUsage.java

        Além disso, outras falhas que não eram semânticas foram contornadas com mudanças nos arquivos de teste, e estão comentadas nos mesmos.

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    
    > - Entendimento do visitor (TypeChecking e FillSymbolTable) e classes do AST
    > - Dificuldades no debug 
        - Confusão em que parte do visitor estavam ocorrendo erros semânticos, retornos None.
  

7. Qual a participação de cada membro da equipe na etapa de execução?

    > O trabalho foi realizado em conjunto por todos os integrantes, as reuniões foram realizadas por meio de conferências online (Discord) com o intuito de debater sobre a implementação e implementar. Todos os integrantes participaram ativamente da implementação.


# 3º Relatóio: Etapa AI-c (Tradução para o Código Intermediário)

1. Qual é o nome do relator?

    > Mateus Leal Gonçalves

2. A etapa foi completamente ou parcialmente concluída?

    > Parcialmente, adicionalmente às mudanças feitas anteriormente, foram feitas algumas melhorias nos visitors do if, while, arraylookup, newarray e arrayassign, utilizando os métodos RelCx e IfThenElseExp
3. No caso de parcialmente concluída, o que não foi concluído?

    > Não temos certeza se as mudanças feitas são o suficiente

4. O programa passa nos testes automatizados?
    
    > Não existem testes

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?
    
    > Não existem testes

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    
    > Compreender quais visitors deveriamos modificar, além disso, entender como melhorar e quais métodos novos utilizar

7. Qual a participação de cada membro da equipe na etapa de execução?
    
    > O trabalho foi realizado em conjunto por todos os integrantes, as reuniões foram realizadas por meio de conferências online (Discord) com o intuito de debater sobre a implementação e implementar. Todos os integrantes participaram ativamente da implementação.


# 4º Relatóio: Etapa AI-d (Seleção de Instruções)

1. Qual é o nome do relator?

    > Escreva sua resposta aqui

2. A etapa foi completamente ou parcialmente concluída?

    > Escreva sua resposta aqui

3. No caso de parcialmente concluída, o que não foi concluído?

    > Escreva sua resposta aqui

4. O programa passa nos testes automatizados?
    
    > Escreva sua resposta aqui

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?
    
    > Escreva sua resposta aqui

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    
    > Escreva sua resposta aqui

7. Qual a participação de cada membro da equipe na etapa de execução?
    
    > Escreva sua resposta aqui


# 5º Relatóio: Etapa AI-e (Alocação de Registradores)

1. Qual é o nome do relator?

    > Gabriel Marques Maranhão

2. A etapa foi completamente ou parcialmente concluída?

    > Parcialmente concluída

3. No caso de parcialmente concluída, o que não foi concluído?

    > A tradução do arquivo RegAlloc não foi feita, e o método build_interference_graph() não foi concluído.

4. O programa passa nos testes automatizados?
    
    > Não existem testes automatizados

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?
    
    > Não existem testes automatizados

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    > Dificuldade de entender como construir o grafo de interferências, além da falta de tempo devido à uma má organização do nosso tempo e ao choque de horários com atividades de outras disciplinas, o que tornou inviável a implementação das seções mais extensas desse código.

7. Qual a participação de cada membro da equipe na etapa de execução?

   > O trabalho foi realizado em conjunto por todos os integrantes, as reuniões foram realizadas por meio de conferências online (Discord) com o intuito de debater sobre a implementação e implementar. Todos os integrantes participaram ativamente da implementação.



# 6º Relatóio: Etapa AI-f (Integração e Geração do Código Final)

1. Qual é o nome do relator?

    > Escreva sua resposta aqui

2. A etapa foi completamente ou parcialmente concluída?

    > Escreva sua resposta aqui

3. No caso de parcialmente concluída, o que não foi concluído?

    > Escreva sua resposta aqui

4. O programa passa nos testes automatizados?
    
    > Escreva sua resposta aqui

5. Algum erro de execução foi encontrado para alguma das entradas? Quais?
    
    > Escreva sua resposta aqui

6. Quais as dificuldades encontradas para realização da etapa do projeto?
    
    > Escreva sua resposta aqui

7. Qual a participação de cada membro da equipe na etapa de execução?
    
    > Escreva sua resposta aqui