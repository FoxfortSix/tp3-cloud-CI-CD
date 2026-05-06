pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm[cite: 2]
            }
        }
        stage('Build Docker Images') {
            steps {
                // Tambahkan -H tcp://localhost:2375 sebelum kata 'build'
                bat 'docker -H tcp://localhost:2375 build -t backend-kantin ./backend'[cite: 2]
                bat 'docker -H tcp://localhost:2375 build -t frontend-kantin ./frontend'[cite: 2]
            }
        }
        stage('K8s Deployment Test') {
            steps {
                bat 'kubectl apply --dry-run=client -f kantin-k8s.yaml'[cite: 2]
            }
        }
    }
}