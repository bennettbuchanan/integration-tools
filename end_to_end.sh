#!/bin/sh

if [ $CI_TOKEN ]; then
    echo $CI_TOKEN
else
    echo "Environment variable CI_TOKEN not found."
fi

curl -X POST --header "Content-Type: application/json" -d '{
  "build_parameters": {
    "DEFAULT_BRANCH": "foo",
    "SCALITY_QUX_BRANCH": "bar"
  }
}' http://ci.ironmann.io/api/v1/project/scality/Integration/tree/ultron/rel/6.4?circle-token=$CI_TOKEN -k
