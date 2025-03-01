> * use line profiler to profile code
```python
pip install line_profiler
add @profile before def
kernprof -l -v felson/bin/json2txt.py /nas/csv/Q4_5751_2019.10.18.csv ./
```
> * assert with debug info
```python
    assert not isinstance(img, type(None)), "path: %r" % img_path
```
> * change default interpreter
```shell
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
```
> * get python version
```
PYVER=$(python -c "import sys; print('python{}.{}'.format(*sys.version_info))")
```
> * conda remove env
```
conda remove --name base --all
```
> * conda install cudatoolkit && cudnn
```
conda install -c anaconda cudatoolkit=10.0 cudnn
```

> * change builtin print
```
import builtins
from inspect import getframeinfo, stack
original_print = print

def print_wrap(*args, **kwargs):
    caller = getframeinfo(stack()[1][0])
    original_print("FN:",caller.filename,"Line:", caller.lineno,"Func:", caller.function,":::", *args, **kwargs)

builtins.print = print_wrap
``

> * python executable
```

```

> * multiprocess cannot malloc
```
sudo sysctl -w vm.max_map_count=131072
```
