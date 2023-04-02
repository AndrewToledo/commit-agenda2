# commit-agenda2
Esse formulario, que é responsável por coletar informações preenchidas em campos de um formulário (nome, sexo, telefone e email), armazená-las em uma lista chamada "dados", verificar se todos os campos foram preenchidos e, se sim, adicionar essas informações em um banco de dados. Se os dados forem adicionados com sucesso, uma mensagem de sucesso será exibida e os campos do formulário serão limpos. Por fim, a função "mostrar_dados" é chamada para atualizar a visualização dos dados armazenados no banco de dados.

![formulario1](https://user-images.githubusercontent.com/65566371/229381038-3a0d4c9d-a558-4678-815d-a68684b73714.png)


![formulario2](https://user-images.githubusercontent.com/65566371/229381051-c159e22b-0bfa-476c-b1c0-f12814d50875.png)


![formulario3](https://user-images.githubusercontent.com/65566371/229381062-b007bf32-d536-4e22-8771-005c19849882.png)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
![inserir](https://user-images.githubusercontent.com/65566371/229377159-9518e243-a5de-4d09-8bac-d6df7fdefbde.png)

![erro1](https://user-images.githubusercontent.com/65566371/229377266-5470e4b6-a5bd-43ca-8abd-c0503d637511.png)


![adicionadossucesso](https://user-images.githubusercontent.com/65566371/229377348-18fca361-bf1a-4b03-9777-f35168254235.png)


Esse código é uma função chamada "inserir". O objetivo dela é capturar os dados inseridos pelo usuário em campos nome, sexo, telefone e email e adicioná-los em uma lista chamada "dados". Em seguida, é feita uma verificação para verificar se todos os campos foram preenchidos e, caso contrário, uma mensagem de aviso é exibida. Se todos os campos foram preenchidos, a lista "dados" é passada como argumento para a função "adicionar_dados", que adiciona esses dados a um banco de dados. Em seguida, uma mensagem de confirmação é exibida e os campos são limpos. Por fim, é chamada a função "mostrar", que atualiza a lista de dados exibida na tela.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Esse código define uma função chamada "atualizar", que é responsável por atualizar os dados de um item selecionado em uma tabela. 

Primeiro, a função tenta obter os dados do item selecionado na tabela. Se não houver nenhum item selecionado, a função exibe uma mensagem de erro. Caso contrário, a função extrai os valores do item selecionado e os preenche nos campos de entrada correspondentes (nome, sexo, telefone e email).

Em seguida, a função define uma nova função chamada "confirmar", que é responsável por obter os novos valores dos campos de entrada e atualizar os dados do item selecionado na tabela. Quando os novos dados são atualizados com sucesso, a função exibe uma mensagem de sucesso e limpa os campos de entrada.

Por fim, a função cria um botão "Confirmar" que, quando clicado, chama a função "confirmar" para atualizar os dados do item selecionado na tabela. Se nenhum item estiver selecionado na tabela, o botão não será criado e a função "atualizar" exibirá uma mensagem de erro.


![atualizarcodigo](https://user-images.githubusercontent.com/65566371/229379417-95a02a86-a680-48eb-9d60-1b7866e20847.png)


![atualizadosucesso](https://user-images.githubusercontent.com/65566371/229379167-67aceb15-95fa-4f60-aea9-b51a0d112fc1.png)

![atualizarnot](https://user-images.githubusercontent.com/65566371/229379304-3b8cc0ef-e61e-457e-be6b-9b6169ca46a7.png)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


![removecodigo](https://user-images.githubusercontent.com/65566371/229379676-8ebd7e61-9fc2-49aa-a780-b8edb341d739.png)

![removesuceful](https://user-images.githubusercontent.com/65566371/229379709-1f651bf6-2fc1-4ed5-af93-e14830bfcfe2.png)

![removeerror](https://user-images.githubusercontent.com/65566371/229379749-6b6ae537-42fe-4f0c-9406-3e84ae1d05d9.png)



Este código define uma função chamada "remover" que é responsável por excluir um registro da tabela exibida na interface do usuário. 

A função tenta obter informações do registro selecionado na tabela, como o valor da terceira coluna, que é armazenado na variável "valor". Em seguida, a função chama outra função chamada "remover_dados" para excluir o registro do banco de dados.

Se a exclusão for bem-sucedida, uma caixa de mensagem será exibida informando o sucesso da operação. Em seguida, a função limpa a tabela da interface do usuário e a atualiza com os registros restantes. 

Se nenhum registro for selecionado na tabela ou ocorrer um erro ao tentar excluir o registro, uma caixa de mensagem de erro será exibida.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------







![procuraron](https://user-images.githubusercontent.com/65566371/229380148-034c2967-79c0-48b8-a3fa-94cfcd5b2dcb.png)




![procurarfoi2](https://user-images.githubusercontent.com/65566371/229380151-e0a3e948-b12c-4386-8f7e-ae323de28e75.png)


Esse código define uma função chamada "procurar", que é chamada quando o usuário clica em um botão. A função começa obtendo um número de telefone da caixa de entrada "e_procurar". Em seguida, ela chama outra função chamada "procurar_dados" para obter informações relacionadas a esse número de telefone. 

A função então define outra função chamada "delete_command", que é usada para limpar todas as linhas de uma tabela chamada "tree". Em seguida, a função chama essa função para limpar a tabela.

A função então itera sobre as informações obtidas da função "procurar_dados" e adiciona cada item como uma nova linha na tabela "tree".

Por fim, a função limpa o conteúdo da caixa de entrada "e_procurar" para que o usuário possa inserir um novo número de telefone.
