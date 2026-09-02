---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher
title: "@ohos.hiviewdfx.jsLeakWatcher (ArkTS泄漏检测)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.jsLeakWatcher (ArkTS泄漏检测)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cc7f59b395463fc3278f4bde3c0cb21f9642f1b5e2e14c74ce4455b077cf5d3d
---

本模块提供了监控ArkTS对象是否发生泄漏的能力，可在应用开发、测试阶段发现并定位ArkTS对象的内存泄漏问题。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## jsLeakWatcher.enable

enable(isEnable: boolean): void

使能ArkTS对象泄漏检测，默认关闭。开启后会收集泄漏信息，可能增加性能开销。

推荐的完整调用流程：enable() → watch() → check() → dump()

使用场景：

* 应用开发调试阶段，用于检测和定位内存泄漏问题。
* 应用测试阶段，用于验证应用的内存管理是否正常。
* 对内存使用有严格要求的应用，需要持续监控内存状态。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnable | boolean | 是 | 是否使能jsLeakWatcher。true：使能jsLeakWatcher；false：不使能jsLeakWatcher。 |

**示例：**

```js
jsLeakWatcher.enable(true);
```

## jsLeakWatcher.watch

watch(obj: object, msg: string): void

注册待检测泄漏的对象。

使用场景：

* 在创建可能发生泄漏的关键对象后（如自定义组件、Window等），立即注册进行监控。
* 对应用生命周期中的重要对象进行注册，以便及时发现泄漏。
* 在特定功能模块中使用到的对象，如XComponent、NodeContainer等，注册以监控其释放情况。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | object | 是 | 需要检测的对象。  **说明**：可传入任何非null的ArkTS对象，不支持undefined和基本类型。 |
| msg | string | 是 | 自定义对象信息。 |

**示例：**

```js
let obj:Object = new Object();
jsLeakWatcher.watch(obj, "Trace Object");
```

## jsLeakWatcher.check

check(): string

获取已通过jsLeakWatcher.watch注册发生泄漏的对象列表，触发GC后未被回收的对象会被标记为泄漏。

使用场景：

* 在应用运行过程中定期检查，以便及时发现内存泄漏问题。
* 在关键功能执行前后检查，对比泄漏情况。
* 根据泄漏列表定位具体的泄漏对象，进行代码排查和修复。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 触发GC后未被回收的泄漏对象列表。  **说明**：check成功，返回JSON格式的泄漏对象列表；check失败，返回空字符串。 |

**示例：**

```js
let leakObjlist:string = jsLeakWatcher.check();
```

## jsLeakWatcher.dump

dump(filePath: string): Array<string>

导出泄漏列表和虚拟机内存快照。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 导出信息生成的文件存放的路径。  **说明**：从API version 24开始，进程生命周期内，仅保留最新的一份快照信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 导出结果。分别为文件名后缀为.jsleaklist的泄漏列表和文件名后缀为.heapsnapshot虚拟机内存快照文件。  **说明**：dump成功，返回泄漏列表文件路径和虚拟机内存快照路径；dump失败，返回空数组。 |

**示例：**

```js
let context = this.getUIContext().getHostContext();
let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```

## jsLeakWatcher.enableLeakWatcher20+

enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void

使能ArkTS对象泄漏检测。

此接口通过一次调用即可检测ArkTS对象的内存泄漏，比之前需要调用四个函数（enable、watch、check、dump）的方法更加简洁。

使用场景：

* 对内存使用有严格要求的应用，需要持续监控内存泄漏情况。
* 监控使用XComponent、NodeContainer、Window、CustomComponent、Ability等组件的应用是否发生泄漏。
* 应用开发调试和测试阶段，快速发现内存泄漏问题。
* 长时间运行的应用，需要定期检测内存泄漏。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否使能ArkTS对象内存泄漏检测功能。true：开启ArkTS内存泄漏检测功能；false：关闭ArkTS内存泄漏检测功能。 |
| configs | Array<string> | 是 | 配置项，数组中每个元素为监测具体对象的类型。  可配置项包括：XComponent，NodeContainer，Window，CustomComponent和Ability。  **说明**：传入空数组代表监测以上全部对象。 |
| callback | Callback<Array<string>> | 是 | 回调函数，用于接收jsLeakWatcher.enableLeakWatcher接口返回的内存泄漏文件列表和虚拟机内存快照文件。  回调函数中传入一个数组对象，索引0为泄漏列表文件名，后缀为.jsleaklist；索引1为虚拟机内存快照文件名，后缀为.rawheap。 |

**错误码：**

以下错误码的详细介绍请参见[JsLeakWatcher错误码](errorcode-jsleakwatcher.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例：**

```ts
let config: Array<string> = ['XComponent'];
// 监测ArkTS对象XComponent的内存泄漏
// 传入空数组代表监测全部对象
jsLeakWatcher.enableLeakWatcher(true, config, (filePath: Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
});
```

## jsLeakWatcher.enableLeakWatcher24+

enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void

使能ArkTS对象泄漏检测。

此接口通过一次调用即可检测ArkTS对象的内存泄漏，比之前需要调用四个函数（enable、watch、check、dump）的方法更加简洁；通过configs可配置项参数，自定义设置监测项各属性，相比较之前极大提升了泄漏检测性能。

**注意** 

当前jsLeakWatcher泄漏检测性能开销较大，会导致应用卡顿，建议增大检测间隔时间，减少卡顿频率。

使用场景：

* 对性能要求较高的应用，需要通过配置检测间隔、阈值等参数来平衡检测精度和性能开销。
* 大型应用或复杂应用，需要精细控制泄漏检测的参数，如检测间隔、泄漏阈值、最大dump数量等。
* 使用特定组件（如CustomComponent、Window、Ability等）的应用，需要针对性监控这些组件的泄漏。
* 对内存管理有严格要求的应用，需要设置过滤规则排除某些不需要监控的对象。
* 长时间运行或需要持续监控的应用，需要合理设置检测间隔和最大保存数量。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否使能ArkTS对象内存泄漏检测功能。  true：开启ArkTS内存泄漏检测功能。  false：关闭ArkTS内存泄漏检测功能。 |
| configs | [LeakWatcherConfig](js-apis-jsleakwatcher.md#leakwatcherconfig24) | 是 | LeakWatcherConfig对象类型，对象中包含多个用于内存泄漏监测的可配置属性。  **说明**：对象中参数类型传入空值或假值代表该属性设置为默认值。 |
| callback | Callback<Array<string>> | 是 | 回调函数，用于接收泄漏检测的导出文件路径。回调函数中传入一个数组对象，索引0为泄漏列表文件名，后缀为.jsleaklist；索引1为虚拟机内存快照文件名，后缀为.rawheap。 |

**错误码：**

以下错误码的详细介绍请参见[JsLeakWatcher错误码](errorcode-jsleakwatcher.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例：**

```ts
// 监测ArkTS对象CustomComponent和Window的内存泄漏
// 对象中类型传入空值或假值代表该属性设置为默认值
let config: jsLeakWatcher.LeakWatcherConfig = {
    monitorObjectTypes: jsLeakWatcher.MonitorObjectType.CUSTOM_COMPONENT | jsLeakWatcher.MonitorObjectType.WINDOW,
    objectUniqueIDs: [],
    checkInterval: 10000,
    fgLeakCountThreshold: 5,
    bgLeakCountThreshold: 3,
    maxStoredHeapDumps: 5,
    dumpHeapWaitTimeMs: 5000,
    exclusionList: []
};
jsLeakWatcher.enableLeakWatcher(true, config, (filePath : Array<string>) => {
    console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
    console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
});
```

## LeakWatcherConfig24+

LeakWatcherConfig对象类型，对象中包含多个用于内存泄漏监测的可配置属性。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| monitorObjectTypes | [MonitorObjectType](js-apis-jsleakwatcher.md#monitorobjecttype24) | 否 | 否 | 被监测对象类型。  默认监测所有组件类型。 |
| objectUniqueIDs | Array<number> | 否 | 是 | 被监测泄漏对象ID列表。  只作用于自定义组件，不会影响其他组件类型的监测。  例如：白名单中设置的对象类名ID与自定义ID列表存在相同值时，生效自定义ID列表参数。  默认为空数组。 |
| checkInterval | number | 否 | 是 | 每轮泄漏检测间隔时间，单位：ms，取值范围为[90000, +∞)。  默认为90000ms。  如果应用输入的自定义检测间隔时间小于默认值，jsLeakWatcher强制将间隔设置为默认值。  当前jsLeakWatcher泄漏检测性能开销较大，会导致应用卡顿，建议增大该参数，减少卡顿频率。  传入不在取值范围内的值时将使用默认值。 |
| fgLeakCountThreshold | number | 否 | 是 | 应用在前台泄漏个数达到设定值触发dump，取值范围为[0, +∞)。  GC/Dump阶段，大于等于5时触发Dump。  阈值默认为5。  传入不在取值范围内的值时将使用默认值。 |
| bgLeakCountThreshold | number | 否 | 是 | 应用在后台泄漏个数达到设定值触发dump，取值范围为[0, +∞)。  GC/Dump阶段，大于等于1时触发Dump。  阈值默认为1。  传入不在取值范围内的值时将使用默认值。 |
| maxStoredHeapDumps | number | 否 | 是 | 最大dump保存个数，取值范围为(0, 10]，避免磁盘空间占满，超过则删除时间戳最小的rawheap、jsleaklist文件。  默认保存10个rawheap、10个jsleaklist文件。  传入不在取值范围内的值时将使用默认值。 |
| dumpHeapWaitTimeMs | number | 否 | 是 | 延迟执行dump，保证GC能调度且执行完再执行dump，延迟间隔小于等于泄漏检测间隔时间，单位：ms，取值范围为[0, +∞)。  设置延迟时长超过泄漏间隔时长则默认与泄漏间隔时长保持一致。  若无新增泄漏对象将不会触发dump。  GC结束后默认延迟5秒执行dump。  传入不在取值范围内的值时将使用默认值。 |
| exclusionList | Array<string> | 否 | 是 | 过滤不想监测的对象类名。  作用于Window、CustomComponent和Ability组件，不会影响其他组件类型的过滤。  存在混淆问题时无法进行过滤，只在开发态生效。  配置项冲突优先级：ID列表 > 白名单。  默认为空数组。 |

## MonitorObjectType24+

需要监控的组件对象类型枚举。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ALL | -1 | 监测所有组件类型。 |
| CUSTOM\_COMPONENT | 1 << 0 | 监测自定义组件类型。 |
| WINDOW | 1 << 1 | 监测Window组件类型。 |
| NODE\_CONTAINER | 1 << 2 | 监测NodeContainer组件类型。 |
| X\_COMPONENT | 1 << 3 | 监测XComponent组件类型。 |
| ABILITY | 1 << 4 | 监测Ability组件类型。 |
