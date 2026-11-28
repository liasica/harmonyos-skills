---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-analyze-dump
title: 解析应用minidump/coredump文件
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 解析应用minidump/coredump文件
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:40+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:1cb8653f37181a3c0c3ba9d2a7054e8ad09b17da8dc1f9614044406974282e4a
---

从26.0.0版本开始，DevEco Studio支持对应用minidump/coredump文件进行解析，展示堆栈信息，帮助开发者快速定位问题。

## 获取dump文件

* minidump文件：获取方式请参考[OH\_HiAppEvent\_SetEventConfig接口说明](hiappevent-watcher-crash-events.md#oh_hiappevent_seteventconfig接口说明)。
* coredump文件
  1. 应用需要在module.json5中配置[ohos.permission.ALLOW\_COREDUMP权限](permissions-for-all.md#ohospermissionallow_coredump)，配置方式请参考[声明权限](declare-permissions.md)。
  2. 在2in1设备的任务管理器中右键应用进程，选择**创建转储文件**。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/CCVMIylDTJeRP4zMLroFyw/zh-cn_image_0000002779567248.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=5312AA19848BE1101F048CE7C5608A0FF61B32810A7A7C360BF979DF1FBB0B3D)
  3. 创建成功后，会提示coredump文件的保存位置。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/PSDZRyz2QquUiwu8g7qkUA/zh-cn_image_0000002808766833.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA7381E3692E42BA9DC25A5CB5C65B7993C5AD3B748BB58199700E509464A7B9)

## 解析dump文件

1. 打开DevEco Studio的**Log**窗口，点击**AnalyzeDump**页签打开界面，选择要解析的dump文件和带调试信息的so目录（默认是模块下的build/{product}/intermediates/libs/{target}/{abi}，其中product和target默认是default，{abi}是设备CPU架构类型，如arm64-v8a），点击**Start Analyze**开始解析。

   **说明** 

   应用产生的dump，需要借助同一次构建生成的so文件中的符号信息才能解析。若使用源码变更后重新构建生成的so目录，可能会因符号不一致导致解析结果不准确或解析失败。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/xLHNd_UTQHWUtMKTeHFlig/zh-cn_image_0000002779407278.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=07B9A607C27289D27CF7E098BA05143B0D0CDADE26C8F51C51E883B6E9784BAF)
2. 等待解析成功后，默认会展示异常线程和对应的堆栈，展开堆栈可查看变量信息，支持切换查看不同线程的堆栈，点击堆栈中的超链接可以跳转到对应的源码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xafLeBeAR9W4KnwGJ4b1Cw/zh-cn_image_0000002779407272.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=3A5965ABD3BD16DCE81FD9F3A4DE2031F590ECAFBC28E4E7716139B004C1F43A)
3. 支持查看指定地址的内存，填写内存地址，点击**View**即可查看。也可以直接右键点击变量查看内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/m33eCYqJRmOUiUg6oKD34w/zh-cn_image_0000002779567254.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=D064007ABD93A9C75711D94DFE7EC83B57413316C4885B441B011701D2AC0E42)

   点击**Settings**，可设置进制、偏移量和展示的内存字节数量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/1fekuIT3TL6YlhBcfbAupA/zh-cn_image_0000002808886917.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=03D084BB37F9FB482D3DF087DDC97EDA246D8C32A142D3B6FE79F5B003A48916)
