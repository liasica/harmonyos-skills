---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-3
title: 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-05-08
content_hash: sha256:0627593321a9a14a561c451da114e0a20dd138dc38dab5b4cf71977fdf53d17c
---

未配置网络权限将出现如下异常日志：

```typescript
ohos.permission.INTERNET check failed
```

请开发者在“src/main/module.json5”的requestPermissions层级中添加网络权限。

```typescript
{
  "module": {
    // ...
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET"
      }
    ]
  }
}
```
