---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-options
title: 斜杠命令
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > 斜杠命令
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:25+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3c5502ef3688ca56ca0fd3e7613fe00662e46e89112b5078a02d7327cf8b2a81
---

## collect

DevEco Code从0.2.0版本开始，当DevEco Code出现异常（如卡顿、报错、崩溃等）时，支持通过该命令触发日志上传弹框，在弹框中勾选需要上传的日志文件，以便定位和修复工具问题。DevEco Code日志默认存储路径为：

* Windows：C:\Users\用户名\.local\share\deveco\log
* macOS：~/.local/share/deveco/log

鸿蒙电脑版DevEco Code不支持该命令。

**命令格式：**

```txt
/collect
```

**说明** 

若应用非正常退出（如卡顿闪退等），当应用再次启动时会自动弹出上传日志弹框。

执行/privacy命令，选择**disable crash detect**输入回车，可关闭自动触发上传日志功能。

## analyze

DevEco Code从0.3.0版本开始，支持通过该命令触发DFX（HarmonyOS应用问题定位定界）诊断，对[AppFreeze](appfreeze-guidelines.md)、[Cpp Crash](cppcrash-guidelines.md)、[JS Crash](jscrash-guidelines.md)三类故障类型的日志进行根因分析。用户指定日志文件路径后，DFX诊断将自动完成日志类型识别、符号解析、堆栈解析等处理流程，定位故障根因，输出分析报告并提供修复建议。若本地有日志对应源码，工具可给出源码级别的修复建议。

鸿蒙电脑版DevEco Code不支持该命令。

**命令格式：**

```txt
/analyze 用户需求描述
```

**示例：**

```shell
/analyze 请帮忙分析xxxx目录下的日志
/analyze 请帮忙分析xxxx目录下的日志：xxxappfreeze.log
```

**说明** 

* 分析AppFreeze日志时，可结合采样栈日志辅助定位；分析CppCrash日志时，可结合GWP-ASAN日志辅助定位。
* 执行该命令，需要安装Python 3.8及以上版本。
