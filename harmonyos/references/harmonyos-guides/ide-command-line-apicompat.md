---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-apicompat
title: API变更查询工具（api-compat）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > API变更查询工具（api-compat）
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:10+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5be91c2fa9af8073d3349f096c234fc6ac4269578e0200371bb7a0f243a32995
---

## 简介

从26.0.1版本开始，Command Line Tools集成api-compat工具，支持查询和对比从某个选定的SDK版本开始，当前工程、模块或文件中使用的API接口是否存在行为变更，帮助开发者完成兼容性检查和代码适配修改。

api-compat命令行格式为：

```bash
api-compat [options]
```

options：可选，命令行的配置参数，具体请参考表1。

表1 api-compat命令行配置参数

|  |  |
| --- | --- |
| **参数** | **说明** |
| --help / -h | 查看api-compat命令行的帮助信息。 |
| --startVersion | 必选，指定API变更扫描的起始版本，格式为："HarmonyOS\_SDK版本号\_Beta/Release"，如"HarmonyOS\_5.0.0(12)\_Release"，可在菜单栏点击**File** > **Settings** > **HarmonyOS SDK**中查询。 |
| --endVersion | 必选，指定API变更扫描的结束版本，格式为："HarmonyOS\_SDK版本号\_Beta/Release"，如"HarmonyOS\_6.1.0(23)\_Beta1"，可在菜单栏点击**File** > **Settings** > **HarmonyOS SDK**中查询。 |
| --projectPath | 可选，指定工程根目录路径，进行工程级别扫描，支持绝对路径和相对路径。 |
| --modulePaths | 可选，指定模块路径，进行模块级别扫描，支持绝对路径和相对路径。  支持同时指定多个模块，模块路径使用英文逗号分隔。 |
| --arkTsFiles | 可选，指定ArkTS文件路径，进行文件级别扫描，支持绝对路径和相对路径。  支持同时指定多个文件，文件路径使用英文逗号分隔。 |
| --cppFiles | 可选，指定C++文件路径，进行文件级别扫描，支持绝对路径和相对路径。  支持同时指定多个文件，文件路径使用英文逗号分隔。 |
| --files | 可选，指定文件（.ets、.c、.cpp文件）路径，支持绝对路径和相对路径。  支持同时指定多个文件，文件路径使用英文逗号分隔。 |
| --outputPath | 可选，指定扫描结果的输出路径，默认值是用户的临时目录。 |
| --format | 可选，指定扫描结果的输出格式，包括json和csv，默认值为csv。 |

**说明** 

* --projectPath、--modulePaths、--arkTsFiles、--cppFiles、--files参数不可同时使用，仅支持使用其中一个参数。
* 若命令行中输入的路径包含"$"、"|"、"<"、">"、"%"、"^"、","、":"、"="、"\*"等特殊字符，命令可能会解析异常，导致扫描结果导出失败。建议用引号包裹路径字符串，或删除路径中的特殊字符。
* 因操作系统差异导致的参数解析问题，请开发者处理使命令参数符合规格，保证可正常解析。

## 环境准备

api-compat工具在Command Line Tools的bin目录下，执行命令前，需要[将bin目录配置到PATH变量中](ide-commandline-get.md#section17776863449)。

## 约束与限制

该工具功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 使用示例

* 查看帮助信息。

  ```bash
  api-compat -h
  ```
* 执行工程级别的API变更扫描，完成后打开outputPath所在目录查看扫描结果。

  ```bash
  api-compat --startVersion "HarmonyOS_5.0.0(12)_Release" --endVersion "HarmonyOS_6.1.0(23)_Beta1" --projectPath "D：//待检测项目路径" --outputPath " D://扫描结果输出路径"
  ```
* 执行模块级别的API变更扫描，完成后打开outputPath所在目录查看扫描结果。

  ```bash
  api-compat --startVersion "HarmonyOS_5.0.0(12)_Release" --endVersion "HarmonyOS_6.1.0(23)_Beta1" --modulePaths "D：//待检测模块1路径,D：//待检测模块2路径" --outputPath " D://扫描结果输出路径"
  ```
* 执行文件级别的API变更扫描，完成后打开outputPath所在目录查看扫描结果。

  ```bash
  api-compat --startVersion "HarmonyOS_6.1.1(24)_Release" --endVersion "HarmonyOS_26.0.0_Beta2" --arkTsFiles "D：//待检测ArkTS文件路径" --cppFiles "D：//待检测C++文件路径" --outputPath " D://扫描结果输出路径
  ```

* 指定输出为json格式。

  ```bash
  api-compat --startVersion "HarmonyOS_5.0.0(12)_Release" --endVersion "HarmonyOS_6.1.0(23)_Beta1" --projectPath "D：//待检测项目路径" --format "json"
  ```
