---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fed41e0e27cdfb964974f45cd55e3d0453213a1d145aebda77e21061a24cba32
---

prefetch\_test\_tool是为周期性预加载功能提供的一种命令行工具，开发者集成预加载服务后，使用该工具可以更方便、更高效地进行周期性预加载功能测试和调试，提高开发效率，同时确保预加载服务的平稳运行。

当前命令行工具支持的命令集如下：

| 命令名 | 描述 |
| --- | --- |
| [getcache](cloudfoundation-commandtool-debug.md#调试命令) | 提供获取周期性预加载数据的能力。 |

## 调试准备

使用命令行工具调试周期性预加载之前，需要完成以下准备工作：

* 您已在开发者联盟官网注册账号并通过实名认证，详情请参见[账号注册认证](../start/registration-and-verification-0000001053628148.md)。
* 您已在本地安装DevEco Studio 5.0.3 Release及以上版本。
* 手机/平板终端设备的ROM版本已升级至HarmonyOS 6.0.0 Beta5及以上版本。
* 设置HAP包的“Build Mode”为“debug”，且已[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/e7fGv9qLQ2Og-zXFaIAmsw/zh-cn_image_0000002552958872.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=5F3176B9F7AB584121E1F27BE720DDA8B2C835311A909596F9F9145F3940F080)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ntnhJn9rRnuzRfjrip7cQA/zh-cn_image_0000002583478873.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=9E34FAAF83A715451B28D211F905056F5F274F669F545702411E2FBE3B1ADBD9)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/f2n6fXrrQImG0OCUctW7NA/zh-cn_image_0000002552799224.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=373F24645D41CE63B0001A346994F8ED67315BDC4621CB7D30E3F3A7695C6A55)

## 调试命令

命令名“getcache”，提供获取周期性预加载数据的能力。

### 命令格式

```
1. cf_prefetch getcache -m <bundlename>
```

### 命令选项

| 命令选项 | 必填(M)/选填(O) | 描述 | 示例 |
| --- | --- | --- | --- |
| -m | M | 应用包名。此处的包名需要与您在AppGallery Connect中创建应用时配置的包名保持一致。 | cf\_prefetch getcache -m com.huawei.hms.xs.test |

## 调用示例

### 正常场景

* 输入cf\_prefetch help，获取命令行工具的使用说明。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Ldo1MI_uQUKTIJ-3Ys_yNA/zh-cn_image_0000002583438919.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=03F294E19A02D29113D39EE7F8176352A6CF0A04AAE28D67BEC631B66A06BE0E)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/0ZAiAuZlQJmVLD5FPvLbmw/zh-cn_image_0000002552958874.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=127F8A8D6200D6073C91CC2F546A6D24C5F39E6427B2137CF33205F970DECA77)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/YuDh-844Roa7nN0-eTCpDA/zh-cn_image_0000002583478875.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=972F9EBCAED96E9D467B32977EA9CD2A32C2454910C05BDA98200519FE19A8DC)

  说明

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/wf5gQ4iSRhGkL4ZoaNiFcA/zh-cn_image_0000002552799226.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=6A54164A13C201967B0B1B3183C3785010AA6D4D3DB87AD3614D1D502C6FD0C0)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/kszay_VqT6uGXe-ERXUlew/zh-cn_image_0000002583438921.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=D74A79E00B1163905F7068B25482CF3918107FEC168482802CD7E73E4734E04D)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/nj58igRYRBKgAdE62rZsqg/zh-cn_image_0000002552958876.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=0C2142FED1B96FFD048093F7048ECE5267A311FFB037DFB618265EB334474738)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/CPE9yQE-THmGcZShuivbtg/zh-cn_image_0000002583478877.png?HW-CC-KV=V1&HW-CC-Date=20260427T234847Z&HW-CC-Expire=86400&HW-CC-Sign=4AB7914E431792ACE6581A5FB59A79D57AE2294CF0902FF4579163B9991E4D8A)
