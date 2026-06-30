pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Packaging the app into a Docker Image...'
                sh 'docker build -t todo-fastapi-app .'
            }
        }
        stage('Deploy Container') {
            steps {
                echo 'Starting the live server...'
                sh 'docker rm -f my-live-app || true'
                sh 'docker run -d -p 8000:8000 --name my-live-app todo-fastapi-app'
            }
        }
    }
}
