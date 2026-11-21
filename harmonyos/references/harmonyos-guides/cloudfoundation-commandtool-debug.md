---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-commandtool-debug
title: 调试周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > （可选）使用命令行工具调试周期性预加载 > 调试周期性预加载
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3a032db4b6eb9082b9d0a1ea518e20741eee0679bb613dce3c2814b5e06e00a8
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/yHDXj9V1QZiqTt4NrKXQpQ/zh-cn_image_0000002793037950.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8CED3B284A336F9B1E8ED6D4EFF39C77137A06B9DA821F276EDD5B288A08C0C)

## 切换shell环境

prefetch\_test\_tool命令行工具基于hdc shell调试，需要切换到hdc shell命令环境。

1. PC连接调试设备。连接方式请根据实际情况选择，详情请参见[设备连接管理](hdc.md#设备连接管理)。
2. 打开DevEco Studio，菜单栏选择“View > Tool Windows > Terminal”进入Terminal窗口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/opDAHpBuR-Kb1Ls_udK47Q/zh-cn_image_0000002792877980.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=430AD6339DBC3C65F234C8FB7C0CBE5763247D0A35866BB3203B12B568CFF35D)
3. 输入hdc shell，切换到hdc shell命令环境。切换过程中如果出现报错，请参见[常见问题](hdc.md#常见问题)排查解决。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/E09RwLBgQwKNnRAgzYPofw/zh-cn_image_0000002821837887.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B255E4138A01BFA0755B8A45B56EA86EEC6D7FC16E10462C2120B7D35891A20)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/aFZ_5oApSY2OPEkv74bpDw/zh-cn_image_0000002821757889.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEA380551459596C8979D282954C6251D48B1CBD0BE42A118D0EC6A9FA69AA76)
* 输入cf\_prefetch getcache -h，获取getcache命令支持的参数信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/II1eT2GbQpmZfNZ_2hN6gQ/zh-cn_image_0000002793037952.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=32D8378D49AC36E203DB1B55A3BE84BB5987B824B6FF3ECC0F9177679D4EC57A)
* 输入cf\_prefetch getcache -m <bundlename>，立即向云侧请求获取一次周期性预加载数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/e2rDuk6kTvK_8kVmCy95Wg/zh-cn_image_0000002792877982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A30C6E589E283437C17618563C0DA1341DCA6E056D57244F8F2F71A10899CA5)

  **说明** 

  如果返回结果中的“fetch data timestamp”不是当前时间，则表示仍为上一次成功拉取数据的时间戳，此次数据拉取失败，请参见[异常场景](cloudfoundation-commandtool-debug.md#异常场景)排查。

### 异常场景

* 链路不通，例如无网络情况；或周期性预加载配置不正确。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/mGt58eOETRK0REDnaIc1Ww/zh-cn_image_0000002821837889.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=E516EC3C41018D2D742F5A4EC0C1FF8E23057C186356ECDA11B12B7BD4BF0D93)
* 命令行工具内部错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/So3VLgLQRC-CH0Tn8tKfaA/zh-cn_image_0000002821757891.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2A280FE873D6FC92B16046808C58E3ADAB4EC2C9EFBDB2FC81BFB223D96E6BF)
* HAP包非debug调试模式。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/lyhGyW_yQjW4VMwSOiyDxA/zh-cn_image_0000002793037954.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=92C397596A014D7AC79BCE95B4507707B5EE219C3B22AD8DF6446054375041FB)
* 应用包名输入错误。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/hnVMfdYtQIq1M9UT8lYjSQ/zh-cn_image_0000002792877984.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFEA0B2F3680E3A6CDEE2DA214C66CCB90C7B7CB436DF845757AD0396D4D38EB)
