---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-build-obfuscation
title: 混淆加固
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 混淆加固
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:23+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c427c0eac07d719240289323f8e5f27de6db3a6144e580d025b1ca3a2694abd0
---

鸿蒙电脑DevEco Studio默认关闭源码混淆功能。如果在模块级build-profile.json5配置文件中开启源码混淆，则混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四个混淆选项，开发者可进一步在obfuscation-rules.txt文件中选择开启的混淆选项，关于混淆选项的介绍请查看[ArkGuard混淆配置选项](source-obfuscation-rule-options.md)。

## 使用约束

* 在[构建模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)为release模式时生效。
* 模块及模块依赖的HAR和HSP均未关闭混淆。

## 字段说明

可在模块级build-profile.json5文件中进行代码混淆相关配置。obfuscation字段说明如下：

| 配置项 | | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- | --- |
| ruleOptions | | 对象 | 否 | 混淆规则配置。 |
|  | enable | 布尔值 | 是 | 是否启用源码混淆：   * true：启用。 * false（默认值）：不启用。 |
| files | 字符串数组 | 否 | 配置混淆规则文件的相对路径，默认使用obfuscation-rules.txt文件。文件中配置的混淆规则仅在本模块编译时生效（包含依赖代码）。  说明：  * 规则文件中支持配置所有混淆规则，包括[混淆选项](source-obfuscation-rule-options.md)和[保留选项](source-obfuscation-keep-options.md)。 * 支持配置多个文件，文件名称支持自定义，当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。 |
| consumerFiles | | 字符串/字符串数组 | 否 | 仅HAR/HSP模块可配置，配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，文件名称支持自定义。  说明：  * 为保证HAR/HSP模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的保留选项，例如HAR/HSP模块中导出的变量或函数。  * 规则文件中配置的混淆选项会与集成方的混淆规则进行合并，进而影响集成方的编译混淆，因此，建议仅配置保留选项。 |

## 使能混淆

为保护代码资产，建议开启混淆，您可以在模块级的build-profile.json5配置文件中开启源码混淆功能：

```json5
"arkOptions": {
  "obfuscation": {
    "ruleOptions": {
      "enable": true  // 配置true，即可开启源码混淆功能
    }
  }
}
```

开启混淆后，混淆规则配置文件obfuscation-rules.txt中默认开启推荐的混淆规则，包含-enable-property-obfuscation、-enable-toplevel-obfuscation、-enable-filename-obfuscation、-enable-export-obfuscation四项混淆项。

**说明** 

使用[release模式](ide-hmos-hvigor-compilation-options-customizing-guide.md#section192461528194916)编译发布时，建议开启混淆，需要正确配置混淆规则，否则可能会有[运行时问题](source-obfuscation-questions.md)。

## 使能高阶混淆

在[开启混淆](ide-hmos-build-obfuscation.md#section18326541833)后，若您需要更高阶的混淆能力，可以通过以下操作配置高阶混淆规则。

### 配置所有混淆规则

1. 打开模块级build-profile.json5文件，在"files"字段下配置混淆规则文件的相对路径，支持配置多个文件，默认为./obfuscation-rules.txt。

   ```json5
   {
     "apiType": "stageMode",
     "buildOptionSet": [
       {
         "name": "release",
         "arkOptions": {
           "obfuscation": {
             "ruleOptions": {
               "enable": true,
               "files": [
                 "./obfuscation-rules.txt"  // 混淆规则文件
               ]
             }
           }
         }
       },
     ],
   }
   ```
2. 打开模块目录内的obfuscation-rules.txt文件配置混淆规则，具体请参考[混淆选项](source-obfuscation-rule-options.md)，对于不需要混淆的内容，请配置[保留选项](source-obfuscation-keep-options.md)。

   当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/6XuCf8AASweL1mV65LWt3A/zh-cn_image_0000002779728863.png)

### HAR/HSP配置保留选项

为保证HAR/HSP模块可被正确集成使用，若有不希望被集成方混淆的内容，建议在规则文件中配置对应的[保留选项](source-obfuscation-keep-options.md)，例如HAR/HSP模块中导出的变量或函数。

1. 打开模块级build-profile.json5文件，在"consumerFiles"字段下配置传递给集成方的混淆规则文件的相对路径，支持配置多个文件，默认为./consumer-rules.txt，对应编译后HAR包中的obfuscation.txt文件。

   ```json5
   {
     "apiType": "stageMode",
     "buildOptionSet": [
       {
         "name": "release",
         "arkOptions": {
           "obfuscation": {
             "ruleOptions": {
               "enable": true,
               "files": [
                 "./obfuscation-rules.txt"   
               ]
             },
             "consumerFiles": [              // 该模块被依赖时的混淆规则
               "./consumer-rules.txt"   
             ]
           }
         }
       },
     ],
   }
   ```
2. 打开模块目录内的consumer-rules.txt文件配置保留选项。

   当存在多个混淆规则文件时，规则合并以及合并后的作用范围可参考[混淆规则合并策略](source-obfuscation.md#混淆规则合并策略)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/7PUe0lz5T_KbRyGUVJs22Q/zh-cn_image_0000002750169688.png)
