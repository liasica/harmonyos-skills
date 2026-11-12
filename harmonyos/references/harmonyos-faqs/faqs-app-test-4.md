---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-4
title: 出现“container is not running”错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 出现“container is not running”错误
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:a048518f4b50e0269b73998312710465d07294c47de73daf7082bcd23a2bb167
---

**问题现象**

在HarmonyOS设备上运行命令“hdc -n shell param set persist.ace.testmode.enabled 1”时，出现错误提示“container is not running”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/j-GIDDGATyCEKejybFbBJQ/zh-cn_image_0000002654798185.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFEC5C6148E4110D284538E1EEF2DDB10DF24C4E887B871FFE043819EFB3D058)

**解决措施**

在DevEco Studio中运行一个测试用例，推包到设备上，然后运行命令hdc -n shell param set persist.ace.testmode.enabled 1。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/90O9HCyyS9ax2p4fsz3UUA/zh-cn_image_0000002624638724.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C277B4AC681B02CFEDBA05BC20DE39F8142EA63A81161A1D23ACE0B083741D1)
