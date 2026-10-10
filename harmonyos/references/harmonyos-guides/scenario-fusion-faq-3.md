---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-10-11T07:22:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:4382da872d08ca2e95316d37a3d61d07aac04a8804dec1d2464bc9618540f110
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/UELEdki5RvOAer0jwdClcw/zh-cn_image_0000002755024994.jpg)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```typescript
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
