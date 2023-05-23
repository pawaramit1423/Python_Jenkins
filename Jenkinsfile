pipeline {
  agent any

    stage('Build and Package') {
      steps {
          sh "sudo apt install python3.10-venv -y"
          sh "sudo apt install python3-pip -y"
          sh "sudo apt install python3 -y"     
          sh 'pip install -r requirements.txt'
          sh 'python setup.py install'
      }
    }

    stage('Deploy to Azure VM') {
      steps {
        script {
          def azureVmIp = '20.40.49.192'
          def azureVmUser = 'cicd'
          def azureVmAppDir = '/var/www/app'

          sshagent(['azurevmcicd']) {
            sh "scp -r . ${azureVmUser}@${azureVmIp}:${azureVmAppDir}"
            sh "ssh ${azureVmUser}@${azureVmIp} 'cd ${azureVmAppDir} && pip install -r requirements.txt'"
            sh "ssh ${azureVmUser}@${azureVmIp} 'cd ${azureVmAppDir} && python setup.py install'"
            sh "ssh ${azureVmUser}@${azureVmIp} 'cd ${azureVmAppDir} && nohup python app.py > /dev/null 2>&1 &'"
          }
        }
      }
    }
  }
}

