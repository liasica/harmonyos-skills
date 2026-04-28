---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3
title: 剪贴板粘贴框遮挡智能填充选择框
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > Scenario Fusion Kit常见问题 > 剪贴板粘贴框遮挡智能填充选择框
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34208f000a2526f527a24564be5db9c9d581863e09d639fe73f0ec8cd30048f3
---

**现象描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/73dVjnQESMSEXMPcK5u5-g/zh-cn_image_0000002552799512.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235049Z&HW-CC-Expire=86400&HW-CC-Sign=3813B7902140A695D823C137DEAAF3D625372EAC989DB33988C9CDCDDBC12468)

**解决措施**

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

```
1. Row() {
2. Text('收货人：').textAlign(TextAlign.End).width('25%')
3. TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
4. }
```
