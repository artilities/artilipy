## Artilipy is an official API wrapper written in Python
The library is made for easier interactions with Artilities API using Python. The library is maintained by Artilities Team.

### Installation:
```python
pip install artilipy
```

### Client initialisation example:

```python
from artilipy import client

# client init
artilities_client = client.Client()

# generate an idea
generated_idea = artilities_client.generate_idea()
```

### Add-on client initialisation example:

```python
from artilipy import addons

# add-on client init
addon_client = addons.ClientWithAddOns()

# fill ideas' cache
_ = [addon_client.generate_idea() for i in range(10)]

# use add-on functionality to beautify cached responses
print(addon_client.beautifyIdeaCache(lang='ru'))
```

### Read more about the wrapper in the docs:
https://artilities.github.io/artilipy/ (WIP)

### Explore other open-source projects provided by Artilities team:
https://github.com/artilities
