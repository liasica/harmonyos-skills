---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:53fbd047a622ccb192e4619bb9090dc55e1dc7456b66d5a70256fe7c89f47407
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。
* TSan不支持静态链接libc或libc++库。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/PPc8gEXDTp2eEy1qCciRvQ/zh-cn_image_0000002530753432.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=00E20C20BAEC9F50F879A5F83755C7EDAF2929F00397A273F6E0A50C853A7225)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/dGOYwo6qSSehrskRqb5IDw/zh-cn_image_0000002561833357.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=BA80FC2B2BC59F159E93E7EC99CD687078ED20C933489D8CBCE9B882F684F12A)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```
   1. "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xe0noCoORTiT5xAlkG6N9w/zh-cn_image_0000002561753375.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=F975431BDA67AD00BF80E89472C0BB6FAE3C7BBE7FE209A3B781AAB6757AD641)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```
   1. "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/jN8ERONEQVWFlgOVYf4I8Q/zh-cn_image_0000002561753371.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=A6DFAE37E6424102A62E5F9E294CCFE3AF0D105E93F7596F15C077BEC0FA8C87)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   说明

   当前使用call\_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加\_\_attribute\_\_((no\_sanitize("thread")))来屏蔽该问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/cJ1UnK30QvShOpEiI8HoFA/zh-cn_image_0000002530753434.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=5CFE219EBA4686EE4C0E920145B6C6C04B64BA6808FFEF9343924D5E886C7F18)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/oBKai-6HSvuKS9p6PJwAjQ/zh-cn_image_0000002530913430.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=0E8C7EC1F820F5E6FB233925E293E62BA3B5D2320532393E62827B3C5659395C "点击放大")
