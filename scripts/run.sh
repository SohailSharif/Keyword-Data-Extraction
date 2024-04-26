set -o errexit -o nounset

PROJECT="python-app"
FLASK_ENV="development"
FLASK_APP="main:app"

cd server

# Start your local development server.
# export FLASK_SETTINGS_FILENAME="settings.py"
FLASK_ENV="$FLASK_ENV" FLASK_APP="$FLASK_APP" flask run --host=0.0.0.0 --port=8080