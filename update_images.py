import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

BASE = r'D:\Users\user\Desktop\蝦皮影片專案\sites\smileladypicks\content'

updates = {
    'home/home-cleaning.md':              '/images/cleaning.jpg',
    'home/sleep-goods.md':                '/images/sleep.jpg',
    'home/wireless-earphone.md':          '/images/earphone.jpg',
    'beauty/hair-care.md':                '/images/hair-care.jpg',
    'beauty/eye-makeup.md':               '/images/eye-makeup.jpg',
    'posts/2025-mosquito-guide.md':       '/images/mosquito.jpg',
    'posts/2025-wearable-nail-guide.md':  '/images/nail-wearable.jpg',
}

for rel_path, img in updates.items():
    path = os.path.join(BASE, rel_path)
    if not os.path.exists(path):
        print(f'找不到: {rel_path}')
        continue
    with open(path, encoding='utf-8') as f:
        content = f.read()
    # 替換已有的 image: 行
    new_content = re.sub(r'image:.*\n', f'image: "{img}"\n', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'✅ {rel_path} → {img}')

print('\n完成！')
