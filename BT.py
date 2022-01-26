import requests


def work(input):
        post_url = 'https://fanyi.baidu.com/sug'
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
        data = {'kw': str(input)}
        response = requests.post(url=post_url, data=data, headers=headers)
        dic_obj = response.json()
        '''
        with open('C:/Users/lenovo/Desktop/Translator', 'w', encoding='utf-8') as fp:
                fp.write(page_text)
        '''
        data_output = dic_obj['data']
        output = []
        for i in data_output:
                output.append(i['v'])

        output = '\n'.join(output)

        if output == '':
                return('目前还不支持该词条TAT')

        else:
                return(output)

