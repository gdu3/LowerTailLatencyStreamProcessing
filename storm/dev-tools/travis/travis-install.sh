#!/bin/bash
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

PYTHON_VERSION_TO_FILE=`python -V > /tmp/python_version 2>&1`
PYTHON_VERSION=`cat /tmp/python_version`
RUBY_VERSION=`ruby -v`
NODEJS_VERSION=`node -v`
MVN_VERSION=`mvn -v`

echo "Python version : $PYTHON_VERSION"
echo "Ruby version : $RUBY_VERSION"
echo "NodeJs version : $NODEJS_VERSION"
echo "mvn version : $MVN_VERSION"

STORM_SRC_ROOT_DIR=$1

TRAVIS_SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd ${STORM_SRC_ROOT_DIR}

python ${TRAVIS_SCRIPT_DIR}/save-logs.py "install.txt" mvn clean install -DskipTests -Pnative --batch-mode
BUILD_RET_VAL=$?

if [[ "$BUILD_RET_VAL" != "0" ]];
then
  cat "install.txt"
fi

exit ${BUILD_RET_VAL}
