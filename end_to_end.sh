#!/bin/sh

# Set the base URL to use the default ultron branch.
if [ $CI_TOKEN ]; then
    BASE=http://ci.ironmann.io/api/v1/project/scality/Integration/tree/ultron/rel/6.2.5?circle-token=
    URL=$BASE$CI_TOKEN
else
    echo "Environment variable CI_TOKEN not found."
fi

curl -X POST --header "Content-Type: application/json" -d '{
  "build_parameters": {
    "DEFAULT_BRANCH": "qux",
    "SCALITY_FOO_BRANCH": "bar"
  }
}' $URL -k
