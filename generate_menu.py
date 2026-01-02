import os
import json

ROOT_DIR = 'data_menu'
output_data = {}

if not os.path.exists(ROOT_DIR):
    os.makedirs(ROOT_DIR)

for category in os.listdir(ROOT_DIR):
    cat_path = os.path.join(ROOT_DIR, category)
    if os.path.isdir(cat_path):
        output_data[category] = {}
        
        for subcategory in os.listdir(cat_path):
            sub_path = os.path.join(cat_path, subcategory)
            if os.path.isdir(sub_path):
                items = []
                files = os.listdir(sub_path)
                
                # Cari semua file gambar
                images = [f for f in files if f.lower().endswith(('.jpg', '.png', '.jpeg', '.webp'))]
                
                for img in images:
                    base_name = os.path.splitext(img)[0]
                    # Cari file teks yang namanya sama (case-insensitive search)
                    txt_file = None
                    for f in files:
                        if f.lower() == (base_name + ".txt").lower():
                            txt_file = f
                            break
                    
                    price = "Tanya Harga"
                    desc = ""
                    
                    if txt_file:
                        with open(os.path.join(sub_path, txt_file), 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            if len(lines) > 0: price = lines[0].strip()
                            if len(lines) > 1: desc = " ".join([l.strip() for l in lines[1:]])
                    
                    items.append({
                        "name": base_name.replace('_', ' '),
                        "image": f"{ROOT_DIR}/{category}/{subcategory}/{img}",
                        "price": price,
                        "desc": desc
                    })
                
                if items:
                    output_data[category][subcategory] = items

with open('menu.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=4)
