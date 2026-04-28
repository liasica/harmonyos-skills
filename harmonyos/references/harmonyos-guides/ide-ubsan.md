---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ubsan
title: 使用UBSan检测未定义行为
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用UBSan检测未定义行为
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:03d63e201106a73ccae92cef0c612ef4f2f9635aa0ba46b4d7b3823f3a0469d9
---

代码中出现未定义行为，最初可能不会产生任何问题，但是随着代码的复杂度提高，未定义行为可能造成程序崩溃或发生错误，检测出根源会变得更加困难。UBSan（Undefined Behavior Sanitizer）可以检测代码中出现的未定义行为，帮助用户清除未定义行为引起的运行时错误。

常见的未定义行为有：

* 除数为零。
* 使用未对齐的指针，或未对齐的引用。
* 浮点数转换导致的溢出。
* 访问空指针。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

## 使用约束

ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启UBSan

可通过以下两种方式开启UBSan。

### 方式一

点击****Run > Edit Configurations >** Diagnostics**，勾选**Undefined Behavior Sanitizer**开启检测。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/ubENeP26Q_24T81RVp-DUA/zh-cn_image_0000002530753114.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=9BA3C0AC60A49F210098E50EAF6F37316BBF11ACFB13F3FBE3B8E1D130E1B1A5)

### 方式二

在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

```
1. "arguments": "-DOHOS_ENABLE_UBSAN=ON"
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/_ulBfao-QKuXcONd9tujjw/zh-cn_image_0000002530753110.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=816606EF2A3B256442C5C8068F5B223763C8C1AD2F3E9BA7988F334FFDCFA3B6)

## 使用UBSan

1. 运行或调试当前应用。
2. 当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](../best-practices/bpta-stability-ubsan-detection.md#section124211321406)。

   说明

   无论[编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)是debug或release，均有链接可直接跳转至源码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/WfBlW5GZRjevFQu_3aeVqQ/zh-cn_image_0000002561833031.png?HW-CC-KV=V1&HW-CC-Date=20260427T235658Z&HW-CC-Expire=86400&HW-CC-Sign=9CFF719896C1B3A947AD265AF923EB0DABFDAF826A3EFAAC0C7C403FA2464776)
