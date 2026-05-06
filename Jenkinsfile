pipeline {
    agent any
    environment {
        // Point Jenkins to your user's kubeconfig
        KUBECONFIG = 'C:/Users/pinda/.kube/config'
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Images') {
            steps {
                // Building images with tags that match our K8s manifests
                bat 'docker -H tcp://localhost:2375 build -t backend-kantin:latest ./backend'
                bat 'docker -H tcp://localhost:2375 build -t frontend-kantin:latest ./frontend'
            }
        }
        stage('K8s Deployment Test') {
            steps {
                // Testing Kubernetes manifests with the specified context
                bat 'kubectl apply --dry-run=client -f kantin-k8s.yaml --context=docker-desktop'
            }
        }
    }
}