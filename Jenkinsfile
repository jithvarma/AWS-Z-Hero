pipeline {
    agent any
    environment { 
        NAME = 'jith'
        BRANCH_NAME = 'dev'
    }
    parameters {
        choice(name: 'VERSION', choices: ['1.1', '1.2', '1.9'], description: 'Select environment to deploy')
    }
    stages {
        stage("build") {
            steps {
                echo "build process started for ${NAME}"
            }
        }
        stage("test") {
            steps {
                echo "test process started"
            }
        }
        stage("deploy") {
            when {
                expression {
                    BRANCH_NAME == 'test'
                }
            }
            steps {
                echo "deploy started for ${params.VERSION}"
            }
        }
    }
    post {
        success {
            echo 'I will say Hello only if job is success'
        }
        failure {
            echo 'I will say Hello only if job is failure'
        }
    }
}
