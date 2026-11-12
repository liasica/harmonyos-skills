---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:9bc3f1ddebb0c7c4c10cca31158ee3a456ef9bc06cdb49bea985c729537ac6df
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Cj0grEsnSaCVECl2tmjnMw/zh-cn_image_0000002779407342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D1EEF253B14258366C3FB263F3CBF0B96597BEBFB28B9F6518024BDC1B335967)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/ablD9XyeQhCxQGM6K5E4Dg/zh-cn_image_0000002779567320.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=70CC6D8444E14C68B18DD53A40BC95ECBA583DF9DFF09A96D85A7BB95DD8C215)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```json5
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/k_1CBSKKQ_WLIDxkO6hpJg/zh-cn_image_0000002779407346.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4EE4D64385242E079A17CF8DF559F5D8D07A37D5297CB041C1A554469D420CD)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```json5
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/A2mYZfegQ_y6HScib4fTKQ/zh-cn_image_0000002779567322.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED5222201ACA1DD8CEA01BC92DB1F6587BEC9FAE9CE44BBA8C8B94247EBB30FC)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/Ik1bwMFETOyRvp18QXGhuw/zh-cn_image_0000002808766905.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2CCF0D74E3492E5446FC5CE4C071D748C884A598A3C3F766B03A4D83B2A5E44)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/-i1KT7biQE6765_FPXTC3g/zh-cn_image_0000002779407344.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=339606541EDE306C75B86F388FF1D497BC4D5160FC4C289D929B100E2DA80CBD)
