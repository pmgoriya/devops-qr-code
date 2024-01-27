FROM node:18-alpine

WORKDIR /qrapp

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .

RUN npm run build

CMD ["npm","start"]

