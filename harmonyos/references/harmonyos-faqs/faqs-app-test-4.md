---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b21026d52935ae407cd5b2800f44b96394775bee4e93fe5caa3f35b0f9bdf1c9
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/BGdmwSFtS8me43F30fWBZA/zh-cn_image_0000002194318268.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=642F83D246256FE245C52DD3D9CF17FE45C1211EF788BE61C1C5A2412A65AAF6)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Rk-eljvMRzKfaeFtb_drGw/zh-cn_image_0000002194158644.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=B895CDBA7E1619F544F53EAA2481FB5B53B47668503C075ED3C9BC929E47EA8D)
