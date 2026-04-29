---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:41+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:66d4e25c2fdaf894aed473431e196c508bbb39f97998222dcd5a79c1e52a738f
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/tmU8h5riQxKlpFJRW6AhbA/zh-cn_image_0000002561753631.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=C9CCFF2B25D0A5E7E0CCD736DBC94B8B19A1CFA81BAE12DF9DC30C17796FAEFE)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Z-5PpwHgTAqQI4mVxWlTcQ/zh-cn_image_0000002561833599.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=4EF4B0CFFCFA43E02162527B325D8763EC564249D1FC8F12E83D1291E24722E5)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/7R4gCo1qRd6Rh-mjNLAS3g/zh-cn_image_0000002561833609.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=4B7E19999F835E3D9A2F35AFD4223C32CDC1AF5836984E14AFCBA19CB52322C9)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all process。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/ChfpGrKnQcCni9SCvYOXvQ/zh-cn_image_0000002561753623.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=CE5A0C055F86E243ACAB5831A20B3EE39CFF656BB38764561A6C6F6B03A42BCF)

   说明

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/RQnlE7tQSU-XV8vfTgVpEg/zh-cn_image_0000002530913674.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=4BB5F95A8A6A5DCB1FC109FE45A355264CA500456F5AFA8C1FE2D49835F92731)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/YuNh5-P8TNOTnDY_gQnfXg/zh-cn_image_0000002530753682.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=3740030A6F9BC8B5AD842B39E4329ABB2DEFDB0758267D8771CC7D21F583C01C)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/RK84mygjQcefD3DIMoYaAA/zh-cn_image_0000002530753688.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=DDF94275F4414B4E26FE2814C2858348C6C2EC84C27A2B7AC2F7D9249A433A7C)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/1tsZOcrARlKOle-2oTpRRQ/zh-cn_image_0000002561753627.png?HW-CC-KV=V1&HW-CC-Date=20260429T054640Z&HW-CC-Expire=86400&HW-CC-Sign=2B71A70FCF07B2D8713F0E71E52781B369A1E932789150A2328A80A76F990CA7)
