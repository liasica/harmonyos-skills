---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-asan
title: 使用ASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用ASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:55+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:81b1f0adf65f378044c91c136562797c7f5053b9caf41b5ea422baf5509f1d7a
---

为追求C/C++的极致性能，编译器和OS运行框架不会对内存操作进行安全检测。针对该场景，鸿蒙电脑DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于ASan的检测原理请参考[ASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section159561141247)。

## 使用约束

* 如果应用内的任一模块开启ASan，那么entry模块需同时开启ASan。如果entry模块未开启ASan，该应用在启动时将闪退，出现CPP Crash报错。
* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启ASan

可通过以下两种方式开启ASan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/u3fJE5BJTsKwjVyJaq4ZSw/zh-cn_image_0000002791841154.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB1752DE6A67E29A1FA07C2EFBC546AB09C2288DE53E1A7C95D76A9424526F26)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/VKutliUmSDiVO0npokrYoA/zh-cn_image_0000002792001130.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A2A224A3D7EDEA77065C6A205A8EBA79BB31C5884A0449798AD0D5DB1956826 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/bU1deg2PSvCrzvqRhNk_mA/zh-cn_image_0000002820721095.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F423E545D2F8AC5279CD7A5F7DD487AE6C1D5E71A8423A837788C164D73DD7E0)
2. 在配置界面点击**故障分析**，勾选**地址越界检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/g6z4BWaAQlmk9lo_s-pHrw/zh-cn_image_0000002820721097.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=5B4A7C97D096F9929D1E776999EB506B9FBAA36553D926CA2126F080018CEAA3)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/1xJPt3oNTCyBcWyjGJmIwg/zh-cn_image_0000002820681089.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=1789F13DBFAD3F2F625BF01D293970596B066E0D7E394800101C89B1C4E518C4)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加ASan配置开关。

   ```screen
    "asanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/C-H85KXASjKJuUTDu0DNlQ/zh-cn_image_0000002791841156.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=256021F7377DAE5105E4179896E63772B78FF50729D3EE347B49599D6FA65C47)
2. 设置模块级构建ASan插桩。

   在需要开启ASan的模块中，通过添加构建参数开启ASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_ASAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/OyiI5WnWRly4Mz8UuJVUFQ/zh-cn_image_0000002820681091.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9D461787280311850B7CDCE78B44AE6E3134A9C6DF3D4778C1964E232C65B9C)

   **说明** 

   该参数未配置不会报错，但是除包含malloc和free函数等少数内存错误外，出现其他需要插桩检测的内存错误时，ASan无法检测到错误。

## 配置参数（可选）

ASAN\_OPTIONS用于在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等。ASAN\_OPTIONS支持在app.json5中配置，也支持在运行/调试配置中配置。app.json5的优先级更高，即两种方式都配置后，以app.json5中的配置为准。关于ASAN\_OPTIONS的配置方式和常用参数请参考[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。

## 使用ASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[ASan日志规格](address-sanitizer-guidelines.md#asan日志规格)，异常检测类型请参考[ASan异常检测类型](../best-practices/bpta-stability-asan-detection.md#section12508111110451)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/oIcNEYF4SoSlRbktVIUAlQ/zh-cn_image_0000002792001128.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB9C0BC51641D7F896FCCEAC82E08BE74677801BDFE844E75B8EFD869C08CA84)
