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

# ## Descrição [2]
# 
# ### `Google Chrome`
# 
# O `Google Chrome` é um dos navegadores da _web_ mais populares e amplamente utilizados atualmente. Desenvolvido pela Google, ele se destaca por sua velocidade, eficiência e integração com os serviços da Google. O Chrome oferece uma experiência de navegação rápida e suave, suportando uma ampla gama de extensões e aplicativos que o tornam altamente personalizável. Além disso, ele é conhecido por seu robusto sistema de segurança e atualizações automáticas, que ajudam a manter os usuários protegidos contra ameaças _online_. Com recursos como guias separadas em processos independentes e a sincronização de dados entre dispositivos, o `Google Chrome` é uma escolha popular para usuários que buscam uma experiência de navegação confiável e versátil.

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

# ### Código completo
# 
# Para configurar/instalar o `Google Chrome` no Linux Ubuntu sem precisar digitar linha por linha, você pode seguir estas etapas:
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
#     sudo apt install snapd -y
#     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#     sudo dpkg -i google-chrome-stable_current_amd64.deb
#     sudo apt install -f
#     ```

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

# ### Código completo
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

# ## Referências
# 
# [1] OPENAI. ***Instalar Google Chrome via Terminal.*** Disponível em: <https://chat.openai.com/c/4ed19d31-b772-4cad-9cbb-b85f2f125b83> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 14/11/2023 09:33.
# 
