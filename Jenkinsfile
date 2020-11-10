properties([pipelineTriggers([githubPush()])])
pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                sh 'python Deloitte.py'
            }
        }
    }
}