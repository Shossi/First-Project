package jenkins

def userInput
pipeline {
    agent {
        label 'docker_node'
    }
    stages {
        stage('build docker image'){
            steps{
                dir() {
                    script {
                        sh "sudo docker build -t weatherapi /weather/. "
                    }
                }
            }
        }
        stage('weather.test docker image') {
            steps {
                dir('weather.test'){
                    script{
                        sh "sh ./weather/test/test.sh"
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
