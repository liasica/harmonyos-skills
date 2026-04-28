---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-private
title: 使用JSVM-API接口进行private相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用JSVM-API实现JS与C/C++语言交互 > JSVM-API使用指导 > 使用JSVM-API接口进行private相关开发
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:11dd89a228b03c885c17328563ac8c5600a457ab3a3dd86075af27f22b516e6a
---

## 简介

JSVM-API 提供操作私有属性的接口。

## 基本概念

JSVM-API提供创建private key的能力，并支持在对象上使用该key进行属性的创建与删除，同时持久化保存private key symbol。

## 接口说明

| 接口 | 功能说明 |
| --- | --- |
| OH\_JSVM\_CreateDataReference | 在JSVM中创建一个带有指定引用计数的数据引用。 |
| OH\_JSVM\_GetReferenceData | 检查指定的引用是否有效, 返回该引用关联的JavaScript数据, 无效result设置为NULL。 |
| OH\_JSVM\_CreatePrivate | 创建一个js private key对象。 |
| OH\_JSVM\_SetPrivate | 为传入的object设置一个private属性。 |
| OH\_JSVM\_GetPrivate | 获取传入的object中private key对应的private属性。 |
| OH\_JSVM\_DeletePrivate | 删除传入的object中private key对应的private属性。 |

## 使用示例

JSVM-API接口开发流程参考[使用JSVM-API实现JS与C/C++语言交互开发流程](use-jsvm-process.md)，本文仅对接口对应C++相关代码进行展示。

### 使用接口创建 private key 并添加对应 private property，随后删除

cpp部分代码

```
1. static JSVM_Value privateTest(JSVM_Env env, JSVM_CallbackInfo info) {
2. JSVM_VM vm;
3. JSVM_HandleScope outerScope;
4. OH_JSVM_GetVM(env, &vm);
5. OH_JSVM_OpenHandleScope(env, &outerScope);

7. JSVM_HandleScope handleScope;
8. JSVM_Data privateKey;
9. JSVM_Value object;
10. JSVM_Value property;
11. JSVM_Ref privateRef;
12. {
13. OH_JSVM_OpenHandleScope(env, &handleScope);
14. OH_JSVM_CreateObject(env, &object);
15. OH_JSVM_CreatePrivate(env, nullptr, &privateKey);
16. OH_JSVM_CreateInt32(env, 1, &property);
17. OH_JSVM_SetPrivate(env, object, privateKey, property);
18. OH_JSVM_GetPrivate(env, object, privateKey, &property);
19. int propertyValue = 0;
20. OH_JSVM_GetValueInt32(env, property, &propertyValue);
21. OH_LOG_INFO(LOG_APP, "private property set: %{public}d\n", propertyValue);
22. OH_JSVM_DeletePrivate(env, object, privateKey);
23. OH_JSVM_GetPrivate(env, object, privateKey, &property);
24. bool isUndefined = false;
25. OH_JSVM_IsUndefined(env, property, &isUndefined);
26. OH_LOG_INFO(LOG_APP, "private property deleted is undefined: %{public}d\n", isUndefined);
27. OH_JSVM_CreateDataReference(env, privateKey, 1, &privateRef);
28. OH_JSVM_CloseHandleScope(env, handleScope);
29. }
30. {
31. OH_JSVM_OpenHandleScope(env, &handleScope);
32. OH_JSVM_GetReferenceData(env, privateRef, &privateKey);
33. OH_JSVM_CreateObject(env, &object);
34. OH_JSVM_CreateInt32(env, 2, &property);
35. OH_JSVM_SetPrivate(env, object, privateKey, property);
36. OH_JSVM_GetPrivate(env, object, privateKey, &property);
37. int propertyValue = 0;
38. OH_JSVM_GetValueInt32(env, property, &propertyValue);
39. OH_LOG_INFO(LOG_APP, "second private property set: %{public}d\n", propertyValue);
40. OH_JSVM_CloseHandleScope(env, handleScope);
41. }

43. OH_JSVM_CloseHandleScope(env, outerScope);
44. return nullptr;
45. }

47. static JSVM_CallbackStruct param[] = {
48. {.data = nullptr, .callback = privateTest},
49. };

51. static JSVM_CallbackStruct *method = param;

53. // wrapperObject方法别名，供JS调用
54. static JSVM_PropertyDescriptor descriptor[] = {
55. {"privateTest", nullptr, method++, nullptr, nullptr, nullptr, JSVM_DEFAULT},
56. };

58. // 样例测试JS
59. const char *srcCallNative = R"JS(privateTest();)JS";
```

## 预期输出结果

```
1. private property set: 1
2. private property deleted is undefined: 1
3. second private property set: 2
```
