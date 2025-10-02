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

quicc_org_url = "git@github.com:QuICC/"

yaml_filename = 'models.yml'

repo_configs = {
        'Model-BoussinesqShellTC':{
            'branch':'main',
            'dirname':'BoussinesqShellTC',
            'name':'BoussinesqShellTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqShellRTC':{
            'branch':'main',
            'dirname':'BoussinesqShellRTC',
            'name':'BoussinesqShellRTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqShellITO':{
            'branch':'main',
            'dirname':'BoussinesqShellITO',
            'name':'BoussinesqShellITO',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqShellDynamo':{
            'branch':'main',
            'dirname':'BoussinesqShellDynamo',
            'name':'BoussinesqShellDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    }
                }
            },
        'Model-BoussinesqSphereTC':{
            'branch':'main',
            'dirname':'BoussinesqSphereTC',
            'name':'BoussinesqSphereTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereRTC':{
            'branch':'main',
            'dirname':'BoussinesqSphereRTC',
            'name':'BoussinesqSphereRTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereRDDC':{
            'branch':'main',
            'dirname':'BoussinesqSphereRDDC',
            'name':'BoussinesqSphereRDDC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereITO':{
            'branch':'main',
            'dirname':'BoussinesqSphereITO',
            'name':'BoussinesqSphereITO',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    }
                }
            },
        'Model-BoussinesqSphereDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereDynamo',
            'name':'BoussinesqSphereDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereRDDDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereRDDDynamo',
            'name':'BoussinesqSphereRDDDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereInertialessDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereInertialessDynamo',
            'name':'BoussinesqSphereInertialessDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqSphereModifiedTaylor':{
            'branch':'main',
            'dirname':'BoussinesqSphereModifiedTaylor',
            'name':'BoussinesqSphereModifiedTaylor',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqPlaneRBC':{
            'branch':'main',
            'dirname':'BoussinesqPlaneRBC',
            'name':'BoussinesqPlaneRBC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        'Model-BoussinesqPlaneRRBC':{
            'branch':'main',
            'dirname':'BoussinesqPlaneRRBC',
            'name':'BoussinesqPlaneRRBC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    'name':'Model description',
                    },
                },
            },
        }

with open(data_dir + yaml_filename, 'w') as yaml_file:
    for reponame,repoinfo in repo_configs.items():
        with tempfile.TemporaryDirectory() as dir:
            repo = git.Repo.clone_from(quicc_org_url + reponame, dir, depth=1, branch=repoinfo['branch'], env ={'GIT_SSH_COMMAND':ssh_cmd})
            tree = repo.head.commit.tree
            repo_dir = docs_dir + repoinfo['dirname'] + '/'
            pathlib.Path(repo_dir).mkdir(parents=True, exist_ok=True)
            yaml_data = {
                    'name':repoinfo['name'],
                    'dirname':repoinfo['dirname'],
                    'pages':list(),
                    }
            for filename,info in repoinfo['files'].items():
                yaml_data['pages'].append(info)
                with open(repo_dir + f'{info['page']}.markdown', 'wb') as f:
                    f.write(tree[filename].data_stream.read())
            yaml.dump([yaml_data], yaml_file)
