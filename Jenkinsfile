pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Hapus teks[cite: 2] di sini
                checkout scm
            }
        }
        stage('Build Docker Images') {
            steps {
                // Pastikan Docker Desktop sudah diatur ke 'Expose daemon'
                bat 'docker -H tcp://localhost:2375 build -t backend-kantin ./backend'
                bat 'docker -H tcp://localhost:2375 build -t frontend-kantin ./frontend'
            }
        }
        stage('K8s Deployment Test') {
            steps {
                // Memeriksa validasi file Kubernetes Anda
                bat 'kubectl apply --dry-run=client -f kantin-k8s.yaml'
            }
        }
    }
}