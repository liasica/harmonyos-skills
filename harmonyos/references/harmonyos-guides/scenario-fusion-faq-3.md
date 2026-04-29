---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:472f48d430131b9e0bca451f2b07f11010385368bef233653415d585f8882e74
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/njK9mG1TRG2jRCQW2YvrMw/zh-cn_image_0000002558606006.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T054020Z&HW-CC-Expire=86400&HW-CC-Sign=BCD348A70A77DA461787E20527782DBDD4FADAA396F60FF2E3D8BF4AADBCB5D8)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```
1. Row() {
2. Text('收货人：').textAlign(TextAlign.End).width('25%')
3. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
4. }
```
