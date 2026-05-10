pipeline {

    // Run on any available Jenkins machine
    agent any

    stages {

        // Stage 1 - Get latest code from GitHub
        stage('Checkout Code') {
            steps {
                checkout scm
                echo '✅ Code checkout complete!'
            }
        }

        // Stage 2 - Install all required packages
        stage('Setup Environment') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'

                // Install packages from requirements.txt
                bat 'venv\\Scripts\\pip install -r requirements.txt'

                echo '✅ Environment setup complete!'
            }
        }

        // Stage 3 - Run all pytest tests
        stage('Run Tests') {
            steps {
                // Run tests using our virtual environment
                bat 'venv\\Scripts\\pytest tests/test_google.py -v -s'

                echo '✅ Tests complete!'
            }
        }
    }

    // What happens after all stages finish
    post {

        // All stages passed
        success {
            echo '🎉 All tests PASSED!'
        }

        // Any stage failed
        failure {
            echo '❌ Something failed! Check the logs!'
        }

        // Always runs no matter what
        always {
            echo '📋 Pipeline finished!'
        }
    }
}