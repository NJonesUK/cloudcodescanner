import os
import pathlib
import subprocess
import sys

inputpath = sys.argv[1]
resultpath = sys.argv[2]

if not os.path.exists(resultpath):
    os.makedirs(resultpath)
if not os.path.exists(os.path.join(resultpath, "checkov")):
    os.makedirs(os.path.join(resultpath, "checkov"))
if not os.path.exists(os.path.join(resultpath, "tflint")):
    os.makedirs(os.path.join(resultpath, "tflint"))
if not os.path.exists(os.path.join(resultpath, "tfsec")):
    os.makedirs(os.path.join(resultpath, "tfsec"))

projects = [ f.path for f in os.scandir(inputpath) if f.is_dir() ]

for project in projects:
    print("Running Checkov against {}".format(project.split('/')[-1]))
    results = subprocess.run("checkov --quiet -d {}/ > {}/checkov/{}.txt".format(project, resultpath, project.split('/')[-1]), shell=True)

    print("Running tflint against {}".format(project.split('/')[-1]))
    results = subprocess.run("tflint --no-color  {}/ > {}/tflint/{}.txt".format(project, resultpath, project.split('/')[-1]), shell=True)

    print("Running tflint against {}".format(project.split('/')[-1]))
    results = subprocess.run("tfsec {}/ --concise-output -f default,json,csv --no-colour --no-module-downloads --soft-fail --out {}/tflint/{}".format(project, resultpath, project.split('/')[-1]), shell=True)
    