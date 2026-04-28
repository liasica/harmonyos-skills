---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach
title: attach启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > attach启动调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:46+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:06f9a3079f55d02ef2ee2a3e54e94df74d7a1dbdecd26c90e2d0390b2c984f72
---

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

## 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

## 使用约束

attach不支持的场景：

* 本地无源码。
* bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5p1eKlWZR7SqrdOPA7pRuQ/zh-cn_image_0000002561753631.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=8A311BA38E0E786BE456C8A1FA25D3D557EB7EDE844296C42396B6DE4B3DB47B)

## 操作步骤

1. 在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/HEbIlulgSPurdy1BcKFP7w/zh-cn_image_0000002561833599.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=8DE2E384283DA4685E73C2518F2B08345AC1B66249EFA476264780D76E531DD9)启动调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/sZOQC4C5S7KEj4rO0DeE8Q/zh-cn_image_0000002561833609.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=942BDF95729DF888AC66F18DD977427E14A248500BD91872CF6B0576D1751BE8)
2. 选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all process。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/MUW_Ct0xS5ihhVosm1vnFw/zh-cn_image_0000002561753623.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=7150EE5934F3E7A1576E8B17B54E77F0D9E8242160D2CFF3977F699FC8234532)

   说明

   正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
3. 选择需要使用的调试配置，或者使用默认配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/UPBCeEJBTnSJ71fS5D5MpA/zh-cn_image_0000002530913674.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=4FE48F6B14C516895328C0D1F5A022E43FB17BF8A917C3E6B84612C29298250C)
4. 选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Ff8WT6HPTMqeRUkZfUSDzg/zh-cn_image_0000002530753682.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=FE319082471763D1F05F5C546F403F03106BCC63CCD22ED12E4818CFB9F6137E)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/FRymTfVeRImlN-IOAvFX_A/zh-cn_image_0000002530753688.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=1D3F3D7EDBF0EC2DFA3D065A156BCDFF72BA93FC03C278A49D3759A0F616CA0A)
5. 点击**OK**开始attach调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Vf0IxZ8oTDW5sZqtfdLywg/zh-cn_image_0000002561753627.png?HW-CC-KV=V1&HW-CC-Date=20260427T235645Z&HW-CC-Expire=86400&HW-CC-Sign=5A450A8034E2D6BD767ABBDAACE210F1EF73DDCF00952161B5CD7834CDBBD46E)
