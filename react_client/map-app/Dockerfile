# Use a base image with Node.js pre-installed
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /

# Copy package.json and package-lock.json into the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app
RUN npm run build

# Expose the port on which the React app will run (typically 3000)
EXPOSE 3000

# Command to run the React app
CMD ["npm", "start"]
