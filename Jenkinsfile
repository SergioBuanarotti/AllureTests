pipeline {
    agent {
                label 'linux'
            }
    environment {
      PROJECT_NAME = "Neptun"
      OWNER_NAME   = "SergioBuanarotti"
    }

    stages {
        stage('1-Build') {
            steps {
                sh "sudo apt install -y python3-pip"
                sh "sudo apt install -y python3.8-venv"
                sh "sudo apt install -y allure"
                sh "sudo apt install -y docker.io"
                echo "Start Building dependencies..."
                sh "python3 -m venv venv"
                sh 'pip3 install -r requirements.txt'
                sh "docker run -p 80:80 -d kennethreitz/httpbin"

            }
        }
        stage('2-Test') {
            steps {
                sh 'python3 -m pytest --alluredir=./allure-results tests'
            }
        }
        stage('3-Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {
                echo "Start of Stage Deploy..."
                sh "allure serve allure-results"
                echo "End of Stage Build..."
            }
        }
    }
}