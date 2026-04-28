---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-v8-trace
title: 使用HiSmartPerf采集jsvm trace
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM性能调试指导 > 使用HiSmartPerf采集jsvm trace
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eef88fe63398123956051c56b8c7406bb37d5da4facc8d6b32056c3d8ab623c2
---

## 简介

jsvm的trace是jsvm引擎提供的一种用于分析和调试JavaScript代码执行过程的工具。它可以记录并输出关于代码执行的详细信息，包括函数调用、执行时间、内存使用情况等，帮助开发者了解代码的性能、诊断潜在问题，进行优化。

HiSmartPerf目前已经对接了jsvm的compile、runtime、builtin、JS\_Execution类别的trace点，可以在HiSmartPerf中直接看到这些类别event的相关信息。

## 使用方法

### 默认状态

jsvm是否采集trace由运行时开关“web.debug.rcs”控制，默认状态下该开关为关闭状态。启动web场景，在hilog中可以观察到有“RCS is off”日志打印输出。

### 采集jsvm trace

1. 要采集jsvm的trace，需要在启动web场景前，打开“web.debug.rcs”开关。在启动web场景前，执行以下命令：

   ```
   1. hdc shell setenforce 0
   2. hdc shell param set web.debug.rcs true
   ```
2. 启动web场景，可以看到hilog中有“RCS is on”的日志打印输出
3. 使用hitrace工具抓取对应场景的trace，hitrace使用方法可参考[hitrace](hitrace.md)使用指导文档。
4. 使用HiSmartPerf工具解析抓取到的trace，可以看到有“RCS\_”前缀的trace点，即为jsvm对接到HiSmartPerf中的trace点。
5. 要查看compile、runtime、builtin、JS\_Execution不同类别的trace数据，可使用以下关键字进行过滤：

   * compile：RCS\_v8.compile
   * runtime：RCS\_V8.Runtime
   * builtin：RCS\_v8.runtime\_V8.Builtin
   * JS\_Execution：RCS\_JS\_Execution
