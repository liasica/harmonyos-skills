---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:10+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:385ff8d9d37163970fc51d6ea5a8e0c031cf230e77dbf702e1370ad3976b831c
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/jno8D2lxRiqaCIAWupHckA/zh-cn_image_0000002779728917.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/ebpQBhfWQruX7Jn31UfSzw/zh-cn_image_0000002779608769.png "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/rLXmutGDSlOFJ-2g0mAkqQ/zh-cn_image_0000002750009856.png)
2. 在配置界面点击**故障分析**，勾选**数据竞争检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/jg4ZnE8oRo-NAayRBaYZ1A/zh-cn_image_0000002779728919.png)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/1G7-eohGRh6KCeAfq3dm3Q/zh-cn_image_0000002750169746.png)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```screen
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/3o4r-qErTUqSySMx6YnQiw/zh-cn_image_0000002750009854.png)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/3MI3ddF8T0SuznKqhUMQOg/zh-cn_image_0000002750169748.png)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/IexOpNLmTvmzGvZQGfodxA/zh-cn_image_0000002779608771.png)
