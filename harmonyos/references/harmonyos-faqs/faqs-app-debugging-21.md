---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-21
title: Hot Reload执行失败原因说明
breadcrumb: FAQ > DevEco Studio > 应用调试 > Hot Reload执行失败原因说明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:743cf63caf977bd091db261edc9253e3ee0329c85df8b4d5561a3f24d689983c
---

**问题现象**

热重载执行结果失败，控制台打印蓝色重启链接：“Reloaded 1 files failed. Please reinstall and restart.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/Z_8HkpvdSuyYBmfoGWMGRQ/zh-cn_image_0000002194318548.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=F1FE8988F393E2AE7BE6D8FE746CE3147D094B4E058CCD10EEDCD95D08C01F98 "点击放大")

**解决措施**

热重载的最后一步是将补丁包安装到设备并执行quickfix命令。如果quickfix命令执行失败，热重载也会失败。

导致补丁包安装失败的原因可检查以下几个方面：

* 检查工程签名是否正确，热重载需要使用debug签名（不支持release签名），否则热重载将无法执行。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/wSV19nQmRlW_AR86U1P9RA/zh-cn_image_0000002229604317.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=7CF417770084E957C792B488FF83BA61DE0D4C7BF1E3CA1844AD6835EE32D12A "点击放大")
* 检查工程的Build Mode，热重载不支持release模式，支持debug和<None>。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UIXOj7MDSwCQBj0mljaQIA/zh-cn_image_0000002487886068.png?HW-CC-KV=V1&HW-CC-Date=20260428T003007Z&HW-CC-Expire=86400&HW-CC-Sign=941F2242DA4EEC8E6D865DA8DCCA14713D1BB16D3D51FEC8E5EFB4584C0790E0)
