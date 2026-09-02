---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9ff095adef8c31e452b24a049b52b77029bb7fabc4c2b8badd42ac672bd2ba9
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/njK9mG1TRG2jRCQW2YvrMw/zh-cn_image_0000002558606006.jpg)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```
1. Row() {
2. Text('收货人：').textAlign(TextAlign.End).width('25%')
3. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
4. }
```
