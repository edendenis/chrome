#!/usr/bin/env python
# coding: utf-8

# <!-- LOGOTIPO DO PROJETO -->
# <div style="display: flex; justify-content: center;">
#    <a href="https://github.com/edendenis/readme_set_up_install_use_google_chrome_in_linux_ubuntu">
#      <img src="figures/gold_edf_technology_logo_transparent_background_and_gold_name.png" alt="Logo" width="160" height="160">
#    </a>
# </div>
# 
# <h3 align="center">Configurar/instalar/usar o `Google Chrome` no `Linux Ubuntu`</h3>
# 
# <!-- <div style="display: flex; justify-content: center;">
#   <a href="https://zenodo.org/doi/10.5281/zenodo.10668919">
#     <img src="https://zenodo.org/badge/758237447.svg" alt="DOI">
#   </a>
# </div> -->
# 
# <p align="center">
#  Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Google Chrome` no `Linux Ubuntu`.
#  <br />
#  <a href="https://github.com/edendenis/readme_set_up_install_use_google_chrome_in_linux_ubuntu"><strong>Explore os documentos »</strong></a>
#  <br />
#  <br />
#  <a href="https://github.com/edendenis/readme_set_up_install_use_google_chrome_in_linux_ubuntu">Ver demonstração</a>
#  ·
#  <a href="https://github.com/edendenis/readme_set_up_install_use_google_chrome_in_linux_ubuntu">Relatar bug</a>
#  ·
#  <a href="https://github.com/edendenis/readme_set_up_install_use_google_chrome_in_linux_ubuntu">Solicitar recurso</a>
# </p>
# 

# # Como configurar/instalar/usar o `Google Chrome` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Google Chrome` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use the `Google Chrome` on `Linux Ubuntu`._

# ### Construído com
# 
# Esta seção deve listar todas as principais estruturas/bibliotecas usadas para inicializar seu projeto. Deixe quaisquer complementos/plugins para a seção de agradecimentos. Aqui estão alguns exemplos.
# 
# * [![Python 3.8](https://img.shields.io/badge/Python%203.8-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
# 
# * [![Anaconda](https://img.shields.io/badge/Anaconda-44A833?style=flat-square&logo=anaconda&logoColor=white)](https://www.anaconda.com/)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- COMEÇANDO -->
# ### Começando
# 
# Este é um exemplo de como você pode dar instruções sobre como configurar seu projeto localmente.
# Para obter uma cópia local instalada e funcionando, siga estas etapas simples de exemplo.
# 
# ### Pré-requisitos
# 
# Este é um exemplo de como listar os itens necessários para usar o software e como instalá-los.
# * Python 3.8
# 
# * Anaconda 24.1.0
# 
# * Git
# 
# * IDE para executar o arquivo `.ipynb` (PyCharm, Spyder, VS Code etc.)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Descrição [2]
# 
# ### `Google Chrome`
# 
# O `Google Chrome` é um dos navegadores da _web_ mais populares e amplamente utilizados atualmente. Desenvolvido pela Google, ele se destaca por sua velocidade, eficiência e integração com os serviços da Google. O Chrome oferece uma experiência de navegação rápida e suave, suportando uma ampla gama de extensões e aplicativos que o tornam altamente personalizável. Além disso, ele é conhecido por seu robusto sistema de segurança e atualizações automáticas, que ajudam a manter os usuários protegidos contra ameaças _online_. Com recursos como guias separadas em processos independentes e a sincronização de dados entre dispositivos, o `Google Chrome` é uma escolha popular para usuários que buscam uma experiência de navegação confiável e versátil.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ## Como configurar/instalar o `Google Chrome` no `Linux Ubuntu` [1]
# 
# Para configurar o `Google Chrome`, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 

# 3. **Navegue até o diretório onde o arquivo `.deb` estará localizado:** Use o comando `cd` para navegar até o diretório onde o arquivo `.deb` está localizado. Por exemplo, se o arquivo `.deb` estiver na sua pasta `Downloads`, você pode usar o seguinte comando: `cd ~/Downloads`
# 
# 4. **Baixar o Pacote do `Google Chrome`**: `wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb`
# 
#     Esse comando baixa o pacote de instalação mais recente do `Google Chrome` para sistemas baseados em `Debian`, como o `Ubuntu`.
# 
# 5. **Instale o arquivo `.deb`:** Use o comando `dpkg` para instalar o arquivo `.deb`. Substitua `<nome_do_arquivo>.deb` pelo nome real do arquivo `.deb` que você deseja instalar: `sudo dpkg -i google-chrome-stable_current_amd64.deb`
# 
#     Você precisará fornecer sua senha de administrador (`sudo`) para continuar.
# 
# 6. **Resolva as dependências (se necessário):** Às vezes, a instalação do arquivo `.deb` pode gerar erros devido a dependências ausentes. Se isso acontecer, você pode usar o seguinte comando para tentar resolver as dependências: `sudo apt install -f`
# 
#     O comando acima tentará instalar automaticamente as dependências necessárias para o pacote `.deb` que você está instalando.
# 
# 7. **Verifique a instalação:** Após a conclusão do processo, verifique se o programa ou pacote foi instalado corretamente. Você pode fazer isso procurando o aplicativo no menu de aplicativos ou executando-o a partir do terminal.
# 
# Isso deve permitir que você instale um arquivo `.deb` no seu sistema Ubuntu. Lembre-se de que os arquivos .deb são pacotes de software específicos para distribuições baseadas no Debian, como o Ubuntu, e geralmente são seguros de usar, especialmente se você os obtiver de fontes confiáveis. No entanto, sempre esteja ciente da origem dos arquivos .deb que você baixa e evite fontes não confiáveis para garantir a segurança do seu sistema.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Google Chrome` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install snapd -y
#     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#     sudo dpkg -i google-chrome-stable_current_amd64.deb
#     sudo apt install -f
#     ```
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Desinstalar o `Google Chrome` no `Linux Ubuntu`
# 
# Para desinstalar o `Google Chrome` pelo terminal do `Linux Ubuntu`, você pode seguir os seguintes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`

# Para desinstalar o `Google Chrome` execute os passos abaixo:
# 
# 3. Digite o seguinte comando para listar todos os pacotes relacionados ao `Google Chrome` instalados no seu sistema: `dpkg -l | grep google-chrome`
# 
#     Isso mostrará uma lista de pacotes relacionados ao `Google Chrome` instalados no seu sistema. Anote o nome do pacote principal do Chrome, que normalmente é algo como `google-chrome-stable`. Por exemplo, você pode ver algo assim: `ii  google-chrome-stable       96.0.4664.93-1     amd64    The web browser from Google`
# 
# 2. Agora, use o comando `apt` para remover o pacote do Chrome. Substitua `google-chrome-stable` pelo nome do pacote que você anotou no passo anterior: `sudo apt remove google-chrome-stable`
# 
#     2.1 O sistema pode pedir sua senha de administrador para confirmar a desinstalação. Digite-a e pressione `Enter`.
# 
#     2.2 O comando irá remover o `Google Chrome` do seu sistema. Após a conclusão, você pode verificar se o Chrome foi removido com sucesso executando o comando `dpkg -l | grep google-chrome` novamente. Se não houver saída, isso significa que o Chrome foi desinstalado com sucesso.
# 
# Isso deve desinstalar o `Google Chrome` do seu sistema Ubuntu usando o terminal. Certifique-se de fazer backup dos seus favoritos e dados importantes antes de prosseguir com a desinstalação, caso queira reinstalá-lo posteriormente.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# ### Código completo para desinstalar
# 
# Para desinstalar o `Google Chrome` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- LICENÇA -->
# ## Licença
# 
# Distribuído sob a licença MIT. Consulte `LICENSE.txt` para obter mais informações.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

# <!-- ROTEIRO -->
# ## Roteiro
# 
# - [x] Adicionar registro de alterações
# 
# - [x] Adicionar links de volta ao topo
# 
# - [x] Adicionar modelos adicionais com exemplos
# 
# - [x] Suporte multilíngue
# 
#      - [ ] Espanhol
# 
#      - [ ] Inglês
# 
#      - [ ] Português
#      
#      - [x] Português brasileiro 
# 
# Consulte os [problemas abertos](https://github.com/edendenis/google_chrome/issues) para obter uma lista completa dos recursos propostos (e problemas conhecidos).
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- CONTRIBUIÇÔES -->
# ## Contribuições
# 
# As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.
# 
# Se você tiver uma sugestão que possa melhorar isso, bifurque o repositório e crie uma solicitação `pull`. Você também pode simplesmente abrir um problema com a tag “aprimoramento”.
# Não se esqueça de dar uma estrela ao projeto! Obrigado novamente!
# 
# 1. Bifurque o projeto
# 
# 2. Crie sua ramificação de recursos (`git checkout -b feature/AmazingFeature`)
# 
# 3. Confirme suas alterações (`git commit -m 'Add some AmazingFeature'`)
# 
# 4. Envie para a filial (`git push origin feature/AmazingFeature`)
# 
# 5. Abra uma solicitação pull
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# <!-- ACKNOWLEDGMENTS -->
# ## Agradecimentos
# 
# * [Best README Template](https://github.com/othneildrew/Best-README-Template?tab=readme-ov-file)
# 
# * [Choose an Open Source License](https://choosealicense.com)
# 
# * [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
# 
# * [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
# 
# * [Malven's Grid Cheatsheet](https://grid.malven.co/)
# 
# * [Img Shields](https://shields.io)
# 
# * [GitHub Pages](https://pages.github.com)
# 
# * [Font Awesome](https://fontawesome.com)
# 
# * [React Icons](https://react-icons.github.io/react-icons/search)
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar google chrome via terminal.*** Disponível em: <https://chat.openai.com/c/4ed19d31-b772-4cad-9cbb-b85f2f125b83> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
# [3] USER: OTHNEILDREW. ***Best readme template.*** Disponível em: <https://github.com/othneildrew/Best-README-Template>. Seaborn team. Acessado em: 23/02/2024 11:27.
# 
# <p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
# 
