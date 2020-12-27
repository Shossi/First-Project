package jenkins
def lastCommit
def latestVersion
pipeline {
    agent {
        label 'docker_node'
    }
    stages {
        stage('build docker image'){
            steps{
                dir('weather') {
                    script {
                        println("Getting commit id and latest Version")
                        _lastCommit = sh script: "git log | head -1 | awk '{print \$2}' | cut -c1-6", returnStdout: true
                        _latestVersion = sh script: "git branch -r | cut -d '/' -f2 | grep 0. | sort -r | head -1", returnStdout: true
                        lastCommit = _lastCommit.trim()
                        latestVersion = _latestVersion.trim()
                        println("Latest Version seen is ${latestVersion}")
                        println("Latest commit seen is ${lastCommit}")
                        sh "sudo docker build -t weatherapi:${latestVersion}-${lastCommit} . "
                    }
                }
            }
        }
        stage('test docker image') {
            steps {
                dir('weather/test'){
                    script{
                        try {
                            sh "sh ./test.sh weatherapi:${latestVersion}-${lastCommit}"
                        } catch (err) {
                            println('error thrown on test file execution')
                            currentBuild.abort = 'ABORTED'
                            error('Error thrown on test file execution')
                        }
                    }
                }

            }
        }
        stage("upload image to hub") {
            steps {
                sh "sudo docker push joey/weatherapi:${latestVersion}-${lastCommit}"
            }
        }
        stage('Deployment') {
            steps{
                script{
                    dir('deploy'){
                        sh "ansible-playbook -i inv.ini ansible.yml --extra-vars tag=${latestVersion}-${lastCommit}"
                    }
                }
            }
        }
    }
}
