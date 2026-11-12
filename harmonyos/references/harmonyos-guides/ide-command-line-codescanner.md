---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-codescanner
title: 跨语言代码检查工具（codescanner）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > 跨语言代码检查工具（codescanner）
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:10+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9921c1f509e92f08fae2a58ac8b8d709131ee6650a0fcb43352d572e36297c1d
---

## 简介

从26.0.1版本开始，Command Line Tools集成codescanner工具，用于检查整个项目的资源泄漏问题。开发者可根据扫描结果中的告警提示，手动修复代码缺陷，在代码开发阶段，确保代码质量。

codescanner命令行格式为：

```bash
codescanner [options] [projectPath]
```

options：可选，命令行的配置参数，具体请参考[表1 codescanner命令行配置](ide-command-line-codescanner.md#table29720562617)。

projectPath：可选，待检查的工程根目录，支持绝对路径和相对路径。默认为当前所在目录。

**表1** codescanner命令行配置参数

| 参数 | 说明 |
| --- | --- |
| -h, --help | 查看codescanner命令行工具帮助信息。 |
| -v, --version | 查看codescanner命令行工具的版本。 |
| -s, --sdkPath | 可选，ArkTS规则检查时，指定HarmonyOS SDK路径。  HarmonyOS SDK加载优先级如下：命令指定的sdk路径 > Command Line Tools工具自带的sdk路径 > 环境变量`DEVECO\_SDK\_HOME`与`DEVECO\_PATH/sdk/default`路径。  默认为Command Line Tools自带的HarmonyOS SDK。 |
| -o, --output | 可选，指定检查报告的输出位置。  默认输出到当前目录下的output文件夹中。 |
| -f, --format | 可选，指定检查报告的输出格式，包括sarif、html。默认为sarif。 |
| -l, --logPath | 可选，指定运行日志的输出位置。  默认输出到当前目录下的scanner文件夹中。 |
| -c, --config | 可选，指定[codescanner检查规则](ide-code-scanner-rule.md)配置文件的位置，工具按照配置文件进行检查。  默认执行ArkTS和CPP的所有规则。 |
| --compileCommandsDir | CPP规则检查时必选，用于指定compile\_commands.json（编译数据库文件）所在文件夹位置。   * 若使用DevEco Studio开发应用，compile\_commands.json文件所在位置为：项目/.idea/.deveco/cxx。 * 若未使用DevEco Studio开发应用，compile\_commands.json文件所在位置为：项目根目录/模块/.cxx/default/default/debug/计算机环境（如arm\_x86）/。 |
| --no-cpp | 可选，禁止执行CPP检查规则。 |
| --no-arkts | 可选，禁止执行ArkTS检查规则。 |

**codescanner检查规则配置文件**

规则配置文件是开发者手动创建的.json格式文件，包含的配置字段和说明如下：

* cpp/arkts：用于指定执行CPP或ArkTS规则检查。
* ruleId：规则名称。
* severity： 规则告警级别，可配置为warning、error、fatal。
* skip： 是否跳过检查规则，可配置为true、false。true表示跳过检查规则，false表示不跳检查规则。

示例：

```json
// 规则配置文件：xxxxxx.json
{
  "rules": {  // 规则总结构
    "cpp": {      // CPP检查规则 
      "ResourceLeak": [  // 规则集
        {
          "ruleId": "FileHandleNotClosed",        // 规则名称
          "severity": "warning/error/fatal",   // 规则告警级别
          "skip": false                           // 是否跳过该检查规则  
        },
        {
          "ruleId": "MemoryNotFreed",             // 规则名称
          "severity": "warning/error/fatal",   // 规则告警级别
          "skip": false                           // 是否跳过该检查规则  
        }
      ]
    },
    "arkts": {     // ArkTS检查规则 
      "ResourceLeak": [        // 规则集
        {
          "ruleId": "MediaResourceNotReleased",    // 规则名称
          "severity": "warning/error/fatal",    // 规则告警级别
          "skip": false                            // 是否跳过该检查规则 
        },
        {
          "ruleId": "FileDescriptorNotClosed",    // 规则名称
          "severity": "warning/error/fatal",    // 规则告警级别
          "skip": false                            // 是否跳过该检查规则 
        }
      ]
    }
  }
}
```

## 约束与限制

该工具功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 使用示例

* 查看帮助。

  ```bash
  codescanner -h
  Usage: codescanner [options] [projectPath]

  Arguments:
    projectPath                 Path to the project root directory

  Options:
    -v, --version               output the version number
    -s, --sdkPath <dir>         Path to the SDK directory
    -o, --output <dir>          Directory for output (default: "output")
    -f, --format <format>       Output format: sarif or html (default: "sarif")
    -l, --logPath <dir>         Directory for log files (default: "scanner/logs")
    -c, --config <path>         Path to the rule config file
    --compileCommandsDir <dir>  Directory containing compile_commands.json (C++ rules)
    --no-cpp                    Disable C++ rule checking
    --no-arkts                  Disable ArkTS rule checking
    -h, --help                  display help for command
  ```

* 查看codescanner命令行版本。

  ```bash
  codescanner -v
  ```

* 对当前目录进行CPP规则检查，输出检测结果在当前目录的output文件夹下，输出检测运行日志在当前目录scanner目录下。

  ```bash
  codescanner --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx
  ```

* 指定项目路径进行检查。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx
  ```

* 指定HarmonyOS SDK路径进行检查。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -s D:\HarmonyOS\sdk
  ```

* 指定报告输出格式为静态html网页。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -f html
  ```

* 指定报告输出位置。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -f html -o D:\MyApplication\codescanner\reports
  ```

* 指定日志输出位置。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -f html -l D:\MyApplication\codescanner\logs
  ```

* 指定检测时执行的规则。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -f html -c D:\MyApplication\codescanner\rule_config.json
  ```

* 禁用CPP规则。

  ```bash
  codescanner D:\MyApplication -f html --no-cpp
  ```

* 禁用ArkTS规则。

  ```bash
  codescanner D:\MyApplication --compileCommandsDir D:\MyApplication\.idea\.deveco\cxx -f html --no-arkts
  ```
