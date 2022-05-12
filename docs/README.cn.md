# AutoSysPath
## 一个Python自动添加项目位置到sys.path的工具

## 安装:
```shell
pip install toautosyspath 
```

## 示例: (存在以下项目结构)
example-project:  
&nbsp;&nbsp;&nbsp;&nbsp;- package1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `__init__`.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- main.py  
&nbsp;&nbsp;&nbsp;&nbsp;- package2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- `__init__`.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- util.py  

在 main.py 中存在如下代码:
```python
import autosyspath

from package2.util import helloworld

helloworld()
```

<p>你能够在任何路径运行main.py而不会出现依赖错误.</p>  
<p>示例:</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd /example-project && python package1/main.py</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd / && python example-project/package1/main.py</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd /example-project/package1 && python main.py</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd /xxx && python /example-project/package1/main.py</p>

<p>以上方式均可正常运行.</p>  