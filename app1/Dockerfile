# Imagem Node 18.12.0 Alpine para segurança, tamanho reduzido e versão LTS específica.
FROM node:18.12.0-alpine

# Define o diretório de trabalho dentro do container.
WORKDIR /app

# Copia os arquivos package*.json primeiro para aproveitar o cache de camadas do Docker.
COPY app1/package*.json ./

# Instala as dependências da aplicação.
RUN npm ci

# Copia o restante do código da aplicação para o container.
COPY . ./

# Expõe a porta 3000 onde a aplicação estará ouvindo.
EXPOSE 3000

# Comando para iniciar a aplicação.
CMD [ "npm", "start" ]