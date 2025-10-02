back to [home](/)/[legacy](/legacy)

# Contents

QuICC uses Git for versioning. If you're not familiar with Git, the reference book [Pro Git](http://git-scm.com/book/) is available online.

# Get Sources

1. Request an account from philippe.marti@erdw.ethz.ch

2. Get the sources from GitHub HTTPS:
```
git clone https://github.com/QuICC/QuICC.git
```
or over SSH (upload your SSH key first):
```
git clone git@github..com:QuICC/QuICC.git 
```
Note that on Janus you may need to perform the following to clone:  ssh-add ~/.ssh/id_rsa (might need first to: eval "$(ssh-agent -s)")
Furthermore the connection with Janus should be established with the -Y or -X option to allow the identification windows for username and password to open.


3. Go into new diretory
````
cd QuICC
```

4. Get external modules (currently only Eigen):
```
git submodule init
git submodule update
```

5. Read about the code in the [tutorial](/legacy)

# Get test suite

# Get benchmarks

back to [home](/)/[legacy](/legacy)
