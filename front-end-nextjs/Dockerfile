FROM node:18-alpine

WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN npm install

# Run build command
RUN npm run build

# Specify the command to start the application
CMD npm start

