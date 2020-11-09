properties([pipelineTriggers([githubPush()])])
pipeline {
    agent {
        label 'github-ci'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: 'master']],
                    userRemoteConfigs: [[
                        url: 'git@github.com:edenavital5/pythonScript.git',
                        credentialsId: '',
      ]]
     ])
   }
}
        stage('build') {
            steps {
                echo "Hello python script!"
                //sh 'python --version'
                sh 'python Deloitte.py'
            }
            // steps{
            //     withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',credentialsId: 'aws',usernameVariable: 'AWS_ACCESS_KEY_ID',passwordVariable: 'AWS_SECRET_ACCESS_KEY']]){
            //         sh "export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"
            //         sh "export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY" 
                    
            //         echo "Hello World Michel!"
            //         sh 'python --version'
            //         sh 'python Deloitte.py'
            //     }
            // }
        }
    }
}