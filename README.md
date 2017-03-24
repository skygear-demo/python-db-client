# Skygear Database Usage - Python Example

Perform simple actions to write / read data from Skygear database.

## Before start
 1. Sign up on [Skygear Developer Portal](https://portal.skygear.io).
 2. Login to portal and create and app.
 3. Go to **Info** page.
 4. Copy the **Server Endpoint** and **API Key** in Server Details section.
 5. Open **set_env.sh** in this directory and update the environment variables to your own information (or set the environment variables directly).

## Get Started

Assume you have Python 3.5 installed.

Open terminal and call the followings:

```
$ cd <directory containing this file>
$ pyvenv-3.5 py3.5
$ source py3.5/bin/activate
$ pip install -r requirements.txt
$ source ./set_env.sh
```

Then you can look at the example in *example.py* to see how to call the functions. You may try out the sample script:

```
$ python example.py
```
You will see the result in your [Web Browser Database](https://portal.skygear.io/browser/index.html).

## How to script

### Initialize

```
sky = SkyHandler()
```

### Create / Update a record

```
sky.update_record(table_name, record_id, {
		'record_field_1': 'record_content_1',
		'record_field_2': 'record_content_2',
		'record_field_3': 'record_content_3'
	}
)
```

### Update records in a batch

Please beware of the `_id` format when using

```
sky.update_records(
  {
    '_id': 'record_type/record_1_id',
		'record_field_1': 'record_1_content_1',
		'record_field_2': 'record_1_content_2',
		'record_field_3': 'record_1_content_3'
	},
  {
    '_id': 'record_type/record_2_id',
		'record_field_1': 'record_2_content_1',
		'record_field_2': 'record_2_content_2',
		'record_field_3': 'record_2_content_3'
	}
)
```

### Search records

```
content_to_fetch = sky.search_records(table_name, {
    'field_for_search_1': 'content_for_search_1',
    'field_for_search_2': 'content_for_search_2',
    'field_for_search_3': 'content_for_search_3',
  }
)

content_to_search = sky.filter_result(fetched_content, field_to_search)
```
For example if you have a table called friends, you know the name and phone number of a user, and you want to search for his address:

```
james_info = sky.search_records('friends', {
    'name': 'james',
    'phone_no': '98765432',
  }
)

james_address = sky.filter_result(james_info, 'address')
```

Please note that the values returned will be an array.
