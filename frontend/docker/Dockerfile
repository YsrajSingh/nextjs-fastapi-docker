# Use the official Node.js image as a base
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY frontend/package*.json /app

# Install dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Expose the port on which the app will run
EXPOSE 3000

# Start the Next.js app
CMD ["npm", "run", "dev"]
