echo off

echo "Deploy to dev server"
echo "======================="

export ROOT_DIR=$1
export FIREBASE_PROJECT_ID=$2
export FIREBASE_TOKEN=$3
export SITE_TARGET_NAME=$4

python3 scripts/deploy_dev.py $ROOT_DIR $FIREBASE_PROJECT_ID $FIREBASE_TOKEN $SITE_TARGET_NAME 