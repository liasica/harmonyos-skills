---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1254
title: 如何通过ArrayBuffer流数据的方式注册全局字体
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何通过ArrayBuffer流数据的方式注册全局字体
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cda8f718120b1a935511ee83799017e2cd0d27ae7d0566f80db399de0fc7fa4
---

## 问题现象

在HarmonyOS中，除了通过font.registerFont接口注册本地的字体文件，是否支持将字体包通过ArrayBuffer流数据的方式进行加载和注册？

## 背景知识

* ArkUI层提供了font.registerFont接口，此种方案可以直接注册本地工程或者Rawfile文件夹中的字体文件，参考[如何加载和使用自定义字体](faqs-arkui-21.md)。
* NAPI层的drawing模块提供了OH\_Drawing\_RegisterFontBuffer接口，支持通过ArrayBuffer流数据的方式注册字体文件，具体接口说明和传参可参考[OH\_Drawing\_RegisterFontBuffer](../harmonyos-references/capi-drawing-register-font-h.md#oh_drawing_registerfontbuffer)。

## 解决方案

1. 从目标字体文件中读取其对应的ArrayBuffer数据，并将该数据传递至NAPI（Native API）层；
2. 在NAPI层通过调用OH\_Drawing\_RegisterFontBuffer接口，完成对该字体数据的注册操作；
3. 在ArkUI框架中调用已注册的字体，实现对应字体的使用与展示。

ArkTS实现：

```ts
import fontNapi from 'libentry.so';

@Entry
@Component
struct Index {
  message: string = 'Hello World';

  aboutToAppear(): void {
    // 此处是模拟的读取本地字体文件后得到ArrayBuffer，实际场景中可以直接传入字体的ArrayBuffer
    const fontName = 'MyCustomFont'; // 自定义字体名称
    const fontPath = 'XXXX.ttf'; // 此处仅为示例，请开发者替换为可用的字体文件。
    const file = this.getUIContext().getHostContext()?.resourceManager.getRawFileContentSync(fontPath);
    fontNapi.registerFontFamily(fontName, file?.buffer);
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Text(this.message)
          .fontFamily('MyCustomFont');
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

NAPI实现：

```cpp
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
 */

#include "napi/native_api.h"
#include "native_drawing/drawing_register_font.h"
#include "native_drawing/drawing_font_collection.h"

static napi_value registerFontFamily(napi_env env, napi_callback_info info) 
{
    // 获取全局字体集对象OH_Drawing_FontCollection
    OH_Drawing_FontCollection *fontCollection = OH_Drawing_GetFontCollectionGlobalInstance();
    size_t argc = 2;
    napi_value args[2];
    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    // 获取字体名称
    char fontName[256];
    size_t fontNameLen;
    napi_get_value_string_utf8(env, args[0], fontName, sizeof(fontName), &fontNameLen);
    // 获取字体的ArrayBuffer数据
    void *bufferData;
    size_t bufferLength;
    napi_get_arraybuffer_info(env, args[1], &bufferData, &bufferLength);
    // 注册字体
    OH_Drawing_RegisterFontBuffer(fontCollection, fontName, reinterpret_cast<uint8_t *>(bufferData), bufferLength);
    return nullptr;
}
EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports) 
{
    napi_property_descriptor desc[] = {
        {"registerFontFamily", nullptr, registerFontFamily, nullptr, nullptr, nullptr, napi_default, nullptr}};
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
    .nm_priv = ((void *)0),
    .reserved = {0},
};
extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
```

Index.d.ts声明：

```ts
export const registerFontFamily: (fontName: string, file: ArrayBuffer) => void;
```

CMakeLists.txt：

```cpp
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.5.0)
project(registerFontBuffer)
set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
if(DEFINED PACKAGE_FIND_FILE)
    include(${PACKAGE_FIND_FILE})
endif()
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include)
add_library(entry SHARED napi_init.cpp)
target_link_libraries(entry PUBLIC libace_napi.z.so libnative_drawing.so)
```

**说明** 

OH\_Drawing\_GetFontCollectionGlobalInstance这个接口是API 14才支持，需要把DevEco Studio和系统版本升级到对应的配套版本上进行使用，DevEco Studio请使用5.0.7.210及以上版本。
