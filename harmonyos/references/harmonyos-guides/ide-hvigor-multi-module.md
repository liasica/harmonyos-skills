---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-multi-module
title: 多模块管理
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 多模块管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:57ed671b645336102f62ff851e1825bb659aed9f9b97cd23fbe1721320bc931b
---

模块是应用/元服务的基本功能单元，包含了源代码、资源文件、第三方库及应用/元服务配置文件，Hvigor支持工程多模块管理。您可在工程下的build-profile.json5配置文件中增加对应模块信息，即可对模块进行工程绑定和管理，或在hvigorconfig.ts脚本中动态添加或排除某个模块。同时也支持分模块配置、编译和打包。

## 多模块配置

### 静态配置模块

工程级build-profile.json5配置文件中"modules"字段，用于记录工程下的模块信息，主要包含模块名称、模块的源码路径以及模块的 target 信息。target信息主要用于定制多目标构建产物，更多详细信息可参考[配置多目标产物](ide-customized-multi-targets-and-products.md)章节。

例如以下目录中存在两个模块目录，您可在工程下的build-profile.json5配置文件，添加模块信息，使得模块与工程进行绑定：

```
1. 工程结构
2. └─ .hvigor目录    // 构建项目的缓存文件目录，不需要开发者改动，可以删除
3. └─ module1
4. └─ 模块源码文件
5. └─ build-profile.json5    // 模块级别的构建静态配置文件，主要用于定义当前模块的构建信息、hap(hsp、har)的构建行为等
6. └─ hvigorfile.ts    // 模块级别的构建动态自定义脚本，主要用于定义和扩展hap(hsp、har)的构建流程
7. └─ 其他配置文件
8. └─ module2
9. └─ hvigor目录
10. └─ hvigor-config.json5    // 构建引擎的配置文件，主要用于定义开发态版本号、依赖插件的版本以及Hvigor相关能力的配置等
11. └─ build-profile.json5    // 工程级别的构建静态配置文件，主要用于定义整个项目的模块信息、应用信息、app的构建行为等
12. └─ hvigorfile.ts    // 工程级别的构建动态自定义脚本，主要用于定义和扩展app的构建流程
13. └─ 其他配置文件
```

其他配置文件：

* oh-package.json5：应用的三方包依赖配置文件。
* local.properties: 应用本地环境配置文件。
* obfuscation-rules.txt: 应用模块的混淆规则配置文件。
* consumer-rules.txt: HAR/HSP模块默认导出的混淆规则文件，会打包到HAR包中。

工程下的build-profile.json5文件中模块配置示例：

```
1. {
2. "modules": [
3. {
4. "name": "module1", // 模块的名称。该名称需与module.json5文件中的module.name保持一致。在FA模型中，对应的文件为config.json。
5. "srcPath": "./module1" // 模块的源码路径，为模块根目录相对工程根目录的相对路径
6. },
7. {
8. "name": "module2",
9. "srcPath": "./module2"
10. }
11. ]
12. }
```

### 动态配置模块

Hvigor支持在[hvigorconfig.ts脚本](ide-hvigor-life-cycle.md#section810245135914)中动态添加或排除某个模块，具体API及示例可参考[HvigorConfig](ide-hvigor-api.md#section7253174081515)。

## 分模块编译

Hvigor支持分模块编译和打包。您可以通过以下两种方式进行分模块构建：

* 在DevEco Studio中，选中需构建的模块目录后，点击Build菜单栏下的"Make module 'module1'"，其中"module1"根据具体工程模块名称显示；
* 在DevEco Studio的Terminal中，指定模块进行编译。比如模块名称为entry，目标产物target为default，构建HAP模块，可执行以下命令：

  ```
  1. hvigorw --mode module -p product=default -p module=entry@default assembleHap
  ```

更多构建HAR/HSP包命令，可参考[命令行工具](ide-hvigor-commandline.md#section9580122622012)章节。
