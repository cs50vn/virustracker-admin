
echo "Build a dev environment"
echo "======================="

export ROOT_DIR=$1
echo "RootDir ${ROOT_DIR}"

#Install prerequisites
echo "Install prerequisites"
echo "======================="

cd $ROOT_DIR/vue

echo "Install Firebase-tools"
npm install -g firebase-tools

echo "Install Vue CLI"
npm install @vue/cli

echo "List all installed packages"
npm list --depth=0

cd $ROOT_DIR

#Compile app
echo -e "\n*****  1  *****"
$ROOT_DIR/make.sh

#Deploy all to dev server
echo -e "\n*****  2  *****"
$ROOT_DIR/deploy-dev.sh $ROOT_DIR $FIREBASE_PROJECT_ID $FIREBASE_TOKEN $SITE_TARGET_NAME_DEV
