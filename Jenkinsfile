pipeline {
    agent any

    triggers {
        gitlab(
            triggerOnPush: true,
            triggerOnMergeRequest: true,
            branchFilterType: 'All',
            addVoteOnMergeRequest: true)
    }

    stages {
        stage('build') {
            steps {
                echo "Hello World michel!"
            }
        }
    }
}