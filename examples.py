import sys
import pprint
import logging
import logging.config

from popit_api import PopIt

# `print` is ok but time to learn some logger :)
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG', # Change this to WARN reduce verbosity
    },
}

# For more info, read this https://docs.python.org/2/library/logging.html
logging.config.dictConfig(LOGGING)
log = logging.getLogger(__name__)

try:
    api = PopIt(
        instance='sinar-malaysia',
        hostname='popit.mysociety.org',
        api_version='v0.1',
        api_key='c7fd488c278814dbdc9c63d294c92d01d5795108'
    )
except Exception as e:
    sys.exit(e)

if api.is_online():
    log.info('ready to popit :)')
else:
    sys.exit('connection failed :(')

##### api.persons section
log.info('adding persons record...')
me = api.persons.post({'name': 'Chow Chee Leong'})
log.info(pprint.pformat(me))

my_id = me['result']['id']
log.info('showing off my new id: {id}'.format(id=my_id))

# this will be our working data
my_info = me['result']

my_info['other_names'].append({'name': 'motionman'})
my_info['contact_details'].append({
    'label': 'Email Address',
    'type': 'email',
    'value': 'motionman@sinarproject.org'
})

log.info('updating my person info...')
try:
    result = api.persons(my_id).put(my_info)
except Exception as e:
    log.error(e)

# get the latest working copy
log.info('haz update \\0/')
my_info = result['result']
log.info(pprint.pformat(my_info))

##### api.persons section ends

##### api.organizations section

log.info('adding organizations record...')
sinar = api.organizations.post({'name': 'Sinar Project'})
log.info(pprint.pformat(sinar))

sinar_id = sinar['result']['id']
log.info('showing off my sinar (shiny) new id: {id}'.format(id=sinar_id))

sinar_info = sinar['result']
sinar_info['contact_details'].append({
    'label': 'Email Address',
    'type': 'email',
    'value': 'info@sinarproject.org'
})
sinar_info['classification'] = 'NGO'

log.info('updating sinar info...')
try:
    result = api.organizations(sinar_id).put(sinar_info)
except Exception as e:
    log.error(e)

sinar_info = result['result']
log.info(pprint.pformat(sinar_info))

##### api.organizations section ends

##### api.posts section

# a tip of advice, create posts first ;)
log.info('adding posts in Sinar Project...')
my_post = api.posts.post({
    'label': 'IT Department',
    'organization_id': sinar_id,
})
log.info(pprint.pformat(my_post))

post_id = my_post['result']['id']
log.info('new posts id: {id}'.format(id=post_id))

# OPTIONAL
# post_info = my_post['result']
# organization_id can be changed anytime
# post_info['organization_id'] = sinar_id
# log.info('updating post info...')
# try:
#     result = api.posts(post_id).put(post_info)
# except Exception as e:
#     log.error(e)
# post_info = result['result']
# log.info(pprint.pformat(post_info))

##### api.posts section ends

##### api.memberships section
log.info('adding memberships record...')
my_membership = api.memberships.post({
    'organization_id': sinar_id,
    'post_id': post_id,
    'person_id': my_id,
    'role': 'Software Developer',
    'start_date': '2013-05-01',
    'end_date': None,
})
log.info(pprint.pformat(my_membership))

membership_id = my_membership['result']['id']
log.info('my membership id: {id}'.format(id=membership_id))

##### api.memberships section ends

# For testing only, comment these to persist the record
# log.info('deleting memberships record...')
# api.memberships(membership_id).delete()
# log.info('membership deleted :(')

# log.info('deleting posts record...')
# api.posts(post_id).delete()
# log.info('post deleted :(')

# log.info('deleting my persons record...')
# api.persons(my_id).delete()
# log.info('my persons record deleted :(')

# log.info('deleting my organizations record...')
# api.organizations(sinar_id).delete()
# log.info('sinar organization record deleted, not again!? :(')

# Foot note
log.info('done')
