pipeline {
    agent any // Or use a specific agent/Docker image, e.g., agent { docker { image 'python:3.9.7' } }
    options {
        skipDefaultCheckout(true) // Required to clean before the default SCM checkout
    }
    stages {
        stage('Clean and Checkout') {
            steps {
                cleanWs() // Clean the workspace
                checkout scm // Explicitly checkout SCM
                echo 'Workspace is clean and code is checked out.'
            }
        }
        stage('Run Python Script') {
            steps {
                // Execute the Python script using a shell command
                bat 'api.py'
                // For Windows, use 'bat' instead of 'sh'
                // bat 'python your_script_name.py'
            }
        }
    }
}
