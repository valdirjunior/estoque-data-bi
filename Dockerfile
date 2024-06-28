
# Use uma imagem base do Python
FROM python:3.11

# Defina o diretório de trabalho dentro do container
WORKDIR /estoque-data-bi

# Copie os arquivos de requisitos
# COPY scripts/requirements.txt .

# Instale as dependências do Python
RUN pip install mysql-connector-python notebook pandas matplotlib

# Copie os scripts e a pasta data para o container
# COPY . .



# Instale o Jupyter Notebook
# RUN pip install notebook

# Exponha a porta 8888 para o Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
