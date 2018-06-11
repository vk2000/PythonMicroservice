#!/bin/sh

export FLASK_APP=../infinity/services/user_service.py
export FLASK_DEBUG=1

flask run --host=0.0.0.0