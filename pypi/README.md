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
