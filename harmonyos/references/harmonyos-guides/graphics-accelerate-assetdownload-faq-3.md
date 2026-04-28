---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-3
title: 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效。
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 集成了游戏资源加速ExtensionAbility方法，未配置网络权限，导致功能未生效。
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6764fda8d6379d4ecf41934a87774f6ceec6682883550c2a51b12b659f15d075
---

未配置网络权限将出现如下异常日志：

```
1. ohos.permission.INTERNET check failed
```

请开发者在“src/main/module.json5”的requestPermissions层级中添加网络权限。

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
