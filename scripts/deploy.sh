#! /bin/bash

echo "Starting..."
echo "Pulling staging staging"
git pull staging master
echo "Pushing staging to staging-master"
git push staging master


echo "Push production?(y/n) \c"
read  MASTER

if [ $MASTER == "y" ] ; then
    git checkout master
    git fetch staging
    git reset --hard staging/master
    echo "Pushing to origin master"
    git push origin master --force
fi

echo "Done!"