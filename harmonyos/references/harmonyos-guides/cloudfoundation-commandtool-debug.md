---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71533f63b6a93715e626aae7ab65112de23d9e91b882da40f1e40625b12bfee5
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/yTqOhyBoT62IvQu2TzsKcg/zh-cn_image_0000002815399769.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=952417AE248D8226052437E3B5305C4B4AD9B640FCD5F2F12B6BEE8AB1BD8483)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Qte1lzpiQGeogpElz4n9Pg/zh-cn_image_0000002786520194.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=D18F72ED6558009A2B421BDC9AA2DB4958D88E63B922230A8DF615E824588B2B)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/fLvBTmTRRW67qdOBRMtl4A/zh-cn_image_0000002786360266.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7E01CE11B0761D311AA074C6C116E5B7E5FC42855E507252A70DDC3269F0071)

## 调试命令

命令名“getcache”，提供获取周期性预加载数据的能力。

### 命令格式

```shell
cf_prefetch getcache -m <bundlename>
```

### 命令选项

| 命令选项 | 必填(M)/选填(O) | 描述 | 示例 |
| --- | --- | --- | --- |
| -m | M | 应用包名。此处的包名需要与您在AppGallery Connect中创建应用时配置的包名保持一致。 | cf\_prefetch getcache -m com.huawei.hms.xs.test |

## 调用示例

### 正常场景

* 输入cf\_prefetch help，获取命令行工具的使用说明。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/w7EYlXj0RMej4rXTmnjh2A/zh-cn_image_0000002815559687.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBA52B68335D280E9C9CD27EA8193519F6F770371979F565A36884734C8303AC)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/oRjmx7d6Sx24PAWAvOFGTw/zh-cn_image_0000002815399771.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=42C18D71F7DAE5DFFCC01E5846782F5E16590A593B03D5A709E3783E093AAF2C)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/wyj1gR7bTwm7SESOe7lPeg/zh-cn_image_0000002786520196.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=14D1B6074DA58CD2085AB761930EE121BFE9DF5D2A482EC664616243875EE5C6)

  **说明** 

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/P4IxZv46TX2Xongq64p-2g/zh-cn_image_0000002786360268.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8BCD8429F949E66D323130BCC6F92376AC4AEC729E43024CFB40324D4C76DF7)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/csGNfW9pRAGeaK0boetdqg/zh-cn_image_0000002815559689.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=1055ABD25444D1FD029A54D528E1BE7DCBAA9535918A5C4F23CF1CC0BF544024)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/zwbdUWzZSeez6k-GjnDvcQ/zh-cn_image_0000002815399773.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=480E3E4C84B78105D4179AE4279FBA62B0F7704004CEBDBB55E175465A49328B)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/4jbgNlKORvS0Q3F1dxpa8Q/zh-cn_image_0000002786520198.png?HW-CC-KV=V1&HW-CC-Date=20261112T233228Z&HW-CC-Expire=31536000000&HW-CC-Sign=65461715615928ACD04498F86BEDA400A7368B01CBBF64A012302979F1320B83)
