---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e5507f3b37bceb78e8d8ebe2c62d8a520bc0f9b6d3c2b6e9b5bf2dbaf7c6199b
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/j1IYGsF2TZWUv-qSMRN80w/zh-cn_image_0000002779407342.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=294CCAB7A056606894772781D6576DED985DA2C194119F92C563A033C7C40A60)
2. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/fKu67t87RDCRPrr3_exVXQ/zh-cn_image_0000002779567320.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5714DF9B2128B04445BB45877ADAF9FE46658B5595C1CD7D93B6C17E6096E5A)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```json5
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/KJLFk4rTQuqWdhbkGSn8kQ/zh-cn_image_0000002779407346.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A2701F3640C68553ED8E93FB64CEB31E5273F5874ADCC6DD21C17F2E50070FB)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```json5
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/279H2eKDThuXzO0glSQ2jg/zh-cn_image_0000002779567322.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=D20EE205D5122B4D911E727C042B6542F5BEB3ABDB59AA994ADF699420E562B0)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/4lLpSg5VQm61uPkh8mFA8g/zh-cn_image_0000002808766905.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=2BE34B14A1023D3D0977A487422229D2BCD480E30993C0D69F408D314D1F0F3D)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/s9_amjJGTMqbVlO9ekPvcw/zh-cn_image_0000002779407344.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=90782501ED5002759EBF12E6FD6445EB5974E2430C4C35A0679BD9B150E96080)
