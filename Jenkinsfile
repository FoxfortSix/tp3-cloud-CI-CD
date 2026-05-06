pipeline {
    agent any
    environment {
        // GANTI 'username' dengan username Docker Hub Anda
        DOCKER_HUB_USER = 'foxfortsix' 
        BACKEND_IMAGE = "${DOCKER_HUB_USER}/backend-kantin:latest"
        FRONTEND_IMAGE = "${DOCKER_HUB_USER}/frontend-kantin:latest"
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build & Push Docker Images') {
            steps {
                // Menggunakan 'sh' untuk Linux Environment di AKS
                sh "docker build -t ${BACKEND_IMAGE} ./backend"
                sh "docker build -t ${FRONTEND_IMAGE} ./frontend"
                
                // Pastikan Anda sudah login ke Docker Hub di Jenkins (via Credentials)
                sh "docker push ${BACKEND_IMAGE}"
                sh "docker push ${FRONTEND_IMAGE}"
            }
        }
        stage('Deploy to AKS') {
            steps {
                // Perintah apply ke cluster AKS
                sh "kubectl apply -f kantin-k8s.yaml"
                sh "kubectl apply -f kantin-ingress.yaml"
            }
        }
    }
}