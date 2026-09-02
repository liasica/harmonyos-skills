---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-arkts
title: 使用HiTraceMeter跟踪性能（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 性能跟踪 > 使用HiTraceMeter跟踪性能（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fcb2d4904afe2d621e2c3e05190ca899dc28ef9aeb76d3a610a3d07b032a79b8
---

## 简介

HiTraceMeter提供系统性能打点接口。开发者在关键代码位置调用这些API，能够有效跟踪进程轨迹，查看系统和应用性能。

## 接口说明

性能打点跟踪接口由HiTraceMeter模块提供，详细API请参考[@ohos.hiTraceMeter (性能打点)](../harmonyos-references/js-apis-hitracemeter.md)。

| 接口名 | 描述 |
| --- | --- |
| hiTraceMeter.startSyncTrace(level: HiTraceOutputLevel, name: string, customArgs?: string): void | 开启一个同步时间片跟踪事件，分级控制跟踪输出。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.finishSyncTrace(level: HiTraceOutputLevel): void | 结束一个同步时间片跟踪事件，分级控制跟踪输出。  level必须与流程开始的startSyncTrace()对应参数值保持一致。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.startAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number, customCategory: string, customArgs?: string): void | 开启一个异步时间片跟踪事件，分级控制跟踪输出。  taskId是trace中用来表示关联的ID，如果有多个name相同的任务并行执行，则开发者每次调用startAsyncTrace()时，传入的taskId需不同；如果具有相同name的任务是串行执行的，则taskId可以相同。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.finishAsyncTrace(level: HiTraceOutputLevel, name: string, taskId: number): void | 结束一个异步时间片跟踪事件，分级控制跟踪输出。  level、name和taskId必须与流程开始的startAsyncTrace()对应参数值保持一致。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.traceByValue(level: HiTraceOutputLevel, name: string, count: number): void | 整数跟踪事件，分级控制跟踪输出。  name和count两个参数分别用来标记一个跟踪的整数变量名及整数值。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.isTraceEnabled(): boolean | 判断当前是否开启应用trace捕获。  使用hitrace命令行工具等方式开启采集时返回true。未开启采集或停止采集后返回false，此时调用HiTraceMeter性能跟踪打点接口无效。  **说明**：从API version 19开始，支持该接口。 |
| hiTraceMeter.registerTraceListener(callback: TraceEventListener): number | 注册应用trace捕获开关通知回调，使用callback异步回调。  注册成功后，立即执行一次回调函数，后续回调函数由应用trace捕获开关状态变化触发执行。  **说明**：从API version 22开始，支持该接口。 |
| hiTraceMeter.unregisterTraceListener(index: number): number | 注销应用trace捕获开关通知回调。  **说明**：从API version 22开始，支持该接口。 |

**注意** 

[用户态trace格式](hitracemeter-view.md#用户态trace格式说明)使用竖线 | 作为分隔符，所以通过HiTraceMeter接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。

### 接口分类

HiTraceMeter打点接口分为三类：同步时间片跟踪、异步时间片跟踪和整数跟踪。HiTraceMeter接口实现均为同步，同步和异步针对的是被跟踪的业务。同步业务使用同步时间片跟踪接口，异步业务使用异步时间片跟踪接口。HiTraceMeter打点接口可与[HiTraceChain](hitracechain-guidelines-arkts.md)一起使用，进行跨设备、跨进程或跨线程的打点关联与分析。

### 接口使用场景

* 同步时间片跟踪接口

  用于顺序执行的打点场景，需按序成对使用startSyncTrace()接口和finishSyncTrace()接口，否则会导致trace文件在smartperf等可视化工具上显示异常。
* 异步时间片跟踪接口

  在异步操作执行前调用startAsyncTrace()接口进行开始打点，在异步操作完成后调用finishAsyncTrace()接口进行结束打点。

  解析trace时，通过name和taskId参数识别不同的异步跟踪。这两个接口必须按序成对使用，并传入相同的name和taskId。

  不同的异步流程中应使用不同的name和taskId，但在异步跟踪流程不会同时发生的情况下，可以使用相同的name和taskId。

  调用错误会导致trace文件在smartperf等可视化工具上显示异常。
* 整数跟踪接口

  用于跟踪整数变量。整数值变动时调用traceByValue()接口，可在smartperf的泳道图中观察变动情况。由于从开始采集到首次打点存在时间差，这段时间的数值无法查看。

### 参数解析

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | enum | 是 | 跟踪输出级别。低于系统阈值的跟踪将不会被输出。  log版本阈值默认为INFO，nolog版本阈值默认为COMMERCIAL。 |
| name | string | 是 | 要跟踪的任务名称或整数变量名称。 |
| taskId | number | 是 | 用来表示关联的ID，如果有多个name相同的任务并行执行，则开发者每次调用startAsyncTrace()时，传入的taskId需不同。 |
| count | number | 是 | 整数变量的值。 |
| customCategory | string | 是 | 自定义聚类名称，用于聚合同一类异步跟踪打点。  若不需要聚类，可传入一个空字符串。 |
| customArgs | string | 否 | 自定义键值对，若有多组键值对，使用逗号进行分隔，例"key1=value1,key2=value2"。  若不需要该参数，可不传入该参数或传入一个空字符串。 |
| callback | (boolean) => void | 是 | 注册的回调函数。 |
| index | number | 是 | registerTraceListener()返回的回调索引。 |

**说明** 

[用户态trace](hitracemeter-view.md#用户态trace格式说明)总长度限制为512个字符，超过部分将会被截断。建议name、customCategory和customArgs三个字段的总长度不超过420字符，以避免trace被截断。

## 开发步骤

以下为一个使用HiTraceMeter打点接口的ArkTS应用示例。

### 步骤一：创建项目

1. 在DevEco Studio中新建工程，选择“Empty Ability”，工程的目录结构如下：

   ```txt
   ├── entry
   │   ├── src
   │       ├── main
   │       │   ├── ets
   │       │   │   ├── entryability
   │       │   │   │   └── EntryAbility.ets
   │       │   │   └── pages
   │       │   │       └── Index.ets
   ```
2. 编辑工程中的“entry > src > main > ets > pages > Index.ets”：

   导入所需依赖：

   ```typescript
   import { hiTraceMeter, hilog} from '@kit.PerformanceAnalysisKit';
   ```

   定义测试方法：

   ```typescript
   function testHiTraceMeterASync() {
     const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
     hiTraceMeter.startAsyncTrace(COMMERCIAL, 'myTestAsyncTrace', 1001, 'categoryTest', 'key=value');
     hiTraceMeter.startAsyncTrace(COMMERCIAL, 'myTestAsyncTrace', 1002, 'categoryTest', 'key=value');

     setTimeout(() => {
       // 结束taskId为1001的异步跟踪任务
       hiTraceMeter.finishAsyncTrace(COMMERCIAL, 'myTestAsyncTrace', 1001);
     }, 2000);

     setTimeout(() => {
       // 结束taskId为1002的异步跟踪任务
       hiTraceMeter.finishAsyncTrace(COMMERCIAL, 'myTestAsyncTrace', 1002);
     }, 1000);
   }

   function testHiTraceMeterSync() {
     const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
     // 开始同步跟踪任务
     hiTraceMeter.startSyncTrace(COMMERCIAL, 'myTestSyncTrace', 'key=value');
     // 业务流程
     hilog.info(0x0000, 'testTrace', 'myTraceTest running, synchronizing trace');
     // 结束同步跟踪任务
     hiTraceMeter.finishSyncTrace(COMMERCIAL);
   }

   function testHiTraceMeterValue() {
     const COMMERCIAL = hiTraceMeter.HiTraceOutputLevel.COMMERCIAL;
     let traceCount = 0;
     // trace计数初始值
     hiTraceMeter.traceByValue(COMMERCIAL, 'myTestCountTrace', traceCount);
     traceCount++;
     // trace打点变化后的值
     hiTraceMeter.traceByValue(COMMERCIAL, 'myTestCountTrace', traceCount);
   }

   function testHiTraceMeter() {
     // 在未开启应用trace捕获时，避免该部分性能损耗
     if (hiTraceMeter.isTraceEnabled()) {
       testHiTraceMeterASync();
       testHiTraceMeterSync();
       testHiTraceMeterValue();
     } else {
       hilog.info(0x0000, 'testTrace', 'myTraceTest running, trace is not enabled');
     }
   }
   ```

   添加按钮以触发接口调用：

   ```typescript
   Button("testHiTraceMeter").backgroundColor('#FFFF00FF')
     .onClick(testHiTraceMeter)
   ```

### 步骤二：采集trace信息并查看

1. 在DevEco Studio Terminal窗口中执行以下命令，开启应用的trace捕获。

   ```shell
   PS D:\xxx\xxx> hdc shell
   $ hitrace --trace_begin app
   ```
2. 单击DevEco Studio界面上的运行按钮，启动应用。点击应用界面的“testHiTraceMeter”按钮，执行包含HiTraceMeter打点的业务逻辑。然后执行如下命令抓取trace数据，并使用“myTest”关键字过滤trace数据（示例打点接口传递的name字段前缀均为“myTest”）。

   ```shell
   $ hitrace --trace_dump | grep myTest
   ```

   成功抓取的trace数据如下所示：

   ```text
   <...>-30265   (-------) [003] ..... 223860.709694: tracing_mark_write: S|30265|H:myTestAsyncTrace|1001|M62|categoryTest|key=value
   <...>-30265   (-------) [003] ..... 223860.709735: tracing_mark_write: S|30265|H:myTestAsyncTrace|1002|M62|categoryTest|key=value
   <...>-30265   (-------) [003] ..... 223860.710081: tracing_mark_write: B|30265|H:myTestSyncTrace|M62|key=value
   <...>-30265   (-------) [003] ..... 223860.710305: tracing_mark_write: C|30265|H:myTestCountTrace|0|M62
   <...>-30265   (-------) [003] ..... 223860.710332: tracing_mark_write: C|30265|H:myTestCountTrace|1|M62
   <...>-30265   (-------) [003] ..... 223861.711284: tracing_mark_write: F|30265|H:myTestAsyncTrace|1002|M62
   <...>-30265   (-------) [003] ..... 223862.709901: tracing_mark_write: F|30265|H:myTestAsyncTrace|1001|M62
   ```

   每一行trace数据中，tracing\_mark\_write为打点事件类型，应用程序中调用HiTraceMeter接口打点使用的均为此事件。打点事件类型前面的数据分别为线程名-线程ID、进程ID、CPU和打点时间（从开机到当前的时间，单位为秒）；打点事件类型后面的数据可查看[用户态trace格式](hitracemeter-view.md#用户态trace格式说明)。

### 步骤三：停止采集trace

1. 执行以下命令，停止应用的trace捕获。

   ```shell
   $ hitrace --trace_finish
   ```
2. 再次点击应用界面的“testHiTraceMeter”按钮，此时应用trace捕获已关闭，isTraceEnabled()接口返回false。在DevEco Studio Log窗口使用关键字“not enabled”进行过滤，会打印如下日志。

   ```text
   myTraceTest running, trace is not enabled
   ```

   **说明** 

   log版本在使用hitrace --trace\_finish命令停止采集后会自动拉起快照模式，打开trace捕获，此时isTraceEnabled()接口返回true，不会打印上述日志。
