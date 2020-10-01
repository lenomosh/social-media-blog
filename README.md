# Social Media Blog

## Description 

 A Flask/React application that functions both as Social media and blog. It allows the community to share their ideas and moderate the application on their own 

### Author

#### [Lennox Omondi](https://linkedin.com/in/lenomosh)


## User Stories
* As user I would like to:
* As a user, I would like to view the blog posts on the site
* As a user, I would like to comment on blog posts
* As a user, I would like to view the most recent posts
* As a user, I would like to an email alert when a new post is made by joining a subscription.
* As a user, I would like to see random quotes on the site
* As a writer, I would like to sign in to the blog.
* As a writer, I would also like to create a blog from the application.
* As a writer, I would like to delete comments that I find insulting or degrading.
* As a writer, I would like to update or delete blogs I have created.


## Setup Instructions
### React Setup Instructions
- create a new directory
- `git init` and run `git remote add origin git@github.com:lenomosh/pitching-app.git` id you are using SSH or `https://github.com/lenomosh/pitching-app.git`
- `git pull origin front`
- run `yarn` or `npm install`
- finally serve via `yarn start` or `npm start`

### Flask Setup Instruction
- create a new directory
- `git init` and run `git remote add origin git@github.com:lenomosh/pitching-app.git` id you are using SSH or `https://github.com/lenomosh/pitching-app.git`
- `git pull origin back`
- From the project directory run `conda create --prefix=./env` or `python -m venv virtual`
- Run `source activate ./env` for conda or `source virtual/bin/activate`
- Run `pip install -r requirements.txt`
- open `run.py` and change `create_app` argument to `development`
- run `export EMAIL_USER='your_username'`
- run `export EMAIL_PASSWORD='your_email_password'`
- if you wish to run the app on production, you have to export the database url by running `export DATABASE_URL='your_database_url'`
- run the app either via `flask run` or `python run.py runserver`

## LICENSE
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

Copyright (c) 2020 Lennox Omondi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
