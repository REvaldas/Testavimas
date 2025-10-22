pipeline {
    agent { label 'docker-agent-python' }

    stages {
        stage('Run Unit Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
