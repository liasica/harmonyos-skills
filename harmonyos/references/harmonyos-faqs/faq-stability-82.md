---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-82
title: 代码调试断点不生效问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 代码调试断点不生效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7dcab180c9909721eec0c8d600717077f2e9c41b39305587684f25e994e1c0e5
---

## 问题现象

使用DevEco Studio开发工具调试代码的过程中，设置的断点不生效，尤其是在Native代码调试时，经常会碰到代码无法停在断点处的情况，影响代码开发调试效率。

## 背景知识

* DevEco Studio开发工具支持[ArkTS代码调试](../harmonyos-guides/ide-debug-arkts.md)和[Native代码调试](../harmonyos-guides/ide-debug-native.md)。开发者需要基于调试代码类型[自定义调试配置](../harmonyos-guides/ide-run-debug-configurations.md)。
* 代码调试时通常会用到行断点、日志断点、临时断点、函数断点、异常断点等断点类型，以满足不同的调试场景。

## 问题定位

1. 当调试断点不生效时，首先应确认调试类型与调试代码是否匹配，确认方式参考[设置调试代码类型](../harmonyos-guides/ide-run-debug-configurations.md#section1170735241213)。
2. 当调试C/C++代码时，确认编译类型是否被设置成了Release，确认在模块级build-profile.json5文件"externalNativeOptions"配置项中，"arguments"参数配置中存在"-DCMAKE\_BUILD\_TYPE=Release"配置项，如下所示：

   ```json
   "externalNativeOptions": {
     "arguments": "-DCMAKE_BUILD_TYPE=Release"
   }
   ```

   若存在，则表示此时编译类型被设置成了Release，会导致调试断点不生效。
3. 当调试C/C++代码时，确认编译时是否剥离了符号表信息，即确认"cppFlags"参数是否存在"-s"配置，如下所示：

   ```json
   "externalNativeOptions": {
     "cppFlags": "-s"
   }
   ```

   若存在，则表示编译时会剥离符号表信息，会导致调试断点不生效。

## 分析结论

* **原因1：** 调试类型与调试代码不匹配。
* **原因2：** 编译类型被设置成了Release。
* **原因3：** "cppFlags"参数存在"-s"配置，导致编译时剥离了符号表信息。

## 修改建议

* **场景1：** 原因1修改策略。

  [设置调试代码类型](../harmonyos-guides/ide-run-debug-configurations.md#section1170735241213)，将调试类型设置成和调试代码相同的类型，工程调试类型默认为Detect Automatically，若默认调试类型不行，可以尝试修改成和调试代码相同的类型再进行调试。
* **场景2：** 原因2修改策略。

  将编译类型修改成Debug，即将"-DCMAKE\_BUILD\_TYPE=Release"修改成"-DCMAKE\_BUILD\_TYPE=Debug"。
* **场景3：** 原因3修改策略。

  删除"cppFlags"参数的"-s"配置，让编译时保留符号表信息，即修改成"cppFlags": ""。
