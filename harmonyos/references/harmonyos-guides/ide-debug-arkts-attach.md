---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:16+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e4504d64b2440f6a541cb5150ae56e1e312a9aec25ea09178cf8c4ce72d73217
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/EwBSgFiuTKqaeDYOI46dZA/zh-cn_image_0000002701823594.png)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/Sq7lpqpZThSB2tb9na9DNg/zh-cn_image_0000002701823596.png)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/BsdCtQaOSbuJtTP-5scOgA/zh-cn_image_0000002701663674.png)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all process。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/x9enCtXGT76nhIlCU45vVw/zh-cn_image_0000002701663676.png)

   **说明** 

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/emKw-CMRRayTHwaD6Vz-jA/zh-cn_image_0000002731542867.png)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/G8QLmziCTPaxIFJkRRenpQ/zh-cn_image_0000002731382895.png)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/KYiJdU1nRwKtQy9TND6lRg/zh-cn_image_0000002701663672.png)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/RGOvS0vGS2yC92LJCTxCMQ/zh-cn_image_0000002731382897.png)
