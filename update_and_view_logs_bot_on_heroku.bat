git init
heroku git:remote -a liza-aiogram
git pull
git add .
git commit -am "start"
git push heroku master
heroku ps:scale worker=1
heroku logs --tail