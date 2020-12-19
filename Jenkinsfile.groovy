pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage("check pwd") {
            steps {
                sh "pwd"
            }
        }

    }
}
}
