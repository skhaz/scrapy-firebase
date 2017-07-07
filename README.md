scrapy-firebase
===============
Firebase pipeline for Scrapy.

Installation
------------
Install via `pip`:

    pip install scrapy-firebase

Configuration
-------------

### Basic configuration example

Follow the steps on this [guide](https://firebase.google.com/docs/admin/setup), once you downloaded the json with firebase secrets, convert it to base64. On macos you can use the follwing command line to convert and copy to your clipboard:

```bash
cat firebase_secrets.json | openssl base64 | pbcopy
```

Add `scrapy-firebase` to your projects `settings.py` file and setup some variables.

```python
ITEM_PIPELINES = [
  'scrapy_firebase.FirebasePipeline',
]

FIREBASE_SECRETS = """
  YOUR BASE64 ENCODED JSON HERE
"""

FIREBASE_DATABASE = 'https://project-id.firebaseio.com/'  # replace project-id to yours

FIREBASE_REF = ''  # insert an appropriate value

FIREBASE_KEYS = ['uid', 'spider_name']  # to compose more robust
                                        # child paths, you can add
                                        # a list of properties

```
