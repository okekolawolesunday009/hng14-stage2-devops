FROM node:18-alpine3.21
RUN apk update && apk upgrade --no-cache
WORKDIR /app
COPY . .
RUN npm install

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:3000/ || exit 1

EXPOSE 3000
CMD ["node", "app.js"]