---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-appanalyzer
title: 应用与元服务体检工具（appanalyzer）
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 命令行工具 > 应用与元服务体检工具（appanalyzer）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:558066f4f5d663ff122b9b8942744490fb2dd7114f9638a1eed6befea1aeb912
---

从26.0.1版本开始，Command Line Tools集成[应用与元服务体检工具appanalyzer](ide-app-analyzer.md)，用于对应用和元服务进行本地测试体检，并给出体检报告、分析指导以及修改建议，帮助开发者提升应用与元服务质量。

## 约束与限制

仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 环境准备

1. appanalyzer工具在Command Line Tools的bin目录下，执行命令前，需要[将bin目录配置到PATH变量中](ide-commandline-get.md#section17776863449)。
2. 首次使用appanalyzer命令行工具需要执行[init](ide-commandline-appanalyzer.md#section175922024914)子命令完成环境初始化。

## 命令列表

appanalyzer命令行格式如下，其中subcommand是子命令，options是子命令的参数。

```bash
appanalyzer [subcommand] [options]
```

| 子命令 | 说明 |
| --- | --- |
| init | 初始化工具环境。 |
| autoAnalyze | 自动遍历检测。 |
| uxAnalyze | 手动多设备检测。 |

## 公共参数

| 参数 | 说明 |
| --- | --- |
| -h, --help | 查看appanalyzer命令帮助信息。 |
| -v, --version | 查看appanalyzer版本。 |
| -l, --language | 设置appanalyzer单次执行的语言，支持CN、EN（不区分大小写），默认为EN。 |

**示例：**

```bash
appanalyzer -h
appanalyzer -h -l CN
appanalyzer -v
```

## 环境初始化（init）

init子命令用于初始化appanalyzer命令行所需的环境，执行检测前必须完成环境初始化。

```bash
appanalyzer init -p <proxy> -s <true/false>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -p, --proxy | 可选参数，如果网络受限，环境初始化时可以尝试配置代理。  代理格式：{代理协议}://{用户名}:{密码}@{代理主机名}:{端口号}，代理协议支持http或https，密码中包含特殊字符时需进行转义。 |
| -s, --sslVerify | 可选参数，表示开启/关闭SSL证书校验，默认为true。 |

**示例：**

```bash
appanalyzer init
appanalyzer init -p http://[user:pass@]host:port
appanalyzer init -p http://[user:pass@]host:port -s false
```

## 自动遍历检测（autoAnalyze）

autoAnalyze子命令用于自动化遍历页面并进行检测和诊断。

```bash
appanalyzer autoAnalyze -b <bundleName> -p <projectPath> -s <Dxx,Sxx> -t <num> -d <serial|IP:port> -o <reportPath> -m <hapPaths>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -b, --bundleName | 必选参数，指定检测的应用或元服务包名。 |
| -p, --projectPath | 必选参数，指定检测的应用或元服务项目路径。 |
| -s, --scenes | 可选参数，设置需要检测的分类或场景，多个分类或场景使用英文逗号隔开，默认使用推荐场景。  Dxx表示分类，Sxx表示场景，设置为分类时会检测其下所有场景，标\*为推荐场景。  支持的场景或分类：  D03[多设备](ide-app-analyzer-scenes.md#section15619191841215)：S14截断\*、S15大图大字\*、S16留白\*、S17避让区遮挡\*、S18基础 |
| -t, --duration | 可选参数，设置自动遍历时长，单位为分钟，默认遍历10分钟。 |
| -d, --device | 可选参数，设置用于检测的设备，支持真机和模拟器，支持的设备类型请参考[多设备](ide-app-analyzer-scenes.md#section15619191841215)。   * 真机：设备SN号 * 模拟器：IP+端口   如果未设置，将执行hdc list targets发现已连接设备，优先选择第一个可用的真机，若无则选择第一个可用的模拟器。 |
| -o, --output | 可选参数，设置检测报告的保存路径，默认为当前工作路径。 |
| -m, --hapPaths | 可选参数，仅在选择基础场景后生效，用于指定待检测的HAP文件路径，多个文件使用英文逗号（,）分隔。用于检测HAP中的应用或元服务图标是否符合设计规范。 |

**示例：**

```bash
appanalyzer autoAnalyze -b com.example.demo -p ./demoProject
appanalyzer autoAnalyze -b com.example.demo -p ./demoProject -s D03 -d 127.0.0.1:5555 -t 5 -m ./entry-default-signed.hap -o ./output
```

## 手动多设备检测（uxAnalyze）

uxAnalyze子命令用于手动执行[多设备](ide-app-analyzer-scenes.md#section15619191841215)UX问题检测和诊断，执行前需要操作设备进入待检测页面并保持亮屏状态。

```bash
appanalyzer uxAnalyze -b <bundleName> -p <projectPath> -s <Dxx,Sxx> -d <serial|IP:port> -o <reportPath> -m <hapPaths>
```

**参数：**

| 参数名 | 说明 |
| --- | --- |
| -b, --bundleName | 必选参数，指定检测的应用或元服务包名。 |
| -p, --projectPath | 必选参数，指定检测的应用或元服务项目路径。 |
| -s, --scenes | 可选参数，设置需要检测的分类或场景，多个场景或分类使用英文逗号隔开，默认使用推荐场景。  Dxx表示分类，Sxx表示场景，设置为分类时会检测其下所有场景，标\*为推荐场景。  支持的场景或分类：  D03多设备：S14截断\*、S15大图大字\*、S16留白\*、S17避让区遮挡\*、S18基础 |
| -d, --device | 可选参数，设置用于检测的设备，支持真机和模拟器，支持的设备类型请参考[多设备](ide-app-analyzer-scenes.md#section15619191841215)。   * 真机：设备SN号 * 模拟器：IP+端口   如果未设置，将执行hdc list targets发现已连接设备，优先选择第一个可用的真机，若无则选择第一个可用的模拟器。 |
| -o, --output | 可选参数，设置检测报告的保存路径，默认为当前工作路径。 |
| -m, --hapPaths | 可选参数，仅在选择基础场景后生效，用于指定待检测的HAP文件路径，多个文件使用英文逗号（,）分隔。用于检测HAP中的应用或元服务图标是否符合设计规范。 |

**示例：**

```bash
appanalyzer uxAnalyze -b com.example.demo -p ./demoProject
appanalyzer uxAnalyze -b com.example.demo -p ./demoProject -s D03 -d 127.0.0.1:5555 -m ./entry-default-signed.hap -o ./output
```

## 查看报告

通过命令行执行检测后，会生成json和zip两种格式的报告。

### json报告

```json5
{
  "reportVersion": "1.0",          // 报告版本号
  "generateTime": "2026-08-26T10:06:10+08:00",          // 报告生成时间
  "taskId": "838c7fc2-0fde-4f99-b00e-c2350c86d40a",     // 本次检测任务的唯一标识
  "bundleName": "com.example.example",                  // 被检测应用或元服务的包名
  "deviceInfo": {                  // 执行检测时所使用的设备信息
    "deviceId": "29L***193",       // 设备唯一标识
    "deviceModel": "HUAWEI Mate XT | ULTIMATE DESIGN",  // 设备型号
    "apiVersion": "23"             // 系统API版本
  },
  "uxIssues": [      // UX检测问题列表
    {
      "scene": "White Space",     // UX问题所属的检测场景
      "page": "entry/src/main/ets/pages/ux/block_align_issue.ets",        // 当前问题所在页面对应的源码文件路径
      "ruleName": "Basic Layout Requirements",          // UX检测规则名称
      "testSeq": 1,            // 测试序号
      "result": "fail",        // 检测结果
      "details": [             // 问题详情列表
        {
          "pageState": "Dual-screen state landscape",      // 问题发生时设备所处的形态
          "screenshot": "screenshots\\ori_state_screen_20260826100520_cover.jpeg",         // 问题截图文件路径
          "componentId": 239,             // 问题组件标识
          "componentType": "Text",        // 问题组件类型
          "issueAttribute": "",           // 组件属性
          "sourceFile": "entry/src/main/ets/pages/ux/block_align_issue.ets:79",       // 问题源码位置
          "location": [114, 622, 344, 689],             // 问题组件在截图中的矩形区域，格式为[left, top, right, bottom]
          "errorMsg": "Page controls block each other: widget bounds:[114, 622, 344, 689]"    // 检测出的具体问题描述
        }
      ]
    }
  ]
}
```

### zip报告

zip报告可以导入到DevEco Studio中的AppAnalyzer进行查看，具体请参考[导入报告](ide-app-analyzer-history-reports.md#section438013151813)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/tA1-dCHBRLqQt68kpg74tw/zh-cn_image_0000002779407244.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=12F456EE25824BC8C834499528B018A9AA20D5EEA215F79EAD8CDA92BE6D1F2F "点击放大")
