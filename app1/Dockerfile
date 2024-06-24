# Imagem Node 18 Alpine para segurança e tamanho reduzido
FROM node:18-alpine

WORKDIR /app

# Copia os arquivos package*.json primeiro para aproveitar o cache de camadas do Docker
COPY app1/package*.json ./

RUN npm install

COPY app1/ ./

EXPOSE 3000

CMD [ "npm", "start" ]