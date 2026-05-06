pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                // Gunakan 'bat' untuk Windows, bukan 'sh'
                bat 'docker build -t backend-kantin ./backend'
                bat 'docker build -t frontend-kantin ./frontend'
            }
        }

        stage('K8s Deployment Test') {
            steps {
                // Pastikan kubectl sudah terinstal dan ada di PATH Windows
                bat 'kubectl apply --dry-run=client -f kantin-k8s.yaml'
                bat 'kubectl apply --dry-run=client -f kantin-ingress.yaml'
            }
        }
    }
}