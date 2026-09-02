---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-14
title: C++侧使用ArrayBuffer接收Float数组时异常
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > C++侧使用ArrayBuffer接收Float数组时异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fab320a06cd32ff167001e69907050dd1f22ac102395c708270ec76dabcf5f75
---

## 问题现象

C++端要如何接收number[]数组，数组里保存的是Float类型，使用[napi\_get\_arraybuffer\_info](../harmonyos-guides/use-napi-about-arraybuffer.md#napi_get_arraybuffer_info)接口接收，获取到的status是napi\_arraybuffer\_expected。

## 背景知识

[使用Node-API接口进行Array相关开发](../harmonyos-guides/use-napi-about-array.md)：使用Node-API接口进行数组相关开发时，涉及的基本概念主要包括数组的创建、访问、修改、遍历以及与数组相关的操作。这些概念对于理解如何在Node-API模块中与ArkTS数组交互非常重要。

## 解决方案

ArkTS中的number数组是普通数组类型，而ArrayBuffer是二进制缓冲区类型，二者在NAPI层不兼容。

**方案一**：基于ArrayBuffer接收Float数组：

需要将数组类型改为[Float32Array](../harmonyos-references/arkts-apis-arkts-collections-float32array.md)类型进行传递。使用[napi\_get\_typedarray\_info](../harmonyos-guides/use-napi-about-array.md#napi_get_typedarray_info)获取给定TypedArray的各种属性。

* C++侧代码：

  ```cpp
  static napi_value TransmitByTypedArray(napi_env env, napi_callback_info info)
  {
      // 获取ArkTS侧传入的参数
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 定义napi_get_typedarray_info所需参数
      void *data;
      napi_typedarray_type type;
      size_t byteOffset, length;
      napi_value arraybuffer;
      // 调用接口napi_get_typedarray_info获得TypedArray类型数据的信息
      napi_get_typedarray_info(env, args[0], &type, &length, &data, &arraybuffer, &byteOffset);
      float* displayArr = (float*)data;
      float a = displayArr[0];
      float b = displayArr[1];
      OH_LOG_INFO(LOG_APP, "First element in TypedArray: %{public}f", a);
      OH_LOG_INFO(LOG_APP, "Second element in TypedArray: %{public}f", b);
      return NULL;
  }
  ```
* 接口声明：

  ```ts
  export const transmitByTypedArray: <T>(typeArray: T, b: number) => void;
  ```
* ArkTS侧代码：

  此处使用了Button组件，点击触发接收数据，并打印日志。

  ```ts
  Button('use TypedArray')
    .onClick(() => {
      let fa: Float32Array = new Float32Array([1.10, 2.22222, 3.69, 4.5]);
      testNapi.transmitByTypedArray(fa, 4);
    })
  ```

**方案二**：仍使用number[]接收Float数组：

由于ArkTS中number本质上为Double类型、应显式转换为Float类型，使用循环语句逐个提取Float元素。

* C++侧代码：

  ```cpp
  static napi_value TransmitByNumber(napi_env env, napi_callback_info info)
  {
      // 获取ArkTS侧传入的参数
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 判断是否为数组
      bool isArr = false;
      napi_is_array(env, args[0], &isArr);
      if (!isArr) {
          napi_throw_error(env, nullptr, "Argument should be an object of type array");
          return NULL;
      }
      // 获取数组长度
      uint32_t arrayLength;
      napi_get_array_length(env, args[0], &arrayLength);
      // 循环语句逐一提取number[]元素
      std::vector<float> floatData;
      for (uint32_t i = 0; i < arrayLength; i++) {
          napi_value element;
          napi_get_element(env, args[0], i, &element);
          double val;
          napi_get_value_double(env, element, &val); // 转换为double
          floatData.push_back(static_cast<float>(val)); // 显式转为float
      }
      float a = floatData[0];
      float b = floatData[1];
      OH_LOG_INFO(LOG_APP, "First element in number[]: %{public}f", a);
      OH_LOG_INFO(LOG_APP, "Second element in number[]：%{public}f", b);
      return NULL;
  }
  ```
* 接口声明：

  ```ts
  export const transmitByNumber: <T>(arr: Array<T>, index: number) => void;
  ```
* ArkTS侧代码：

  此处使用了Button组件，点击触发接收数据，并打印日志。

  ```ts
  Button('use number[]')
    .onClick(() => {
      let na: number[] = [1.10, 2.22222, 3.69, 4.5];
      testNapi.transmitByNumber(na, 4);
    })
  ```

完整示例参考如下：

* C++侧代码：

  ```cpp
  /*
   * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
   * Licensed under the Apache License, Version 2.0 (the "License");
   * you may not use this file except in compliance with the License.
   * You may obtain a copy of the License at
   * 
   *     http://www.apache.org/licenses/LICENSE-2.0
   * 
   * Unless required by applicable law or agreed to in writing, software
   * distributed under the License is distributed on an "AS IS" BASIS,
   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   * See the License for the specific language governing permissions and
   * limitations under the License.
   */
  #include "napi/native_api.h"
  #include "hilog/log.h"
  #include <cstddef>
  #include <vector>

  #undef LOG_DOMAIN
  #undef LOG_TAG
  #define LOG_DOMAIN 0x0000  // 全局domain宏，标识业务领域
  #define LOG_TAG "MY_TAG"   // 全局tag宏，标识模块日志tag
  static napi_value TransmitByTypedArray(napi_env env, napi_callback_info info)
  {
      // 获取ArkTS侧传入的参数
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 定义napi_get_typedarray_info所需参数
      void *data;
      napi_typedarray_type type;
      size_t byteOffset, length;
      napi_value arraybuffer;
      // 调用接口napi_get_typedarray_info获得TypedArray类型数据的信息
      napi_get_typedarray_info(env, args[0], &type, &length, &data, &arraybuffer, &byteOffset);
      float* displayArr = (float*)data;
      float a = displayArr[0];
      float b = displayArr[1];
      OH_LOG_INFO(LOG_APP, "First element in TypedArray: %{public}f", a);
      OH_LOG_INFO(LOG_APP, "Second element in TypedArray: %{public}f", b);
      return NULL;
  }
  static napi_value TransmitByNumber(napi_env env, napi_callback_info info)
  {
      // 获取ArkTS侧传入的参数
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 判断是否为数组
      bool isArr = false;
      napi_is_array(env, args[0], &isArr);
      if (!isArr) {
          napi_throw_error(env, nullptr, "Argument should be an object of type array");
          return NULL;
      }
      // 获取数组长度
      uint32_t arrayLength;
      napi_get_array_length(env, args[0], &arrayLength);
      // 循环语句逐一提取number[]元素
      std::vector<float> floatData;
      for (uint32_t i = 0; i < arrayLength; i++) {
          napi_value element;
          napi_get_element(env, args[0], i, &element);
          double val;
          napi_get_value_double(env, element, &val); // 转换为double
          floatData.push_back(static_cast<float>(val)); // 显式转为float
      }
      float a = floatData[0];
      float b = floatData[1];
      OH_LOG_INFO(LOG_APP, "First element in number[]: %{public}f", a);
      OH_LOG_INFO(LOG_APP, "Second element in number[]：%{public}f", b);
      return NULL;
  }
  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          {"transmitByTypedArray", nullptr, TransmitByTypedArray, nullptr, nullptr, nullptr, napi_default, nullptr },
          {"transmitByNumber", nullptr, TransmitByNumber, nullptr, nullptr, nullptr, napi_default, nullptr}
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
* 接口声明：

  ```ts
  export const transmitByTypedArray: <T>(typeArray: T, b: number) => void;
  export const transmitByNumber: <T>(arr: Array<T>, index: number) => void;
  ```
* ArkTS侧代码：

  ```ts
  import testNapi from 'libentry.so';

  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column({space: 10}) {
          Button('use TypedArray')
            .onClick(() => {
              let fa: Float32Array = new Float32Array([1.10, 2.22222, 3.69, 4.5]);
              testNapi.transmitByTypedArray(fa, 4);
            })
            .width('50%')
          Button('use number[]')
            .onClick(() => {
              let na: number[] = [1.10, 2.22222, 3.69, 4.5];
              testNapi.transmitByNumber(na, 4);
            })
            .width('50%')
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
