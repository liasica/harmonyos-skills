---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:31+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:84f4988a6c8e9d55d0932bc660114d77f5f8a252972f9690ab620757d65420bb
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/JlooeXU1TM-laYzlO8Jsfg/zh-cn_image_0000002788308310.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004647Z&HW-CC-Expire=31536000000&HW-CC-Sign=241A6D841335B35D6FE9166A2B8F4C6A3FC29A9286EF1B76B11B62AEEE05BB20)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```typescript
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
