---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-list
title: ohpm list
breadcrumb: 指南 > 命令行工具 > 三方依赖管理工具（ohpm） > 常用命令 > ohpm list
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:52+08:00
doc_updated_at: 2026-04-22
content_hash: sha256:0a9b0eb37ac8677eab52e828052f6997023723a078c11137b69e9b26dfe6c3e5
---

列出已安装的三方库。

## 命令格式

```
1. ohpm list [options] [[<@group>/]<pkg>[@<version>]]
2. alias: ls
```

说明

* @group：三方库的命名空间，可选。
* pkg：三方库名称，可选。
* version：三方库的版本号，可选。

## 功能描述

以树形结构列出当前项目安装的所有三方库信息，以及它们的依赖关系。

当指定三方库名称时，会列出指定三方库名称的所有父依赖；当未指定三方库名称时，默认只列出所有的直接依赖，可通过添加选项 depth 来指定要打印的依赖层级。

## Options

### depth

* 默认值：0
* 类型：number
* 别名：d

可以在 list 命令后面配置 -d <number> 或者 --depth <number> 参数，设置输出树形结构的最大深度，超过该深度则不进行输出，不配置则取默认值 0，只展示直接依赖。

由于DevEco Studio控制台默认最多输出5000行，对于大工程建议通过 ohpm list -d <number> > fileName.txt 命令，将内容输出到指定文件中。

说明

若输出出现乱码问题，请执行 powershell -Command "(Get-Content 'fileName.txt') -replace ([char]27 + '\[[0-9;]\*m'), ''" > result.txt，将内容输出到result.txt文件中。

### json

* 默认值：无
* 别名：j

可以在 list 命令后面配置 -j 或者 --json 参数，以 json 格式输出当前项目安装的所有三方库信息，以及它们的依赖关系。

### prefix

* 默认值：""
* 类型： string

可以在 list 命令后面配置 --prefix <string> 参数，用来指定包的根目录，该目录下必须存在 oh-package.json5 文件。

### parameterFile

* 默认值：无
* 类型： string
* 别名：pf

可以在 list 命令后面配置 --pf <string> 或者 --parameterFile <string> 参数，用来指定参数化配置文件地址。使用该命令前需保证项目级别的oh-package.json5中已配置parameterFile参数。

### recursive

* 默认值：无
* 别名：r

OHPM客户端从5.2.0版本开始，可以在 list 命令后面配置 -r 或者 --recursive 参数，以打印工程所有module安装的三方库信息，以及它们的依赖关系。

### target\_path

* 默认值：无
* 类型：string

可以在 list 命令后面配置 --target\_path <string> 参数，用来指定在特定目标产物target语境下各模块的依赖配置文件（oh-package.json5）的路径。在执行ohpm list时，ohpm会优先安装<target\_path>/<moduleName>/oh-package.json5文件中依赖。详情参见[target\_path](ide-ohpm-install.md#section79331822125611)。

### log\_level

* 默认值：无
* 类型： String

从ohpm 6.0.2.636版本开始，可以在 list 命令后配置--log\_level <string>参数，指定执行当前命令的日志级别（info、debug、warn、error），如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

### debug

* 默认值：false
* 类型： Boolean

从ohpm 6.0.2.636版本开始，可以在命令后配置--debug参数，指定执行当前命令的日志级别为debug，该命令仅在当前命令行生效，不修改.ohpmrc中的日志级别，如果未指定该值则日志级别为.ohpmrc中配置的log\_level的级别。

## 示例

* 查看当前项目安装的**所有**三方库及依赖关系。

  执行以下命令：

  ```
  1. ohpm list
  ```

  结果示例：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/zOgaQMLnTzmVHVAShP4F1A/zh-cn_image_0000002530913386.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=02D282B700EBF1E91701BAA3BF6626E56C934BBB888728FDA5E7710CC7254916 "点击放大")
* 查看当前项目安装的**某个**三方库的依赖关系

  执行以下命令：

  ```
  1. ohpm list universalify
  ```

  结果示例：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/JwRtmHb4QSWXpRsme6VoIw/zh-cn_image_0000002561753335.png?HW-CC-KV=V1&HW-CC-Date=20260429T054751Z&HW-CC-Expire=86400&HW-CC-Sign=D493FAE410E9C3C75B0BFC86B16CAFCC8BC412230276461F73260E49FFEEDA63)
* 查看当前项目所有module安装的**所有**三方库及依赖关系。

  执行以下命令：

  ```
  1. ohpm list -r
  ```

  结果示例：

  ```
  1. . D:\xxx\ProjectName
  2. └── @ohos/hypium 1.0.6

  4. module1 D:\xxx\ProjectName\module1
  5. ├─┬ lib1 1.0.0
  6. │ ├── lib1_sub1 1.0.0
  7. │ └── lib1_sub2 1.0.0
  8. └─┬ lib2 1.0.0
  9. ├── lib2_sub1 1.0.0
  10. └── lib2_sub2 1.0.0

  12. module2 D:\xxx\ProjectName\module2
  13. └── @ohos/lib3 1.0.0
  ```

* 指定target\_path选项时，查看当前项目所有module安装的**所有**三方库及依赖关系。

  如果target\_path目录下新增了module：dynamic，且module1新增了依赖：lib3，执行以下命令：

  ```
  1. ohpm list -r --target_path xxx/.hvigor/dependencyMap
  ```

  结果示例：

  ```
  1. . D:\xxx\ProjectName
  2. └── @ohos/hypium 1.0.6

  4. dynamic D:\xxx\ProjectName1\dynamic // target_path引入模块
  5. └── @ohos/lib4 1.0.0

  7. module1 D:\xxx\ProjectName\module1
  8. ├─┬ lib1 1.0.0
  9. │ ├── lib1_sub1 1.0.0
  10. │ └── lib1_sub2 1.0.0
  11. └─┬ lib2 1.0.0
  12. ├── lib2_sub1 1.0.0
  13. └── lib2_sub2 1.0.0
  14. └── lib3 1.0.0 // target_path新增依赖

  16. module2 D:\xxx\ProjectName\module2
  17. └── @ohos/lib3 1.0.0
  ```
