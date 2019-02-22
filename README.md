Sanic-Jinja
===

**install**:

> pip install Sanic-Jinja

**example**:

```python
from sanic_jinja import generate_template
template = generate_template('app')

@app.route("/")
async def index(request):
    return template('index.html', name='ben')
```