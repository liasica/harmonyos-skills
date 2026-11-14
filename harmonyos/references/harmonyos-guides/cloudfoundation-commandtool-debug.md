---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:146443cc74f68a1a6de7dfdedabe740aa8142338038b6a380d99d35ba26f170a
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/y0HzrOXHSWGvQwMjIKK_rg/zh-cn_image_0000002817507429.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=34E496DD44321D6DB28C61086B9417386E655CD990D782E8F137960185B43677)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/mpjMEkGUQcGiBcAZo_bASQ/zh-cn_image_0000002788307998.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE9ED0B8467A231F74E123E62078B76FACE97AECED8695D42AB1941F40238466)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/U5favUwOTxqs8MPtA-dN8g/zh-cn_image_0000002817427361.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE6B71B3D8E7B7D36D829D9B5C700C9E88F4D7B6D9216D2D448E3F5260BC2B02)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/WcQfPQ23RUO-SvSGZfSbhg/zh-cn_image_0000002788467942.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=A325F664F96B9ED945A5A0EDEFE668F823D883B58F765AA40B077B6E7DE5C784)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/5lsTfXsWRI2sTtokAt8-wg/zh-cn_image_0000002817507431.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C543E8174219A79293E6870D5FF2CD81864E2BA406C670A7B406BECCD5F91AA)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/koQoMqskQauVcVIrUOzr5Q/zh-cn_image_0000002788308000.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=5CBB689B53E5A34CC8C4ABDC0393D3542818D652FAA35F0EC86FDFFEC0208647)

  **说明** 

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/qFqNctPOSFeObq28pATaYA/zh-cn_image_0000002817427363.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC7CF0381947A0B4C066251A411AC9903830099D5ECFEB98509F8ABF97C95FC1)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/L-acXtjwSIWj1aAP-ICz7Q/zh-cn_image_0000002788467944.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDF8D5BBEBB7B8AA5AEA8FFDF3352A21F812B60D87B552B1317FFB8E2CEFF387)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/OKgoR7EIRX6pbMefg0dW6Q/zh-cn_image_0000002817507433.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=359FE674ACD6736894E69B97C1205C6B7F42C6500B8326904D3361202B185530)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/i-uWsMwfSHaI0Xo8opWHrg/zh-cn_image_0000002788308002.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=64F181CC5A676019B936643FE760848534900A1B652B29D5120BF6F9C37C0EE6)
