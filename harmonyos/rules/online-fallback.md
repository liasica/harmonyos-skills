# 在线兜底

本地镜像没命中，或 `doc_updated_at` 明显早于用户项目要求的版本时，用这里的方式拉取华为文档的最新正文，并在回答里说明走了在线兜底。

不要用 `WebFetch` 或浏览器：`developer.huawei.com/consumer/cn/doc/` 是 SPA 站点，直接抓 URL 只有 1.5KB 的加载占位页。走文档接口（HTML 端点，毫秒级）：

```bash
# 把 URL 最后一段作为 objectId
URL="https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide"
OBJECT_ID="${URL##*/}"
OBJECT_ID="${OBJECT_ID%%\?*}"   # 去掉 ?istab=1&m=1 等 query

curl -sL -X POST "https://developer.huawei.com/consumer/cn/documentPortal/getDocumentById" \
  -H "Content-Type: application/json" \
  -d "{\"objectId\":\"${OBJECT_ID}\",\"language\":\"cn\"}" \
  | jq -r '.value.content.content'   # 输出原始 HTML
```

请求体只有 `objectId` 与 `language` 两个字段，接口是公开的，不需要凭据。

返回结构：

```json
{
  "code": 0,
  "value": {
    "title": "应用开发导读",
    "lang": "cn",
    "anchorList": [],
    "content": {"type": "html", "content": "<html>...<h1>...</h1>...</html>"}
  }
}
```

需要 Markdown 时把 HTML 喂给 `pandoc -f html -t markdown`，或用 Python `markdownify`：

```bash
curl ... | jq -r '.value.content.content' | pandoc -f html -t gfm
```

接入了本仓库 MCP 服务 `harmonyos-docs` 的客户端，直接调 `fetch_online` 工具即可，效果等价。
