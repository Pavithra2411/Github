#Program return details of the repository with the most numbers of stars.
import pandas as pd
import requests 
from datetime import datetime
df = pd.DataFrame(columns=['repository_ID', 'name', 'URL', 'created_date',  'description', 'number_of_stars'])
results = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc').json()

for repo in results['items']:
        d_tmp = {'repository_ID': repo['id'],
                'name': repo['name'],
                'URL': repo['html_url'],
                'created_date': datetime.strptime(repo['created_at'], '%Y-%m-%dT%H:%M:%SZ'),
                'number_of_stars': repo['stargazers_count']}
        df = df.append(d_tmp, ignore_index=True)
        
        
print(d_tmp)