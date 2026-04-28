---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-trigger-gc
title: 使用JSVM-API感知JSVM引擎生命周期管理
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API感知JSVM引擎生命周期管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:03a122913375f12c1bebd1d7c07c770c05da02a20a88abaa333fc39480f2fccc
---

## 简介

JSVM-API提供了注册回调函数的能力，用于监测JavaScript虚拟机的内存GC。开发者可以在垃圾回收前后添加自定义逻辑，从而在垃圾回收时执行优化、调试或性能监控操作。

## 基本概念

在JavaScript中，内存的垃圾回收是自动进行的，用户并不直接感知JavaScript虚拟机的GC行为。每次GC执行之前，JS引擎会先进入一个"Prologue"阶段。每次GC执行之后，JS引擎会进入一个"Epilogue"阶段。"Prologue"阶段是GC的初始阶段，主要目标是做一些准备工作，以确保垃圾回收能够顺利进行。"Epilogue"阶段则是垃圾回收的最终清理和整理，确保内存恢复到一个正常的状态，并为下一次分配做好准备。在这两个阶段，JS引擎会分别调用用户提前注册的函数。用户可以在"Prologue"阶段所执行的注册函数中暂停某些任务、记录内存使用情况、执行性能调优等。在"Epilogue"阶段所执行的注册函数中，也可以去记录GC后的内存状态、启动后续的任务等等。

JSVM-API提供了OH\_JSVM\_AddHandlerForGC接口，可以在VM中注册回调函数。通过传入JSVM\_CB\_TRIGGER\_BEFORE\_GC来控制回调函数在"Prologue"阶段执行；通过传入JSVM\_CB\_TRIGGER\_AFTER\_GC来控制回调函数在"Epilogue"阶段执行。通过OH\_JSVM\_RemoveHandlerForGC，可以从VM中移除注册过的回调函数。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_AddHandlerForGC | 用于向VM中注册回调函数 |
| OH\_JSVM\_RemoveHandlerForGC | 用于从VM中移除注册过的回调函数 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### OH\_JSVM\_AddHandlerForGC & OH\_JSVM\_RemoveHandlerForGC

可以多次调用OH\_JSVM\_AddHandlerForGC向VM注册回调函数，所有注册的回调函数都会生效。注册时，以回调函数指针和native-data作为键。如果多次注册存在相同的键，则视为无效注册，并返回JSVM\_INVALID\_ARG错误码。在相同触发条件下，回调函数的回调顺序与注册顺序不严格一致。

通过OH\_JSVM\_RemoveHandlerForGC可以从VM中移除注册过的回调函数。重复移除具有相同key的回调函数，则会判定为无效移除，并返回JSVM\_INVALID\_ARG错误码。

**cpp部分代码**

```
1. // hello.cpp
2. #include <iostream>

4. static bool before_flag1 = false;
5. static bool before_flag2 = false;
6. static bool after_flag1 = false;
7. static bool after_flag2 = false;

9. void OnBeforeGC(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void *data)
10. {
11. OH_LOG_INFO(LOG_APP, "== before GC ==");
12. OH_LOG_INFO(LOG_APP, "gc type: %{public}d", gcType);
13. OH_LOG_INFO(LOG_APP, "gc flag: %{public}d", flags);
14. before_flag1 = true;
15. }

17. void OnBeforeGC2(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void *data)
18. {
19. OH_LOG_INFO(LOG_APP, "== before GC2 ==");
20. OH_LOG_INFO(LOG_APP, "gc type: %{public}d", gcType);
21. OH_LOG_INFO(LOG_APP, "gc flag: %{public}d", flags);
22. OH_LOG_INFO(LOG_APP, "data: %{public}d", *(int*)data);
23. if (*(int*)data == 2024) {
24. before_flag2 = true;
25. }
26. }

28. void OnAfterGC(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void *data)
29. {
30. after_flag1 = true;
31. }

33. void OnAfterGC2(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void *data)
34. {
35. after_flag2 = true;
36. }

38. void OnAfterGC3(JSVM_VM vm, JSVM_GCType gcType, JSVM_GCCallbackFlags flags, void *data)
39. {
40. after_flag2 = true;
41. }

43. static JSVM_Value TriggerGC(JSVM_Env env, JSVM_CallbackInfo info)
44. {
45. bool remove_repeated = false;
46. bool remove_notAdded = false;
47. bool add_repeated = false;
48. before_flag1 = false;
49. before_flag2 = false;
50. after_flag1 = false;
51. after_flag2 = false;
52. JSVM_VM vm;
53. OH_JSVM_GetVM(env, &vm);
54. // 设置两个回调函数，在GC执行之前触发回调
55. int data = 2024;
56. JSVM_CALL(OH_JSVM_AddHandlerForGC(vm, JSVM_CB_TRIGGER_BEFORE_GC, OnBeforeGC, JSVM_GC_TYPE_ALL, NULL));
57. JSVM_CALL(OH_JSVM_AddHandlerForGC(vm, JSVM_CB_TRIGGER_BEFORE_GC, OnBeforeGC2, JSVM_GC_TYPE_ALL, (void*)(&data)));
58. // 设置两个回调函数，在GC执行之后触发回调
59. JSVM_CALL(OH_JSVM_AddHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC, JSVM_GC_TYPE_ALL, NULL));
60. JSVM_CALL(OH_JSVM_AddHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC2, JSVM_GC_TYPE_ALL, NULL));
61. // (OnAfterGC2, NULL)的组合已经注册过了，重复注册为无效行为
62. if (OH_JSVM_AddHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC2, JSVM_GC_TYPE_ALL, NULL) == JSVM_INVALID_ARG) {
63. add_repeated = true;
64. }
65. // 移除OnAfter2回调函数
66. JSVM_CALL(OH_JSVM_RemoveHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC2, NULL));
67. // 重复移除OnAfter2属于无效用法
68. if (OH_JSVM_RemoveHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC2, NULL) == JSVM_INVALID_ARG) {
69. remove_repeated = true;
70. }
71. // 移除从未设置过的函数属于无效用法
72. if (OH_JSVM_RemoveHandlerForGC(vm, JSVM_CB_TRIGGER_AFTER_GC, OnAfterGC3, NULL) == JSVM_INVALID_ARG) {
73. remove_notAdded = true;
74. }
75. // 通知引擎当前存在比较大的内存压力，能大概率触发JS引擎的GC流程。
76. JSVM_CALL(OH_JSVM_MemoryPressureNotification(env, JSVM_MEMORY_PRESSURE_LEVEL_CRITICAL));
77. if ((before_flag1) &&
78. (before_flag2) &&
79. (after_flag1) &&
80. (!after_flag2) &&
81. (remove_repeated) &&
82. (remove_notAdded) &&
83. (add_repeated)) {
84. OH_LOG_INFO(LOG_APP, "JSVM Trigger GC: success");
85. } else {
86. OH_LOG_ERROR(LOG_APP, "JSVM Trigger GC: failed");
87. }
88. JSVM_Value checked;
89. OH_JSVM_GetBoolean(env, true, &checked);
90. return checked;
91. }

93. static JSVM_CallbackStruct param[] = {
94. {.data = nullptr, .callback = TriggerGC},
95. };
96. static JSVM_CallbackStruct *method = param;

98. static JSVM_PropertyDescriptor descriptor[] = {
99. {"triggerGC", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
100. };
```

**样例测试JS**

```
1. const char *srcCallNative = R"JS(triggerGC();)JS";
```

**执行结果**

在LOG中输出下面结果：

```
1. == before GC ==
2. gc type: 4
3. gc flag: 4
4. == before GC2 ==
5. gc type: 4
6. gc flag: 4
7. data: 2024
8. JSVM Trigger GC: success
```
