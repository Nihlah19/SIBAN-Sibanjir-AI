import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

os.makedirs('model', exist_ok=True)

np.random.seed(42)
n = 3000

curah_hujan = np.random.normal(120, 60, n).clip(0,300)
jarak_sungai = np.random.normal(400, 250, n).clip(10,1000)
ketinggian = np.random.normal(20, 15, n).clip(0,100)
drainase = np.random.uniform(0,1,n) # 0 = buruk, 1 = baik
kepadatan = np.random.uniform(0,1,n) # urban density

risk_score = (
    (curah_hujan/300)*0.4 +
    (1 - jarak_sungai/1000)*0.2 +
    (1 - ketinggian/100)*0.2 +
    (1 - drainase)*0.1 +
    kepadatan*0.1
)

status = []
for r in risk_score:
    if r < 0.4:
        status.append(0)
    elif r < 0.7:
        status.append(1)
    else:
        status.append(2)

df = pd.DataFrame({
    'curah_hujan': curah_hujan,
    'jarak_sungai': jarak_sungai,
    'ketinggian': ketinggian,
    'drainase': drainase,
    'kepadatan': kepadatan,
    'status': status
})

X = df.drop(columns=['status'])
y = df['status']

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)

model.fit(X,y)

with open('model/flood_model.pkl','wb') as f:
    pickle.dump(model,f)

print("Model baru lebih realistis berhasil disimpan!")