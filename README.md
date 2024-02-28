## Automação de Extração de Extratos Bancários

Esta automação em Python foi desenvolvida para automatizar o processo de extração de extratos bancários do site do Itaú. A colaboração neste projeto inclui contribuições significativas de Richard Arias.

### Objetivo

O objetivo principal deste script é simplificar a tarefa de baixar extratos bancários do Itaú num total de "X" contas dispostas em um documento excel, automatizando as interações necessárias através do navegador Google Chrome. O script realiza ações como login, seleção de contas, download de extratos e salvando em local específico, tornando o processo mais ágil e eficiente.

### Pré-requisitos

Antes de executar o script, certifique-se de ter o seguinte configurado:

- Python 3.x instalado
- Bibliotecas necessárias: Selenium, PyAutoGUI, Pandas
  ```bash
  pip install selenium pyautogui pandas
  ```
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) instalado e configurado

### Configuração

Antes de executar o script, é necessário configurar as opções do Chrome no arquivo `script.py` para atender às suas necessidades específicas. As opções podem incluir argumentos de inicialização do Chrome, como tamanho da janela e localização do driver.

```python
# Configuração do Chrome
options = Options()
# Adicione as opções desejadas
```

### Execução

Siga os passos abaixo para executar o script:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script:
   ```bash
   python script.py
   ```

### Colaborador

- Richard Arias: Contribuições significativas na melhoria do código e otimização de interações.

### Aviso Importante

Este script realiza automação em um site bancário. Antes de utilizar, certifique-se de entender e seguir os termos de serviço do site e as leis locais relacionadas à automação de interações com instituições financeiras. 

**Proteja informações sensíveis, como senhas e dados bancários, e utilize com responsabilidade.**

### Personalização

O script pode ser personalizado para atender às necessidades específicas do usuário. Algumas modificações sugeridas incluem:

- Atualização do local do arquivo Excel contendo as contas bancárias (`'base.xlsx'`).
- Ajustes nos caminhos de salvamento dos extratos.
- Adaptação para diferentes sites bancários, se necessário.

### Autor

[ Lauro Bonometti ]

### Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.

---

