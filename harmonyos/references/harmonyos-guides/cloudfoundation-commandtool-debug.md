---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4868697d8ef7c275823988a2bd043e8784409be927dc5fea0fc0474847ed127a
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/aTPLlJPCStq6Wboeo1Pxyg/zh-cn_image_0000002558765372.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=8747C9ECD23FC56E12153EBCB3C1153B309773DE45C6716558B126F086CD1ED5)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/qXjSvUoUQwWDQu-83bCvGw/zh-cn_image_0000002558605716.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=79BB48A7E4AAC246A3216EC300FDF7A19228BBEA9E6F8EF08470D92696A66C1D)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/8BEdML1uRLqC9RkwdOQKdQ/zh-cn_image_0000002589325243.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=4F582C81F3F9844251AA38D9245402BA706F9FF4AEB898C38E89AAA155FC98D4)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/ZC1-OZ4KRuy2BqKalYOxow/zh-cn_image_0000002589245179.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=5D52859CB840C456A1FF3E422CEE24EB9AE845EF3FA055264520E0CBAF35E429)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/nDdmS_qhRrSfsIzU9ZLkVA/zh-cn_image_0000002558765374.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=811872613EFDE791316507D4ADCB8A10DD149E97EA6271C3E2D6E4721B51CD5A)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/3hrsw8RgQ9OLKh09N2zTFg/zh-cn_image_0000002558605718.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=1564B7152E746D33892B7936EAC4FB76F83E697066DBBBF787B64C8C1CFF2139)

  说明

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/1H6aEs8KTHGjqC29SMqNNw/zh-cn_image_0000002589325245.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=3C60B6E66DC0F434FAD4014898F2117FA60CE0C138DB888DDFA6CB9B52E63064)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/MyIMGAaqREm06kyDBhX-NQ/zh-cn_image_0000002589245181.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=927D2C4F4928BDE7048095094884A6D96E21258AFC03641616917173828CE16E)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/4ryFX4c1QJueJU0sKzVdMw/zh-cn_image_0000002558765376.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=D898DD5B99FC4E652849CD14FAB279B1F7DCFBEEC31FD3C9AFB240ECA7145319)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/vJrW-fkwRS2UQmNQ0isHpw/zh-cn_image_0000002558605720.png?HW-CC-KV=V1&HW-CC-Date=20260429T053752Z&HW-CC-Expire=86400&HW-CC-Sign=86E4AB11CDE2619909401B3D242D0B57A9FCD9D328FDE933CBA85E7E338010CC)
