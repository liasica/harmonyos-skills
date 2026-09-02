---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-35
title: 如何方便地管理项目中各模块的依赖库版本
breadcrumb: FAQ > DevEco Studio > 工程管理 > 如何方便地管理项目中各模块的依赖库版本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a07eb30ea331e17047447c0f5f4d9c36a627ec2d9a2b5b0b404e9ff33db008f6
---

## 问题现象

在项目中有多个模块，如何方便地管理依赖库的版本号，而不用每次更新的时候修改各模块中oh-package.json5文件的依赖库版本号？

## 背景知识

利用OHPM新增的参数化配置功能。开发者可在项目根目录配置一个参数化文件（json5格式文件），在该文件中维护模块或依赖版本信息，不同模块将根据该文件中的版本进行配置，满足不同构建场景下，开发者快速切换依赖版本的需要。OHPM客户端在1.6.0版本开始支持参数化配置。可以在项目级别的oh-package.json5文件（即项目根目录下的oh-package.json5）中添加[parameterFile](../harmonyos-guides/ide-oh-package-json5.md#section122411462820)配置，并同时指定parameterFile文件路径。配置规则如下：

* parameterFile文件路径支持配置相对路径，并以项目根目录为起点，如："parameterFile": "./parameterFile.json5"。
* 配置文件内容采用json5格式，支持多层json对象嵌套。
* 参数化key支持的字符与包名一致，请见模块级oh-package.json5字段说明中name字段要求，大小写敏感。
* 参数化value类型只能是"string"或"object"，value类型为string时，需符合semver规范。

## 解决方案

1. 在模块级的oh-package.json5文件中，使用@param:dependencies.mpchartV1来作为mpchartV1依赖的版本号；@param:devDependencies.mpchartV2来作为mpchartV2依赖的版本号；@param:devDependencies.mpchartV3来作为mpchartV3依赖的版本号。

   ```screen
   {
     "name": "entry",
     "version": "@param:version",    // 使用时必须以'@param:'开头
     "description": "Please describe the basic information.",
     "main": "",
     "author": "",
     "license": "",
     "dependencies": {
       "@ohos/mpchart": "@param:dependencies.mpchartV1"
     },
     "devDependencies": {
       "@ohos/mpchart": "@param:devDependencies.mpchartV2"
     },
     "dynamicDependencies": {
       "@ohos/mpchart": "@param:dynamicDependencies.mpchartV3"
     }
   }
   ```
2. 在工程级oh-package.json5中添加parameterFile字段开启参数化，并指定参数化配置文件路径。

   ```screen
   "parameterFile": "./parameterFile.json5",
   ```
3. 在parameterFile.json5文件中添加各个版本号的配置，后续只需要更改parameterFile.json5中的版本。

   ```screen
   {
     "version": "1.0.0",
     "dependencies": {
       "mpchartV1": "3.0.25"
     },
     "devDependencies": {
       "mpchartV2": "3.0.24"
     },
     "dynamicDependencies": {
       "mpchartV3": "3.0.23"
     }
   }
   ```
