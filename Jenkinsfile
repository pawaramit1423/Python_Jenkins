pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/your-repo.git'
      }
    }

    stage('Build and Package') {
      steps {
        sh 'pip install -r requirements.txt'
        sh 'python setup.py install'
      }
    }

    stage('Deploy to Azure VM') {
      steps {
        script {
          def azureVmIp = 'your-azure-vm-ip'
          def azureVmUser = 'your-vm-username'
          def azureVmAppDir = '/var/www/app'

          sshagent(['your-ssh-credentials']) {
            sh "scp -r . ${azureVmUser}@${azureVmIp}:${azureVmAppDir}"
            sh "ssh ${azureVmUser}@${azureVmIp} 'cd ${azureVmAppDir} && pip install -r requirements.txt'"
            sh "ssh ${azureVmUser}@${azureVmIp} 'cd ${azureVmAppDir} && python setup.py install'"
          }
        }
      }
    }
  }
}
