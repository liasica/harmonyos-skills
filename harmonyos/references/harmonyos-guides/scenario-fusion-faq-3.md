---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:12+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:5fa6941f7b16b2c3ab60b23505fc58d591bf215b88f4c0acffba69ec35fe15f6
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/qwasNiyjRMu6evVXThajDQ/zh-cn_image_0000002820406591.jpg?HW-CC-KV=V1&HW-CC-Date=20261119T014818Z&HW-CC-Expire=31536000000&HW-CC-Sign=E34B4E42F4FDF5991746C9AA5B9E70BB75B12774709CD01D9E08C7E90AC2E1CD)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```typescript
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
