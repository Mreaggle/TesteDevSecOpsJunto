# Utiliza uma imagem Node.js 18.12.0 Alpine como base (segurança, tamanho reduzido, versão específica)
FROM node:18.20.0-alpine

# Declara variáveis de ambiente para o build
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}

# Define o usuário não-root para executar o aplicativo (segurança)
RUN addgroup -S appuser && adduser -S -G appuser appuser
USER appuser

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas os arquivos necessários para o build (reduz o tamanho da imagem)
COPY package*.json ./
RUN npm install --omit=dev && npm cache clean --force

# Copia o restante do código da aplicação para o container
COPY . .

# Define a porta que a aplicação irá escutar
EXPOSE 3000

# Comando para iniciar a aplicação em modo produção
CMD [ "npm", "start" ]