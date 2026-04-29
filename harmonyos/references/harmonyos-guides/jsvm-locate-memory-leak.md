---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-locate-memory-leak
title: JSVM-API 内存泄漏问题定位指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API 内存泄漏问题定位指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0129c52b423f64a85249ec147777ee6d873d41eb1e56a9dcdc60226cf10f5176
---

JSVM的内存占用包括Native内存占用(C/C++侧的内存占用)和底层的JS引擎的堆内存占用，JS引擎会维护一个堆来管理其生成的JS对象，其生命周期由JS引擎维护，除此之外的内存我们归为Native内存。用户在使用JSVM时，可能碰到这两种内存异常增长的情况。

本文先介绍如何定性分析，然后分两个部分介绍如何定位Native内存泄漏和JS引擎堆内存泄漏。

## 定性分析

可以通过hdc连接设备，执行如下命令行的方式对目标应用的内存进行采样，比较一段时间内的内存变化情况，从而定性分析是Native内存泄漏还是JS内存。下图中Pss Total列，native heap对应Native内存占用，AnonPage other对应js堆内存占用。

```
1. hidumper --mem $(pidof dest_app)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/KyCFY9w9Tv6jV-vgK0B1xw/zh-cn_image_0000002558606222.png?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=E25741625503FDAA6B8FBC6AA06C91B025D1E1CE8ADAED2F8DBFFE6B7EA9C59C)

## Native内存泄漏定位

### 典型场景

1. OH\_JSVM\_CreateReference 和 OH\_JSVM\_DeleteReference 接口没有成对调用，导致Reference没有被释放。

```
1. JSVM_Value obj = nullptr;
2. OH_JSVM_CreateObject(env, &obj);
3. // 创建引用
4. JSVM_Ref reference;
5. OH_JSVM_CreateReference(env, obj, 1, &reference);

7. // 使用引用
8. JSVM_Value result;
9. OH_JSVM_GetReferenceValue(env, reference, &result);

11. // 未释放引用
12. // OH_JSVM_DeleteReference(env, reference);
```

### 定位步骤

为了分析Native内存泄漏，可以借助DevEco Studio的内存分析模块，具体参考文档：[内存分析及优化](ide-insight-session-allocations-memory.md)。

1. 使用Profiler的Allocation模块记录一段时间内的Native内存信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/1Kkyy3mNQh64VQJf6js_Qw/zh-cn_image_0000002589325749.png?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=357167A2905796AD54BA64BC23E58D3FEF16C7B7A28536FCC75CC71F3EB38364)
2. 比较这段时间内"Created & Existing"的内存变化情况，如果存在占比较大且Count较大的未释放内存，则怀疑存在内存泄漏，展开进一步查看调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/7zs47NJKQLy5QRv3Eh2ZNg/zh-cn_image_0000002589245689.png?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=68FF85291E40D94433D1BD347F727669CDCD1621F63E49038379B1525DE19AFA)

## JS引擎堆内存泄漏定位

### 典型场景

1. 全局变量滥用，导致DOM元素未释放。

```
1. const elements = [];
2. function createElements() {
3. for (let i = 0; i < 1000; i++) {
4. const el = document.createElement('div');
5. document.body.appendChild(el);
6. elements.push(el); // 即使从 DOM 移除，数组仍保留引用
7. }
8. }
```

### 定位步骤

JSVM目前提供了OH\_JSVM\_OpenInspector开启inspector，参考[使用OH\_JSVM\_OpenInspector](jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-oh_jsvm_openinspector),在此基础上可以[使用 Chrome inspect 页面进行调试](jsvm-debugger-cpuprofiler-heapsnapshot.md#使用-chrome-inspect-页面进行调试)。

通过使用DevTools工具，对目标场景内的堆内存进行快照（快照前先点击上方的垃圾回收按钮进行垃圾回收），利用快照对比功能，找到未释放的JS对象和其所在源码中的位置，进一步指导定位堆内存未释放的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/0cyW7iIdS8OaA00XwMPGdg/zh-cn_image_0000002558765880.png?HW-CC-KV=V1&HW-CC-Date=20260429T054421Z&HW-CC-Expire=86400&HW-CC-Sign=D1E0CBC6944CE09EF6173DB02911667E62EDDFCECAF7264A565A0C4BD8A98426)
