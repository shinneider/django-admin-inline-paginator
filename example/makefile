MAKEFLAGS += --silent  # No print command executed
ARGS = $(filter-out $@,$(MAKECMDGOALS))

#####
## Utils
###

check_virtualenv:
	# if is not a docker, activate virtualenv
	if [ ! -f /.dockerenv ] && [ -z "${VIRTUAL_ENV}" ] ; then \
		echo "\033[0;31mError: No Virtualenv activated.${NC}"; \
		exit 1; \
	fi

#####
## Run
###

before_run: check_virtualenv
	pip install -r requirements.txt
	python manage.py migrate

run: before_run
	python manage.py runserver 0:8000

#####
## Shortcuts
###

dj: check_virtualenv
	python manage.py "${ARGS}"

dump_data: check_virtualenv
	python manage.py dumpdata --indent 4 --exclude admin.logentry --exclude auth.permission --exclude auth.group --exclude contenttypes.contenttype --exclude sessions.session> fixtures/bkp.json

load_data: check_virtualenv
	python manage.py loaddata fixtures/bkp.json