---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:503cb35d2a5e6d95ff58be73be8d6fb0ef71d0a24268a03a8eb5db0e55ae6685
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/BGdmwSFtS8me43F30fWBZA/zh-cn_image_0000002194318268.png)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Rk-eljvMRzKfaeFtb_drGw/zh-cn_image_0000002194158644.png)
