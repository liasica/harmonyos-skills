---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-environmental-life-cycle
title: 使用Node-API接口关联数据，使其生命周期与当前环境的生命周期相关联
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口关联数据，使其生命周期与当前环境的生命周期相关联
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a46cc25fc700ca629741060dd2469d1ec0a6d8f26651018c04285332018ea12
---

## 简介

在Node-API模块中，可以使用Node-API接口将特定数据与当前环境相关联，并在需要时检索该数据。

## 基本概念

在Node-API中，关联数据指的是将自定义的C++数据结构与当前环境的生命周期绑定，这意味着只要当前运行环境存在，关联数据就会保持有效。

## 场景和功能介绍

以下接口可在Node-API模块中更方便地管理对象实例所需的状态信息、引用计数或其他自定义数据，它们的使用场景如下：

| 接口 | 描述 |
| --- | --- |
| napi\_set\_instance\_data | 绑定与当前运行的环境相关联的数据项。 |
| napi\_get\_instance\_data | 检索与当前运行的环境相关联的数据项。 |

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_set\_instance\_data

将需要绑定的数据与当前运行的环境相关联。

cpp部分代码

```
1. #include "napi/native_api.h"

3. // 定义一个结构来存储实例数据
4. struct InstanceData {
5. int32_t value;
6. };

8. // 对象被释放时的回调函数，用于清理实例数据
9. void FinalizeCallback(napi_env env, void *finalizeData, void *finalizeHint)
10. {
11. if (finalizeData) {
12. InstanceData *data = reinterpret_cast<InstanceData *>(finalizeData);
13. // 释放内存，清除指针指向地址
14. delete (data);
15. }
16. }

18. // napi_set_instance_data
19. static napi_value SetInstanceData(napi_env env, napi_callback_info info)
20. {
21. size_t argc = 1;
22. napi_value argv[1];
23. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
24. int32_t instanceDataValue;
25. napi_get_value_int32(env, argv[0], &instanceDataValue);
26. InstanceData *instanceData = new InstanceData;
27. instanceData->value = instanceDataValue;
28. // 调用napi_set_instance_data将实例数据关联到Node-API环境，并指定FinalizeCallback函数
29. napi_status status = napi_set_instance_data(env, instanceData, FinalizeCallback, nullptr);
30. if (status != napi_ok) {
31. delete instanceData;
32. napi_throw_error(env, nullptr, "Test Node-API napi_set_instance_data failed");
33. return nullptr;
34. }
35. bool success = true;
36. napi_value result = nullptr;
37. napi_get_boolean(env, success, &result);
38. return result;
39. }
```

接口声明

```
1. export const setInstanceData: (data: number) => boolean | undefined; // napi_set_instance_data
```

ArkTS侧示例代码

```
1. // napi_set_instance_data
2. let data = 5;
3. let value = testNapi.setInstanceData(data);
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_instance_data:%{public}s', value);
```

### napi\_get\_instance\_data

检索与当前运行的环境相关联的数据项。

cpp部分代码

```
1. // napi_get_instance_data
2. static napi_value GetInstanceData(napi_env env, napi_callback_info info)
3. {
4. InstanceData *resData = nullptr;
5. // napi_get_instance_data获取之前相关联的数据项
6. napi_status status = napi_get_instance_data(env, (void **)&resData);
7. if (status != napi_ok) {
8. return nullptr;
9. }

11. if (resData == nullptr) {
12. napi_throw_error(env, nullptr, "Instance data not set or already freed");
13. return nullptr;
14. }
15. napi_value result = nullptr;
16. napi_create_int32(env, resData->value, &result);
17. return result;
18. }
```

接口声明

```
1. export const getInstanceData: () => number | undefined; // napi_get_instance_data
```

ArkTS侧示例代码

```
1. // napi_get_instance_data
2. let data = 5;
3. testNapi.setInstanceData(data);
4. let value = testNapi.getInstanceData();
5. hilog.info(0x0000, 'testTag', 'Test Node-API napi_set_instance_data:%{public}d', value);
```

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
