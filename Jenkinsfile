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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-login', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    script {
                        // Cek OS: Gunakan 'bat' untuk Windows, 'sh' untuk Linux
                        if (isUnix()) {
                            sh "docker build -t ${USER}/kantin-backend:latest ./backend"
                            sh "docker build -t ${USER}/kantin-frontend:latest ./frontend"
                            sh "echo ${PASS} | docker login -u ${USER} --password-stdin"
                            sh "docker push ${USER}/kantin-backend:latest"
                            sh "docker push ${USER}/kantin-frontend:latest"
                        } else {
                            bat "docker build -t %USER%/kantin-backend:latest ./backend"
                            bat "docker build -t %USER%/kantin-frontend:latest ./frontend"
                            bat "docker login -u %USER% -p %PASS%"
                            bat "docker push %USER%/kantin-backend:latest"
                            bat "docker push %USER%/kantin-frontend:latest"
                        }
                    }
                }
            }
        }
        stage('Deploy ke Azure AKS') {
            steps {
                withKubeConfig([credentialsId: 'aks-config']) {
                    script {
                        if (isUnix()) {
                            sh "kubectl apply -f kantin-k8s.yaml"
                            sh "kubectl apply -f kantin-ingress.yaml"
                            sh "kubectl rollout restart deployment backend-kantin"
                            sh "kubectl rollout restart deployment frontend-kantin"
                        } else {
                            bat "kubectl apply -f kantin-k8s.yaml"
                            bat "kubectl apply -f kantin-ingress.yaml"
                            bat "kubectl rollout restart deployment backend-kantin"
                            bat "kubectl rollout restart deployment frontend-kantin"
                        }
                    }
                }
            }
        }
    }
}