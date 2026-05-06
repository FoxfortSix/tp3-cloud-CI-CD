pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm // Mengambil kode dari repositori[cite: 1]
            }
        }

        stage('Build Docker Images') {
            steps {
                // Membangun image untuk backend dan frontend[cite: 1]
                sh 'docker build -t backend-kantin ./backend'
                sh 'docker build -t frontend-kantin ./frontend'
            }
        }

        stage('K8s Deployment Test') {
            steps {
                // Validasi file konfigurasi Kubernetes Anda[cite: 1]
                sh 'kubectl apply --dry-run=client -f kantin-k8s.yaml'
                sh 'kubectl apply --dry-run=client -f kantin-ingress.yaml'
            }
        }
    }
}