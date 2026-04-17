"""
把 pictures/ 的圖複製到 static/images/，並重命名成乾淨的英文檔名
"""
import os, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE     = os.path.dirname(os.path.abspath(__file__))
SRC      = os.path.join(BASE, "pictures")
DST      = os.path.join(BASE, "static", "images")
os.makedirs(DST, exist_ok=True)

# 對應表：原始檔名 → 目標檔名（英文，方便 URL）
mapping = {
    "banner.jpg":                                                              "banner.jpg",
    "小孩在浴室總是滑倒？這款防滑墊讓洗澡安心很多.jpg":                       "bath-mat.jpg",
    "小孩洗澡不肯乖乖洗？這款浴室玩具讓氣氛大不同.jpg":                       "bath-toys.jpg",
    "小孩洗頭總是哭鬧？選對這款洗髮精真的差很多.jpg":                         "kids-shampoo.jpg",
    "居家清潔神器推薦 2025：除螨、疏通、吸塵一次搞定，懶人必備.jpg":          "cleaning.jpg",
    "眼部彩妝推薦：讓眼神更有電力的精選好物.jpg":                             "eye-makeup.jpg",
    "睡眠改善好物推薦：讓你每晚都睡得更好.jpg":                               "sleep.jpg",
    "穿戴式美甲推薦 2025：7款開箱比較，不傷指甲也能超美（新手必看.jpg":       "nail-wearable.jpg",
    "藍牙耳機推薦 2025：3款比較，降噪、可愛、骨傳導各選哪款.jpg":             "earphone.jpg",
    "護髮好物推薦：微笑小姐精選護髮產品清單.jpg":                             "hair-care.jpg",
    "驅蚊不求人！2025年4種驅蚊商品實測比較，嬰兒、寵物、戶外各選哪款.jpg":    "mosquito.jpg",
}

for src_name, dst_name in mapping.items():
    src = os.path.join(SRC, src_name)
    dst = os.path.join(DST, dst_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"✅ {src_name[:30]}... → /images/{dst_name}")
    else:
        print(f"⚠️  找不到: {src_name[:40]}")

print("\n完成！")
