pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                aws --region us-east-2 ssm start-automation-execution --document-name UpdateMyLatestWindowsAmi
                echo "Hello World Michel!"
                sh 'python --version'
                sh 'python Deloitte.py'
            }
        }
    }
}