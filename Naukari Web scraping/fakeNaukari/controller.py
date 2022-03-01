import json
import redis
import pandas as pd

class Controller:
    data = []
    r = redis.Redis(connection_pool=redis.ConnectionPool(host='localhost',port=6379))
    def __init__(self) -> None:
        for page_number in range(1, 11):
            pageDataJson = self.r.get(r'page-'+str(page_number))
            if pageDataJson is not None: 
                json_data = pd.DataFrame.from_dict(json.loads(pageDataJson))
                self.parseJson(json_data.to_dict(orient='records'))

        self.data = sorted(self.data, key=lambda x: x['Job_Post_History'], reverse=True)
    
    def parseJson(self, json_data):
        for x in json_data:
            self.data.append(x)
    
    def getTop(self, record):
        df_all =  pd.DataFrame(self.data[0:record])
        return json.loads(df_all.to_json (orient='records'))
    
    def getJobsInLocationAtPage(self,location, page):
        return [obj for obj in json.loads(self.r.get(r'page-'+str(page))) if location in obj['Location']]

