@echo off
echo ===== Deploying to Heroku =====

echo --- Logging into Heroku ---
heroku login

echo --- Creating Heroku app ---
heroku create review-pickle || echo App may already exist, continuing...

echo --- Adding Heroku git remote ---
heroku git:remote -a review-pickle

echo --- Pushing to Heroku ---
git push heroku master

echo --- Opening the deployed app ---
heroku open

echo ===== Deployment Complete ===== 