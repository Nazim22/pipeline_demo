pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the repository
                git 'https://github.com/Nazim22/Capstone_Project.git'
            }
        }
        
        stage('Build') {
            steps {
                // Install dependencies and build the Python application
                sh 'pip install -r requirements.txt'
                sh 'python setup.py build'
            }
        }
        
       