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
docs_dir = "docs/"
if not pathlib.Path('docs').is_dir():
    sys.exit("Could not find docs/ directory!")

pathlib.Path(docs_dir).mkdir(parents=True, exist_ok=True)

quicc_org_url = "git@github.com:QuICC/"

yaml_filename = 'tutorial.yml'

repo_configs = {
        'QuICC-Solver':{
            'branch':'dev',
            'name':'Tutorial',
            'dirname':'tutorial',
            'files':{
                'README.md':{
                    'page':'quickstart', 
                    'name':'Quick start'},
                'README_clusters.md':{
                    'page':'clusters', 
                    'name':'Clusters'},
                'README_docker.md':{
                    'page':'docker', 
                    'name':'Docker'},
                'README_stability.md':{
                    'page':'stability', 
                    'name':'Stability solver'}
                }
            }
        }

with open(data_dir + yaml_filename, 'w') as yaml_file:
    for reponame,repoinfo in repo_configs.items():
        with tempfile.TemporaryDirectory() as dir:
            repo = git.Repo.clone_from(quicc_org_url + reponame, dir, depth=1, branch=repoinfo['branch'], env ={'GIT_SSH_COMMAND':ssh_cmd})
            tree = repo.head.commit.tree
            repo_dir = docs_dir + repoinfo['dirname'] + '/'
            pathlib.Path(repo_dir).mkdir(parents=True, exist_ok=True)
            yaml_data = [{'name':repoinfo['name'], 'dirname':repoinfo['dirname'], 'entry':repoinfo['dirname'], 'pages':list()}]
            for filename,info in repoinfo['files'].items():
                yaml_data[0]['pages'].append(info)
                with open(repo_dir + f'{info['page']}.markdown', 'wb') as f:
                    f.write(tree[filename].data_stream.read())
            yaml.dump(yaml_data, yaml_file)
