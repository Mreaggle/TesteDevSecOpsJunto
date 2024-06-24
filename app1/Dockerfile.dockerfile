# Use a imagem oficial do NodeJS
FROM node:14

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos necessários e instale dependências
COPY ./app1/package*.json ./
RUN npm install

# Copie o restante dos arquivos
COPY ./app1 .

# Exponha a porta necessária pela aplicação (se aplicável)
# EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["node", "index.js"]
