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
