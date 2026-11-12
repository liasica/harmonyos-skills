---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:df4be5ec1d53146f35ee86480ee86dc3f53bd7f27a38911ac1fd6806641d402f
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/aAbRAMqPQHClSRggJtR_Ig/zh-cn_image_0000002810630775.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=33E0A0DC33B8D8CC88D16AA4CB7452669C18E79BAC23C23DE932010228C58A78)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Z9GbCVbiQ46xbrLqcfgEcw/zh-cn_image_0000002781311290.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=27547F472E376D8DC03AC9FDC4E725973E68BC85F5F5DFFE8FACE8CF2D0769D3 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/i-EG0TN2Qyu92UBTH_7pMQ/zh-cn_image_0000002781471226.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E26D3EDF245A7E592A39E0BD3DA7B3B16FDA56D98E13B367E3FA0F77C2181974)
2. 在配置界面点击**故障分析**，勾选**数据竞争检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/OetzDS5vTmuZ_0blGOQ68w/zh-cn_image_0000002810630777.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=64697845D71496424DA72C835E6666F993900B91AEDD05733DC0D5FAEE248BE1)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/p1-5wrriSUiCBp4F31RmvQ/zh-cn_image_0000002810750883.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D44972D9A94CED4F359DB524B671F7792115F775EA46155098EEF5B2203A14D0)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```screen
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/44x_T_BbQa-RkklWZQyUlg/zh-cn_image_0000002781471224.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FDEFA3A3A0531134215534730AEFC211A0D6BDD028C728E7E2EBBC496CC890D)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/DU54P-KZRG2LspCUlAAXXA/zh-cn_image_0000002810750885.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C566963212D4494797EC33E0B1A015685BBFADC54E316151F55D9CEF4DD235EF)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/7pyIVGl4QhmeN_zqBTwfNA/zh-cn_image_0000002781311292.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=364C6C407EC78F9F9793EA22FC6398964548A2906D21D2D7CCF100A90BFA4A42)
