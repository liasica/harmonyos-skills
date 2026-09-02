---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:67a2f0be1505620337b69daeebd8deba5acc218d07fe6eeac5348ce8b4930636
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Yq9TCNm9QDy5xMSHoYJZ6Q/zh-cn_image_0000002229603801.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/LW7FPmZnRAiGLwdsW1E-pw/zh-cn_image_0000002194318016.png)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/NdjcNgEVQN2qJwPY_4uXRg/zh-cn_image_0000002229603789.png)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/SrerHbDGTNG3dimJLbBIVg/zh-cn_image_0000002194158400.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/GUd1BCKfT3mpXVDaVMFYsw/zh-cn_image_0000002229758273.png)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EYQoXLKdQjaOJntefOhhWA/zh-cn_image_0000002229758269.png)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/xe5zEyHjRWaA1lCbrRdTxA/zh-cn_image_0000002194158396.png)
