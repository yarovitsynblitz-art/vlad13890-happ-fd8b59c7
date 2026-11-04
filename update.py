import base64
import re
import urllib.request
from pathlib import Path

SOURCE = "https://raw.githubusercontent.com/mohammadaz2/v2rayConfigsForYou/main/configs.txt"

def b64(text):
    return "base64:" + base64.b64encode(text.encode("utf-8")).decode("ascii")

request = urllib.request.Request(
    SOURCE,
    headers={"User-Agent": "Vlad13890-Happ-subscription"}
)
with urllib.request.urlopen(request, timeout=30) as response:
    text = response.read().decode("utf-8")

nodes = []
for line in text.splitlines():
    line = line.strip()
    if not re.match(
        r"^(vless|vmess|trojan|ss|hysteria2|hy2|socks)://",
        line, re.I
    ):
        continue
    if re.match(
        r"^vless://[^@\s]+@(127(?:\.\d{1,3}){3}|localhost|\[::1\])(?::|/|\?|#|$)",
        line, re.I
    ):
        continue
    nodes.append(line)

if not nodes:
    raise SystemExit("Ошибка: исходный список серверов пуст")

content = "\n".join([
    "#profile-title: " + b64("🟠 Vlad13890"),
    "#profile-update-interval: 1",
    "#announce: " + b64("🟠 Оформление: Vlad13890 • ♾️ Лимит не указан"),
    *nodes,
    ""
])

Path("configs.txt").write_text(content, encoding="utf-8")
print(f"Подготовлено конфигураций: {len(nodes)}")
