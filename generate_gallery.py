import os

categories = ['you', 'us', 'group']
base_folder = 'images'

for category in categories:
    folder_path = os.path.join(base_folder, category)
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            print(f'''
<div class="item {category}">
  <img src="{folder_path}/{filename}" alt="{filename}">
</div>
''')
