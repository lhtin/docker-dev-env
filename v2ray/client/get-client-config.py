#!python3 -u

import argparse
import requests
import base64
import json

def b64decode (s):
  return str(base64.b64decode(s), "utf-8")

parser = argparse.ArgumentParser(description="")
parser.add_argument('--url', type=str, required=False, help="Subscript URL")
args = parser.parse_args()

print (f"Fetching: {args.url}")
server_txt = b64decode(requests.get(args.url).text)
server_list = server_txt.splitlines()
config_template = open("./config-template.txt").read()
open("./server-config.txt", "w").write(server_txt)
id = 0
for s in server_list:
  if s.startswith("vmess://"):
    server_config = json.loads(b64decode(s[8:]))
    config = config_template.replace("{address}", server_config["add"]) \
                            .replace("{port}", server_config["port"]) \
                            .replace("{id}", server_config["id"]) \
                            .replace("{host}", server_config["host"]) \
                            .replace("{path}", server_config["path"]) \
                            .replace("{ps}", server_config["ps"])
    ps = server_config["add"]
    open(f"./config{id}-{ps}.json", "w").write(config)
    id = id + 1

# 测试代理是否生效：all_proxy=socks5://127.0.0.1:10808 curl -L youtube.com
