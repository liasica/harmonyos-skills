---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-20
title: 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
breadcrumb: FAQ > DevEco Studio > 应用运行 > 模拟器在后台放置一段时间后会卡在加载状态，CPU占用率高
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa151d5ade024d8a31896db84fea78ea26f312699cb1363bb6d77fb598a07ab6
---

**问题描述**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Yq9TCNm9QDy5xMSHoYJZ6Q/zh-cn_image_0000002229603801.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=03F7450F55A4898D0EDE8C6F3DDB3A16A6083518363153A9FE35C0DEE6422E7C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/LW7FPmZnRAiGLwdsW1E-pw/zh-cn_image_0000002194318016.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=4441871C11DD189AB8E9D41A58901E29785839600EADBFF9F36D4AFE1F110A67)

打开活动检测器，发现模拟器的CPU占用率为80%。

**解决措施**

1.打开模拟器设备管理页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/NdjcNgEVQN2qJwPY_4uXRg/zh-cn_image_0000002229603789.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=B0CF9ABD34B467FA75A6E166D53FC528A93825B6C43290B72920CF0C36F13C3D)

2.选择“新建模拟器”弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/SrerHbDGTNG3dimJLbBIVg/zh-cn_image_0000002194158400.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=7167DE1ABD81C69193C2F74C2A175F5F79F0B863A9E85ABB478E10DBE960BAD9)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/GUd1BCKfT3mpXVDaVMFYsw/zh-cn_image_0000002229758273.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=4C80C79EB849357641460BBDFD7A3B40FA7F13C4D2808389FABB824808247303)

3.复制路径并用文件夹打开system-image\HarmonyOS-NEXT-DB1\phone\_x86。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/EYQoXLKdQjaOJntefOhhWA/zh-cn_image_0000002229758269.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=7F1EF168AB9147533214BB25761C5A0F8BF9428C93975F5A7AC6B42659AF0801)

4.打开features.ini文件，将bootanimation.feature.key的值改为true，保存后重启模拟器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/xe5zEyHjRWaA1lCbrRdTxA/zh-cn_image_0000002194158396.png?HW-CC-KV=V1&HW-CC-Date=20260428T002957Z&HW-CC-Expire=86400&HW-CC-Sign=73B993F0EB85D8B5CD8E553FAA88B12BC2BAE93FEE3860E33B7CC995A974AE0E)
