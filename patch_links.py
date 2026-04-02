"""
patch_links.py
把蝦皮聯盟連結塞進文章的 .md 檔案
使用方法：在 C:\sites\smileladypicks 資料夾執行
  python patch_links.py
"""

import os
import re

# ==== 商品連結對應表 ====
# key = 文章裡會出現的商品關鍵字, value = 蝦皮聯盟連結
LINK_MAP = {
    # ── 驅蚊文章 ──
    "天然植萃精油防蚊凝膠":  "https://s.shopee.tw/1BHpcBOOTg",
    "天然精油防蚊凝膠":       "https://s.shopee.tw/1BHpcBOOTg",
    "超聲波電驅蚊器":         "https://s.shopee.tw/6AgVZnt4sa",
    "超聲波驅蚊":             "https://s.shopee.tw/6AgVZnt4sa",
    "中藥防蚊香包":           "https://s.shopee.tw/5fkEySfQfo",
    "中藥驅蟲包":             "https://s.shopee.tw/5fkEySfQfo",

    # ── 穿戴甲文章 ──
    "絲絨穿戴甲":             "https://s.shopee.tw/6VJLyQAmZs",
    "微笑線穿戴甲":           "https://s.shopee.tw/4LErOSRMES",
    "百款穿戴甲":             "https://s.shopee.tw/4LErOSRMES",
    "法式黑白線":             "https://s.shopee.tw/4LErOSRMES",
    "冰透裸色穿戴甲":         "https://s.shopee.tw/4LErOSRMES",
    "韓系法式穿戴甲":         "https://s.shopee.tw/4LErOSRMES",
    "手工穿戴甲":             "https://s.shopee.tw/9fGNkK04mG",
    "烏風格穿戴甲":           "https://s.shopee.tw/9fGNkK04mG",
}

# 佔位符的各種可能寫法
PLACEHOLDERS = [
    "👉 蝦皮購買連結",
    "👉蝦皮購買連結",
    "[蝦皮購買連結]",
    "蝦皮購買連結",
]


def find_url_for_section(section_text):
    """根據段落內容找對應連結"""
    for keyword, url in LINK_MAP.items():
        if keyword in section_text:
            return url
    return None


def patch_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 用 ## 或 ### 切分段落
    sections = re.split(r'(?=\n#{2,3} )', content)
    patched = False

    new_sections = []
    for section in sections:
        url = find_url_for_section(section)
        new_section = section
        for ph in PLACEHOLDERS:
            if ph in section:
                if url:
                    replacement = f"[👉 立即在蝦皮購買]({url})"
                    new_section = new_section.replace(ph, replacement)
                    patched = True
                    print(f"  ✅ 替換：{ph} → {url}")
                else:
                    print(f"  ⚠️  找不到對應連結，段落關鍵字：{section[:60].strip()!r}")
        new_sections.append(new_section)

    if patched:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("".join(new_sections))
        print(f"  💾 已儲存：{filepath}")
    else:
        print(f"  — 沒有找到佔位符，略過")

    return patched


def main():
    content_dir = os.path.join(os.path.dirname(__file__), "content")
    if not os.path.exists(content_dir):
        print("❌ 找不到 content/ 資料夾，請確認你在 C:\\sites\\smileladypicks 執行")
        return

    md_files = []
    for root, _, files in os.walk(content_dir):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))

    print(f"找到 {len(md_files)} 個 .md 檔案\n")

    total = 0
    for fp in md_files:
        print(f"📄 {fp}")
        if patch_file(fp):
            total += 1
        print()

    print(f"\n✅ 完成！共修改 {total} 個檔案")
    print("下一步：git add . && git commit -m 'add affiliate links' && git push")


if __name__ == "__main__":
    main()
