 coletor-de-precos-automaticos

O script segue as seguintes etapas:

- Abrir o navegador: Usa o WebDriver do Chrome para acessar o site desejado.
- Aguardar o carregamento da página: Aplica um sleep(5) para garantir que os elementos necessários estejam visíveis.
#- Extrair informações:
- Coleta os nomes dos produtos usando XPath.
- Obtém os preços correspondentes também via XPath.
#- Salvar os dados em CSV: Itera pelos produtos e preços e grava os dados no arquivo produtos.csv.

