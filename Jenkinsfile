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
                sh 'docker compose build --no-cache'
            }
        }

        stage('Start Containers') {
            steps {
                sh '''
                docker compose up -d
                sleep 10
                docker ps
                '''
            }
        }

        stage('Wait for App to be Running') {
            steps {
                sh '''
                for i in {1..10}; do
                  if docker inspect -f '{{.State.Running}}' ${APP_CONTAINER} | grep true; then
                    echo "Container is running"
                    exit 0
                  fi
                  echo "Waiting for container..."
                  sleep 5
                done
                echo "Container failed to start"
                docker logs ${APP_CONTAINER}
                exit 1
                '''
            }
        }

        stage('Run Database Migrations') {
            steps {
                sh 'docker exec ${APP_CONTAINER} python manage.py migrate'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully'
        }
        failure {
            echo '❌ Deployment failed – check logs above'
        }
    }
}







