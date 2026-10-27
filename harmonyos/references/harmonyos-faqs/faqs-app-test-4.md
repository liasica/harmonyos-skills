---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a048518f4b50e0269b73998312710465d07294c47de73daf7082bcd23a2bb167
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/j-GIDDGATyCEKejybFbBJQ/zh-cn_image_0000002654798185.png)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/90O9HCyyS9ax2p4fsz3UUA/zh-cn_image_0000002624638724.png)
