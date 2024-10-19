from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args={
    'owner': 'Aleksander Kirsten',
    'starting_date': datetime(2024, 10, 19, 9, 00)
}

def get_data():
    import requests
    import json

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    # print(json.dumps(res, indent= 3))
    return res

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}" ## I might need to double check here later
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registerted_date'] = res['registered']['date']
    data['phone'] = res['phones']
    data['picture'] = data['picture']['medium']
    return data
    
                    



    


def stream_data():
    import json
    import requests

    




# with DAG('user_automation',
#         default_args=default_args,
#         schedule_interval='@daily',
#         catchup=False) as dag:

#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )

stream_data()