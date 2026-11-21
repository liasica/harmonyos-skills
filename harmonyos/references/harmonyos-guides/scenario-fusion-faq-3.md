---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:38+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ff0c9969958b27675450a7a365f24df3702eb8626f0a385db865da758f424b88
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/uduq0HurTNKoN3wj6N0SAQ/zh-cn_image_0000002821758201.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011238Z&HW-CC-Expire=31536000000&HW-CC-Sign=218C0D7CB692DBCA8215DC1BA20F6DB511F8B913EDA90B07C0D74963BB207334)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```typescript
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
