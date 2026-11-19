---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:404fc2e040709da0fae991b4984beba935d6a4193b3c0a71c11271ef1e42a522
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/w_bSqqZ_SuKFKXnKiX2x5w/zh-cn_image_0000002820526279.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC4CE9A94AD325A77087AA18E28CEE8E5E6FBF9CF192D8A59769CDF4AE137F26)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/WrTrU5u1TPaJ81lQvRWLRw/zh-cn_image_0000002820406279.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3E947EE60C127562736D5818BA02D9D288D8F8C6869EC1D4EC1702B533A386E)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/d9dmiixRQS2L5kgo0Np78Q/zh-cn_image_0000002791726300.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=894B341EDF3A82A6A7C32AC05CD278AA11F853CC806C11FBC8C0D1E274A812E8)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/Bt_R0AxPQTWKM9eWj7sosA/zh-cn_image_0000002791566328.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=554A68B569343216D69F9ACDE1B4A928A8A03EF0E9D153A5FDF7B2E68C57929C)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/q29Y6HkJQL2qYeezr9TY0g/zh-cn_image_0000002820526281.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BD90CA892521B8FA40AE296ABEDC452015F6F5D0B503C6A95F980D5371F1A23)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/3kXaDLi2QRGtD7DEUC9NCA/zh-cn_image_0000002820406281.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=37F7E2B6C29EA4B896CAE95F2745398BC472D718BE14F22EE5806C4B24DB83D9)

  **说明** 

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/YFonur5NR063ssrbo8wQvA/zh-cn_image_0000002791726302.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=49BFB49CADE74785D3174B6F4DF35DA8D59E2C64D1EE4EC51C850FA7A58B8899)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/rmroI58KQBKoHSNodAPpiw/zh-cn_image_0000002791566330.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F725FF6D260FC12EE6013B8ADCB0907FC1501454C284AE2F80B5DE0493790DC)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/VyVO-08IQ4OUuAilBN4ihQ/zh-cn_image_0000002820526283.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=178D659D55E49D258935C7CEFE972506AE84E2981184D845733C86F0706C7AE1)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/SA2zMeyGS1-JTUssP3IkGg/zh-cn_image_0000002820406283.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8B76A5BD933942720284E5CE00618331B88395B8DAE440F42A35784D31D381E)
