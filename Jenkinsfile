pipeline {
    agent { docker { image 'python:3.9-slim-buster' } }
    stages {
        stage('install deps') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt -r requirements-dev.txt
                '''
            }
        }
        stage('lint and test') {
            steps {
                sh '''
                    python -m black .
                    python -m pytest
                '''
            }
        }
    }
}
