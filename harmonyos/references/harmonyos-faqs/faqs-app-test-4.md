---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:de701fb42d1db620f0f33425f927ed3073019b5e2860a3b5edad93e20c254b51
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/BGdmwSFtS8me43F30fWBZA/zh-cn_image_0000002194318268.png?HW-CC-KV=V1&HW-CC-Date=20260429T062134Z&HW-CC-Expire=86400&HW-CC-Sign=5DC93E6E1AB556FA42CD4B15F4393953E41DB500055ADB651E2E8D16A305B115)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Rk-eljvMRzKfaeFtb_drGw/zh-cn_image_0000002194158644.png?HW-CC-KV=V1&HW-CC-Date=20260429T062134Z&HW-CC-Expire=86400&HW-CC-Sign=995CF356B2B3DD0C12094D0D9DADCBF2A082170797D572E264F71ED9A6A6D95D)
