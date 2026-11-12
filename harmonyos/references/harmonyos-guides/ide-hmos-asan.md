---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-asan
title: 使用ASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用ASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:580b94511fad833b6684eed8f59922e9eb9f6fb214bbdadbb85d691af4541e67
---

为追求C/C++的极致性能，编译器和OS运行框架不会对内存操作进行安全检测。针对该场景，鸿蒙电脑DevEco Studio集成ASan（Address-Sanitizer）为开发者提供面向C/C++的地址越界检测能力，并通过FaultLog展示错误的堆栈详情及导致错误的代码行。关于ASan的检测原理请参考[ASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section159561141247)。

## 使用约束

* 如果应用内的任一模块开启ASan，那么entry模块需同时开启ASan。如果entry模块未开启ASan，该应用在启动时将闪退，出现CPP Crash报错。
* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启ASan

可通过以下两种方式开启ASan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/eTfEQgZRQTSifewIjAt2DA/zh-cn_image_0000002810750961.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=099760297D40C50F032C3F0FD85F6B404848A056BA817F8734EF76016F03CF3A)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/SYDSlyPNTSGgToh91z7CIA/zh-cn_image_0000002810750959.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=57A6B4744616BD6BD01632DCE14F4868F30B23B15ED16C541F5A825C7ECEFE49 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/ck2FXypFTXO_NHz9IoN93Q/zh-cn_image_0000002781311366.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=18932533EE22A595F68499844CF1F1F0D8991625FFF19DB906A20F9D3740E539)
2. 在配置界面点击**故障分析**，勾选**地址越界检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/YdyAeAaEQNmLUsIiQkSl-g/zh-cn_image_0000002810630853.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0464C3E60C73D50461674C442AF63B7D1DEED2A7BF75BD24CD6242348AD31E4)
3. 如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/lW7o3pmHQW2Ux0CuC8Agyw/zh-cn_image_0000002781471300.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AB55E105F95E9FEB708AA5FCC109167A9F0E2A009DC01954898845BEB3F66E9)

### 方式二

1. 修改工程目录下AppScope/app.json5，添加ASan配置开关。

   ```screen
    "asanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/Wd34IjyXRYSOVDpRdG4fOQ/zh-cn_image_0000002781471304.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=267895153EF269875A36524E5B397A368BB52A26ADA896AACB4FD62DD2C6B231)
2. 设置模块级构建ASan插桩。

   在需要开启ASan的模块中，通过添加构建参数开启ASan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_ASAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/JqJlsyvCQ6q7huErMZOBvA/zh-cn_image_0000002781311364.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D6DB37068F1FE1152D771A66EDBF44584D6E24D9FE66956093471BB1D15BBC8)

   **说明** 

   该参数未配置不会报错，但是除包含malloc和free函数等少数内存错误外，出现其他需要插桩检测的内存错误时，ASan无法检测到错误。

## 配置参数（可选）

ASAN\_OPTIONS用于在运行时配置ASan的行为，包括设置检测级别、输出格式、内存错误报告的详细程度等。ASAN\_OPTIONS支持在app.json5中配置，也支持在运行/调试配置中配置。app.json5的优先级更高，即两种方式都配置后，以app.json5中的配置为准。关于ASAN\_OPTIONS的配置方式和常用参数请参考[配置参数](../best-practices/bpta-stability-asan-detection.md#section1496994494018)。

## 使用ASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[ASan日志规格](address-sanitizer-guidelines.md#asan日志规格)，异常检测类型请参考[ASan异常检测类型](../best-practices/bpta-stability-asan-detection.md#section12508111110451)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/G498oFnxR_GkgsWXT4Wkhg/zh-cn_image_0000002810630851.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E90FE896065E6AA6E486D5E4D2583791EF09AD00EB6F89274A04DECC9194285C)
