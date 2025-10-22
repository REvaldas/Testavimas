pipeline {
    agent { docker { image 'python:3.11' } }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install pytest'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }
}
