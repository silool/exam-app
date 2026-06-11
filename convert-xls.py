import xlrd, json

wb = xlrd.open_workbook(r'\Users\admin\Desktop\信息网络管理(1).xls')
ws = wb.sheet_by_index(0)

# Answer letter → index
MAP = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

questions = []
for r in range(1, ws.nrows):
    seq   = str(ws.cell_value(r, 0)).rstrip('.0')
    title = str(ws.cell_value(r, 1)).strip()
    opt_a = str(ws.cell_value(r, 2)).strip()
    opt_b = str(ws.cell_value(r, 3)).strip()
    opt_c = str(ws.cell_value(r, 4)).strip()
    opt_d = str(ws.cell_value(r, 5)).strip()
    ans   = str(ws.cell_value(r, 6)).strip().upper()

    if not title:
        continue

    questions.append({
        "type": "single",
        "question": f"({seq}) {title}",
        "options": [opt_a, opt_b, opt_c, opt_d],
        "answer": MAP.get(ans, 0),
        "explanation": ""
    })

bank = {
    "name": "信息网络管理",
    "description": f"共 {len(questions)} 题（单选题）",
    "questions": questions
}

out_path = r'exam-app/信息网络管理.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(bank, f, ensure_ascii=False, indent=2)

print(f"✅ 转换完成：{len(questions)} 题 → {out_path}")
