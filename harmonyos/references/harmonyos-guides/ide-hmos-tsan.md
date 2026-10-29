---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-10-29T07:58:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:22a7ed0858337bb28e02e4d7d1b8d5623b71e900954939bb96a3a3e8cc079b8c
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/F_csFLihTWyfTQ4EH8pCkg/zh-cn_image_0000002779728917.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/SlmgjXq-TMuGh7v8aNi6Qw/zh-cn_image_0000002779608769.png "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/xI6i1RzGSSOfo_qrx3yKuw/zh-cn_image_0000002750009856.png)
2. 在配置界面点击**故障分析**，勾选**数据竞争检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/Yx04GdktSuGQK7xIHu1Dig/zh-cn_image_0000002779728919.png)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/f_eaefaLS4eiZDb64_6J6g/zh-cn_image_0000002750169746.png)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```screen
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/SxjQr9h_TdW0_dWqF2LTgQ/zh-cn_image_0000002750009854.png)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/xMo3kg4yQHKDjM_XNciMlg/zh-cn_image_0000002750169748.png)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Pb3fVzN3QvuzpEaZ6V2Wiw/zh-cn_image_0000002779608771.png)
