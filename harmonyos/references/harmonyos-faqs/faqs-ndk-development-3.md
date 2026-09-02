---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-3
title: 如何解决napi_create_bool无法创建C++的bool类型
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何解决napi_create_bool无法创建C++的bool类型
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd2c4989826b4d97ccada9f665d553334c464507aed36b5ebc55e566cfe8f5ac
---

## 问题现象

Node-API提供了一批接口帮助把标准数据类型转为napi\_value，比如napi\_create\_double、napi\_create\_int32等等，但是napi\_create\_bool无法创建bool类型并转换为napi\_value。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/rRZf_4i7Rci9hIXCD5VqiA/zh-cn_image_0000002628899078.png "点击放大")

## 背景知识

HarmonyOS Node-API是基于Node.js 10.x LTS的[Node-API](https://nodejs.org/docs/latest-v10.x/api/n-api.html)规范扩展开发的机制，为开发者提供了ArkTS/JS与C/C++模块之间的交互能力。它提供了一组稳定的、跨平台的API，可以在不同的操作系统上使用。一般情况下HarmonyOS应用开发使用ArkTS/JS语言，但部分场景由于性能、效率等要求，比如游戏、物理模拟等，需要依赖使用现有的C/C++库。Node-API规范封装了I/O、CPU密集型、OS底层等能力并对外暴露ArkTS/JS接口，从而实现ArkTS/JS和C/C++的交互。

## 问题定位

Node-API提供了专用接口napi\_get\_boolean用于将bool类型的值转换为napi\_value类型。

## 分析结论

未使用Node-API专用接口导致了无法正常获取native侧的bool值。

## 修改建议

使用napi\_get\_boolean即实现将C++中的bool类型转换为napi，参考代码如下：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
#include "napi/native_api.h"

bool  GetExcuteResult()
{
    return true;
}

static napi_value BooleanJudge(napi_env env, napi_callback_info info)
{
    bool value = GetExcuteResult();
    napi_value jsResult;
    napi_get_boolean(env, value, &jsResult);
    return jsResult;

}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        { "booleanJudge", nullptr, BooleanJudge, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&demoModule);
}
```

**说明** 

napi\_get\_boolean的函数定义：根据给定的C中的boolean值，获取js中的bool对象。

## 总结

对于C++语言可以借助Node-API功能实现跨语言交互，官方参考链接：HarmonyOS的napi接口参考了[Node.js文档](https://nodejs.org/docs/latest/api/n-api.html#napi_get_boolean)。
