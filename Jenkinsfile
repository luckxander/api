pipeline {
    agent any // Or use a specific agent/Docker image, e.g., agent { docker { image 'python:3.9.7' } }
    options {
        skipDefaultCheckout(true) // Required to clean before the default SCM checkout
    }
    stages {
        stage('Clean and Checkout') {
            steps {
                cleanWs() // Clean the workspace
            }
        }
        stage('Git Checkout') {
            steps {
                // The pipeline automatically checks out code if configured as 'Pipeline script from SCM'
                // For a separate step, use the git DSL command:
                git branch: 'main', url: 'https://github.com/luckxander/api'
            }
        }
        stage('Run Python Script') {
            steps {
                // Execute the Python script using a shell command
                bat 'api.py'
            }
        }
    }
}
