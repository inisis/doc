> * build package
```
python3 -m build
```

> * upload python package to pypi
```
python3 -m twine upload --repository pypi dist/*
```

> * only generate tar
```
python setup.py sdist
```

> * pypi org
```
-i https://pypi.org/simple
```

> * pip uninstall many
```
pip uninstall `pip freeze | grep torch`
```

> * pip install
```
pip install torch===1.7.1+cu118 torchvision===0.8.2+cu118 torchaudio===0.7.2+cu118 -f https://mirror.sjtu.edu.cn/pytorch-wheels
```

> * pip install cannot find installed packages
```
pip install --no-build-isolation -e .
```
