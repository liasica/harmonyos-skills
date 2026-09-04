---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/compilation-tool-chain-overview
title: ArkTS编译工具链概述
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > ArkTS编译工具链概述
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:53+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:f27c5adace48d32cd4d669d2c1482c1932c8ce9c9c03209dc496e33d55e49df6
---

ArkTS SDK提供了一套完整的编译工具链，以支持ArkTS的应用编译，通过集成至[Hvigor](ide-hvigor.md)编译任务的编排工具上，实现将应用的ArkTS/TS/JS源码编译生成方舟字节码文件（\*.abc）。

编译工具链在编译过程中首先执行语法转换，包括语法检查和UI转换。为确保源码安全，编译工具链使用[ArkGuard源码混淆工具](source-obfuscation.md)对源码进行混淆操作。在字节码落盘之前，编译工具链会判断是否需要进行[字节码自定义修改](customize-bytecode-during-compilation.md)，如果需要，则加载并执行自定义修改代码。在生成字节码文件后，开发者可以使用[Disassembler反汇编工具](tool-disassembler.md)查看字节码文件的内容。关于字节码的具体内容，可参考[方舟字节码文件格式](arkts-bytecode-file-format.md)章节。

ArkTS编译工具链目前主要包含以下功能：

1. 语法检查：检查ArkTS/TS语法正确性。
2. UI转换：将UI声明式范式语法转换为标准TS语法。
3. 源码混淆：使用ArkGuard源码混淆工具对源码进行混淆，开发者可以根据具体业务需求选择开启。
4. 生成方舟字节码文件：使用方舟编译器生成方舟字节码文件（\*.abc）。
5. 自定义修改方舟字节码：提供开发者修改字节码能力的入口，在字节码编译落盘前调用。
6. 反汇编：使用Disassembler反汇编工具将方舟字节码文件反汇编成可阅读的汇编指令。

ArkTS编译工具链参与构建HAP的流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/zxGJamy5SX2yOUQkGJNQ1Q/zh-cn_image_0000002742002291.png)
