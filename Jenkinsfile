def gv

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
        stage("init") {
            steps {
                script {
                   gv = load "script.groovy" 
                }
            }
        }

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
                    BRANCH_NAME == 'dev'
                }
            }
            input {
                message "input environment"
                ok "env selected"
                parameters {
                    choice(name: 'environment', choices: ['dev', 'uat', 'prod'], description: 'Select environment to deploy')
                }
            }
            steps {
                script {
                    gv.deployApp()
                }
                echo "this also deploy message of ${environment}"
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
