---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:38+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:da88632c4d62c7f63204cd8a7bc2aa2cdb2c2a2018cdbfd2fc834b08c3188ac4
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/LiXSJ9DCRPOpTcjsfFDLaQ/zh-cn_image_0000002808886807.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=95B808212A6D7C7DA01EBABFDD7DF393582F7E1861CA6E5B96D9C29254A66CAF)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/WHHAV9DCT-iroHJFImo83A/zh-cn_image_0000002808886801.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C7F5835F35183A5AE961E109B0026E0158AA6E6CE8D85D212DA3A1EC7248FC7)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/i1IEG8vVRRCbB5H7wrUGfg/zh-cn_image_0000002779407166.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=7507E84439EEA8277A4CBB355463F4C4C8499EB9DDBAF74AB4120D4E00F43680)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all processes。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/1zTGhpoQQSe1qVuVZf7sxw/zh-cn_image_0000002779567142.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E8C6F9990841FAD347FB683C56F686BEC89EF8479F6295C8A2460F80A3E7AA6)

   **说明** 

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/HLKroqmeQXKd09st-3uYyA/zh-cn_image_0000002808766719.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=190D74837A905F69041C89B7F0B046491C1C22E619FCAB8F4F67C0B2F907C72A)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/CNeZhpnFQlSSr2kTJ_ELtA/zh-cn_image_0000002808766721.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=6466AEC6323F7BD32F7895FC157412A64A091FD8F8063E2CE146906611FEE26F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0GoDmXt9Tx2psM_HqycfIA/zh-cn_image_0000002779567144.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=AAC6D311A45907DAB7A519244ACE5B829B9163E440ADB9994D20F071C1D34A4F)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/5xFv7YKGSd6GVOJowQ-OxA/zh-cn_image_0000002779407164.png?HW-CC-KV=V1&HW-CC-Date=20261128T023438Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C49D6945EBE4B6C6CBBFFC3DE7AA04DBA9797E29FBB934EA3D4A1D874319249)
