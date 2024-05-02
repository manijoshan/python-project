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
	stage('test'){
	steps{
	sh 'chmod +x start.sh'
        sh './start.sh'
	}
	}
	stage('deploy'){
	steps{
	sh '''
	. .venv/bin/activate
	nohup python3 main.py > ~/flasklogs.log 2>&1 &
	'''
	}
	}
    }
}

