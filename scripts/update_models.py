import git
import tempfile
import pathlib
import sys, getopt
import yaml

ssh_key = ''
argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv,"hk:")
except getopt.GetoptError:
    print('update_models.py -k <ssh_key>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('update_models.py -k <ssh_key>')
        sys.exit()
    elif opt in ("-k"):
        ssh_key = arg

ssh_cmd = f'ssh -i {ssh_key}'

data_dir = "docs/_data/"
docs_dir = "docs/models/"
if not pathlib.Path('docs').is_dir():
    sys.exit("Could not find docs/ directory!")

pathlib.Path(docs_dir).mkdir(parents=True, exist_ok=True)

quicc_url = "git@github.com:QuICC/"

model_repos = [
        "Model-BoussinesqShellTC",
        "Model-BoussinesqShellRTC",
        "Model-BoussinesqShellITO",
        "Model-BoussinesqShellDynamo",
        "Model-BoussinesqSphereTC",
        "Model-BoussinesqSphereRTC",
        "Model-BoussinesqSphereRDDC",
        "Model-BoussinesqSphereITO",
        "Model-BoussinesqSphereDynamo",
        "Model-BoussinesqSphereRDDDynamo",
        "Model-BoussinesqSphereInertialessDynamo",
        "Model-BoussinesqSphereModifiedTaylor",
        "Model-BoussinesqPlaneRBC",
        "Model-BoussinesqPlaneRRBC"
        ]

with open(data_dir + 'models.yml', 'w') as model_yml:
    for m in model_repos:
        model_name = m.removeprefix('Model-')
        yaml.dump([{'name':model_name, 'entry':f'{model_name}/model'}], model_yml)
        with tempfile.TemporaryDirectory() as dir:
            model = git.Repo.clone_from(quicc_url +  m, dir, depth=1, branch='main', env ={'GIT_SSH_COMMAND':ssh_cmd})
            tree = model.head.commit.tree
            model_dir = docs_dir + model_name
            pathlib.Path(docs_dir + model_name).mkdir(parents=True, exist_ok=True)
            with open(model_dir + '/model.md', 'wb') as f:
                f.write(tree['Readme.md'].data_stream.read())
