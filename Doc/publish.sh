#!/bin/bash

set -e -x -u

_SPHINX_PROJECT_DIR=$(cd $(dirname $0); pwd)
_BASEDIR=$(cd ${_SPHINX_PROJECT_DIR}/..; pwd)
_DOCS_DIR="${_BASEDIR}/docs"

cd "${_SPHINX_PROJECT_DIR}"
make clean html

rm -rf "${_DOCS_DIR}"/*
echo "${_DOCS_DIR}"/.nojekyll
cp -rp "${_SPHINX_PROJECT_DIR}/build/html"/* "${_DOCS_DIR}/"

git add --all "${_DOCS_DIR}"
git commit -m "commit at $(date)"
git push

echo 'Success'
