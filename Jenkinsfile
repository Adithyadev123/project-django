pipeline {
    agent any

    stages {
        stage('Clean Old Containers') {
            steps {
                // Force remove any existing containers with these names
                sh 'docker rm -f postgres_db django_app || true'
                sh 'docker volume prune -f || true'  // optional: remove dangling volumes
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




