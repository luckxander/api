pipeline {
    agent any // Or use a specific agent/Docker image, e.g., agent { docker { image 'python:3.9.7' } }
    stages {
        stage('Git Checkout') {
            steps {
                // The pipeline automatically checks out code if configured as 'Pipeline script from SCM'
                // For a separate step, use the git DSL command:
                git branch: 'main', url: 'https://github.com'
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
