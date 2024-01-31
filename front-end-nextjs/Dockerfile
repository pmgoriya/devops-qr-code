FROM node:18-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the files
COPY . .

# Run build command
RUN npm run build

# Specify the command to start the application
CMD npm start

