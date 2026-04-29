---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-2
title: 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:982110dd2e67a830bed9fd955b2d8c883e3687e6c0f0412d0aa3bb191b6b2e7b
---

**问题现象**

当同时预览多个工程时，点击帮助菜单中的“压缩日志”按钮，可能会因日志文件被占用而无法压缩。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/A_hKpDKYRRS7Fpj1W8OJiw/zh-cn_image_0000002229603945.png?HW-CC-KV=V1&HW-CC-Date=20260429T062017Z&HW-CC-Expire=86400&HW-CC-Sign=D8C38DEBA765B2E8E6DAF773E20EC2CC02EE4009D6098D5A9D66FE86BDA5930C)

此时右下角会出现压缩失败的提示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QjPV5E4bShS3gEiRl4wSSw/zh-cn_image_0000002229758417.png?HW-CC-KV=V1&HW-CC-Date=20260429T062017Z&HW-CC-Expire=86400&HW-CC-Sign=4DFF57CAEC4DC45A277E30DE420910B77CD514213B18EB4D5EEA65461C7AC593)

**解决措施**

请关闭预览过的工程，或者重启DevEco Studio后不要打开预览器，即可再次压缩收集日志。
