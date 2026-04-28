---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger
title: @ohos.faultLogger (故障日志获取)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > 已停止维护的接口 > @ohos.faultLogger (故障日志获取)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:af4511950f9ec5a22daf3f68ecbe49b3e4a2d187185abb118d5cb9c11ac2ab0c
---

应用可以使用faultLogger接口查询系统侧缓存的当前应用的故障日志。接口以应用包名和系统分配的UID作为唯一键值。

系统侧保存的应用故障日志数量受系统日志的压力限制，推荐使用[@ohos.hiviewdfx.hiAppEvent](js-apis-hiviewdfx-hiappevent.md)订阅APP\_CRASH及APP\_FREEZE等故障事件。

说明

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口从API version 18开始废弃使用, 该接口不再维护。后续版本推荐使用[@ohos.hiviewdfx.hiAppEvent](js-apis-hiviewdfx-hiappevent.md)订阅APP\_CRASH，APP\_FREEZE事件。

查阅[从Faultlogger接口迁移崩溃事件](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md#从faultlogger接口迁移崩溃事件)，了解使用hiAppEvent订阅APP\_CRASH的具体信息。

查阅[从Faultlogger接口迁移应用冻屏事件](../harmonyos-guides/hiappevent-watcher-freeze-events-arkts.md#从faultlogger接口迁移应用冻屏事件)，了解使用hiAppEvent订阅APP\_FREEZE的具体信息。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
```

## FaultType

PhonePC/2in1TabletTVWearable

故障类型枚举。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_SPECIFIC | 0 | 不区分故障类型。 |
| CPP\_CRASH | 2 | C++程序故障类型。 |
| JS\_CRASH | 3 | JS程序故障类型。 |
| APP\_FREEZE | 4 | 应用程序卡死故障类型。 |

## FaultLogInfo

PhonePC/2in1TabletTVWearable

故障信息数据结构，获取到的故障信息的数据结构。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 故障进程的进程id。 |
| uid | number | 否 | 否 | 故障进程的用户id。 |
| type | [FaultType](js-apis-faultlogger.md#faulttype) | 否 | 否 | 故障类型。 |
| timestamp | number | 否 | 否 | 日志生成时的毫秒级时间戳。 |
| reason | string | 否 | 否 | 发生故障的原因。 |
| module | string | 否 | 否 | 发生故障的模块。 |
| summary | string | 否 | 否 | 故障的概要。 |
| fullLog | string | 否 | 否 | 故障日志全文。 |

## FaultLogger.query9+

PhonePC/2in1TabletTVWearable

query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faultType | [FaultType](js-apis-faultlogger.md#faulttype) | 是 | 输入要查询的故障类型。 |
| callback | AsyncCallback<Array<[FaultLogInfo](js-apis-faultlogger.md#faultloginfo)>> | 是 | 回调函数，在回调函数中获取故障信息数组。  - value拿到故障信息数组；value为undefined表示获取过程中出现异常，error返回错误提示字符串。 |

**错误码：**

以下错误码的详细介绍参见[faultLogger错误码](errorcode-faultlogger.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed, Parameter type error. |
| 801 | The specified SystemCapability name was not found. |
| 10600001 | The service is not started or is faulty. |

**示例：**

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
5. if (error) {
6. console.error(`error code:${error.code}, error msg:${error.message}`);
7. } else {
8. console.info("value length is " + value.length);
9. let len: number = value.length;
10. for (let i = 0; i < len; i++) {
11. console.info(`log: ${i}`);
12. console.info(`Log pid: ${value[i].pid}`);
13. console.info(`Log uid: ${value[i].uid}`);
14. console.info(`Log type: ${value[i].type}`);
15. console.info(`Log timestamp: ${value[i].timestamp}`);
16. console.info(`Log reason: ${value[i].reason}`);
17. console.info(`Log module: ${value[i].module}`);
18. console.info(`Log summary: ${value[i].summary}`);
19. console.info(`Log text: ${value[i].fullLog}`);
20. }
21. }
22. }
23. try {
24. FaultLogger.query(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
25. } catch (err) {
26. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
27. }
```

## FaultLogger.query9+

PhonePC/2in1TabletTVWearable

query(faultType: FaultType) : Promise<Array<FaultLogInfo>>

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faultType | [FaultType](js-apis-faultlogger.md#faulttype) | 是 | 输入要查询的故障类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[FaultLogInfo](js-apis-faultlogger.md#faultloginfo)>> | Promise实例，可以在其then()方法中获取故障信息实例，也可以使用await。  - value拿到故障信息数组；value为undefined表示获取过程中出现异常。 |

**错误码：**

以下错误码的详细介绍参见[faultLogger错误码](errorcode-faultlogger.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed, Parameter type error. |
| 801 | The specified SystemCapability name was not found. |
| 10600001 | The service is not started or is faulty. |

**示例：**

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function getLog() {
5. try {
6. let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS_CRASH);
7. if (value) {
8. console.info(`value length: ${value.length}`);
9. let len: number = value.length;
10. for (let i = 0; i < len; i++) {
11. console.info(`log: ${i}`);
12. console.info(`Log pid: ${value[i].pid}`);
13. console.info(`Log uid: ${value[i].uid}`);
14. console.info(`Log type: ${value[i].type}`);
15. console.info(`Log timestamp: ${value[i].timestamp}`);
16. console.info(`Log reason: ${value[i].reason}`);
17. console.info(`Log module: ${value[i].module}`);
18. console.info(`Log summary: ${value[i].summary}`);
19. console.info(`Log text: ${value[i].fullLog}`);
20. }
21. }
22. } catch (err) {
23. console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
24. }
25. }
```

## FaultLogger.querySelfFaultLog(deprecated)

PhonePC/2in1TabletTVWearable

querySelfFaultLog(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>) : void

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[FaultLogger.query](js-apis-faultlogger.md#faultloggerquery9)替代。

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faultType | [FaultType](js-apis-faultlogger.md#faulttype) | 是 | 输入要查询的故障类型。 |
| callback | AsyncCallback<Array<[FaultLogInfo](js-apis-faultlogger.md#faultloginfo)>> | 是 | 回调函数，在回调函数中获取故障信息数组。  - value拿到故障信息数组；value为undefined表示获取过程中出现异常，error返回错误提示字符串。 |

**示例：**

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
5. if (error) {
6. console.error(`error code:${error.code}, error msg:${error.message}`);
7. } else {
8. console.info(`value length: ${value.length}`);
9. let len: number = value.length;
10. for (let i = 0; i < len; i++) {
11. console.info(`log: ${i}`);
12. console.info(`Log pid: ${value[i].pid}`);
13. console.info(`Log uid: ${value[i].uid}`);
14. console.info(`Log type: ${value[i].type}`);
15. console.info(`Log timestamp: ${value[i].timestamp}`);
16. console.info(`Log reason: ${value[i].reason}`);
17. console.info(`Log module: ${value[i].module}`);
18. console.info(`Log summary: ${value[i].summary}`);
19. console.info(`Log text: ${value[i].fullLog}`);
20. }
21. }
22. }
23. FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
```

## FaultLogger.querySelfFaultLog(deprecated)

PhonePC/2in1TabletTVWearable

querySelfFaultLog(faultType: FaultType) : Promise<Array<FaultLogInfo>>

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[FaultLogger.query](js-apis-faultlogger.md#faultloggerquery9-1)替代。

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**系统能力**：SystemCapability.HiviewDFX.Hiview.FaultLogger

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| faultType | [FaultType](js-apis-faultlogger.md#faulttype) | 是 | 输入要查询的故障类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[FaultLogInfo](js-apis-faultlogger.md#faultloginfo)>> | Promise实例，可以在其then()方法中获取故障信息实例，也可以使用await。  - value拿到故障信息数组；value为undefined表示获取过程中出现异常。 |

**示例：**

```
1. import { FaultLogger } from '@kit.PerformanceAnalysisKit';

3. async function getLog() {
4. let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.querySelfFaultLog(FaultLogger.FaultType.JS_CRASH);
5. if (value) {
6. console.info(`value length: ${value.length}`);
7. let len: number = value.length;
8. for (let i = 0; i < len; i++) {
9. console.info(`log: ${i}`);
10. console.info(`Log pid: ${value[i].pid}`);
11. console.info(`Log uid: ${value[i].uid}`);
12. console.info(`Log type: ${value[i].type}`);
13. console.info(`Log timestamp: ${value[i].timestamp}`);
14. console.info(`Log reason: ${value[i].reason}`);
15. console.info(`Log module: ${value[i].module}`);
16. console.info(`Log summary: ${value[i].summary}`);
17. console.info(`Log text: ${value[i].fullLog}`);
18. }
19. }
20. }
```
