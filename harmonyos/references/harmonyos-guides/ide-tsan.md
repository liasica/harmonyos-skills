---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:40+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cb1a8af9b8e9eeb0b8be82acb7ae20a946cdca2c780dde763ff1c5f6d3e48288
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/J_lYPRBYSl-56bOyU0GR_Q/zh-cn_image_0000002779407342.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F04EA955D0CFDF0B207E1F68E9723D0A81A80088DC380935DF76D63607E6BAA)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/pxnJahkaT_GbORFMO13FEg/zh-cn_image_0000002779567320.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=0BA2E7C77854AE4EF39B65680ABB5025CEDAA269F753E8F3E35C4846836063BF)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```json5
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/WNoWSaFvSfuV1kaeZbIQEw/zh-cn_image_0000002779407346.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=536C4F3555A60E4CBCAAFF6446BA8AB43A6405D459CDDEC7B28428E67DD9ABB3)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```json5
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Xtnz9-H_S5-y96S5Drp5yg/zh-cn_image_0000002779567322.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=A302E4125F1EFF979F4AA5723525CAE4CFD9EA412870994CF7684264DE07E717)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/jPHHUSNbRtKVyVvcbnc_BQ/zh-cn_image_0000002808766905.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=42AD4290DE5E13E6842DC05FDD78B2832CFEC8FBDC8F5131088C13762017D5E7)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/sgb4E1pxTkS45SVOdRoyCw/zh-cn_image_0000002779407344.png?HW-CC-KV=V1&HW-CC-Date=20261128T023439Z&HW-CC-Expire=31536000000&HW-CC-Sign=128B90D0775CD953FABED664DA7263EA27BCBCD6B3369043F8F2CF41A2F9C3F5)
