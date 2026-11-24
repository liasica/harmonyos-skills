---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-tsan
title: 使用TSan检测线程错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用TSan检测线程错误
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cbf86f1d277b2e5ddb7b31834b9e0f9e700dcc0a8deb9aa599f990772e6d5f0c
---

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](../best-practices/bpta-stability-tsan-detection.md)。

## 使用约束

* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。
* TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

## 开启TSan

可通过以下两种方式开启TSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Z8AWkIKzQEqblv0KducMnA/zh-cn_image_0000002820680899.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=776D0788D11E0D0B23583B7DF598EB4712882B148640FEDBC118807055660FC9)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/TTb88pnQT8WvYnS6PClV8A/zh-cn_image_0000002820680895.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E31174BE54DAF42C93CC1E1E5585BF755E05CD6610BF15C374F2902C5BDD649C "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/jCBCwKj_TOiDBkSI6NPW6g/zh-cn_image_0000002820680897.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=46E4DC16380424C26CA932A80509231E79B62A2826104886931290BA99F33500)
2. 在配置界面点击**故障分析**，勾选**数据竞争检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/b2bQlw0UTquSZEDjDCRiOA/zh-cn_image_0000002791840964.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE40631F3B72360D29EBB4FB5CD8C95EEC3BF75DF86A26ECFFEDF074FB7ABA35)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EDbAU78ARHO94OMCFp73vg/zh-cn_image_0000002791840968.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F11122CF44C68892EB3B2CED321620F3270D1D62E8E63AB28C040A65385F5C51)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加TSan配置开关。

   ```screen
    "tsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/H1TxdAGRSAaOKqB2PIsj5Q/zh-cn_image_0000002791840962.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=062A16C10C812902A472CA0BB32948EB4C7E392FF171F94F026B1421348B9F81)
2. 设置模块级构建TSan插桩。

   在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_TSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/0ASa817ZT2-6WPSckrtBTQ/zh-cn_image_0000002791840960.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=E07AB0BC4999BCD607694315863E46486EDED7F39500B9272F2C65582794214C)

## 使用TSan

1. 运行或调试当前应用。
2. 当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](../best-practices/bpta-stability-tsan-detection.md#section1180812915516)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/k9h3SppsTwSRJ7cZMRiFVw/zh-cn_image_0000002820680891.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=374B9D7F8CCC59DAC0C8AE5F6A139CF38723DD91B7D85DA29B37D7DAE42305ED)
