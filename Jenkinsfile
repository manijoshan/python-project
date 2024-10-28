pipeline {
    agent { 
        label "agentfarm"
    }
    environment {
        ADMIN_USER = credentials('ravi')        
        ADMIN_PASSWORD = credentials('ravi@123') 
    }
    stages {
        stage('Build') {
            steps {
                sh 'chmod +x build.sh'
                sh 'bash build.sh'
            }
        }
        stage('Test') {
            steps {
                sh 'chmod +x start.sh'
                sh 'bash start.sh'
            }
        }
        stage('Artifact') {
            steps {
                sh 'chmod +x artifact.sh'
                sh 'bash artifact.sh'
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
        }
    }
    
}
