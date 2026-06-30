pipeline {
    agent any
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Creating Python Virtual Environment...'
                sh 'python3 -m venv venv'
                echo 'Installing Dependencies...'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                echo 'Running the tests...'
                sh './venv/bin/pytest test_main.py -v'
            }
        }
    }
    post {
        always {
            echo 'Cleaning...'
            sh 'rm -rf venv'
        }
        success {
            echo 'Success: All tests passed! The API is working perfectly!'
        }
        failure {
            echo 'Failed: Check Logs to see what went wrong!'
        }
    }
}
