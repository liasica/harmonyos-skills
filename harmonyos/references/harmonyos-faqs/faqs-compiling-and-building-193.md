---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-193
title: 并行编译多个大型Hap/Hsp模块可能会导致DevEco Studio闪退
breadcrumb: FAQ > DevEco Studio > 编译构建 > 并行编译多个大型Hap/Hsp模块可能会导致DevEco Studio闪退
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:123bcbf2fba5139c69e35e0b2c60e5118620f4a5b014b887501b33ccbd7e54c4
---

**问题现象**

当应用包含了多个Hap/Hsp，每个模块的代码量都是100万行级别，直接点击DevEco Studio的构建（点击Build然后点击Build Hap(s)/APP(s)）之后DevEco Studio工具出现闪退。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/6O5ehSdHQrWtZE4_BmCxfA/zh-cn_image_0000002515675178.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=EB175C11A4A82EC2FA953A79A68DC9367BFA3F094015B7CAC620FE7051A7FA65)

**可能原因**

单个模块代码量大于100万行时单模块编译消耗内存大于5G，4个以上的模块并行编译内存会达到20G导致系统内存不足。

**解决措施**

将并行编译改为串行编译执行。在DevEco Studio上依次选中每个模块再点击编译(左侧选中模块，然后点击Build,再点击第一个按钮Make Module 'xxx')。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/oBYvcGUXQ6KCsmevI3JUew/zh-cn_image_0000002515835104.png?HW-CC-KV=V1&HW-CC-Date=20260429T062103Z&HW-CC-Expire=86400&HW-CC-Sign=2F3C8BABE5CD1F424EBE03B936B6CCBAA386CEF3349E664B3FB788274C1CCFAC)
