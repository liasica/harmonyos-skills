---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:29+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:e3cda9f9644986d38e3ed309ff3dcadba6aac469d05b1fefca9248d775436681
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/33as21VEQ7OvN5eOEXanow/zh-cn_image_0000002747291995.jpg)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```typescript
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
