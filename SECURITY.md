# 安全说明

## 报告漏洞

通过 GitHub Security Advisory（仓库 Security 页 -> Report a vulnerability）提交，或发邮件到 magicrolan@qq.com。请附上复现步骤与受影响的文件路径。

只维护 `master` 分支的最新状态，修复直接推到 `master` 并随下一次 Release 发布。

## 组件与权限边界

| 组件 | 说明 |
|---|---|
| `harmonyos/` | 华为开发者文档的离线 Markdown 镜像，只读参考资料，不含可执行代码 |
| `mcp/server.py` | 本地 stdio MCP 服务，只读本仓库文件；仅 `fetch_online` 工具会访问 `developer.huawei.com` 的公开文档接口 |
| `scraper/` | 文档采集脚本，只在 GitHub Actions 与维护者本机运行，不随插件分发 |
| `install.sh` | 把 `harmonyos/` 软链到各 CLI 的 skills 目录，不写入其他位置 |

插件不需要任何密钥或令牌，不读取 `.env`、SSH 私钥等本地敏感文件，也不上传工作区内容。

## 扫描器误报

`harmonyos/references/` 下是华为官方文档原文。加解密、网络请求、支付等章节的示例代码里带有 PEM 私钥块头尾、示例口令、示例 client secret 一类的占位字符串，密钥扫描器会把它们判为硬编码凭据。这些都是华为文档正文中的示例值，不指向任何真实账号或服务。仓库根的 `.plugin-scanner.toml` 已把该目录加入 `ignore_paths`。

`harmonyos/rules/online-fallback.md` 中的 `curl` 示例调用的是华为公开文档接口，请求体只含从文档 URL 中截取的 `objectId`，不携带工作区数据。
