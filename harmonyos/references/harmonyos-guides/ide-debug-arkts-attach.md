---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f29e4264aeb2d4abad979ecf727c203fa8cf7cc232a1b02bfe308bea64b3007e
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/VxVdvNCNRrK1ro53hOnUlw/zh-cn_image_0000002808886807.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DDA65647D2AEF406A52942C011055A7BC9D6E2875716A696D9C5D68F2A685C0)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/szdZAb-fQTaKMfyMbgXvOw/zh-cn_image_0000002808886801.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6710539C3FF18CE1031266F2B465E713F0182F9023E65CB9B5547855BABD89FE)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/33LnFqhHR2-Ivt-JcjGo0g/zh-cn_image_0000002779407166.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D75708756030EE1521889CA590D73B10261837B79728D2C3A787A46B27EC16A)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all processes。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/QWhIBP7EQkONUMGwpEqyyQ/zh-cn_image_0000002779567142.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED0AD33F43E8A1FBAE2BE86E93B2E40ED8A3389B02089E9CBA35D1EBC358A33A)

   **说明** 

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/8Y23J1tiQyu8avvZ-qHoxw/zh-cn_image_0000002808766719.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C598097EA7A89FD9891A473F5C1A7833FAEF46230706D06DE563D770DFB657F)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Rp2ZpMzyRZeJQfJSZZOyXg/zh-cn_image_0000002808766721.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA56E1373BD19C31013DB9B602B2586BD047DC4CA92462B3264AA3BAE7AFB9AD)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Mv_Rfz-tR1CnjUmUnCCIbg/zh-cn_image_0000002779567144.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5445C22D396D61A495F937C1C3D371CB3BDBB70476A0B62D5425230CAAF88FF4)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/KK6-7cYtRJmJDyqmEM79mw/zh-cn_image_0000002779407164.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=ECD79C77914E0D8EF0EC944EEAEEB725D69A1CB3F48ADA13CF32585CFA21BE9A)
