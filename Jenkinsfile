pipeline{
    agent { 
        label "agentfarm"
    }
   stages {
        stage('Build') {
            steps {
		sh 'chmod +x build.sh'
                sh './build.sh'
           }
        }
    }
}

