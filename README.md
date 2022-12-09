# heroku-gsheet-collector

Provides a write-only public API for Google Sheets using a Heroku app. (Well, it did, until Heroku killed free tier. Thanks.)

## Install

```bash
$ pip install -r requirements.txt
```

## Deploy

Set `$PROJECT` to your project name.

```bash
$ heroku create $PROJECT
$ heroku git:remote -a $PROJECT
$ git push heroku master
```

Done! Your hello-world website should be live now at https://$PROJECT.herokuapp.com/.
