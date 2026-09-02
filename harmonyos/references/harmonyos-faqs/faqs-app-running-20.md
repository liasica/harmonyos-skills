---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:5c4842641479e660703650f26557284e70294e398333aeac5d915334b0de66da
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/-FNXf_mVRyakoYMYH6cfKA/zh-cn_image_0000002654798119.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vBQmbFOwTZatTKmzvjXovw/zh-cn_image_0000002624638666.png)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/5gmvG1NrTfaWbo3xvQB44Q/zh-cn_image_0000002654838069.png)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/19YR_tGsT9yPYMJt8fwdQg/zh-cn_image_0000002624478756.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/O1Bvc7sMSeeTN2HxqNzo7w/zh-cn_image_0000002654798121.png)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/aAV4-5LbTWeClSf_TENGKQ/zh-cn_image_0000002624638668.png)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/2jjNuPbPTN2eVX5UzimkKQ/zh-cn_image_0000002654838073.png)
