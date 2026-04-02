"""
patch_mask.py
用蝦皮搜尋連結暫代口罩文章的佔位符
放到 D:\sites\smileladypicks\ 執行：python patch_mask.py
"""

import os
import re

# 蝦皮搜尋連結（暫代，之後換成真正聯盟連結）
MASK_LINKS = {
    "3D 立體口罩":      "https://shope.ee/search?keyword=3D立體口罩 成人",
    "4D 韓版蝴蝶型":    "https://shope.ee/search?keyword=4D韓版蝴蝶口罩",
    "5D 日系模型":      "https://shope.ee/search?keyword=5D口罩 日系",
    "KN95 兒童口罩":    "https://shope.ee/search?keyword=KN95兒童口罩",
    "4D 韓版兒童口罩":  "https://shope.ee/search?keyword=4D韓版兒童口罩",
    "3D 兒童立體口罩":  "https://shope.ee/search?keyword=3D兒童立體口罩",
    "買100送10 成人":   "https://shope.ee/search?keyword=口罩 買100送10 成人",
    "買100送10 兒童":   "https://shope.ee/search?keyword=口罩 買100送10 兒童",
}

# 搜尋用通用蝦皮連結（萬用）
SHOPEE_SEARCH = "https://shopee.tw/search?keyword={}"

PLACEHOLDERS = [
    "👉 蝦皮購買連結",
    "👉蝦皮購買連結",
    "蝦皮購買連結",
]

def patch_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not any(ph in content for ph in PLACEHOLDERS):
        print(f"  — 沒有佔位符，略過")
        return False

    # 用 ## 或 ### 切段落
    parts = re.split(r'(?=\n#{2,3} )', content)
    new_parts = []
    count = 0

    for part in parts:
        new_part = part
        has_ph = any(ph in part for ph in PLACEHOLDERS)
        if has_ph:
            # 找對應連結
            url = None
            for kw, link in MASK_LINKS.items():
                if kw in part:
                    url = link
                    break
            # 找不到就用口罩通用搜尋
            if not url:
                url = SHOPEE_SEARCH.format("口罩")

            for ph in PLACEHOLDERS:
                if ph in new_part:
                    new_part = new_part.replace(ph, f"[👉 蝦皮搜尋購買]({url})")
                    count += 1
                    print(f"  ✅ 替換 → {url}")

        new_parts.append(new_part)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("".join(new_parts))
    print(f"  💾 共替換 {count} 個，已儲存：{filepath}")
    return True


def main():
    content_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
    if not os.path.exists(content_dir):
        print("❌ 找不到 content/ 資料夾")
        return

    total = 0
    for root, _, files in os.walk(content_dir):
        for f in files:
            if f.endswith(".md"):
                fp = os.path.join(root, f)
                print(f"📄 {fp}")
                if patch_file(fp):
                    total += 1
                print()

    if total:
        print(f"✅ 完成！修改 {total} 個檔案")
        print("下一步：git add . && git commit -m 'add mask links' && git push")
    else:
        print("沒有需要修改的檔案")


if __name__ == "__main__":
    main()
