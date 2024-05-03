pipeline {
    agent { 
        label "agentfarm"
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
	stage('artifact'){
	steps{
	sh'chmod +x artifact.sh'
	sh 'bash artifact.sh'
	}
      }
    }
post {
        always {
            archiveArtifacts artifacts: '/dist/*.tar.gz', fingerprint: true
            
        }
    }
}
