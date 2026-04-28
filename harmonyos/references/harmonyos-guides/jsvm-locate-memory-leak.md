---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jsvm-locate-memory-leak
title: JSVM-API 内存泄漏问题定位指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > JSVM-API 内存泄漏问题定位指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6db0a2d7ff309b8bd778c7dee64e6423192c7b735e55238885a3d68d2da323b8
---

JSVM的内存占用包括Native内存占用(C/C++侧的内存占用)和底层的JS引擎的堆内存占用，JS引擎会维护一个堆来管理其生成的JS对象，其生命周期由JS引擎维护，除此之外的内存我们归为Native内存。用户在使用JSVM时，可能碰到这两种内存异常增长的情况。

本文先介绍如何定性分析，然后分两个部分介绍如何定位Native内存泄漏和JS引擎堆内存泄漏。

## 定性分析

可以通过hdc连接设备，执行如下命令行的方式对目标应用的内存进行采样，比较一段时间内的内存变化情况，从而定性分析是Native内存泄漏还是JS内存。下图中Pss Total列，native heap对应Native内存占用，AnonPage other对应js堆内存占用。

```
1. hidumper --mem $(pidof dest_app)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/9ljydue8S4mEP8So0dWFbw/zh-cn_image_0000002552799728.png?HW-CC-KV=V1&HW-CC-Date=20260427T235425Z&HW-CC-Expire=86400&HW-CC-Sign=5F0A85323B2C2F7DE6A6CCC610B2FE870CDAC0AE635EF0606A32B763994904C0)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/QhPGNwVNTFet5FZX-JxKCw/zh-cn_image_0000002583439423.png?HW-CC-KV=V1&HW-CC-Date=20260427T235425Z&HW-CC-Expire=86400&HW-CC-Sign=2F7AF2E18326B8D623AECE2EE8472706779DE08D1666C1FA4F4E5D540778666E)
2. 比较这段时间内"Created & Existing"的内存变化情况，如果存在占比较大且Count较大的未释放内存，则怀疑存在内存泄漏，展开进一步查看调用栈。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/5Wm4PPwLRS6W-CEB5VhNYQ/zh-cn_image_0000002552959378.png?HW-CC-KV=V1&HW-CC-Date=20260427T235425Z&HW-CC-Expire=86400&HW-CC-Sign=5C73ECA3CBE8D735A9281DD54A7ED55673DF8EAF939C63837906C21B2F4BD19E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/3FeSuilxSVCdcgkDSgETvQ/zh-cn_image_0000002583479379.png?HW-CC-KV=V1&HW-CC-Date=20260427T235425Z&HW-CC-Expire=86400&HW-CC-Sign=F3ED0934D9E19F3814B3E7BAEDC6279E8EC8676E649B408A84CE4042728B8101)
