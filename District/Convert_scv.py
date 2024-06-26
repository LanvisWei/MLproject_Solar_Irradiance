import pandas as pd

# 創建一個站名到區域的對照表
station_to_district = {
    '桃改樹林分場': '新北市',
    '茶改北部分場': '新北市',
    '桃園農改': '桃園市',
    '茶改場': '南投縣',
    '農工中心': '台中市',
    '桃改五峰分場': '新竹縣',
    '桃改新埔分場': '新竹縣',
    '畜試北區分所': '苗栗縣',
    '苗改生物防治研究中心': '苗栗縣',
    '苗栗農改': '苗栗縣',
    '種苗繁殖': '台中市',
    '農業試驗所': '台中市',
    '王功漁港': '彰化縣',
    '臺中農改': '台中市',
    '中改埔里分場': '南投縣',
    '林試畢祿溪站': '南投縣',
    '臺大內茅埔': '南投縣',
    '臺大和社': '南投縣',
    '臺大溪頭': '南投縣',
    '臺大竹山': '南投縣',
    '茶改中部分場': '南投縣',
    '茶改南部分場': '嘉義縣',
    '萬大發電廠': '南投縣',
    '蓮華池': '南投縣',
    '南改斗南分場': '雲林縣',
    '口湖工作站': '雲林縣',
    '四湖植物園': '雲林縣',
    '水試臺西試驗場': '雲林縣',
    '海口故事園區': '雲林縣',
    '臺大雲林校區': '雲林縣',
    '麥寮合作社': '雲林縣',
    '農試嘉義分所': '嘉義市',
    '南改義竹分場': '嘉義縣',
    '南改鹿草分場': '嘉義縣',
    '布袋國中': '嘉義縣',
    '農試溪口農場': '嘉義縣',
    '七股研究中心': '台南市',
    '六官養殖協會': '台南市',
    '水試所海水繁養殖中心': '台南市',
    '畜試所': '屏東縣',
    '臺南蘭花園區': '台南市',
    '臺南農改': '台南市',
    '林試六龜中心': '高雄市',
    '林試扇平站': '高雄市',
    '農試鳳山分所': '高雄市',
    '高改旗南分場': '高雄市',
    '崎峰國小': '屏東縣',
    '恆春工作站': '屏東縣',
    '東港工作站': '屏東縣',
    '畜試南區分所': '屏東縣',
    '高雄農改': '高雄市',
    '畜試東區分所': '台東縣',
    '花改蘭陽分場': '宜蘭縣',
    '花蓮農改': '花蓮縣',
    '東改班鳩分場': '花蓮縣',
    '東改賓朗果園': '花蓮縣',
    '林試太麻里1': '台東縣',
    '林試太麻里2': '台東縣',
    '茶改東部分場': '台東縣'
}

# 將對照表轉換成DataFrame
df = pd.DataFrame(list(station_to_district.items()), columns=['站名', '區域'])

# 保存為CSV文件
csv_file_path = 'stations_districts.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved to {csv_file_path}")