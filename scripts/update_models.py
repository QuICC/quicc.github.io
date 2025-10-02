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
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqShellRTC':{
            'branch':'main',
            'dirname':'BoussinesqShellRTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqShellITO':{
            'branch':'main',
            'dirname':'BoussinesqShellITO',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqShellDynamo':{
            'branch':'main',
            'dirname':'BoussinesqShellDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereTC':{
            'branch':'main',
            'dirname':'BoussinesqSphereTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereRTC':{
            'branch':'main',
            'dirname':'BoussinesqSphereRTC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereRDDC':{
            'branch':'main',
            'dirname':'BoussinesqSphereRDDC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereITO':{
            'branch':'main',
            'dirname':'BoussinesqSphereITO',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereRDDDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereRDDDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereInertialessDynamo':{
            'branch':'main',
            'dirname':'BoussinesqSphereInertialessDynamo',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqSphereModifiedTaylor':{
            'branch':'main',
            'dirname':'BoussinesqSphereModifiedTaylor',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqPlaneRBC':{
            'branch':'main',
            'dirname':'BoussinesqPlaneRBC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
                }
            },
        'Model-BoussinesqPlaneRRBC':{
            'branch':'main',
            'dirname':'BoussinesqPlaneRRBC',
            'files':{
                'Readme.md':{
                    'page':'model',
                    }
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
            for filename,info in repoinfo['files'].items():
                yaml.dump([{'name':repoinfo['dirname'], 'entry':f'{repoinfo['dirname']}/{info['page']}'}], yaml_file)
                with open(repo_dir + f'{info['page']}.markdown', 'wb') as f:
                    f.write(tree[filename].data_stream.read())
