#! /bin/bash


echo "Commit?(y/n) \c"
read COMMIT
if [ $COMMIT == 'y' ] ; then
    echo "Enter a commit message: \c "
    read COMMIT_MSG
    git add .
    git commit -m '$COMMIT_MSG'
fi

echo "Starting..."
echo "Pulling staging staging"
git pull staging staging
echo "Pushing staging staging"
git push staging staging
echo "Pushing staging to staging-master"
git push staging staging:master


echo "Push production?(y/n) \c"
read  MASTER

if [ $MASTER == "y" ] ; then
    git checkout master
    git fetch staging
    git reset --hard staging/master
    echo "Pusing to origin master"
    git push origin master
fi

echo "Done!"