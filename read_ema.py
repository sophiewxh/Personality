import os
import json
from datetime import datetime
from pprint import pprint
from operator import itemgetter
from util import write_feature_to_csv

# questions = ["Dimensions protestors",     #2013-04-24-22:41:36
#             "Administration's response",  #2013-04-26-02:50:26
#             "Dartmouth now",              #2013-04-27-10:47:19
#             "Dimensions",
#             "Cancelled Classes"]

questions = [r'Stress']

ids = ['%02d' % i for i in range(60)]
count = {id:0 for id in ids}
#q1 = {id:'NA' for id in ids}

def read_response():
    
    dir = os.path.join('dataset', 'EMA', 'response', 'Stress')
    for file in os.listdir(dir):
        
        id = file.split('.')[0][-2:]
        fr = open(os.path.join(dir, file))
        data = json.load(fr)

        if not data:
            continue
        
        if not id in ['59']:
            continue
        
        print '-------------'
        print 'ID: ' + id
        #sorted_entries = []
        entries = []
        for entry in data:
            entries.append(entry)
        entries = sorted(entries, key=itemgetter('resp_time'))
        
        print 'number of responses ' + str(len(entries))
        
        for entry in entries:
            time = datetime.fromtimestamp(entry['resp_time']).strftime('%Y-%m-%d-%H:%M:%S')
            print 
            print time
            print entry
                
              
def read_question():     
    json_data=open(r'dataset\EMA\EMA_definition.json').read()
    data = json.loads(json_data)
    pprint(data)       
                               
#pp.pprint(count)
#write_feature_to_csv(count, 'reply_count', False)
#write_feature_to_csv(id_value, 'q3', False)

if __name__ == '__main__':
    #read_question()
    read_response()
    
