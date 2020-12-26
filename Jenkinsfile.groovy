def userInput
pipeline {
    agent any

    stages {
        stage('build docker image'){
            steps{
                dir('API') {
                    script {
                        sh "sudo docker build -t weatherapi . "
                    }
                }
            }
        }
        stage('test docker image') {
            steps {
                dir('API/test'){
                    script{
                        sh "sh ./test.sh"
                    }
                }

            }
        }
        stage("print input") {
            steps {
                println("Input was : " + userInput)
            }
        }

    }
}
