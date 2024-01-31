FROM node:18-alpine

WORKDIR /app

# Copy package.json and package-lock.json from the front-end-nextjs folder
COPY front-end-nextjs/package.json front-end-nextjs/package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the files from the front-end-nextjs folder
COPY front-end-nextjs/ .

# Run build command
RUN npm run build

# Specify the command to start the application
CMD npm start

