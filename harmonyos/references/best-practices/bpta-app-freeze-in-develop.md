---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-freeze-in-develop
title: 开发态快速定位AppFreeze冻屏指导
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 应用冻屏类问题分析 > 开发态快速定位AppFreeze冻屏指导
category: best-practices
scraped_at: 2026-09-04T06:33:26+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:8dc0f0d79a3698269876ff7bb7354bc3261a26f922d984e365c78245d5ba797b
---

## 概述

当应用发生冻屏时，开发者通常会观察到以下现象：

1. 界面无响应：应用界面点击无效、画面静止、无法响应用户操作（如滑动、点击按钮等）。
2. 系统弹窗提示：持续3-6秒后，系统会弹出“应用未响应”对话框，提示用户等待或关闭应用。
3. 应用闪退或强制终止：若冻屏状态持续，系统为保障整体流畅度，可能会强制终止该应用进程，导致应用闪退。
4. 日志特征：在系统或应用日志中会出现特定的故障类型关键字，如THREAD\_BLOCK\_6S（应用主线程冻屏超时）、APP\_INPUT\_BLOCK（用户输入响应超时）。

本文将通过高频冻屏场景及分析案例，协助开发者快速定位冻屏问题。

## 高频冻屏场景

### THREAD\_BLOCK\_6S（应用主线程冻屏超时）

* **触发条件**
  1. 如果主线程超过3秒未执行判活检测任务，系统会上报THREAD\_BLOCK\_3S警告事件，并抓取一次瞬时堆栈（Warning栈）。
  2. 如果主线程超过6秒仍未执行判活检测任务，系统则判定主线程已冻屏，上报THREAD\_BLOCK\_6S主线程冻屏事件，并抓取最终堆栈（Error栈）。
  3. 两个事件匹配后，系统会生成完整的应用冻屏日志，并通常会强制终止应用。
* **根本原因**

  这表明应用主线程长时间阻塞，无法处理新任务。常见原因包括在主线程执行耗时计算、同步网络请求、大文件IO或复杂UI渲染。此外，死锁或消息队列中高优先级任务过多，也会导致系统无法及时调度watchdog任务。

### APP\_INPUT\_BLOCK（用户输入响应超时）

* **触发条件**

  如果应用侧的回执超时，系统即判定为用户输入响应超时，上报APP\_INPUT\_BLOCK故障。
* **根本原因**

  主线程繁忙或阻塞，导致无法及时处理输入事件。

## 标准化排查流程

冻屏检测会生成故障日志，其中包含冻屏堆栈（3s Warning栈和6s Error栈）。

1. **获取冻屏日志**

通过DevEco Studio的底部FaultLog模块或触发冻屏现象时DevEco Studio右下提示框直接跳转至FaultLog。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/x6AFv05xQE651jCtU9U8jw/zh-cn_image_0000002644940872.png "点击放大")

2. **查看信息分析故障类型**

进入Fault Analysis页签查看Freeze type。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/T8WXZ5JSTkygLuL-2hHlig/zh-cn_image_0000002675100579.png "点击放大")

* THREAD\_BLOCK\_6S：应用主线程冻屏超时（前台6秒，后台21秒）。
* APP\_INPUT\_BLOCK：用户输入响应超时。

3. **分析主线程堆栈**

查看Sampling Stack定位故障指向，根据场景不同会存在没有采样栈的情况，有采样栈时需要检查采样栈是否一致。

* 采样栈一致：主线程阻塞需要分析堆栈信息。
* 采样栈不一致：如果占比超30%采样栈相同则确认为主线程繁忙，分析30%以上的堆栈定位；没有超30%采样栈时建议结合APMS大数据分析。
* 没有采样栈场景：查看3s/6s Compare页签对比3s和6s堆栈是否一致，一致时确认为主线程阻塞，分析3s/6s堆栈定位。不一致时说明主线程任务还在执行，无法确认卡死栈，需结合APMS大数据分析。

4. **优化代码修复问题**

结合指向的业务路径和系统负载信息，推断导致主线程繁忙或阻塞的业务代码逻辑并优化修复。

冻屏问题的标准化排查流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/2z9_Z6wuRVu7YlL-TbrSYQ/zh-cn_image_0000002675020727.jpg "点击放大")

## 冻屏分析案例

### 案例背景

开发者测试应用时（如点击按钮、滑动屏幕、按键），应用界面完全无反应，仿佛“冻结”了一般。持续等待约5秒后，系统终止应用进程或弹出“应用无响应”提示框。

### 分析流程

1. **配置获取App冻屏增强日志**

   查看采样栈数据之前，需要在AppScope/app.json5文件中配置如下环境变量，获取App冻屏增强日志。

   ```json
    "appEnvironments": [
       {
         "name": "DFX_APPFREEZE_LOG_OPTIONS",
         "value": "mainthread_sampling:enable"
       }
     ]
   ```
2. **查看FaultLog**

   打开FaultLog窗口，双击app冻屏日志，查看FaultLog头部的Event、Timestamp及Reason字段可以初步定位场景。

   如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/FNpwr6ZTSJGbWrVIAElp8g/zh-cn_image_0000002645100776.png "点击放大")
3. **查看****Fault Analysis**

   Fault Info右侧会出现Fault Analysis页签，点击Fault Analysis页签，会展示结构化的日志信息。

   查看Freeze type确认场景为THREAD\_BLOCK\_6S（主线程卡死超时）。

   如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/6tcHhqo4TFyDAVYDWEPRQg/zh-cn_image_0000002644940874.png "点击放大")

   **对比3秒（Warning）和6秒（Error）的堆栈**

   * 3秒和6秒的栈不一致：说明线程仍在执行业务代码，可能是任务过重导致主线程繁忙，需结合采样栈进一步确认。如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/5xawvhPsR8-bhWI-uxvFxQ/zh-cn_image_0000002675100581.png "点击放大")
4. **分析Sampling Stack**

   Sampling Stack页签展示应用堆栈（绿色标识）和系统堆栈（蓝色标识）。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/YqfMLUqDRSq_KpRzhfVKhA/zh-cn_image_0000002675020729.png "点击放大")

   点击切换图表类型按钮，可切换到堆栈火焰图，并通过不同颜色标识堆栈类型。其中红色代表异常堆栈，图中异常堆栈指向业务Page，结合前面步骤3s/6s堆栈不一致的场景，此时需要定位Page中导致主线程繁忙的业务逻辑。如下图所示：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/8t2qtMPmT7isiltpRwWjGg/zh-cn_image_0000002645100778.png "点击放大")

   开发者检查对应业务代码后，可发现两处导致主线程繁忙的严重问题。

   1. 这是一个空循环，在主线程上持续运行3秒**，**循环体内没有任何操作，纯粹占用CPU资源。在此期间，主线程完全阻塞，无法响应任何UI事件、触摸输入或渲染更新。

   2. 超大规模的同步I/O操作。

   如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/FVzBnnVDSYCGHnpRK5wwGg/zh-cn_image_0000002644940876.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/U1kS4niDSxSgFShQ9Cbq9g/zh-cn_image_0000002675100583.png)

### 优化修复

1. 移除忙等待循环。

2. 使用异步API替代同步API。

3. 根据实际需求设置合理的循环次数。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/0RTEgpqLSP6EO4MxmwFmgg/zh-cn_image_0000002675020731.png)

## 常见修复建议

根据问题特征，冻屏根因可分为以下几类：

1. 应用代码问题：如执行耗时函数、内存泄漏导致频繁GC、高优先级任务过多。优化方法包括将耗时操作移至子线程、减少内存泄漏、合理控制任务优先级。
2. 死锁问题：堆栈显示持锁等待。需检查代码中的锁使用，避免循环等待。
3. 调度问题：trace显示主线程长时间runnable。需调整任务优先级或联系调度域协助。
4. 系统库或IO问题：堆栈卡在系统库调用或IO操作。需排查系统库接口的耗时或IO阻塞情况。
