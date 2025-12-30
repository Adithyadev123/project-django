pipeline {
    agent any

    stages {
        stage('Clean Old Containers') {
            steps {
                sh 'docker-compose down -v --remove-orphans || true'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d --build --force-recreate'
            }
        }
    }
}



