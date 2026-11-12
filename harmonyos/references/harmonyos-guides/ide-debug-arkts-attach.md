---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a3c55063c12dd7d5a1ee441da5ee37c03d6bd7ac117f40c1376b83a02d9ec039
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/xwdMRSFQRPSkayo1jgbw1Q/zh-cn_image_0000002808886807.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CADA5C5EA1BA3A18CA892468C83668FBAE82CD7C91E7236BE32F27346E8DA23)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/_xEXJnPIRkaKisjAqs1ATw/zh-cn_image_0000002808886801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=1834A44B34657A20A577FD04C3680AABED50A3C20FFCBD7EB3D6CDEFBECA553F)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/E75oM4lnRDa8051qiMNx_Q/zh-cn_image_0000002779407166.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CB882B3E89DCB5FF3ACAE056152D4CECFD0A7EEA0CFC8981C01350A2FD629F1)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all processes。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ZEu0q3rFQV6gdyO8GtLWbQ/zh-cn_image_0000002779567142.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F1624C0AB0ACE40AE8D749BBCA1D74827F52D37297E94302C1A2BBDB8AC81DA5)

   **说明** 

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/jzlAxiSvScOI-8GAAYh9Xw/zh-cn_image_0000002808766719.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B0B1679E282A2E9E23490F89962B881769271C46042C7606D5C0EF71DD51983)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/dXP3t8haT8KrDKIgid2uHw/zh-cn_image_0000002808766721.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ED85579172DDDDBF995D067D3BAA604C6CB1B29A254835DC61A2052E08B474F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/qcZF_FnxTBS_-Seu8yxY8g/zh-cn_image_0000002779567144.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2D929FEF49AD387D7C3F1A4D5593DAF0BEB0BFC0B3B9371C321B17D1676962A)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/YHzTfXAGRNmdR1HgHTnJGg/zh-cn_image_0000002779407164.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5B7B66038EDE40998E37969B5D3E5A943E161616724137143BBDBF38F3B98C7)
