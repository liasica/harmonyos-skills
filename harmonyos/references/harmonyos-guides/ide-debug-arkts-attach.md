---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a42d175fad4782ed317a6772942d3b0b3ae81be4e43f61fe099789c0f86d7937
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/bQOJRfimRk23yOBzm7KRNg/zh-cn_image_0000002808886807.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4E1115A5B74CBE5CB4286A042866DC70914358D951399B58CB2C8568C84B2E9)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/_T7a026ZRL-tHsE_mL_PCA/zh-cn_image_0000002808886801.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2FDCB94C96BD738ED3AEE0FCD62481F6D30BBC973292DBE7C0C3D56CF6C1E7F)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/6W5y03K9S-m_BbFdrfeWMg/zh-cn_image_0000002779407166.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=A98BBA003999AB6225E8FB1A3D569995C2CAA4B03E649C78D34E778BC271877B)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all processes。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/SPz7yT7nQh-gBBMoQ0YnIg/zh-cn_image_0000002779567142.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4BCFA62AAA7CEDAEFB06CEF8BB1C21B6CE322CD1102935460DE0C6CB9AB54DE)

   **说明** 

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/hx5Jm0H7T36e9CbO6nSBIw/zh-cn_image_0000002808766719.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=47C47A4C55EE750C7A1AE4A4AEF4C6197429093743F074518508581E4C9BC00E)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/X_--0fP9QzWof-WrfCUJPA/zh-cn_image_0000002808766721.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=77A4EE74F4562E8E30114D7FD4E4631CC9E01792BFC6B0A52EB5567E0F723217)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/HjSPIMYxT8afZ27z5lbY_Q/zh-cn_image_0000002779567144.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CAF79665883F2D89A2255094A10625A6DF96CEE9690A6A950A5E17715C022B1)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/zdHmOYLZRl6MGTYNMrRwUA/zh-cn_image_0000002779407164.png?HW-CC-KV=V1&HW-CC-Date=20261114T004858Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD45C450A001CD3A007615C6CB6FF788C7306C286396533E4DEEFD1A1CB07455)
