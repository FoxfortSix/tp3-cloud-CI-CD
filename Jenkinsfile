pipeline {
    agent any
    environment {
        // GANTI dengan Username Docker Hub Anda
        DOCKER_USER = "foxfortsix"
        // GANTI dengan URL Repo GitHub Anda
        GIT_REPO_URL = "https://github.com/FoxfortSix/tp3-cloud-CI-CD.git"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: "${GIT_REPO_URL}"
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                // Menggunakan Credentials ID 'dockerhub-login' yang dibuat di Jenkins
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "docker build -t ${USER}/kantin-backend:latest ./backend"
                    sh "docker build -t ${USER}/kantin-frontend:latest ./frontend"
                    
                    sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                    sh "docker push ${USER}/kantin-backend:latest"
                    sh "docker push ${USER}/kantin-frontend:latest"
                }
            }
        }
        stage('Deploy ke Azure AKS') {
            steps {
                // Menggunakan Credentials ID 'aks-config' (file kubeconfig AKS)
                withKubeConfig([credentialsId: 'aks-config']) {
                    sh "kubectl apply -f kantin-k8s.yaml"
                    sh "kubectl apply -f kantin-ingress.yaml"
                    
                    // Memastikan Pod terupdate dengan image terbaru
                    sh "kubectl rollout restart deployment backend-kantin"
                    sh "kubectl rollout restart deployment frontend-kantin"
                }
            }
        }
    }
}