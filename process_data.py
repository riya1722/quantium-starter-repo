import pandas as pd
import os

print("👋 Script started")

data_dir = 'data'
output_file = 'output.csv'

if not os.path.exists(data_dir):
    print("❌ 'data' folder not found!")
    exit()

all_data = []

for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        file_path = os.path.join(data_dir, file)
        print(f"📥 Reading: {file_path}")
        
        df = pd.read_csv(file_path)
        print(f"📊 Rows in {file}: {len(df)}")

        df = df[df['product'] == 'pink morsel']

        if df.empty:
            print(f"⚠️ No pink morsel in {file}")
            continue

        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
        df['sales'] = df['price'] * df['quantity']
        df = df[['sales', 'date', 'region']]

        all_data.append(df)

if not all_data:
    print("🚫 No pink morsel data found in any file.")
    exit()

final_df = pd.concat(all_data)
final_df.to_csv(output_file, index=False)
print(f"✅ Done! Output saved to '{output_file}'")
