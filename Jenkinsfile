pipeline {
    agent any

    environment {
        APP_CONTAINER = "django_app"
    }

    stages {

        stage('Cleanup') {
            steps {
                sh '''
                docker rm -f ${APP_CONTAINER} || true
                docker image prune -af || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker compose build --no-cache
                '''
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                docker compose up -d
                '''
            }
        }

        stage('Run Database Migrations') {
            steps {
                sh '''
                docker exec ${APP_CONTAINER} python manage.py migrate
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment completed successfully"
        }
        failure {
            echo "❌ Deployment failed – check logs above"
        }
    }
}






