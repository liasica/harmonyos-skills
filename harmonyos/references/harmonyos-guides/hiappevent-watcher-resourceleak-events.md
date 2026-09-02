---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events
title: 资源泄漏事件介绍
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 资源泄漏事件 > 资源泄漏事件介绍
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-08-04
content_hash: sha256:975e44c497f668782568a20456ad56c663c880eb78e257c83c8dce77c5c1ac5a
---

## 简介

资源泄漏是指句柄、线程或内存等资源在应用运行过程中未被正确释放，导致资源长期占用且无法被其他应用使用。如果某一类资源耗尽，系统可能出现卡死或重启等异常情况。

本文面向开发者介绍资源泄漏事件各字段的含义和规格。如需了解如何使用HiAppEvent接口订阅系统资源泄漏事件，请参考以下文档。目前提供ArkTs和C/C++两种接口。

* [订阅资源泄漏事件（ArkTS）](hiappevent-watcher-resourceleak-events-arkts.md)
* [订阅资源泄漏事件（C/C++）](hiappevent-watcher-resourceleak-events-ndk.md)

**说明** 

资源泄漏事件支持在[应用分身](app-clone.md)场景下使用 HiAppEvent 进行订阅，支持在元服务场景下使用 HiAppEvent 进行订阅，从 API version 22 开始支持在[输入法应用](inputmethod-application-guide.md)场景下使用 HiAppEvent 进行订阅。

## 检测原理

检测原理详见[Resource Leak（资源泄漏）检测](resource-leak-guidelines.md)。

## 自定义规格设置

### setEventConfig接口说明

| 接口名 | 描述 |
| --- | --- |
| setEventConfig(name: string, config: Record<string, ParamType>): Promise<void> | 设置资源泄漏日志规格参数，name应为资源泄漏事件名称常量hiappevent.event.RESOURCE\_OVERLIMIT。**仅支持JS内存泄漏类型。**  **说明**：从API version 20开始，支持该接口。 |

### setEventConfig接口参数设置说明

开发者可以使用HiAppEvent提供的接口，在Record<string, ParamType>中设置RESOURCE\_OVERLIMIT的日志和回调事件规格。具体参数说明如下：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| js\_heap\_logtype | string | 否 | event：应用发生oom时，不传递堆快照。  event\_rawheap：应用发生oom时，系统生成并传递堆快照  **注意**：当前仅接收以上二值，如果传入其他内容，方法将调用失败，不会产生任何效果。 |

**注意** 

即使参数js\_heap\_logtype设置为event\_rawheap，也不能保证生成堆快照文件。这是因为生成堆快照时，应用可能因性能问题触发冻屏而提前退出。

参数配置示例：

```ts
let configParams: Record<string, hiAppEvent.ParamType> = {
    "js_heap_logtype": "event", // 仅获取事件
    // "js_heap_logtype": "event_rawheap", // 同时获取堆快照
};

hiAppEvent.setEventConfig(hiAppEvent.event.RESOURCE_OVERLIMIT, configParams);
```

**注意** 

应用调用setEventConfig接口时，每次调用的内容只会在当前应用生命周期内生效。应用重启后，需要重新通过setEventConfig接口设置。

在同一个应用生命周期内，可以多次调用setEventConfig，以最后一次成功调用的值为准。

开发者在调试以及自测试过程中，单日内触发OOM次数过多，可能会遇到无法收到hiappevent回传JS内存泄漏事件的情况，可以通过将系统时间往后调一天进行规避。

### configEventPolicy接口说明

从**API version 24**开始支持页面切换日志配置。当应用发生资源泄漏故障时，系统可以收集并上报页面切换日志，帮助开发者定位问题。

从**API version 26.0.0**开始支持设置资源泄漏事件的日志和回调事件规格。

| 接口名 | 描述 |
| --- | --- |
| [configEventPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventconfigeventpolicy22) (policy: EventPolicy): Promise<void> | 设置资源泄漏事件策略参数接口，支持开启资源泄漏事件的页面切换日志采集、设置资源泄漏事件的日志和回调事件规格。 |

### configEventPolicy接口参数设置说明

开发者可以通过设置[EventPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#eventpolicy22) 的参数来开启资源泄漏事件的页面切换日志采集以及设置资源泄漏事件的日志和回调事件规格。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resourceOverlimitPolicy | [ResourceOverlimitPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#resourceoverlimitpolicy24) | 否 | 是 | 资源泄漏事件配置策略。 |

参数配置示例：

```ts
import { deviceInfo, BusinessError } from '@kit.BasicServicesKit';
import { hilog, hiAppEvent } from '@kit.PerformanceAnalysisKit';

let policy: hiAppEvent.EventPolicy = {
    resourceOverlimitPolicy: {
        pageSwitchLogEnable: true, // 启用页面切换日志。从API version 24开始支持该参数
        useRefinedLogFileName: true, // 启用事件日志文件名精细化开关。从API版本26.0.0开始支持该参数
        js_heap_logtype: "event", // 仅获取事件。从API版本26.0.0开始支持该参数
        // js_heap_logtype: "event_rawheap", // 同时获取堆快照。从API版本26.0.0开始支持该参数
    }
};
hiAppEvent.configEventPolicy(policy).then(() => {
    hilog.info(0x0000, 'hiAppEvent', `Set resourceOverlimit config policy successfully.`);
}).catch((err: BusinessError) => {
    hilog.error(0x0000, 'hiAppEvent', `Failed to set resourceOverlimit config policy. code: ${err.code}, message: ${err.message}`);
});
```

## params字段说明

资源泄漏事件信息中params属性的详细说明如下：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| time | number | 事件触发时间，单位：ms。 |
| app\_running\_unique\_id | string | 应用运行时唯一关联的id。  **说明**：从API version 24开始支持该参数。 |
| bundle\_version | string | 应用版本。 |
| bundle\_name | string | 应用名称。 |
| pid | number | 应用的进程ID。 |
| uid | number | 应用的用户ID。 |
| resource\_type | string | 资源类型，取值范围详见resource\_type属性。 |
| memory | object | （resource\_type为pss\_memory或js\_heap专有）内存信息，详见[memory字段说明](hiappevent-watcher-resourceleak-events.md#memory字段说明)。 |
| fd | object | （resource\_type为fd专有）文件描述符信息，详见[fd字段说明](hiappevent-watcher-resourceleak-events.md#fd字段说明)。 |
| thread | object | （resource\_type为thread专有）线程信息，详见[thread字段说明](hiappevent-watcher-resourceleak-events.md#thread字段说明)。 |
| external\_log | string[] | 故障日志文件路径。**为避免目录空间超限（限制参考log\_over\_limit），导致新生成的日志文件写入失败，请在日志文件处理完后及时删除。** |
| log\_over\_limit | boolean | 生成的故障日志文件与已存在的日志文件总大小是否超过2GB上限。true表示超过上限，日志写入失败；false表示未超过上限。 |
| page\_switch\_log | string | 页面切换日志路径，日志介绍详见[页面切换日志](pageswitch-log.md)。  **说明**：从API version 24开始支持。 |

### resource\_type字段说明

| 取值 | 说明 |
| --- | --- |
| pss\_memory | pss内存泄漏。 |
| rss\_memory | rss内存泄漏。  **说明**：从API版本26.0.0开始，支持该字段。 |
| ion\_memory | ion内存泄漏。  **说明**：从API version 20开始，支持该字段。 |
| gpu\_memory | gpu内存泄漏。  **说明**：从API version 20开始，支持该字段。 |
| js\_heap | JS内存泄漏。 |
| fd | 句柄泄漏。 |
| thread | 线程泄漏。 |

### memory字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| rss | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）进程实际占用内存大小，单位：KB。 |
| vss | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）进程向系统申请的虚拟内存大小，单位：KB。 |
| pss | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）进程实际使用的物理内存大小，单位：KB。 |
| ion | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）进程实际使用的ION内存大小，单位：KB。  **说明**：从API version 20开始，支持该字段。 |
| gpu | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）进程实际使用的GPU内存大小，单位：KB。  **说明**：从API version 20开始，支持该字段。 |
| sys\_free\_mem | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）空闲内存大小，单位：KB。 |
| sys\_avail\_mem | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）可用内存大小，单位：KB。 |
| sys\_total\_mem | number | （resource\_type为pss\_memory、ion\_memory、gpu\_memory专有）总内存大小，单位：KB。 |
| limit\_size | number | （resource\_type为js\_heap专有）基线大小，单位：KB。 |
| live\_object\_size | number | （resource\_type为js\_heap专有）实际使用内存大小，单位：KB。 |
| rss\_detail | object | （resource\_type为rss\_memory）RSS内存详细分布信息，详见[detail字段说明](hiappevent-watcher-resourceleak-events.md#detail字段说明)。  **说明**：从API版本26.0.0开始，支持该字段。 |
| pss\_detail | object | （resource\_type为pss\_memory）PSS内存详细分布信息，详见[detail字段说明](hiappevent-watcher-resourceleak-events.md#detail字段说明)。  **说明**：从API版本26.0.0开始，支持该字段。 |

### detail字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| .db | number | 数据库文件占用内存大小，单位：KB。 |
| .hap | number | HAP文件占用内存大小，单位：KB。 |
| .so | number | 共享库文件占用内存大小，单位：KB。 |
| .ttf | number | 字体文件占用内存大小，单位：KB。 |
| anon\_page\_other | number | 其他匿名页占用内存大小，单位：KB。 |
| ark ts heap | number | ArkTS堆占用内存大小，单位：KB。 |
| arkweb-js heap | number | ArkWeb JS堆占用内存大小，单位：KB。 |
| arkweb-pa heap | number | ArkWeb PA堆占用内存大小，单位：KB。 |
| dart heap | number | Dart堆占用内存大小，单位：KB。 |
| dev | number | /dev开头的各类文件占用内存大小，单位：KB。 |
| file\_page\_other | number | 其他文件页占用内存大小，单位：KB。 |
| jsvm heap | number | JSVM堆占用内存大小，单位：KB。 |
| kotlin heap | number | Kotlin堆占用内存大小，单位：KB。 |
| native heap | number | Native堆占用内存大小，单位：KB。 |
| other | number | 其他类型占用内存大小，单位：KB。 |
| rn-hermes heap | number | React Native Hermes堆占用内存大小，单位：KB。 |
| stack | number | 栈空间占用内存大小，单位：KB。 |

### fd字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| num | number | fd总数量。 |
| top\_fd\_type | string | 使用最多的fd类型。 |
| top\_fd\_num | number | 使用最多的fd类型的数量。 |

### thread字段说明

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| num | number | thread总数量。 |

## 自定义params参数

当前资源泄漏事件上报**JS内存泄漏**事件信息，可能无法满足开发者的个性化需求，因此提供事件setEventParam方法，自定义事件上报信息。

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void> | 事件自定义参数设置方法。  **说明**：从API version 20开始，支持该接口。 |
