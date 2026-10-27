---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a376f07fc066dac747f3f1eb9e5f4fccb625fe56bf10a6cb352ccecb6d14a95e
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/t-WzczEtQhCu-t-hP8ZYXA/zh-cn_image_0000002654798119.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/j6Tbho0fQgqu2jFqU3xJDw/zh-cn_image_0000002624638666.png)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/9Akcon-7TQOTiTlDofTFCw/zh-cn_image_0000002654838069.png)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/TGIjDc65SIen7f42QxfVFA/zh-cn_image_0000002624478756.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/2H7ccmwQTNuvYjiCX7p4PQ/zh-cn_image_0000002654798121.png)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/3AiSNp-_SXq1OIHmU5vehA/zh-cn_image_0000002624638668.png)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/di7vuAhSR0yzkKep4KIBkQ/zh-cn_image_0000002654838073.png)
