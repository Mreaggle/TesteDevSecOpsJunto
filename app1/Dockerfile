# Imagem Node 18 Alpine para segurança e tamanho reduzido
FROM node:18-alpine

WORKDIR /app

# Copia os arquivos package*.json primeiro para aproveitar o cache de camadas do Docker
COPY app1/package*.json ./

# Instalar dependências com npm ci para garantir consistência
RUN npm ci

COPY app1/ ./

EXPOSE 3000

CMD [ "npm", "start" ]