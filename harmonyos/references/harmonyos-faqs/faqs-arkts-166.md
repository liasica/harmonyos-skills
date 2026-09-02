---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-166
title: Release模式下对象无法使用Object.attribute方式获取属性
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > Release模式下对象无法使用Object.attribute方式获取属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:30d301cbcae3d2bf4eb91fcd8366db1acf00a5f6a59a9cbed422666a044552bd
---

## 问题现象

1. 构建模式选择release的时候，Record对象通过T.a获取到的值为undefined，只能通过T["a"]获取，但是debug或者其他模式构建的应用包可以正常取到值。
2. 开发者希望DevEco Studio可以提供让开发者即开即用，无需二次配置的混淆配置或者项目创建时默认生成一个通用的混淆规则。

## 背景知识

* 从DevEco Studio NEXT Developer Beta3（5.0.3.600）版本开始，新建工程及模块默认关闭代码混淆功能，如果在模块级build-profile.json5配置文件中开启代码混淆，则混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项，开发者可进一步在obfuscation-rules.txt文件中选择开启的混淆项，关于混淆项的介绍请查看[混淆规则](../harmonyos-guides/source-obfuscation-keep-options.md)。
* 开启混淆后，代码中的方法、属性或路径被混淆，但运行的时候访问的是未混淆的方法、属性或路径，可能导致功能不可用，因此需要将对应的字段配置保留选项。关于保留选项的排查场景及配置方式请参考[混淆规则](../harmonyos-guides/source-obfuscation-keep-options.md)。所以如果不想对属性进行混淆，可以打开模块目录内的obfuscation-rules.txt文件配置混淆规则，配置保留选项，避免混淆后属性访问不到的问题，保留选项请参考[保留选项](../harmonyos-guides/source-obfuscation-keep-options.md)。
* 如果需要排查的场景和配置的字段有很多的话，DevEco Studio还提供了混淆助手工具，可以根据模块和场景对源码进行扫描，快速识别需要配置的保留选项和白名单字段，开发者可以一键生成白名单混淆规则文件。不过需要注意由于某些场景是动态访问名称、属性，需要在运行的时候才能确定的字段，ObfuscationHelper会识别该类场景，开发者需要根据业务进一步排查识别白名单后进行配置。参考文档[通过混淆助手配置保留选项](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)。

## 问题定位

1. 排查数据源，确认是否传过来的时候就混淆了。
2. 对比混淆开启和混淆关闭状态下，该问题是否复现。发现开启混淆后T.a无法正确访问到属性值，显示为undefined，关闭混淆后未出现该问题。
3. 混淆助手可以根据模块和场景对源码进行扫描，快速识别需要配置的保留选项和白名单字段，一键生成白名单混淆规则文件。这种方式不仅减少了手动配置的工作量，还能有效避免因遗漏关键配置而导致的运行时问题。

## 分析结论

* 原因是开启了代码混淆，开启混淆导致对象的属性名被混淆，从而使得T.a无法正确访问属性值，而T["a"]之所以可以正常工作，是因为字符串键没有被混淆。
* 针对简化混淆配置的场景，建议可以使用混淆助手工具。

参考文档：[代码混淆](../harmonyos-guides/source-obfuscation-apply-code.md)。

## 修改建议

1. 关闭混淆，可以解决该问题。
2. 如果是必须要开启混淆，则使用T["a"]来获取属性。
3. 如果涉及到代码改动量大，并且不想关闭混淆，则把Record里的属性，使用-keep-property-name选项配置到白名单中。
4. 在HarmonyOS应用开发过程中，若需对特定类或方法进行混淆排除，开发者需要手动配置白名单规则。为了简化这一配置过程，建议开发者可以借助[混淆助手](../harmonyos-guides/ide-build-obfuscation.md#section19439175917123)来自动化处理部分配置工作。
