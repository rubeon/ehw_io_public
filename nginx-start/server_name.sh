#!/bin/bash

# set the server name
conf_file=${NGINX_CONFIGURATION_PATH}/proxy.conf
[ -f $conf_file ] && \
	sed -i "s/APP_SERVICE/${APP_SERVICE}/g" $conf_file
