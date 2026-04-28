---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher
title: @ohos.hiviewdfx.jsLeakWatcher (ArkTS泄漏检测)
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hiviewdfx.jsLeakWatcher (ArkTS泄漏检测)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:18+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:63ba216a4012d1e1ec9329009f26d666e6159be0d5bd8f0c23a011eb7d1c29ed
---

本模块提供了监控ArkTS对象是否发生泄漏的能力。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { jsLeakWatcher } from '@kit.PerformanceAnalysisKit';
```

## jsLeakWatcher.enable

PhonePC/2in1TabletTVWearable

enable(isEnable: boolean): void

使能ArkTS对象泄漏检测，默认关闭。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnable | boolean | 是 | 是否使能jsLeakWatcher。true：使能jsLeakWatcher；false：不使能jsLeakWatcher。 |

**示例：**

```
1. jsLeakWatcher.enable(true);
```

## jsLeakWatcher.watch

PhonePC/2in1TabletTVWearable

watch(obj: object, msg: string): void

注册待检测泄漏的对象。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | object | 是 | 需要检测的对象名。  **说明**：可传入任何类型对象。 |
| msg | string | 是 | 自定义对象信息。 |

**示例：**

```
1. let obj:Object = new Object();
2. jsLeakWatcher.watch(obj, "Trace Object");
```

## jsLeakWatcher.check

PhonePC/2in1TabletTVWearable

check(): string

获取已通过jsLeakWatcher.watch注册发生泄漏的对象列表，触发GC后未被回收的对象会被标记为泄漏。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 触发GC后未被回收的泄漏对象列表。  **说明**：check成功，返回JSON格式的泄漏对象列表；check失败，返回空字符串。 |

**示例：**

```
1. let leakObjlist:string = jsLeakWatcher.check();
```

## jsLeakWatcher.dump

PhonePC/2in1TabletTVWearable

dump(filePath: string): Array<string>

导出泄漏列表和虚拟机内存快照。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 导出信息生成的文件存放的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 导出结果。分别为文件名后缀为.jsleaklist的泄漏列表和文件名后缀为.heapsnapshot虚拟机内存快照文件。  **说明**：dump成功，返回泄漏列表文件路径和虚拟机内存快照路径；dump失败，返回空数组。 |

**示例：**

```
1. let context = this.getUIContext().getHostContext();
2. let files: Array<string> = jsLeakWatcher.dump(context?.filesDir);
```

## jsLeakWatcher.enableLeakWatcher20+

PhonePC/2in1TabletTVWearable

enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void

使能ArkTS对象泄漏检测。

此接口通过一次调用即可检测ArkTS对象的内存泄漏，比之前需要调用四个函数（enable、watch、check、dump）的方法更加简洁。

**系统能力**：SystemCapability.HiviewDFX.HiChecker

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEnabled | boolean | 是 | 是否使能ArkTS对象内存泄漏检测功能。true：开启ArkTS内存泄漏检测功能；false：关闭ArkTS内存泄漏检测功能。 |
| configs | Array<string> | 是 | 配置项，数组中每个元素为监测具体对象的类型。  可配置项包括：XComponent，NodeContainer，Window，CustomComponent和Ability。  **说明**：传入空数组代表监测以上全部对象。 |
| callback | Callback<Array<string>> | 是 | 回调函数，用于接收jsLeakWatcher.enableLeakWatcher接口的返回的内存泄漏的对象。  回调函数中传入一个数组对象，索引0为泄漏列表文件名，后缀为.jsleaklist；索引1为虚拟机内存快照文件名，后缀为.rawheap。 |

**错误码：**

以下错误码的详细介绍请参见[JsLeakWatcher错误码](errorcode-jsleakwatcher.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10801001 | The parameter isEnabled is invalid. |
| 10801002 | The parameter config is invalid. |
| 10801003 | The parameter callback is invalid. Input parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

**示例：**

```
1. let config: Array<string> = ['XComponent'];
2. // 监测ArkTS对象XComponent的内存泄漏
3. // 传入空数组代表监测全部对象
4. jsLeakWatcher.enableLeakWatcher(true, config, (filePath: Array<string>) => {
5. console.info('JsLeakWatcher leaklistFileName:' + filePath[0]);
6. console.info('JsLeakWatcher heapDumpFileName:' + filePath[1]);
7. });
```
