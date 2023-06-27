# hello qt
python+QT 项目基本操作

## hello world
- 使用pyqt创建一个简单的单窗口页面
- 项目位置: 1_example/pyqt
### 1. 一个简单的窗口  
```python
import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hello world")
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(800, 600))
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
# Start the event loop.
app.exec()
```

### 2. 项目打包
- 打包使用pyinstaller工具,需要先安装
```
pip install pyinstaller
pyinstaller.exe -F -w .\window.py
```
- 打包参数

| 参数                         | 解释                                                |
| ---------------------------- | --------------------------------------------------- |
| -F                           | 打包成一个exe文件(无法修改包内文件如config.json)    |
| -D                           | 打包多个文件，在dist中生成很多依赖文件              |
| -w                           | 程序启动不打开命令行                                |
| -n、–name                    | 指定名称打包程序名称(默认值为脚本的基本名称)        |
| -i                           | 指定.exe程序的图标                                  |
| --add-data="源地址;目标地址" | 需要额外打包的附加资源,windows以;分割，linux以:分割 |

- 下面是一个具体的打包脚本的例子
```python
os.system("pyinstaller.exe -D -w -n  %s \
          -i .\\static\\tenpula_256.ico \
           --add-data component;component \
           --add-data static;static \
            .\\app.py" % name)
```
- 为了避免出现打包前后资源相对路径错误的问题,可以使用一个绝对路径函数,下面是一个例子
```python
def resource_path(relative_path):
    """ Get absolute path to resource"""
    base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)
```

### 3. 窗口基本设置
- 窗口名
```python
self.setWindowTitle("My App")
```
- 窗口图标
```python
self.setWindowIcon(QtGui.QIcon("./data/img/mati_ei_256.ico"))
```

- 窗口大小 
```python
self.setFixedSize(QSize(800, 600))
```

### 4. 常用组件,事件,布局
- 组件:文本
```python
self.label = QLabel()
self.label.setText()
```

- 组件:按钮
```python
self.button = QPushButton("Press Me!")
self.button.clicked.connect(self.the_button_was_clicked)
```

- 组件:输入框
```python
self.input = QLineEdit()
self.input.textChanged.connect(self.label.setText)
```

- 事件

| 事件                  | 功能         |
| --------------------- | ------------ |
| mouseMoveEvent        | 鼠标移动     |
| mousePressEvent       | 按下鼠标按钮 |
| mouseReleaseEvent     | 释放鼠标按钮 |
| mouseDoubleClickEvent | 检测到双击   |

```python
def mouseMoveEvent(self, e):
    self.label.setText("mouseMoveEvent")
```

- 四种基本布局

| 布局           | 解释                |
| -------------- | ------------------- |
| QHBoxLayout    | 线性水平布局        |
| QVBoxLayout    | 线性垂直布局        |
| QGridLayout    | 在可转位网格 XxY 中 |
| QStackedLayout | 堆叠 （z） 彼此前面 |

- 线性水平和垂直布局例子  
  - 示例位置1_example/pyqt/layout.py
```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QHBoxLayout
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout( layout2 )

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
```
