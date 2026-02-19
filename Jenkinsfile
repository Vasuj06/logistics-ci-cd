pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t logistics-app .'
            }
        }
        stage('Run Tests Inside Container') {
            steps {
                sh 'docker run --rm logistics-app pytest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop logistics-container || true'
                sh 'docker rm logistics-container || true'
                sh 'docker run -d -p 5000:5000 --name logistics-container logistics-app'
            }
        }
    }
}