---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7d7a4563159b7d2e229daa996bd7af0d040ffb2e2491ec635bed0c9a0eb80bf0
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Yq9TCNm9QDy5xMSHoYJZ6Q/zh-cn_image_0000002229603801.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=CE53C89FC8442D141167F780D8A870FE14250205458F01298D82DC1C95F54418)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/LW7FPmZnRAiGLwdsW1E-pw/zh-cn_image_0000002194318016.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=F6DB72BA88ACD46F2457CA256266E9D3E08CFE4E99EC3D3202F90AF6AB3DCF0D)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/NdjcNgEVQN2qJwPY_4uXRg/zh-cn_image_0000002229603789.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=1457DAB07DD4186C66F67C4AD1DEA1382B7864CDF6EC56777C44EBBAAB00E5CB)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/SrerHbDGTNG3dimJLbBIVg/zh-cn_image_0000002194158400.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=76E43EA9E06729940EFD774443E5826BDE09BAFEFC83F88AE3DC2147CCF71ADA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/GUd1BCKfT3mpXVDaVMFYsw/zh-cn_image_0000002229758273.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=8A830C2DE850EA9FF8F276B1200BA4919AAA5AB35C373F9BB77D0FE7B6DDCDD9)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EYQoXLKdQjaOJntefOhhWA/zh-cn_image_0000002229758269.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=8D5917E65C74439F027AAA42E3F96365879AD029A135B8046133A098914A403C)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/xe5zEyHjRWaA1lCbrRdTxA/zh-cn_image_0000002194158396.png?HW-CC-KV=V1&HW-CC-Date=20260429T062113Z&HW-CC-Expire=86400&HW-CC-Sign=4D593235119BF38954092C5E6159BAB774E3630F0B318F9A406E0392C6750F90)
