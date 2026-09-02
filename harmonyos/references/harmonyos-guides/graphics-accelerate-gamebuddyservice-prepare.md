---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-prepare
title: 开发准备
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏伴随服务 > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:3f0d8fe56d432cd751f0ca7ced6f57fbfcfc4b48597ba4935045d9ec4c2ea461
---

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开发准备项。

## 配置游戏伴随服务权限

在“src/main/module.json5”的requestPermissions层级中配置游戏伴随服务权限。

```typescript
{
    "module":
    {
        // ...
        "requestPermissions":
        [
            {
                "name": "ohos.permission.ACCESS_GAME_BUDDY_SERVICE",
                "reason": "$string:accessGameBuddyService"
            }
        ]
    }
}
```
