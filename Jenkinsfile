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
                // Menggunakan withCredentials tipe 'file' (pengganti withKubeConfig)
                withCredentials([file(credentialsId: 'aks-config', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        def shellCmd = isUnix() ? 'sh' : 'bat'
                        // Mengatur environment variable KUBECONFIG secara eksplisit untuk kubectl
                        withEnv(["KUBECONFIG=${KUBECONFIG_FILE}"]) {
                            ${shellCmd} "kubectl apply -f kantin-k8s.yaml"
                            ${shellCmd} "kubectl apply -f kantin-ingress.yaml"
                            ${shellCmd} "kubectl rollout restart deployment backend-kantin"
                            ${shellCmd} "kubectl rollout restart deployment frontend-kantin"
                        }
                    }
                }
            }
        }
    }
}