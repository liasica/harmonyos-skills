---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-4
title: 上传软件包时提示“上传的软件包与声明支持设备不一致”
breadcrumb: 指南 > 媒体 > Scan Kit（统一扫码服务） > Scan Kit常见问题 > 上传软件包时提示“上传的软件包与声明支持设备不一致”
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e43c3e96b509c24991508d6362a9aacea8a179c82c8112a7385cfa179aa6ac7f
---

**问题现象**

在进行应用上架操作中，上传软件包时，AGC平台提示“上传的软件包与声明支持设备不一致，请重新上传或修改可支持设备”。

**解决措施**

1. 检查工程entry路径下，module.json5文件中的“deviceTypes”是否和AGC平台上应用支持的设备勾选的应用基本信息中支持的设备保持一致。如支持设备勾选手机，那么module.json5中“deviceTypes”需配置为phone。
2. 如还未解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
