---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏资源加速服务 > 资源包后台下载 > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:eb285dca8a28dabc8e344f7b4ec884225d098da8cebf199ca2bf8f71a89543d9
---

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开发准备项。

## 配置网络权限

在“src/main/module.json5”的requestPermissions层级中添加网络权限。

```json5
"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET",
    "usedScene": {
      "abilities": [
        "EntryAbility"
      ],
      "when": "inuse"
    }
  },
  // ...
]
```
