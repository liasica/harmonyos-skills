---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events
title: 主线程超时事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 主线程超时事件 > 主线程超时事件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f8a63efb9edf842b65aa29523dd0ae0ffb5f19fd805cc70b9f3e410ac843646c
---

## 简介

当应用的主线程执行耗时任务时，开发者会感知到应用卡顿，但卡顿时间未达到系统设定的[应用冻屏](appfreeze-guidelines.md)时间限制，因此不会生成故障日志。为了更好地定位和分析问题，开发者可以查看[主线程超时事件检测原理](apptask-timeout-guidelines.md#检测原理)，根据生成的[主线程超时事件日志规格](apptask-timeout-guidelines.md#日志规格)，分析主线程任务的执行情况。

本文面向开发者介绍主线程超时检测原理，以及各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅主线程超时事件，请参考以下文档。目前提供ArkTS和C/C++两种接口，按需选择。

* [订阅主线程超时事件（ArkTS）](hiappevent-watcher-mainthreadjank-events-arkts.md)。
* [订阅主线程超时事件（C/C++）](hiappevent-watcher-mainthreadjank-events-ndk.md)。

说明

主线程超时事件支持在[应用分身](app-clone.md)场景下使用 HiAppEvent 进行订阅，支持在元服务场景下使用HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用 HiAppEvent 进行订阅。

## 检测原理

详见[主线程超时检测原理](apptask-timeout-guidelines.md#主线程超时检测)。

## 自定义参数

setEventConfig接口不提供主线程超时结束自动停止采样栈的功能；从API version 22开始，提供configEventPolicy接口，该接口提供主线程超时结束自动停止采样栈的功能。

### setEventConfig接口说明

| 接口名 | 描述 |
| --- | --- |
| [setEventConfig(name: string, config: Record<string, ParamType>): Promise<void>](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventseteventconfig15) | 设置主线程采样栈参数接口。 |

### setEventConfig接口参数设置说明

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 主线程超时事件名称，此处应为常量hiappevent.event.MAIN\_THREAD\_JANK。 |
| config | Record<string, ParamType> | 是 | 主线程超时采样栈配置参数。 |

主线程超时采样栈配置参数的定义。

注意

log\_type参数为必选项。

log\_type=0或2时，不设置其他参数。

log\_type=1时，所有参数均需设置。

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| log\_type | string | 是 | 采集MAIN\_THREAD\_JANK事件日志类型。  log\_type=0：默认值，主线程连续两次超时150ms~450ms，采集调用栈；主线程超时450ms，采集trace。  log\_type=1：仅采集调用栈。  log\_type=2：仅采集trace。 |
| sample\_interval | string | 否 | 主线程超时检测间隔和采样间隔。  单位为ms，默认值：150，取值范围为[50, 500]。  系统根据开发者设置的sample\_interval进行超时检测判断，并使用该sample\_interval作为周期性任务检测的间隔。 |
| ignore\_startup\_time | string | 否 | 忽略启动时间内的主线程超时检测。单位为s，最小值：3，默认值：10。  线程启动一定时间内，不进行超时检测。一些进程启动时间较长，此时抓全的超时采样栈，分析意义不大。因此，在开发者定义启动时间间隔内，不进行超时检测。 |
| sample\_count | string | 否 | 主线程超时采样次数。系统检测到当前主线程执行任务时长达到可采样阈值时，开始周期性采集堆栈，每个间隔采集一次堆栈，共采集sample\_count次。  默认值：10次。  最小值：1次，最大值需要结合自定义的sample\_interval进行动态计算，计算公式：sample\_count <= (2500 / sample\_interval - 4)。 |
| report\_times\_per\_app | string | 否 | 同一个应用的PID一个生命周期内，主线程超时采样上报次数。一个生命周期内只能设置一次。  默认值：1次，单位：次。  开发者选项打开，每小时范围：[1, 3]。  开发者选项关闭，每天上报次数范围：[1, 3]。 |

1. sample\_count说明：

   （1）2500的含义：根据系统规定，主线程超时事件从检测到上报的时间不可以超过2.5s（即：2500ms）。因此sample\_count的设置值不能超过系统按计算公式得出的最大值。

   （2）4的含义：第一次超时间隔检测时间 + 第二次超时间隔（系统提供两次再次发生超时事件的检测机会）时间 + 收集并上报堆栈信息的时间。

   （3）开发者要结合需求场景，进行合理的设置。
2. 参数设置示例

   展示setEventConfig接口中log\_type分别为0，1，2三种类型：

   （1）log\_type=0，用于采样栈或采样trace。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

   4. let params: Record<string, hiAppEvent.ParamType> = {
   5. "log_type": "0"
   6. };
   7. hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
   8. hilog.info(0x0000, 'hiAppEvent', `Setting default value successfully.`);
   9. }).catch((err: BusinessError) => {
   10. hilog.error(0x0000, 'hiAppEvent', `Failed to set default value. Code: ${err.code}, message: ${err.message}`);
   11. });
   ```

   （2）log\_type=1，仅用于采集调用栈。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

   4. let params: Record<string, hiAppEvent.ParamType> = {
   5. "log_type": "1",
   6. "sample_interval": "100",
   7. "ignore_startup_time": "11",
   8. "sample_count": "21",
   9. "report_times_per_app": "3"
   10. };
   11. hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
   12. hilog.info(0x0000, 'hiAppEvent', `Successfully set sampling stack parameters.`);
   13. }).catch((err: BusinessError) => {
   14. hilog.error(0x0000, 'hiAppEvent', `Failed to set sample stack value. Code: ${err.code}, message: ${err.message}`);
   15. });
   ```

   （3）log\_type=2，仅用于采集trace。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

   4. let params: Record<string, hiAppEvent.ParamType> = {
   5. "log_type": "2"
   6. };
   7. hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
   8. hilog.info(0x0000, 'hiAppEvent', `Set to only collect trace successfully.`);
   9. }).catch((err: BusinessError) => {
   10. hilog.error(0x0000, 'hiAppEvent', `Failed to set only collect trace. code: ${err.code}, message: ${err.message}`);
   11. });
   ```

### configEventPolicy接口说明

| 接口名 | 描述 |
| --- | --- |
| [configEventPolicy(policy: EventPolicy): Promise<void>](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventconfigeventpolicy22) | 设置主线程采样栈参数接口。支持超时卡顿结束自动停止采样。 |

### configEventPolicy接口参数设置说明

开发者可以使用上述hiappevent提供的接口，在[EventPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#eventpolicy22) 中配置采样栈接口的参数。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mainThreadJankPolicy | [MainThreadJankPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#mainthreadjankpolicy22) | 否 | 是 | 主线程超时事件配置策略。 |

**参数设置示例**

展示configEventPolicy接口中logType分别为0，1，2三种类型：

（1）logType=0，用于采样栈或采样trace。仅需配置autoStopSampling参数，其他参数均取默认值，无需设置。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

4. let policy: hiAppEvent.EventPolicy = {
5. "mainThreadJankPolicy" : {
6. "logType": 0, // 采集日志类型
7. "autoStopSampling": true // 超时结束，停止采集堆栈
8. }
9. };
10. hiAppEvent.configEventPolicy(policy).then(() => {
11. hilog.info(0x0000, 'hiAppEvent', `Setting default value successfully.`);
12. }).catch((err: BusinessError) => {
13. hilog.error(0x0000, 'hiAppEvent', `Failed to set default value. Code: ${err.code}, message: ${err.message}`);
14. });
```

（2）logType=1，仅用于采集调用栈。触发检测的阈值用户自定义。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

4. let policy: hiAppEvent.EventPolicy = {
5. "mainThreadJankPolicy" : {
6. "logType": 1, // 采集日志类型
7. "sampleInterval": 70, // 触发检测的阈值，采集堆栈间隔
8. "ignoreStartupTime": 11, // 应用启动期间忽略主线程超时检测的时间
9. "sampleCount": 20, // 主线程超时采样次数
10. "reportTimesPerApp": 3, // 主线程超时采样上报次数
11. "autoStopSampling": true // 超时结束，停止采集堆栈
12. }
13. };
14. hiAppEvent.configEventPolicy(policy).then(() => {
15. hilog.info(0x0000, 'hiAppEvent', `Successfully set sampling stack parameters.`);
16. }).catch((err: BusinessError) => {
17. hilog.error(0x0000, 'hiAppEvent', `Failed to set sample stack value. Code: ${err.code}, message: ${err.message}`);
18. });
```

（3）logType=2，仅用于采集trace。其他参数均不生效，无需设置。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

4. let policy: hiAppEvent.EventPolicy = {
5. "mainThreadJankPolicy" : {
6. "logType": 2 // 采集日志类型
7. }
8. };
9. hiAppEvent.configEventPolicy(policy).then(() => {
10. hilog.info(0x0000, 'hiAppEvent', `Set to only collect trace successfully.`);
11. }).catch((err: BusinessError) => {
12. hilog.error(0x0000, 'hiAppEvent', `Failed to set only collect trace. code: ${err.code}, message: ${err.message}`);
13. });
```

### OH\_HiAppEvent\_SetEventConfig接口说明

| 接口名 | 描述 |
| --- | --- |
| [int OH\_HiAppEvent\_SetEventConfig(const char\* name, HiAppEvent\_Config\* config)](../harmonyos-references/capi-hiappevent-h.md#oh_hiappevent_seteventconfig) | 设置主线程采样栈参数接口。 |

### OH\_HiAppEvent\_SetEventConfig接口参数设置说明

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | const char\* | 是 | 主线程超时事件名称，此处为预定义的宏EVENT\_MAIN\_THREAD\_JANK或EVENT\_MAIN\_THREAD\_JANK\_V2。 |
| config | HiAppEvent\_Config\* | 是 | 主线程超时采样栈配置参数，可使用[OH\_HiAppEvent\_SetConfigItem](../harmonyos-references/capi-hiappevent-h.md#oh_hiappevent_setconfigitem)函数设置config参数的配置项。 |

**name为EVENT\_MAIN\_THREAD\_JANK**

接口不提供主线程超时结束自动停止采样栈的功能，config参数作如下配置。

注意

MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为必选配置项。

MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"0"或"2"时，无其他配置项。

MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"1"时，所有配置项均需设置。

配置项的值均为可转换为整型的字符串字面量或字符指针。

对于API version 21及之前的版本，配置项名称只可使用相关字符串。

对于API version 22及之后的版本，配置项名称可使用预定义的宏及相关字符串。更推荐使用宏，避免开发者手写字符串造成非预期结果。

下文中值的取值范围说明均按转换后的变量类型进行阐述。

| 配置项名称 | 类型 | 必须配置 | 说明 |
| --- | --- | --- | --- |
| 宏：MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE  字符串：log\_type | const char\* | 是 | 采集日志的类型。  值为"0"：默认值，主线程连续两次超时150ms~450ms，采集调用栈；主线程超时450ms，采集trace。  值为"1"：仅采集调用栈。  值为"2"：仅采集trace。 |
| 宏：MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL  字符串：sample\_interval | const char\* | 否 | 主线程超时检测间隔和采样间隔。  单位为ms，默认值：150，取值范围为[50, 500]。  系统根据开发者设置的MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL的值进行超时检测判断，并使用该值作为周期性任务检测的间隔。 |
| 宏：MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME  字符串：ignore\_startup\_time | const char\* | 否 | 忽略启动时间内的主线程超时检测。  单位为s，最小值：3，默认值：10。  线程启动一定时间内，不进行超时检测。一些进程启动时间较长，此时抓全的超时采样栈，分析意义不大。因此，在开发者定义启动时间间隔内，不进行超时检测。 |
| 宏：MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT  字符串：sample\_count | const char\* | 否 | 主线程超时采样次数。系统检测到当前主线程执行任务时长达到可采样阈值时，开始周期性采集堆栈，每个间隔采集一次堆栈，共采集MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT次。  默认值：10次。  最小值：1次，最大值需要结合自定义的MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL进行动态计算，计算公式：MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT <= (2500 / MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL - 4)。 |
| 宏：MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP  字符串：report\_times\_per\_app | const char\* | 否 | 同一个应用的PID一个生命周期内，主线程超时采样上报次数。一个生命周期内只能设置一次。  默认值：1次，单位：次。  开发者选项打开，每小时范围：[1, 3]。  开发者选项关闭，每天上报次数范围：[1, 3]。 |

1. MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT说明：

   （1）2500的含义：根据系统规定，主线程超时事件从检测到上报的时间不可以超过2.5s（即：2500ms）。因此MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT的设置值不能超过系统按计算公式得出的最大值。

   （2）4的含义：第一次超时间隔检测时间 + 第二次超时间隔（系统提供两次再次发生超时事件的检测机会）时间 + 收集并上报堆栈信息的时间。

   （3）开发者要结合需求场景，进行合理的设置。
2. 参数设置示例

   展示OH\_HiAppEvent\_SetEventConfig接口中config参数的配置项MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE分别为"0"，"1"，"2"三种类型：

   （1）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"0"时，用于采样栈或采样trace。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "0");
   10. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK, config);
   11. if (ret == HIAPPEVENT_SUCCESS) {
   12. OH_LOG_INFO(LogType::LOG_APP, "Setting default value successfully.");
   13. }
   14. OH_HiAppEvent_DestroyConfig(config);
   ```

   （2）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"1"时，仅用于采集调用栈。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "1");
   10. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL, "100");
   11. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME, "11");
   12. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT, "21");
   13. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP, "3");

   15. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK, config);
   16. if (ret == HIAPPEVENT_SUCCESS) {
   17. OH_LOG_INFO(LogType::LOG_APP, "Successfully set sampling stack parameters.");
   18. }
   19. OH_HiAppEvent_DestroyConfig(config);
   ```

   （3）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"2"时，仅用于采集trace。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "2");

   11. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK, config);
   12. if (ret == HIAPPEVENT_SUCCESS) {
   13. OH_LOG_INFO(LogType::LOG_APP, "Set to only collect trace successfully");
   14. }
   15. OH_HiAppEvent_DestroyConfig(config);
   ```

**name为EVENT\_MAIN\_THREAD\_JANK\_V2**

从API VERSION 22开始，name可以为EVENT\_MAIN\_THREAD\_JANK\_V2，接口提供主线程超时结束自动停止采样栈的功能，config参数作如下配置。

注意

配置项名称为相关预定义的宏。

config的所有配置项均为可选项，不配置或者为空时取默认值。

MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"0"时，仅需设置MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING，其他配置项均取默认值，无需设置。

MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"2"时，其他配置项均不生效，无需设置。

MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING为"true"或"false"，转换为布尔类型；其他配置项的值均为可转换为整型的字符串字面量或字符指针。

下文中值的取值范围说明均按转换后的变量类型进行阐述。

| 配置项名称 | 类型 | 必须配置 | 说明 |
| --- | --- | --- | --- |
| MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE | const char\* | 否 | 采集日志的类型。  值为"0"：默认值，主线程连续两次超时150ms~450ms，采集调用栈；主线程超时450ms，采集trace。  值为"1"：仅采集调用栈。  值为"2"：仅采集trace。 |
| MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL | const char\* | 否 | 主线程超时检测间隔和采样间隔。  单位为ms，默认值：150，取值范围为[50, 500]。  系统根据开发者设置的MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL的值进行超时检测判断，并使用该值作为周期性任务检测的间隔。 |
| MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME | const char\* | 否 | 忽略启动时间内的主线程超时检测。  单位为s，最小值：3，默认值：10。  线程启动一定时间内，不进行超时检测。一些进程启动时间较长，此时抓全的超时采样栈，分析意义不大。因此，在开发者定义启动时间间隔内，不进行超时检测。 |
| MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT | const char\* | 否 | 主线程超时采样次数。系统检测到当前主线程执行任务时长达到可采样阈值时，系统检测到当前主线程执行任务超过采样限制后，开始周期性采集堆栈，每个间隔采集一次堆栈，共采集MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT次。  默认值：10次。  最小值：1次，最大值需要结合自定义的MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL进行动态计算，计算公式：MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT <= (2500 / MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL - 4)。 |
| MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP | const char\* | 否 | 同一个应用的PID一个生命周期内，主线程超时采样上报次数。一个生命周期内只能设置一次。  默认值：1次，单位：次。  开发者选项打开，每小时范围：[1, 3]。  开发者选项关闭，每天上报次数范围：[1, 3]。 |
| MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING | const char\* | 否 | 主线程超时结束时，是否自动停止采样主线程堆栈。  true: 超时结束或达到设置的采样次数，停止采样。  false：达到设置的采样次数时停止采样。  默认值：false。 |

1. MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT说明：

   （1）2500的含义：根据系统规定，主线程超时事件从检测到上报的时间不可以超过2.5s（即：2500ms）。因此MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT的设置值不能超过系统按计算公式得出的最大值。

   （2）4的含义：第一次超时间隔检测时间 + 第二次超时间隔（系统提供两次再次发生超时事件的检测机会）时间 + 收集并上报堆栈信息的时间。

   （3）开发者要结合需求场景，进行合理的设置。
2. 参数设置示例

   展示OH\_HiAppEvent\_SetEventConfig接口中config参数的配置项MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE分别为"0"，"1"，"2"三种类型：

   （1）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"0"时，用于采样栈或采样trace。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "0");
   10. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING, "true");
   11. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK_V2, config);
   12. if (ret == HIAPPEVENT_SUCCESS) {
   13. OH_LOG_INFO(LogType::LOG_APP, "Setting default value successfully.");
   14. }
   15. OH_HiAppEvent_DestroyConfig(config);
   ```

   （2）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"1"时，仅用于采集调用栈。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "1");
   10. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_SAMPLE_INTERVAL, "100");
   11. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_IGNORE_STARTUP_TIME, "11");
   12. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_SAMPLE_COUNT, "21");
   13. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_REPORT_TIMES_PER_APP, "3");
   14. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_AUTO_STOP_SAMPLING, "true");

   16. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK_V2, config);
   17. if (ret == HIAPPEVENT_SUCCESS) {{
   18. OH_LOG_INFO(LogType::LOG_APP, "Successfully set sampling stack parameters.");
   19. }
   20. OH_HiAppEvent_DestroyConfig(config);
   ```

   （3）MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE为"2"时，仅用于采集trace。

   ```
   1. #include "napi/native_api.h"
   2. #include "hilog/log.h"
   3. #include "hiappevent/hiappevent.h"

   5. #undef LOG_TAG
   6. #define LOG_TAG "testTag"

   8. HiAppEvent_Config* config = OH_HiAppEvent_CreateConfig();
   9. OH_HiAppEvent_SetConfigItem(config, MAIN_THREAD_JANK_PARAM_LOG_TYPE, "2");

   11. int ret = OH_HiAppEvent_SetEventConfig(EVENT_MAIN_THREAD_JANK_V2, config);
   12. if (ret == HIAPPEVENT_SUCCESS) {
   13. OH_LOG_INFO(LogType::LOG_APP, "Set to only collect trace successfully");
   14. }
   15. OH_HiAppEvent_DestroyConfig(config);
   ```

## 事件字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位为ms。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| pid | number | 应用的进程id。 |
| uid | number | 应用的用户id。 |
| begin\_time | number | 主线程任务开始时间。 |
| end\_time | number | 主线程任务结束时间。 |
| external\_log | string[] | 主线程超时日志文件路径。**为避免目录空间超限（参考log\_over\_limit），导致新生成的日志文件写入失败，日志文件处理完后请及时删除。** |
| log\_over\_limit | boolean | 生成的主线程超时日志文件与已存在的日志文件总大小是否超过10M上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
| app\_start\_jiffies\_time | number | 开发者可以获取主线程超时事件时，任务执行的开始时间。**触发采样栈，打印开始时间信息。** |
| heaviest\_stack | string | 生成的主线程超时日志文件中，打印多次的调用栈。**触发采样栈，打印多次的调用栈信息。** |
