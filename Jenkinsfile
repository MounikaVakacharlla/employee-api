pipeline {
    agent any

    environment {
        IMAGE_NAME = "mounikavakacharlla/employee-api:v1"
    }

    stages {

        stage('Git Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Python Dependency Installation') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Django Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python manage.py test
                '''
            }
        }

        stage('Docker Image Build') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Staging Deployment') {
            steps {
                sh '''
                docker compose down || true
                docker compose up -d
                '''
            }
        }
    }

    post {

        success {
            echo "=================================="
            echo "BUILD SUCCESSFUL"
            echo "Application deployed successfully."
            echo "=================================="
        }

        failure {
            echo "=================================="
            echo "BUILD FAILED"
            echo "Please check Jenkins Console Output."
            echo "=================================="
        }

        always {
            cleanWs()
        }
    }
}
