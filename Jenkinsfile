pipeline {
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
                    sh 'nohup python3 main.py > ~/flasklogs.log 2>&1 &'
                }
            }
        }
    }
}

