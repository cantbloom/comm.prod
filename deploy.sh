#! /bin/bash



echo 'Push production?(y/n)'
read -e MASTER
if ['$MASTER' == 'y']
    then
        git checkout master
        git fetch staging
        git reset --hard staging/master
        git push origin master
fi

echo "...done"