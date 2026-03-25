pipeline {
    agent {label 'windows'}
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
                // For a separate step, use the git DSL command:
                git branch: 'main', url: 'https://github.com/luckxander/api'
            }
        }
        stage('Run Python Script') {
            steps {
                // // Automatically aborts after 10 minutes
                // timeout(time: 1, unit: 'MINUTES') {
                //     // Execute the Python script using a shell command
                //     bat 'api.py'
                    script {
                        nstdout = bat(returnStdout: true, script: 'api.py').trim()                                
                        println("stdout ####" + nstdout + "###########")                  

                    }
                }
            }
        }
    }
}
