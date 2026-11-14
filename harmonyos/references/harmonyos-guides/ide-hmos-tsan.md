---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:bde9de00848aa4cd0bb9d71cbca65aae2a2c6b54387d4e8c0d733107eca2b6ed
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/sr2IsTRlRyyQXsegvL1gSw/zh-cn_image_0000002810630775.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=10091A11E284126A06856B3CE9D307A9916E786084A1CDF9FEAE7BE513E82A11)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/WqvbDBVtSOStVNefrO067w/zh-cn_image_0000002781311290.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=6595B2272E27601744EE1612D099522FBC694740017B3CF412DE1AA71895F80B "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/fECTxws9RTKGqL9TuPFhKQ/zh-cn_image_0000002781471226.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=6120A327FBFC5BA7D30E9ADFA7FB3064053724205E0999616EA8E6EB939A33F3)
2. 在配置界面点击**故障分析**，勾选**数据竞争检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/UEh4XZARTiiYso5WPnhxjg/zh-cn_image_0000002810630777.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEBE4BB28D0EC30B0DA49EBC054A95BC4D9F0503A3C0CE7F776003B409BF4B85)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Hf38KLcNRGiRq_XEIIReQw/zh-cn_image_0000002810750883.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=B11D5E45A90F3179FF7CA8360D98B5D061C2998252C07310DCC8EFF4BE5D2D75)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```screen
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/u7VNXA73QqOxFLMXlQRAvQ/zh-cn_image_0000002781471224.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=85FE6EF28C31AE51E9EFD93F2A66E6F450D06BB41B4F569E9EF09FBF18678705)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/qblIn04iTwuWSQou-SCtdA/zh-cn_image_0000002810750885.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=E503FFD73BF47592B2B0AC95A1B78303C75BFB967F04F8E11AA67D67F8916A8C)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/_NVK5mkfRCOqg20If7sCEg/zh-cn_image_0000002781311292.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E36C1382449730440BECE19B8368A875DC90E4DBD3CA548B107F555FE7C2666)
