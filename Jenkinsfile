pipeline {
    agent any
    triggers {
        // Run daily at 1:00 AM
        cron('0 1 * * *') 
    }
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
        stage('Generate Report') {
            steps {
                bat 'echo "<h1>Build Console Output</h1><pre>" > output_report.html'
                bat 'echo "Running build steps..." >> output_report.html'
                bat 'echo "Step 1: Compiling code..." >> output_report.html'
                // You can run any command and append its output
                bat 'dir >> output_report.html' 
                bat 'echo "</pre>" >> output_report.html'
            }
        }
        stage('Publish HTML Report') {
            steps {
                // Use the publishHTML step to archive and display the generated file
                publishHTML (
                    target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: '.', // Directory containing the report file (root)
                        reportFiles: 'output_report.html', // The specific file to display
                        reportName: 'Build Step Output' // The name of the link in Jenkins UI
                    ]
                )
            }
        }
    }
    post {
        try{
            // Send email on success
            success {
                    emailext (
                        subject: "Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                        body: "Build successful! View the details at: ${env.BUILD_URL}",
                        to: "lusenabh@gmail.com",
                        recipientProviders: [
                            culprits(), 
                            requestor()
                        ]
                    )
            }
            // Send email on failure
            failure {
                    emailext (
                        subject: "Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                        body: "Build failed. Check it here: ${env.BUILD_URL}",
                        to: "lusenabh@gmail.com",
                        recipientProviders: [
                            culprits(), 
                            requestor()
                        ]
                    )
            }
        }
        catch (Exception e) {
            echo "Caught an error: ${e.message}"
        }
        finally {
            // This block always runs, whether an exception occurred or not
            echo 'Cleanup or final reporting happens here.'
            if (currentBuild.result == 'FAILURE') {
                echo 'Performing failure-specific cleanup in finally block.'
            } else {
                echo 'Performing general cleanup in finally block.'
            }
    }
}