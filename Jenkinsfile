pipeline {
    agent { 
        label "agentfarm"
    }
environment {
        VENV = '.venv'  // Path to the virtual environment directory
    }
    stages {
        stage('Build') {
            steps {
                sh 'chmod +x build.sh'
                sh './build.sh'
            }
        }
	
	stage('Setup') {
            steps {
                script {
                    // Create virtual environment if it doesn't exist
                    sh "python3 -m venv ${env.VENV}"
                }
            }
        }
        stage('Test') {
            steps {
                sh 'chmod +x start.sh'
                sh './start.sh'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Activate virtual environment if it exists
                    sh '''
                    if [ -d .venv ]; then
                        . .venv/bin/activate
                    fi
                    '''
                    // Run Python application
                  //  sh 'nohup python3 main.py > ~/flasklogs.log 2>&1 &'
		     sh ". .venv/bin/activate && nohup python3 main.py > ~/flasklogs.log 2>&1 &"
                }
            }
        }
    }
}

