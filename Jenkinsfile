pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Github-cred', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_PASSWORD')]) {
                    git url: 'https://github.com/Nazim22/Capstone_Project', credentialsId: 'Github-cred'
                }
            }
        }

        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest test_app.py'
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                }
                sh 'docker build -t my_python_app .'
                sh 'docker tag my_python_app dockeruser2068/my_python_app:V1.0'
                sh 'docker push dockeruser2068/my_python_app:V1.0'
            }
        }
    }
}



