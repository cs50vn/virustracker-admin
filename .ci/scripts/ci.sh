
echo "Build a dev environment"
echo "======================="

export ROOT_DIR=$1
echo "RootDir ${ROOT_DIR}"

#Install prerequisites
echo "Install prerequisites"
echo "======================="

echo "Install Firebase-tools"
npm install -g firebase-tools

echo "Install Firebase-tools"
npm install vue

#Compile app
echo -e "\n*****  1  *****"
$ROOT_DIR/make.sh debug

#Deploy all to dev server
echo -e "\n*****  2  *****"
$ROOT_DIR/deploy-dev.sh $FIREBASE_PROJECT_ID $FIREBASE_TOKEN $SITE_TARGET_NAME_DEV
