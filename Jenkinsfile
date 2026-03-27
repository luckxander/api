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
                // The pipeline automatically checks out code if configured as Pipeline script from SCM'
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
                bat 'echo "<html><body><h1>Last Build Output Summary</h1><p>This is a custom HTML report.</p></body></html>" >> output_report.html'
                bat 'echo "Running build steps..." >> output_report.html'
                bat 'echo "Compiling code..." >> output_report.html'
                bat 'echo "<p>Build Number: ${BUILD_NUMBER}</p>" >> output_report.html'

            }
        }
    }
    post {
        always {
            // Publish the generated HTML report
            publishHTML(
                target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.', // Directory relative to workspace where report.html is located
                    reportFiles: 'output_report.html', // The main HTML file to display
                    reportName: 'Custom Build Output' // Name of the link that appears in Jenkins UI
                ]
            )
            script {
                if (currentBuild.result == 'SUCCESS') {
                    echo 'Build successful! It will send an email'
                    emailext (
                                subject: "Success: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                                body: "Build successful! View the details at: ${env.BUILD_URL}",
                                to: "lusenabh@gmail.com",
                                recipientProviders: [
                                    culprits(), 
                                    requestor()
                                ]
                    )
                } 
                else if (currentBuild.result == 'FAILURE') {
                    echo 'Build failure! It will send an email'
                    emailext (
                                subject: "Build Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                                body: "Build failed. Check the console output here: ${env.BUILD_URL}",
                                to: "lusenabh@gmail.com",
                                recipientProviders: [
                                    culprits(), 
                                    requestor()
                                ]
                    )
                } 
                else {
                    echo "Build finished with an unusual result: ${currentBuild.result}. It will send "
                    emailext (
                                subject: "Unusual build result: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                                body: "Build finished with an unusual result. Check the console output here: ${env.BUILD_URL}",
                                to: "lusenabh@gmail.com",
                                recipientProviders: [
                                    culprits(), 
                                    requestor()
                                ]
                    )                    
                }
            }
        }
    }
}