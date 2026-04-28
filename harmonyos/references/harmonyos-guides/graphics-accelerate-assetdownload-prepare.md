---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97d47c4215c08ef64aa4321085da5fbca3e5f34883805d5f92fb50beeea234b3
---

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开发准备项。

## 配置网络权限

在“src/main/module.json5”的requestPermissions层级中添加网络权限。

```
1. {
2. "module": {
3. // ...
4. "requestPermissions": [
5. {
6. "name": "ohos.permission.INTERNET"
7. }
8. ]
9. }
10. }
```
