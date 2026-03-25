pipeline {
    agent any
    options {
        // Required to clean before the default SCM checkout
        skipDefaultCheckout(true) 
    }
    stages {
        stage('Clean') {
            steps {
                cleanWs() // Clean the workspace
            }
        }
        stage('Git Checkout') {
            steps {
                // The pipeline automatically checks out code if configured as 'Pipeline script from SCM'
                git branch: 'main', url: 'https://github.com/luckxander/api'
            }
        }
        stage('Run Python Script') {
            steps {
                // Automatically aborts after 10 minutes
                timeout(time: 1, unit: 'MINUTES') {
                    // Execute the Python script and print real time output
                    bat 'python -u C:\\Python\\api\\api.py'
                }
            }
        }
        stage('Build and Report') {
            steps {
                // ... your build steps that generate HTML ...
                bat 'mkdir -p build_reports'
                bat 'echo "<html><body><h1>Build Summary</h1></body></html>" > build_reports/index.html'
            }
        }
    }
    post {
        always {
            publishHTML([
                target([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'build_reports', // Directory relative to workspace
                reportFiles: 'index.html',  // Index file
                    reportName: 'HTML Report'   // Name of the link in Jenkins UI
                ])
            ])
        }
    }
}
