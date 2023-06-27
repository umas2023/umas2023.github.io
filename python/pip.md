# pip python包管理工具

- 查看包信息(module not found 时查看安装位置是否正确)
```
pip show xxx
```

- 生成当前环境下的requirements.txt, 附带版本号
```
pip freeze > requirements.txt
```

- 安装requirements.txt
```
pip install -r requirements.txt
```

- 指定清华源
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple xxx
```

- 卸载
```
pip uninstall xxx
(同样支持 -r 批量操作)
```

- 升级pip
```
python -m pip install --upgrade pip
```