pipeline {
    agent { 
        docker { image 'python:3.9-slim-buster' } 
    }
    stages {
        stage('install dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt -r requirements-dev.txt
                '''
            }
        }
        stage('lint and test') {
            steps {
                parallel(
                    lint: {
                        sh 'python -m black .'
                    },
                    test: {
                        sh 'python -m pytest'
                    }
                )
            }
        }
    }
}
