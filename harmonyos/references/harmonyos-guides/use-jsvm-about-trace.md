---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-trace
title: 使用JSVM-API接口进行Trace相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API典型使用场景指导 > 使用JSVM-API接口进行Trace相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:25+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:788f3cb7260181f9b0096ada0a34729bf1e983354ac55b27cb17b055623de149
---

## 简介

JSVM-API中trace相关接口用于在运行时采集并输出各种类型运行时信息。该能力可用于在JSVM模块中定位问题与性能分析。

## 基本概念

JSVM-API中的Trace相关接口能够通过指定一系列分类，采集这些分类所属的JSVM内部事件信息，并以JSON格式通过用户指定的回调函数输出。

在JSVM-API中，通过支持Trace相关能力，JSVM模块能够更紧密地与JavaScript环境集成，提高复杂问题定位和性能分析能力。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_TraceStart | 以指定事件类型与事件数量限制，开始采集运行时信息。 |
| OH\_JSVM\_TraceStop | 停止采集信息，并以JSON格式在用户指定的回调函数中进行输出。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### 使用Trace接口进行数据采集

cpp 部分代码：

```
1. #include <vector>
2. #include <string>

4. bool OutputStream(const char *data, int size, void *streamData) {
5. std::string value(data, size);
6. *(std::string *)streamData = std::string(data, size);
7. return true;
8. }

10. // OH_JSVM_TraceStart/OH_JSVM_TraceStop样例方法
11. static JSVM_Value Trace(JSVM_Env env, JSVM_CallbackInfo info) {
12. // start trace with categories
13. std::vector<JSVM_TraceCategory> categories = {JSVM_TRACE_VM};
14. JSVM_CALL(OH_JSVM_TraceStart(categories.size(), categories.data(), "trace test", 0));

16. // run and trace
17. JSVM_Script script;
18. JSVM_Value jsSrc;
19. JSVM_Value result;
20. const char* trace_js = R"JS(
21. function map(x, y) {
22. return {"a": x, "b": y};
23. }
24. for (var i = 0; i < 80000; ++i) {
25. var x = map(i, i);
26. }
27. )JS";
28. JSVM_CALL(OH_JSVM_CreateStringUtf8(env, trace_js, JSVM_AUTO_LENGTH, &jsSrc));
29. JSVM_CALL(OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script));
30. JSVM_CALL(OH_JSVM_RunScript(env, script, &result));

32. // stop trace and write file
33. std::string data;
34. JSVM_CALL(OH_JSVM_TraceStop(OutputStream, (void *)&data));

36. OH_LOG_INFO(LOG_APP, "JSVM Trace success:%{public}s", data.c_str());
37. return nullptr;
38. }
39. // Trace注册回调
40. static JSVM_CallbackStruct param[] = {
41. {.data = nullptr, .callback = Trace},
42. };
43. static JSVM_CallbackStruct *method = param;
44. // Trace方法别名，供JS调用
45. static JSVM_PropertyDescriptor descriptor[] = {
46. {"trace", nullptr, method, nullptr, nullptr, nullptr, JSVM_DEFAULT},
47. };
48. // 样例测试js
49. const char *srcCallNative = R"JS(trace())JS";
```

预计的输出结果:

```
1. JSVM Trace success:{"trace test":[{"pid":54485,"tid":54485,"ts":341364468711,"tts":139452,"ph":"B","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeBefore":1592824,"type":"allocation failure"}},{"pid":54485,"tid":54485,"ts":341364468727,"tts":139463,"ph":"X","cat":"v8","name":"V8.GCScavenger","dur":203,"tdur":203,"args":{}},{"pid":54485,"tid":54485,"ts":341364468949,"tts":139684,"ph":"E","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeAfter":173472}},{"pid":54485,"tid":54485,"ts":341364471055,"tts":141792,"ph":"B","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeBefore":1208672,"type":"allocation failure"}},{"pid":54485,"tid":54485,"ts":341364471060,"tts":141796,"ph":"X","cat":"v8","name":"V8.GCScavenger","dur":110,"tdur":110,"args":{}},{"pid":54485,"tid":54485,"ts":341364471182,"tts":141918,"ph":"E","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeAfter":173472}},{"pid":54485,"tid":54485,"ts":341364472901,"tts":143638,"ph":"B","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeBefore":1221944,"type":"allocation failure"}},{"pid":54485,"tid":54485,"ts":341364472905,"tts":143641,"ph":"X","cat":"v8","name":"V8.GCScavenger","dur":26,"tdur":26,"args":{}},{"pid":54485,"tid":54485,"ts":341364472940,"tts":143675,"ph":"E","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeAfter":173472}},{"pid":54485,"tid":54485,"ts":341364474583,"tts":145319,"ph":"B","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeBefore":1221944,"type":"allocation failure"}},{"pid":54485,"tid":54485,"ts":341364474585,"tts":145321,"ph":"X","cat":"v8","name":"V8.GCScavenger","dur":17,"tdur":16,"args":{}},{"pid":54485,"tid":54485,"ts":341364474608,"tts":145343,"ph":"E","cat":"devtools.timeline,v8","name":"MinorGC","dur":0,"tdur":0,"args":{"usedHeapSizeAfter":173472}}]}
```

注：用户运行demo输出的结果不一定与给出参考结果相等，id的分配方式和用户环境相关
