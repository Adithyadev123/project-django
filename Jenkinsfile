pipeline {
    agent any

    stages {

        stage('Cleanup') {
            steps {
                sh '''
                docker rm -f django_app postgres_db || true
                docker image prune -af || true
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Database Migrations') {
            steps {
                sh 'docker exec django_app python manage.py migrate'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}




