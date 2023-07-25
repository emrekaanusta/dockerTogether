#
## Start your image with a node base image
#FROM python:18-alpine
#
## The /app directory should act as the main application directory
#WORKDIR /app
#
## Copy the app package and package-lock.json file
#COPY package*.json ./
#
## Copy local directories to the current local directory of our docker image (/app)
#COPY src ./src
#COPY public ./public
#
## Install node packages, install serve, build the app, and remove dependencies at the end
#RUN npm install \
#    && npm install -g serve \
#    && npm run build \
#    && rm -fr node_modules
#
#EXPOSE 3000
#
## Start the app using serve command
#CMD [ "serve", "-s", "build" ]


FROM python:3.11.4-bullseye
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
