#!groovy
//
// QA Complex App tests Runner

// Pipeline
pipeline {
  options {
    timeout(time: 1, unit: 'HOURS')
    timestamps()
  } // options
  stages {
    stage('\u2776 Test') {
      steps {
        script {
          currentBuild.displayName = "#${env.BUILD_NUMBER} (${env.GIT_COMMIT.take(8)}) ${env.GIT_BRANCH}"
          sh '''
            /usr/local/bin/python3.9 -m pip install -r requirements.txt
            /usr/local/bin/python3.9 -m pytest tests/ -n 4
          '''
        } // script
      } // steps
    } // stage
  } // stages
  post {
    always {
      cleanWs()
    } // always
  } // post
} // pipeline

// vim: ft=groovy
// EOF
