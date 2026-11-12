---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:a376f07fc066dac747f3f1eb9e5f4fccb625fe56bf10a6cb352ccecb6d14a95e
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/t-WzczEtQhCu-t-hP8ZYXA/zh-cn_image_0000002654798119.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8BD3E2DE728C48FFF9D5969D80021BBC4A3710349AA2C6C132EB95EB3C14D94)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/j6Tbho0fQgqu2jFqU3xJDw/zh-cn_image_0000002624638666.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=AABD799C2D67190729637CB1AE23D76392DC142B4F5A20EDD20215E47ED2A658)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/9Akcon-7TQOTiTlDofTFCw/zh-cn_image_0000002654838069.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B36FBBC872857368EE5ADF43AD51B2E8D190F5304CBED03E56E22AC1F74DCC5)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/TGIjDc65SIen7f42QxfVFA/zh-cn_image_0000002624478756.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB7042520F2099A69024B61B3F4678AED15C46AD0EDFF9C1E473CECAE99F5680)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/2H7ccmwQTNuvYjiCX7p4PQ/zh-cn_image_0000002654798121.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=948B0FB62B0B21D9237676BD54A6E1A5E960274B03918DE848943FDCAAE6D149)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/3AiSNp-_SXq1OIHmU5vehA/zh-cn_image_0000002624638668.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=F05D24320D7A2F04D28DA14C50A5AC67C7D5E347C4553593D9CF664910028C20)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/di7vuAhSR0yzkKep4KIBkQ/zh-cn_image_0000002654838073.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=840B27564DE70F94E3D8FBB699CE8D2B56E84D36CA4171EF48BE90F02DF1218B)
