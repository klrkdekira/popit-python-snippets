Data Creation with PopIt-Python
===

### Table of contents

[TOC]

Introduction
---
Hi guys, in this blog post, I'll be demonstrating some basics on how to manage PopIt records with `PopIt-Python`. I'll be using the Sinar PopIt instance as the working example.

> **Note**
Since this is a [Python](https://www.python.org/) specific topic. I'll assume most will know how to install remote `Python` packages. Else, read [here](https://packaging.python.org/en/latest/installing.html#setup-for-installing-distribution-packages).

Preparation
---
Install PopIt-Python

```bash
pip install PopIt-Python
```

Let's construct a PopIt-Python object. Your configuration will be stored here and throughout the tutorial we'll be using this object to call the PopIt API.

```python
from popit_api import PopIt

api = PopIt(
instance='sinar-malaysia',
hostname='popit.mysociety.org',
api_version='v0.1',
api_key='yourapikeyhere',
)
```

Now let's proceed to our first record creation.

Persons
---

### Create

```python
me = api.persons.post({'name': 'Chow Chee Leong'})
print(me)
```

The response

```json
{u'result': {u'contact_details': [],
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/persons/54c48c8fdde553347cbe01e3',
u'id': u'54c48c8fdde553347cbe01e3',
u'identifiers': [],
u'links': [],
u'memberships': [],
u'name': u'Chow Chee Leong',
u'other_names': [],
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/persons/54c48c8fdde553347cbe01e3'}}

my_id = me['result']['id']
```

### Update

```python
# this will be our working data
my_info = me['result']

my_info['other_names'].append({'name': 'motionman'})
my_info['contact_details'].append({
    'label': 'Email Address',
        'type': 'email',
            'value': 'motionman@sinarproject.org'
            })

result = api.persons(my_id).put(my_info)

my_info = result['result']
print(my_info)
```

```json
{u'contact_details': [{u'id': u'54c48c90dde553347cbe01e5',
u'label': u'Email Address',
u'type': u'email',
u'value': u'motionman@sinarproject.org'}],
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/persons/54c48c8fdde553347cbe01e3',
u'id': u'54c48c8fdde553347cbe01e3',
u'identifiers': [],
u'links': [],
u'memberships': [],
u'name': u'Chow Chee Leong',
u'other_names': [{u'id': u'54c48c90dde553347cbe01e4', u'name': u'motionman'}],
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/persons/54c48c8fdde553347cbe01e3'}
```

The result [Person](https://sinar-malaysia.popit.mysociety.org/persons/54c48c8fdde553347cbe01e3#political-career) page.

### Delete

```python
api.persons(my_id).delete()
```

Organizations
---

### Create

```python
sinar = api.organizations.post({'name': 'Sinar Project'})
sinar_id = sinar['result']['id']
```

```json
{u'result': {u'contact_details': [],
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/organizations/54c48c90dde553347cbe01e6',
u'id': u'54c48c90dde553347cbe01e6',
u'identifiers': [],
u'links': [],
u'memberships': [],
u'name': u'Sinar Project',
u'other_names': [],
u'posts': [],
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/organizations/54c48c90dde553347cbe01e6'}}
```

### Update

```python
sinar_info = sinar['result']
sinar_info['contact_details'].append({
    'label': 'Email Address',
        'type': 'email',
            'value': 'info@sinarproject.org'
            })
            sinar_info['classification'] = 'NGO'

result = api.organizations(sinar_id).put(sinar_info)

sinar_info = result['result']
print(sinar_info)
```

```json
{u'classification': u'NGO',
u'contact_details': [{u'id': u'54c48c90dde553347cbe01e7',
u'label': u'Email Address',
u'type': u'email',
u'value': u'info@sinarproject.org'}],
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/organizations/54c48c90dde553347cbe01e6',
u'id': u'54c48c90dde553347cbe01e6',
u'identifiers': [],
u'links': [],
u'memberships': [],
u'name': u'Sinar Project',
u'other_names': [],
u'posts': [],
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/organizations/54c48c90dde553347cbe01e6'}
```

### Delete

```python
api.organizations(sinar_id).delete()
```

Posts
---

### Create

```python
my_post = api.posts.post({
    'label': 'IT Department',
        'organization_id': sinar_id,
        })
        print(my_post)
        ```

```json
{u'result': {u'contact_details': [],
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/posts/54c48c91dde553347cbe01e8',
u'id': u'54c48c91dde553347cbe01e8',
u'label': u'IT Department',
u'links': [],
u'memberships': [],
u'organization_id': u'54c48c90dde553347cbe01e6',
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/posts/54c48c91dde553347cbe01e8'}}
```

### Delete

```python
api.posts(post_id).delete()
```

Memberships
---

### Create

```python
my_membership = api.memberships.post({
    'organization_id': sinar_id,
        'post_id': post_id,
            'person_id': my_id,
                'role': 'Software Developer',
                    'start_date': '2013-05-01',
                        'end_date': None,
                        })
                        print(my_membership)
                        ```

```json
{u'result': {u'contact_details': [],
u'end_date': None,
u'html_url': u'http://sinar-malaysia.popit.mysociety.org/memberships/54c48c91dde553347cbe01e9',
u'id': u'54c48c91dde553347cbe01e9',
u'links': [],
u'organization_id': u'54c48c90dde553347cbe01e6',
u'person_id': u'54c48c8fdde553347cbe01e3',
u'post_id': u'54c48c91dde553347cbe01e8',
u'role': u'Software Developer',
u'start_date': u'2013-05-01',
u'url': u'http://sinar-malaysia.popit.mysociety.org/api/v0.1/memberships/54c48c91dde553347cbe01e9'}}
```

### Delete

```python
api.memberships(membership_id).delete()
```

End
---
That concludes our brief introduction of data creation with PopIt-Python.

For the script with all the above examples, check out [examples.py](https://github.com/klrkdekira/popit-python-snippets/blob/master/examples.py). However there are some changes

- Uses Python [logging](https://docs.python.org/2/library/logging.html) module instead of `print`.
- Outputs are pretty-printed with [pprint](https://docs.python.org/2/library/pprint.html).
- Simple exception handling.

Tips & Tricks
---
- For an empty field, empty string `''` is not accepted. Make sure to check and convert them to `null` (or in Python `None`)
- The Python SDK is developed with [slumber](http://slumber.readthedocs.org/en/v0.6.0/), it's a smart decision because it maps the RESTful API as it changes instead of hardcoding.
- Failed API calls throw exception, make sure they're captured to avoid interrupting your program.

Reference
---
- [PopIt API](http://popit.poplus.org/docs/api/)
- [PopIt-Python](https://github.com/mysociety/popit-python)
- [slumber](http://slumber.readthedocs.org/en/v0.6.0/)
