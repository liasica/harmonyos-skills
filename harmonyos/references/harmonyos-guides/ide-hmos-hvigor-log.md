---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-log
title: 使用日志记录
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 构建报错排查 > 使用日志记录
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:13e335811891cbf3e1709a75fd289d3ab5c3f03dbc2c62f1331b65a55fa0b3f4
---

日志是构建工具主要的输出显示部分，如果日志过于冗长，真正的告警和异常将更容易被隐藏；而另一方面，当出现问题时，你也需要相关的信息来定位问题。Hvigor定义了四种日志级别，如下所示。

## 日志级别

| 日志级别 | | 日志信息 |
| --- | --- | --- |
| ERROR | | 错误信息 |
| WARN | | 告警信息 |
| INFO | | 正常信息 |
| DEBUG | | 调试信息 |

## 选择日志级别

您可以使用命令行中的日志选项开关来控制输出不同的日志级别，还可通过配置[hvigor-config.json5](ide-hmos-hvigor-set-options.md)中日志选项logging.level来设置。在stacktrace命令选项中，您可以找到影响堆栈跟踪记录的命令开关，此外，你也可以通过配置hvigor-config.json5中日志选项debugging.stacktrace来设置堆栈跟踪日志开关。

### 日志级别命令行选项

**表1** 日志级别命令行选项

| 日志选项 | 输出日志级别 |
| --- | --- |
| -e 或 --error | 错误且更高级别 |
| -w 或 --warn | 告警且更高级别 |
| -i 或 --info | 信息且更高级别 |
| -d 或 --debug | 调试且更高级别（即所有日志信息） |

### 堆栈跟踪命令行选项

--stacktrace

控制台将打印完整的堆栈跟踪信息。

--no-stacktrace

如果出现构建错误（例如编译错误），则不会将堆栈跟踪信息打印到控制台。
