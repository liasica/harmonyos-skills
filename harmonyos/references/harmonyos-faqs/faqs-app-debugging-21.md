---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-21
title: Hot Reload执行失败原因说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > Hot Reload执行失败原因说明
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f9e299ea4e9d5a32d6c6ca6407712b2da3851c02da86077297a130457e02c4c6
---

**问题现象**

热重载执行结果失败，控制台打印蓝色重启链接：“Reloaded 1 files failed. Please reinstall and restart.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Z_8HkpvdSuyYBmfoGWMGRQ/zh-cn_image_0000002194318548.png "点击放大")

**解决措施**

热重载的最后一步是将补丁包安装到设备并执行quickfix命令。如果quickfix命令执行失败，热重载也会失败。

导致补丁包安装失败的原因可检查以下几个方面：

* 检查工程签名是否正确，热重载需要使用debug签名（不支持release签名），否则热重载将无法执行。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wSV19nQmRlW_AR86U1P9RA/zh-cn_image_0000002229604317.png "点击放大")
* 检查工程的Build Mode，热重载不支持release模式，支持debug和<None>。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UIXOj7MDSwCQBj0mljaQIA/zh-cn_image_0000002487886068.png)
