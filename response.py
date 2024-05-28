from decouple import config
from meapi import Me
from meapi.credentials_managers.json_files import JsonCredentialsManager


class Response_me_api:
    me = ''
    cm = JsonCredentialsManager(config_file="meapi_credentials.json")
    result = ''


    def __init__(self, number, accessnumber):
        try:
            self.me = Me(phone_number=accessnumber, credentials_manager=self.cm)
            self.result = self.api_call(number)
        except:
            self.me = Me(interactive_mode=True)
            self.result = self.api_call(number)

    def api_call(self, number):
        areacode = str(972)
        res = self.me.phone_search(areacode + number[1:])
        # print(res)
        if res:
            return(res['name'])
        else:
            return "error"
