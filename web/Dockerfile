
FROM node 

# Add a work directory
WORKDIR /code/src
# Cache and Install dependencies
COPY package.json .

RUN apt-get update && apt-get -y install bash && apt-get -y install htop

RUN npm install

# Copy app files
COPY . .
# Start the app
CMD [ "npm", "run", "dev" ]
