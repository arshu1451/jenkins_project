pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
                echo 'Code checkout complete!'
            }
        }

        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
                echo 'Environment setup complete!'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest tests/test_google.py -v -s'
                echo 'Tests complete!'
            }
        }
    }

    post {
        success {
            echo 'All tests PASSED!'
        }
        failure {
            echo 'Something failed! Check the logs!'
        }
        always {
            echo 'Pipeline finished!'
        }
    }
}