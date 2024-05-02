pipeline {
    agent { 
        label "agentfarm"
    }
    environment {
        VENV = '.venv'  // Path to the virtual environment directory
    }
    stages {
        stage('Setup') {
            steps {
                script {
		    sh 'chmod +x build.sh'
                    sh './build.sh'
                    // Create virtual environment if it doesn't exist
                    sh "python3 -m venv ${env.VENV}"
                }
            }
        }
        stage('Install dependencies') {
            steps {
                // Activate virtual environment and install dependencies
                script {
                    sh "source ${env.VENV}/bin/activate && pip install -r requirements.txt"
                }
            }
        }
        stage('Run Application') {
            steps {
                // Activate virtual environment and run Python application
                script {
                    sh "source ${env.VENV}/bin/activate && python3 main.py"
                }
            }
        }
    }
}

