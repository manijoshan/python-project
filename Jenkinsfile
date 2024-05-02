pipeline{
    agent { 
        label "agentfarm"
    }
   stages {
        stage('Build') {
            steps {
                sh './build.sh'
           }
        }
    }
}

