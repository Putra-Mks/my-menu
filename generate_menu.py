import os
import json

ROOT_DIR = 'data_menu'
output_data = {}

# Jalan-jalan menelusuri folder
for category in os.listdir(ROOT_DIR):
    cat_path = os.path.join(ROOT_DIR, category)
    if os.path.isdir(cat_path):
        output_data[category] = {}
        
        for subcategory in os.listdir(cat_path):
            sub_path = os.path.join(cat_path, subcategory)
            if os.path.isdir(sub_path):
                items = []
                
                # Cari pasangan file .jpg dan .txt
                files = os.listdir(sub_path)
                images = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg'))]
                
                for img in images:
                    base_name = os.path.splitext(img)[0]
                    txt_file = base_name + '.txt'
                    
                    if txt_file in files:
                        # Baca harga dan deskripsi
                        with open(os.path.join(sub_path, txt_file), 'r', encoding='utf-8') as f:
                            lines = f.readlines()
                            price = lines[0].strip() if len(lines) > 0 else "Tanya Harga"
                            desc = "".join(lines[1:]).strip() if len(lines) > 1 else ""
                        
                        # Nama menu diambil dari nama file (hilangkan underscore)
                        menu_name = base_name.replace('_', ' ')
                        
                        items.append({
                            "name": menu_name,
                            "image": f"{ROOT_DIR}/{category}/{subcategory}/{img}",
                            "price": price,
                            "desc": desc
                        })
                
                if items:
                    output_data[category][subcategory] = items

# Simpan jadi JSON agar bisa dibaca HTML
with open('menu.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=4)

print("Menu berhasil di-update!")