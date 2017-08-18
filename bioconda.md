# (bio)conda

See [https://bioconda.github.io/contributing.html](https://bioconda.github.io/contributing.html)

## setup: once
Fork repository, clone your fork
`git clone https://github.com/<USERNAME>/bioconda-recipes.git`

Install conda build
`conda install conda-build`

## Writing/adapting a conda recipe

### update, create conda environment for testing
```
conda update conda
conda update conda-build
git checkout master
git pull upstream master
./simulate-travis.py --bootstrap /tmp/miniconda --overwrite
```

### Edit/add recipe

Work in a new branch  
`git checkout -b updating-NanoFilt`

Also change the md5sum
```
wget -O- $URL | md5sum
wget -O- https://files.pythonhosted.org/packages/source/n/nanofilt/NanoFilt-1.1.4.tar.gz | md5sum
```


### Test locally
`./simulate-travis.py --git-range HEAD --disable-docker`

### If successful: push, full travis test
```bash
git commit -m "updating nanofilt to 1.2.0" recipes/nanofilt/meta.yaml
git push origin updating-NanoFilt
```
### If successful: pull request
