def userInput
pipeline {
    agent any

    stages {
        stage('input'){
            steps{
                script{
                    userInput = input message: 'please provide your input', ok: 'confirm', parameters: [choice(name: '', choices: ['opt1', 'opt2'], description: '')]
                }
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage("print input") {
            steps {
                println("Input was : " + userInput)
            }
        }

    }
}
