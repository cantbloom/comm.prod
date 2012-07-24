#! /bin/bash


# echo Enter a commit message:
# read -e COMMIT
# git add .
# git commit -m $COMMIT
# echo Starting...
# git pull staging staging
# git push staging staging
# git push staging staging:master


echo "Push production?(y/n)"
read -e MASTER

if ["$MASTER" == "y"]

    then
        git checkout master
        git fetch staging
        git reset --hard staging/master
        git push origin master
fi

echo "...done"