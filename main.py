import pandas as pd
import random
from datetime import datetime, timedelta

# 构造训练数据并保存为training_data.csv
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 1, 1)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# 阈值
amplitude_threshold = 0.02
current_threshold = 2.6
speed_threshold = 1000

data = {
    '日期': [],
    '振幅': [],
    '电流': [],
    '转速': [],
    '机器告警': []
}

random.seed(42)  # 设置随机种子以保持结果可复现

num_alerts = 0  # 记录机器告警为1的条目数量

while len(data['日期']) < 1000:
    date = random.choice(dates)
    data['日期'].append(date)
    data['振幅'].append(random.uniform(0, 0.05))  # 随机生成振幅
    data['电流'].append(random.uniform(2.4, 3.0))  # 随机生成电流
    data['转速'].append(random.randint(900, 1100))  # 随机生成转速

    if data['振幅'][-1] >= amplitude_threshold or data['电流'][-1] >= current_threshold or data['转速'][-1] >= speed_threshold:
        if num_alerts < 10:
            data['机器告警'].append(1)
            num_alerts += 1
        else:
            data['机器告警'].append(0)
    else:
        data['机器告警'].append(0)

df = pd.DataFrame(data)
df.to_csv('training_data.csv', index=False)
