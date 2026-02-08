pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('app') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('app') {
                    sh 'pytest'
                }
            }
        }
    }
}
