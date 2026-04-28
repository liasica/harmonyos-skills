---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-proxy
title: 使用JSVM-API提供的proxy接口
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API提供的proxy接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:24+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:46f5d1402bb4793ee6ba8daea4f3d76a5c18e378abdd7242c49180cd3c0f6bd6
---

## 简介

JSVM-API 提供了创建 Proxy、判断 JSVM\_Value 是否为 Proxy 类型和获取 Proxy 中的目标对象的接口。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateProxy | 创建 Proxy，等价于在 js 中执行 new Proxy(target, handler) |
| OH\_JSVM\_IsProxy | 判断传入的 JSVM\_Value 是否为 Proxy 类型 |
| OH\_JSVM\_ProxyGetTarget | 获取给定 proxy 的目标对象 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅展示接口对应的C++相关代码。

cpp 部分代码

```
1. // OH_JSVM_CreateProxy 的样例方法
2. static JSVM_Value CreateProxy(JSVM_Env env, JSVM_CallbackInfo info) {
3. // 接受两个入参，第 1 个参数为 target，第 2 个参数为 handler
4. size_t argc = 2;
5. JSVM_Value args[2] = {nullptr};
6. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
7. // 用 OH_JSVM_CreateProxy 为目标对象创建代理
8. JSVM_Value result = nullptr;
9. JSVM_Status status = OH_JSVM_CreateProxy(env, args[0], args[1], &result);
10. if (status != JSVM_OK) {
11. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_CreateProxy: failed: %{public}d", status);
12. } else {
13. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_CreateProxy: success");
14. }

16. return result;
17. }

19. // OH_JSVM_IsProxy 的样例方法
20. static JSVM_Value IsProxy(JSVM_Env env, JSVM_CallbackInfo info) {
21. size_t argc = 1;
22. JSVM_Value args[1] = {nullptr};
23. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
24. // 调用 OH_JSVM_IsProxy 判断 JSVM_Value 是否为代理
25. bool result = false;
26. JSVM_Status status = OH_JSVM_IsProxy(env, args[0], &result);
27. if (status != JSVM_OK) {
28. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_IsProxy: failed");
29. } else {
30. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_IsProxy: success: %{public}s", result ? "is a proxy" : "is not a proxy");
31. }
32. JSVM_Value isProxy;
33. JSVM_CALL(OH_JSVM_GetBoolean(env, result, &isProxy));
34. return isProxy;
35. }

37. // OH_JSVM_ProxyGetTarget 的样例方法
38. static JSVM_Value GetProxyTarget(JSVM_Env env, JSVM_CallbackInfo info) {
39. size_t argc = 1;
40. JSVM_Value args[1] = {nullptr};
41. JSVM_CALL(OH_JSVM_GetCbInfo(env, info, &argc, args, nullptr, nullptr));
42. // 调用 OH_JSVM_ProxyGetTarget 获取代理中的目标对象
43. JSVM_Value result = nullptr;
44. JSVM_Status status = OH_JSVM_ProxyGetTarget(env, args[0], &result);
45. if (status != JSVM_OK) {
46. OH_LOG_ERROR(LOG_APP, "JSVM OH_JSVM_ProxyGetTarget: failed");
47. } else {
48. OH_LOG_INFO(LOG_APP, "JSVM OH_JSVM_ProxyGetTarget: success");
49. }

51. return result;
52. }

54. // Proxy 相关回调注册
55. static JSVM_CallbackStruct param[] = {{.data = nullptr, .callback = CreateProxy},
56. {.data = nullptr, .callback = IsProxy},
57. {.data = nullptr, .callback = GetProxyTarget}};
58. static JSVM_CallbackStruct *method = param;
59. // Proxy 相关回调别名
60. static JSVM_PropertyDescriptor descriptor[] = {
61. {"CreateProxy", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
62. {"IsProxy", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
63. {"GetProxyTarget", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT}};

65. const char *srcCallNative = R"JS(
66. target = {
67. message1: "hello",
68. message2: "everyone",
69. };

71. handler = {
72. get(target, prop, receiver) {
73. return "world";
74. },
75. };

77. proxy = CreateProxy(target, handler)
78. isProxy = IsProxy(proxy)
79. target1 = GetProxyTarget(proxy)
80. )JS";
```

预期的输出结果

```
1. JSVM OH_JSVM_CreateProxy: success
2. JSVM OH_JSVM_IsProxy: success: is a proxy
3. JSVM OH_JSVM_ProxyGetTarget: success
```
