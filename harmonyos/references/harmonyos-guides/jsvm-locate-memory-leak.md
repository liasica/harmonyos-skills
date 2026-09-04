---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-locate-memory-leak
title: JSVM 定位内存泄漏问题指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM 定位内存泄漏问题指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3a2470134ad4866eec7b95ee691f682ef4cb744eae3cdeb1b413985e34d1bc04
---

JSVM的内存占用包括Native内存占用(C/C++侧的内存占用)和底层的JS引擎的堆内存占用，JS引擎会维护一个堆来管理其生成的JS对象，其生命周期由JS引擎维护，除此之外的内存我们归为Native内存。用户在使用JSVM时，可能碰到这两种内存异常增长的情况。

本文先介绍如何定性分析，然后分两个部分介绍如何定位Native内存泄漏和JS引擎堆内存泄漏。

## 定性分析

可以通过hdc连接设备，执行如下命令行的方式对目标应用的内存进行采样，比较一段时间内的内存变化情况，从而定性分析是Native内存泄漏，还是JS堆内存异常增长。下图中Pss Total列，native heap对应Native内存占用，AnonPage other对应js堆内存占用。

```hdc
hidumper --mem $(pidof dest_app)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/EWx-LmhtTFygf8aRKDL7fQ/zh-cn_image_0000002712405660.png)

## Native内存泄漏定位

### 典型场景

1. OH\_JSVM\_CreateReference 和 OH\_JSVM\_DeleteReference 接口没有成对调用，导致Reference没有被释放。

```
JSVM_Value obj = nullptr;
OH_JSVM_CreateObject(env, &obj);
// 创建引用
JSVM_Ref reference;
OH_JSVM_CreateReference(env, obj, 1, &reference);

// 使用引用
JSVM_Value result;
OH_JSVM_GetReferenceValue(env, reference, &result);

// 未释放引用
// OH_JSVM_DeleteReference(env, reference);
```

### 定位步骤

为了分析Native内存泄漏，可以借助DevEco Studio的内存分析模块，具体参考文档：[内存分析及优化](ide-insight-session-allocations-memory.md)。

1. 使用Profiler的Allocation模块记录一段时间内的Native内存信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/VREqKBnOSg6it4ooE40q9w/zh-cn_image_0000002742124609.png)
2. 比较这段时间内"Created & Existing"的内存变化情况，如果存在占比较大且Count较大的未释放内存，则怀疑存在内存泄漏，展开进一步查看调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/wKiT4wRgTRCq-IWUEhkStw/zh-cn_image_0000002712245702.png)

## JS引擎堆内存泄漏定位

### 典型场景

1. 全局变量滥用，导致DOM元素未释放。

```js
const elements = [];
function createElements() {
  for (let i = 0; i < 1000; i++) {
    const el = document.createElement('div');
    document.body.appendChild(el);
    elements.push(el); // 即使从 DOM 移除，数组仍保留引用
  }
}
```

### 定位步骤

JSVM目前提供了OH\_JSVM\_OpenInspector开启inspector，参考[使用OH\_JSVM\_OpenInspector](jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-oh_jsvm_openinspector)，在此基础上可以[使用 Chrome inspect 页面进行调试](jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-chrome-inspect-页面进行调试)。

通过使用DevTools工具，对目标场景内的堆内存进行快照（快照前先点击上方的垃圾回收按钮进行垃圾回收），利用快照对比功能，找到未释放的JS对象和其所在源码中的位置，进一步指导定位堆内存未释放的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/Rp8t5mt1TxGV_97WeZAmhQ/zh-cn_image_0000002742004651.png)
