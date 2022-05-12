# Auto sys path
## A python automatically adds the current project sys Path tool

### Use example:
example-project:  
&nbsp;&nbsp;&nbsp;&nbsp;- package1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- __init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- main.py  
&nbsp;&nbsp;&nbsp;&nbsp;- package2  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- __init__.py  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- util.py  

at main.py
```python
import autosyspath

from package2.util import helloworld

helloworld()
```
<p>You can run anywhere main.py without error.</p>  
<p>example:</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd /example-project && python package1/main.py</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd / && python example-project/package1/main.py</p>  
<p>&nbsp;&nbsp;&nbsp;&nbsp;> cd /example-project/package1 && python main.py</p>  

<p>that's all ok.</p>  