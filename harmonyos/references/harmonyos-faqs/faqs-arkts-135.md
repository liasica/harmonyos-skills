---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-135
title: 模块间循环依赖导致运行时未初始化异常问题定位
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 模块间循环依赖导致运行时未初始化异常问题定位
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d735bb7d71d1eeccce2eb18e4c153c3f6af9e2595b0236fa1cd13858a36ffbf1
---

**问题场景**

模块间循环依赖可能导致应用运行时模块依赖的变量未初始化。例如，index.ets文件执行前，会先执行依赖的page.ets文件，而page.ets文件又循环依赖了index.ets导出的foo符号。此时index.ets文件未执行，foo变量尚未初始化，会导致运行时异常。

```
1. // index.ets
2. import { bar } from './page'

4. export function foo() {
5. bar()
6. }
```

[index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CircularDependencies/index.ets#L6-L11)

```
1. // page.ets
2. import { foo } from './index'

4. export function bar() {
5. foo()
6. }
7. bar()
```

[page.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CircularDependencies/page.ets#L6-L12)

**问题现象**

运行时发生JS崩溃，崩溃日志中的错误信息为：错误消息：foo未初始化。

**解决措施**

开发者可以通过DevEco Studio中Code Linter检查工具识别应用代码中的循环依赖并进行代码重构，消除循环依赖影响，工具详情请参考[代码Code Linter检查](../harmonyos-guides/ide-code-linter.md)。操作步骤如下：

1. 在工程根目录下创建code-linter.json5配置文件，请参考[配置代码检查规则](../harmonyos-guides/ide-code-linter.md#section19310459444)，rules新增"@security/no-cycle": "error"来配置循环依赖检查规则。
2. 在工程管理窗口中，选中工程根目录，右键选择“Code Linter > Full Linter”执行代码全量检查。
3. 根据检查结果，重构应用代码中的循环依赖部分。
