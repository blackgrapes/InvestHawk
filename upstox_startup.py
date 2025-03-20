import requests
from datetime import date, timedelta
access_token = 'eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2VUJUN1ciLCJqdGkiOiI2N2Q5MTZkNWNlMGM3ODYwNDM0MjBkZDQiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQyMjgwNDA1LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDIzMzUyMDB9.jevvL5Y9S5cseG_AP9mnScaOuU8hS3k4oJ693ha03xY'
tenstocks = []
fifteenstocks = []
twentystocks = []
dict2 = {'NSE_EQ|INE585B01010': 'MARUTI', 'NSE_EQ|INE139A01034': 'NATIONALUM', 'NSE_EQ|INE947Q01028': 'LAURUSLABS', 'NSE_EQ|INE918I01026': 'BAJAJFINSV', 'NSE_EQ|INE758E01017': 'JIOFIN', 'NSE_EQ|INE522D01027': 'MANAPPURAM', 'NSE_EQ|INE089A01031': 'DRREDDY', 'NSE_EQ|INE00R701025': 'DALBHARAT', 'NSE_EQ|INE848E01016': 'NHPC', 'NSE_EQ|INE917I01010': 'BAJAJ-AUTO', 'NSE_EQ|INE070A01015': 'SHREECEM', 'NSE_EQ|INE982J01020': 'PAYTM', 'NSE_EQ|INE761H01022': 'PAGEIND', 'NSE_EQ|INE749A01030': 'JINDALSTEL', 'NSE_EQ|INE591G01017': 'COFORGE', 'NSE_EQ|INE494B01023': 'TVSMOTOR', 'NSE_EQ|INE160A01022': 'PNB', 'NSE_EQ|INE736A01011': 'CDSL', 'NSE_EQ|INE646L01027': 'INDIGO', 'NSE_EQ|INE010B01027': 'ZYDUSLIFE', 'NSE_EQ|INE102D01028': 'GODREJ', 'NSE_EQ|INE302A01020': 'EXIDEIND', 'NSE_EQ|INE134E01011': 'PFC', 'NSE_EQ|INE009A01021': 'INFY', 'NSE_EQ|INE376G01013': 'BIOCON', 'NSE_EQ|INE619A01035': 'PATANJALI', 'NSE_EQ|INE465A01025': 'BHARATFORG', 'NSE_EQ|INE463A01038': 'BERGEPAINT', 'NSE_EQ|INE397D01024': 'BHARTIARTL', 'NSE_EQ|INE192R01011': 'DMART', 'NSE_EQ|INE540L01014': 'ALKEM', 'NSE_EQ|INE775A01035': 'MOTHERSON', 'NSE_EQ|INE237A01028': 'KOTAKBANK', 'NSE_EQ|INE059A01026': 'CIPLA', 'NSE_EQ|INE732I01013': 'ANGELONE', 'NSE_EQ|INE361B01024': 'DIVISLAB', 'NSE_EQ|INE797F01020': 'JUBLFOOD', 'NSE_EQ|INE811K01011': 'PRESTIGE', 'NSE_EQ|INE180A01020': 'MFSL', 'NSE_EQ|INE949L01017': 'AUBANK', 'NSE_EQ|INE881D01027': 'OFSS', 'NSE_EQ|INE030A01027': 'HINDUNILVR', 'NSE_EQ|INE795G01014': 'HDFCLIFE', 'NSE_EQ|INE476A01022': 'CANBK', 'NSE_EQ|INE745G01035': 'MCX', 'NSE_EQ|INE531E01026': 'HINDCOPPER', 'NSE_EQ|INE823G01014': 'JKCEMENT', 'NSE_EQ|INE721A01047': 'SHRIRAMFIN', 'NSE_EQ|INE028A01039': 'BANKBARODA', 'NSE_EQ|INE670K01029': 'LODHA', 'NSE_EQ|INE280A01028': 'TITAN', 'NSE_EQ|INE158A01026': 'HEROMOTOCO', 'NSE_EQ|INE123W01016': 'SBILIFE', 'NSE_EQ|INE298A01020': 'CUMMINSIND', 'NSE_EQ|INE192A01025': 'TATACONSUM', 'NSE_EQ|INE769A01020': 'AARTIIND', 'NSE_EQ|INE398R01022': 'SYNGENE', 'NSE_EQ|INE155A01022': 'TATAMOTORS', 'NSE_EQ|INE674K01013': 'ABCAPITAL', 'NSE_EQ|INE094A01015': 'HINDPETRO', 'NSE_EQ|INE274J01014': 'OIL', 'NSE_EQ|INE528G01035': 'YESBANK', 'NSE_EQ|INE093I01010': 'OBEROIRLTY', 'NSE_EQ|INE726G01019': 'ICICIPRULI', 'NSE_EQ|INE012A01025': 'ACC', 'NSE_EQ|INE073K01018': 'SONACOMS', 'NSE_EQ|INE095A01012': 'INDUSINDBK', 'NSE_EQ|INE006I01046': 'ASTRAL', 'NSE_EQ|INE562A01011': 'INDIANB', 'NSE_EQ|INE195A01028': 'SUPREMEIND', 'NSE_EQ|INE142M01025': 'TATATECH', 'NSE_EQ|INE849A01020': 'TRENT', 'NSE_EQ|INE669C01036': 'TECHM', 'NSE_EQ|INE136B01020': 'CYIENT', 'NSE_EQ|INE216A01030': 'BRITANNIA', 'NSE_EQ|INE002S01010': 'MGL', 'NSE_EQ|INE111A01025': 'CONCOR', 'NSE_EQ|INE062A01020': 'SBIN', 'NSE_EQ|INE118H01025': 'BSE', 'NSE_EQ|INE364U01010': 'ADANIGREEN', 'NSE_EQ|INE238A01034': 'AXISBANK', 'NSE_EQ|INE081A01020': 'TATASTEEL', 'NSE_EQ|INE044A01036': 'SUNPHARMA', 'NSE_EQ|INE883A01011': 'MRF', 'NSE_EQ|INE075A01022': 'WIPRO', 'NSE_EQ|INE498L01015': 'LTF', 'NSE_EQ|INE935N01020': 'DIXON', 'NSE_EQ|INE002L01015': 'SJVN', 'NSE_EQ|INE038A01020': 'HINDALCO', 'NSE_EQ|INE484J01027': 'GODREJPROP', 'NSE_EQ|INE031A01017': 'HUDCO', 'NSE_EQ|INE242A01010': 'IOC', 'NSE_EQ|INE205A01025': 'VEDL', 'NSE_EQ|INE027H01010': 'MAXHEALTH', 'NSE_EQ|INE692A01016': 'UNIONBANK', 'NSE_EQ|INE04I401011': 'KPITTECH', 'NSE_EQ|INE101D01020': 'GRANULES', 'NSE_EQ|INE010V01017': 'LTTS', 'NSE_EQ|INE263A01024': 'BEL', 'NSE_EQ|INE020B01018': 'RECLTD', 'NSE_EQ|INE685A01028': 'TORNTPHARM', 'NSE_EQ|INE647A01010': 'SRF', 'NSE_EQ|INE121A08PJ0': 'CHOLAFIN', 'NSE_EQ|INE860A01027': 'HCLTECH', 'NSE_EQ|INE974X01010': 'TIINDIA', 'NSE_EQ|INE854D01024': 'UNITDSPR', 'NSE_EQ|INE220G01021': 'JSL', 'NSE_EQ|INE742F01042': 'ADANIPORTS', 'NSE_EQ|INE226A01021': 'VOLTAS', 'NSE_EQ|INE171A01029': 'FEDERALBNK', 'NSE_EQ|INE976G01028': 'RBLBANK', 'NSE_EQ|INE047A01021': 'GRASIM', 'NSE_EQ|INE326A01037': 'LUPIN', 'NSE_EQ|INE262H01021': 'PERSISTENT', 'NSE_EQ|INE584A01023': 'NMDC', 'NSE_EQ|INE084A01016': 'BANKINDIA', 'NSE_EQ|INE085A01013': 'CHAMBLFERT', 'NSE_EQ|INE878B01027': 'KEI', 'NSE_EQ|INE836A01035': 'BSOFT', 'NSE_EQ|INE548A01028': 'HFCL', 'NSE_EQ|INE414G01012': 'MUTHOOTFIN', 'NSE_EQ|INE018E01016': 'SBICARD', 'NSE_EQ|INE669E01016': 'IDEA', 'NSE_EQ|INE776C01039': 'GMRAIRPORT', 'NSE_EQ|INE211B01039': 'PHOENIXLTD', 'NSE_EQ|INE417T01026': 'POLICYBZR', 'NSE_EQ|INE813H01021': 'TORNTPOWER', 'NSE_EQ|INE868B01028': 'NCC', 'NSE_EQ|INE213A01029': 'ONGC', 'NSE_EQ|INE335Y01020': 'IRCTC', 'NSE_EQ|INE931S01010': 'ADANIENSOL', 'NSE_EQ|INE821I01022': 'IRB', 'NSE_EQ|INE053F01010': 'IRFC', 'NSE_EQ|INE323A01026': 'BOSCHLTD', 'NSE_EQ|INE127D01025': 'HDFCAMC', 'NSE_EQ|INE021A01026': 'ASIANPAINT', 'NSE_EQ|INE356A01018': 'MPHASIS', 'NSE_EQ|INE733E01010': 'NTPC', 'NSE_EQ|INE214T01019': 'LTIM', 'NSE_EQ|INE176B01034': 'HAVELLS', 'NSE_EQ|INE022Q01020': 'IEX', 'NSE_EQ|INE545U01014': 'BANDHANBNK', 'NSE_EQ|INE511C01022': 'POONAWALLA', 'NSE_EQ|INE115A01026': 'LICHSGFIN', 'NSE_EQ|INE596I01012': 'CAMS', 'NSE_EQ|INE702C01027': 'APLAPOLLO', 'NSE_EQ|INE343H01029': 'SOLARINDS', 'NSE_EQ|INE388Y01029': 'NYKAA', 'NSE_EQ|INE117A01022': 'ABB', 'NSE_EQ|INE530B01024': 'IIFL', 'NSE_EQ|INE239A01024': 'NESTLEIND', 'NSE_EQ|INE758T01015': 'ZOMATO', 'NSE_EQ|INE154A01025': 'ITC', 'NSE_EQ|INE455K01017': 'POLYCAB', 'NSE_EQ|INE406A01037': 'AUROPHARMA', 'NSE_EQ|INE101A01026': 'M&M', 'NSE_EQ|INE437A01024': 'APOLLOHOSP', 'NSE_EQ|INE208A01029': 'ASHOKLEY', 'NSE_EQ|INE303R01014': 'KALYANKJIL', 'NSE_EQ|INE245A01021': 'TATAPOWER', 'NSE_EQ|INE288B01029': 'DEEPAKNTR', 'NSE_EQ|INE148O01028': 'DELHIVERY', 'NSE_EQ|INE331A01037': 'RAMCOCEM', 'NSE_EQ|INE053A01029': 'INDHOTEL', 'NSE_EQ|INE090A01021': 'ICICIBANK', 'NSE_EQ|INE628A01036': 'UPL', 'NSE_EQ|INE196A01026': 'MARICO', 'NSE_EQ|INE787D01026': 'BALKRISIND', 'NSE_EQ|INE018A01030': 'LT', 'NSE_EQ|INE121J01017': 'INDUSTOWER', 'NSE_EQ|INE140A01024': 'PEL', 'NSE_EQ|INE399L01023': 'ATGL', 'NSE_EQ|INE092T01019': 'IDFCFIRSTB', 'NSE_EQ|INE347G01014': 'PETRONET', 'NSE_EQ|INE067A01029': 'CGPOWER', 'NSE_EQ|INE438A01022': 'APOLLOTYRE', 'NSE_EQ|INE615H01020': 'TITAGARH', 'NSE_EQ|INE423A01024': 'ADANIENT', 'NSE_EQ|INE121E01018': 'JSWENERGY', 'NSE_EQ|INE019A01038': 'JSWSTEEL', 'NSE_EQ|INE151A01013': 'TATACOMM', 'NSE_EQ|INE259A01022': 'COLPAL', 'NSE_EQ|INE522F01014': 'COALINDIA', 'NSE_EQ|INE095N01031': 'NBCC', 'NSE_EQ|INE296A01024': 'BAJFINANCE', 'NSE_EQ|INE765G01017': 'ICICIGI', 'NSE_EQ|INE066F01020': 'HAL', 'NSE_EQ|INE257A01026': 'BHEL', 'NSE_EQ|INE002A01018': 'RELIANCE', 'NSE_EQ|INE203G01027': 'IGL', 'NSE_EQ|INE467B01029': 'TCS', 'NSE_EQ|INE774D08MG3': 'M&MFIN', 'NSE_EQ|INE647O01011': 'ABFRL', 'NSE_EQ|INE079A01024': 'AMBUJACEM', 'NSE_EQ|INE129A01019': 'GAIL', 'NSE_EQ|INE0J1Y01017': 'LICI', 'NSE_EQ|INE481G01011': 'ULTRACEMCO', 'NSE_EQ|INE299U01018': 'CROMPTON', 'NSE_EQ|INE040A01034': 'HDFCBANK', 'NSE_EQ|INE114A01011': 'SAIL', 'NSE_EQ|INE486A01021': 'CESC', 'NSE_EQ|INE935A01035': 'GLENMARK', 'NSE_EQ|INE603J01030': 'PIIND', 'NSE_EQ|INE003A01024': 'SIEMENS', 'NSE_EQ|INE202E01016': 'IREDA', 'NSE_EQ|INE066A01021': 'EICHERMOT', 'NSE_EQ|INE029A01011': 'BPCL', 'NSE_EQ|INE670A01012': 'TATAELXSI', 'NSE_EQ|INE663F01024': 'NAUKRI', 'NSE_EQ|INE752E01010': 'POWERGRID', 'NSE_EQ|INE092A01019': 'TATACHEM', 'NSE_EQ|INE271C01023': 'DLF', 'NSE_EQ|INE318A01026': 'PIDILITIND', 'NSE_EQ|INE200M01039': 'VBL', 'NSE_EQ|INE016A01026': 'DABUR', 'NSE_EQ|INE042A01014': 'ESCORTS'}
# previous_close_data = {}

# for key in dict2:
#     # Get Yesterday's Date
#     yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")

#     # API URL (From Date & To Date are both yesterday to get single day's data)
#     url = f"https://api.upstox.com/v2/historical-candle/{key}/day/{yesterday}/{yesterday}"

#     # Set headers
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }

#     # Make the API request
#     response = requests.get(url, headers=headers)
#     data = response.json()
#     if "data" in data and "candles" in data["data"] and len(data["data"]["candles"]) > 0:
#         previous_close = data["data"]["candles"][0][4]
#         ten = previous_close * 1.1
#         fifteen = previous_close * 1.15
#         twenty = previous_close * 1.2
#         tensell = previous_close * .9
#         fifteensell = previous_close * .85
#         twentysell = previous_close * .8          
#         previous_close_data[key]= {'pre_day':previous_close, 'ten':ten, 'fifteen':fifteen, 'twenty':twenty, 'tensell':tensell, 'fifteensell':fifteensell, 'twentysell':twentysell}
# print(previous_close_data)        



# fake real time data
real_time_data = {
    "ABB": {'Stock Symbol': 'NSE_EQ|INE010B01027', 'Last Traded Price': 902.15, 'Last Traded Time': '1742293347896', 'Last Traded Quantity': '1', 'Closing Price': 892.7, 'Current Timestamp': '1742297201718'}, "ACC": {'Stock Symbol': 'NSE_EQ|INE010B01027', 'Last Traded Price': 902.15, 'Last Traded Time': '1742293347896', 'Last Traded Quantity': '1', 'Closing Price': 892.7, 'Current Timestamp': '1742297201718'}}

# fake previousday data
previous_close_data = {
    'NSE_EQ|INE585B01010': {'pre_day': 11553.7, 'ten': 12709.070000000002, 'fifteen': 13286.755, 'twenty': 13864.44},
    'NSE_EQ|INE139A01034': {'pre_day': 185.03, 'ten': 203.53300000000002, 'fifteen': 212.78449999999998, 'twenty': 222.036},
    'NSE_EQ|INE947Q01028': {'pre_day': 581.35, 'ten': 639.4850000000001, 'fifteen': 668.5525, 'twenty': 697.62},
    'NSE_EQ|INE918I01026': {'pre_day': 1871.6, 'ten': 2058.76, 'fifteen': 2152.3399999999997, 'twenty': 2245.9199999999996},
    'NSE_EQ|INE758E01017': {'pre_day': 219.52, 'ten': 241.47200000000004, 'fifteen': 252.44799999999998, 'twenty': 263.424},
    'NSE_EQ|INE522D01027': {'pre_day': 209.62, 'ten': 230.58200000000002, 'fifteen': 241.063, 'twenty': 251.54399999999998},
    'NSE_EQ|INE089A01031': {'pre_day': 1150.7, 'ten': 1265.7700000000002, 'fifteen': 1323.305, 'twenty': 1380.84},
    'NSE_EQ|INE00R701025': {'pre_day': 1663.35, 'ten': 1829.685, 'fifteen': 1912.8524999999997, 'twenty': 1996.0199999999998},
    'NSE_EQ|INE848E01016': {'pre_day': 78.33, 'ten': 86.16300000000001, 'fifteen': 90.0795, 'twenty': 93.996},
    'NSE_EQ|INE917I01010': {'pre_day': 7486.05, 'ten': 8234.655, 'fifteen': 8608.9575, 'twenty': 8983.26},
    'NSE_EQ|INE070A01015': {'pre_day': 27734.6, 'ten': 30508.06, 'fifteen': 31894.789999999997, 'twenty': 33281.52},
    'NSE_EQ|INE982J01020': {'pre_day': 688.9, 'ten': 757.7900000000001, 'fifteen': 792.2349999999999, 'twenty': 826.68},
    'NSE_EQ|INE761H01022': {'pre_day': 40361.7, 'ten': 44397.87, 'fifteen': 46415.954999999994, 'twenty': 48434.03999999999},
    'NSE_EQ|INE749A01030': {'pre_day': 897.25, 'ten': 986.9750000000001, 'fifteen': 1031.8374999999999, 'twenty': 1076.7},
    'NSE_EQ|INE591G01017': {'pre_day': 7365.05, 'ten': 8101.555000000001, 'fifteen': 8469.807499999999, 'twenty': 8838.06},
    'NSE_EQ|INE494B01023': {'pre_day': 2266.8, 'ten': 2493.4800000000005, 'fifteen': 2606.82, 'twenty': 2720.1600000000003},
    'NSE_EQ|INE160A01022': {'pre_day': 87.47, 'ten': 96.21700000000001, 'fifteen': 100.59049999999999, 'twenty': 104.964},
    'NSE_EQ|INE736A01011': {'pre_day': 1058.2, 'ten': 1164.0200000000002, 'fifteen': 1216.93, 'twenty': 1269.84},
    'NSE_EQ|INE646L01027': {'pre_day': 4780.45, 'ten': 5258.495, 'fifteen': 5497.517499999999, 'twenty': 5736.54},
    'NSE_EQ|INE010B01027': {'pre_day': 892.7, 'ten': 981.9700000000001, 'fifteen': 1026.605, 'twenty': 1071.24},
    'NSE_EQ|INE102D01028': {'pre_day': 1052.3, 'ten': 1157.53, 'fifteen': 1210.1449999999998, 'twenty': 1262.76},
    'NSE_EQ|INE302A01020': {'pre_day': 334.15, 'ten': 367.565, 'fifteen': 384.2724999999999, 'twenty': 400.97999999999996},
    'NSE_EQ|INE134E01011': {'pre_day': 389.7, 'ten': 428.67, 'fifteen': 448.155, 'twenty': 467.64},
    'NSE_EQ|INE009A01021': {'pre_day': 1590.05, 'ten': 1749.055, 'fifteen': 1828.5575, 'twenty': 1908.06},
    'NSE_EQ|INE376G01013': {'pre_day': 333.25, 'ten': 366.57500000000005, 'fifteen': 383.23749999999995, 'twenty': 399.9},
    'NSE_EQ|INE619A01035': {'pre_day': 1725.05, 'ten': 1897.555, 'fifteen': 1983.8075, 'twenty': 2070.06},
    'NSE_EQ|INE465A01025': {'pre_day': 1076.35, 'ten': 1183.985, 'fifteen': 1237.8024999999998, 'twenty': 1291.62},
    'NSE_EQ|INE463A01038': {'pre_day': 502.65, 'ten': 552.915, 'fifteen': 578.0474999999999, 'twenty': 603.18},
    'NSE_EQ|INE397D01024': {'pre_day': 1639.15, 'ten': 1803.0650000000003, 'fifteen': 1885.0225, 'twenty': 1966.98},
    'NSE_EQ|INE192R01011': {'pre_day': 3825.3, 'ten': 4207.830000000001, 'fifteen': 4399.095, 'twenty': 4590.36},
    'NSE_EQ|INE540L01014': {'pre_day': 4818.15, 'ten': 5299.965, 'fifteen': 5540.8724999999995, 'twenty': 5781.78},
    'NSE_EQ|INE775A01035': {'pre_day': 120.99, 'ten': 133.089, 'fifteen': 139.1385, 'twenty': 145.188},
    'NSE_EQ|INE237A01028': {'pre_day': 1993.1, 'ten': 2192.41, 'fifteen': 2292.0649999999996, 'twenty': 2391.72},
    'NSE_EQ|INE059A01026': {'pre_day': 1492.6, 'ten': 1641.8600000000001, 'fifteen': 1716.4899999999998, 'twenty': 1791.12},
    'NSE_EQ|INE732I01013': {'pre_day': 1979.85, 'ten': 2177.835, 'fifteen': 2276.8275, 'twenty': 2375.8199999999997}
}


def call():
    for key2 in real_time_data :
        ltp = real_time_data[key2]['Last Traded Price']
        symbol = real_time_data[key2]['Stock Symbol']
        # print(ltp,symbol)
        # print(previous_close_data[symbol]['ten'])
        
        if ltp>previous_close_data[symbol]['ten']:
            print('buy')
            tenstocks.append[symbol]
        elif ltp<previous_close_data[symbol]['tensell']:
            print('sell')
            tenstocks.append[symbol]
                
call()

def call_ten():
    for i in tenstocks:
        ltp = real_time_data[i]['Last Traded Price']
        symbol = real_time_data[i]['Stock Symbol']
        # print(ltp,symbol)
        # print(previous_close_data[symbol]['ten'])
        
        if ltp>previous_close_data[symbol]['fifteen']:
            print('buy')
            fifteenstocks.append[symbol]
        elif ltp<previous_close_data[symbol]['fifteensell']:
            print('sell')
            fifteenstocks.append[symbol]
            
def call_fifteen():
    for i in fifteenstocks:
        ltp = real_time_data[i]['Last Traded Price']
        symbol = real_time_data[i]['Stock Symbol']
        # print(ltp,symbol)
        # print(previous_close_data[symbol]['ten'])
        
        if ltp>previous_close_data[symbol]['twenty']:
            print('buy')
        elif ltp<previous_close_data[symbol]['twentysell']:
            print('sell')
        