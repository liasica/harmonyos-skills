---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-plugin-options
title: 斜杠命令
breadcrumb: 指南 > DevEco Code > DevEco Studio Plugin > 斜杠命令
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:14+08:00
doc_updated_at: 2026-10-31
content_hash: sha256:2868b7683f497a8117760774185ef8228204ba9f0b99a46b57c8e99c1dbf88eb
---

## new

新建对话。创建一个全新的空白会话，与当前会话的上下文完全隔离。适用于切换到不同任务、不想让之前对话内容干扰新场景时使用。

**命令格式：**

```txt
/new
```

## compact

压缩上下文。当对话过长、上下文接近模型token上限时，该命令会总结当前会话的核心信息，生成精简摘要替换原始历史，从而减少上下文大小。总结后可继续在同一会话中对话，无需切换。

**命令格式：**

```txt
/compact
```

## review

代码审查命令，以子任务方式在独立上下文中运行，审查结果以结构化反馈返回。支持三种审查范围，默认审查当前所有未提交的变更（含暂存区与未跟踪文件）。审查聚焦于Bug识别（逻辑错误、边界条件、安全问题）、代码结构是否符合现有模式、以及明显的性能问题，不会对风格偏好做过度纠偏。

**命令格式：**

```txt
/review
/review <commit hash>
/review <branch name>
/review <PR URL 或编号>
```

**示例：**

```shell
/review
/review a1b2c3d
/review develop
/review https://github.com/org/repo/pull/42
```

## init

AGENTS.md初始化。该命令会分析项目结构（构建配置、CI 工作流、测试脚本、已有指令文件等），提取对未来会话有价值的高信号信息，生成或更新AGENTS.md文件。该文件帮助AI快速理解项目的开发命令、包边界、工具链特性和约定，避免常见错误。如果AGENTS.md已存在，会在原有基础上增量改进而非盲目重写。

**命令格式：**

```txt
/init
```

## debug

ArkTS运行时调试命令。以粘滞模式（sticky mode）运行调试专用智能体，在当前会话中持续保持调试上下文，直到用户显式退出。调试智能体会收集运行时证据（日志、堆栈等）来定位ArkTS问题根因。如果用户描述过于笼统或缺少关键症状信息，智能体会先提出问题以收集具体的故障现象，再开始诊断。支持clea子命令退出调试模式，status子命令查看当前调试状态。

**命令格式：**

```txt
/debug <问题描述>
/debug clear
/debug status
```

**示例：**

```shell
/debug 应用启动后白屏，日志显示 ArkTS undefined 报错
/debug clear
```

## analyze

支持通过该命令触发DFX（HarmonyOS应用问题定位定界）诊断，对[AppFreeze](appfreeze-guidelines.md)、[Cpp Crash](cppcrash-guidelines.md)、[JS Crash](jscrash-guidelines.md)三类故障类型的日志进行根因分析。用户指定日志文件路径后，DFX诊断将自动完成日志类型识别、符号解析、堆栈解析等处理流程，定位故障根因，输出分析报告并提供修复建议。若本地有日志对应源码，工具可给出源码级别的修复建议。

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
