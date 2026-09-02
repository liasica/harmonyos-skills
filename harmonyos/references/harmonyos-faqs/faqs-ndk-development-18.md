---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-18
title: ArkTS侧如何批量传递函数到native侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS侧如何批量传递函数到native侧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aa4b92960dced6fbf34c6a3ce63748c7e0a24b6b1debfd48276c1b447c495b9c
---

## 问题现象

在native侧需要调用一系列ArkTS侧函数，如果每个方法都通过单独的参数传递到native侧的话，会比较繁琐，ArkTS侧如何批量传递函数到native侧？

## 背景知识

* [napi\_get\_element](../harmonyos-guides/use-napi-about-array.md#napi_get_element)：用于从ArkTS数组中获取请求索引位置的元素值。请求索引值应在数组的有效范围内，如果索引超出数组长度，函数会返回undefined。
* [napi\_get\_named\_property](../harmonyos-guides/use-napi-about-property.md#napi_get_named_property)：用于从ArkTS对象中获取命名属性的值。

## 解决方案

可以将函数包装在一个对象或者数组中，通过传递对象或数组达成传递一系列函数的目的。本文通过在数组中传递两个匿名函数及一个对象的方式完成ArkTS侧批量传递函数到native侧的目的。示例代码如下：

* cpp文件：将数组传入到c++侧后，通过napi\_get\_element方法分别获得数组中的两个匿名函数及DataModel对象。在通过napi\_get\_named\_property方法获取DataModel对象中的方法，最后通过napi\_call\_function方法分别调用获得的方法。

  ```cpp
  /*
   * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
   */
  #include "napi/native_api.h"
  static napi_value Test(napi_env env, napi_callback_info info)
  {
      // 期望从ArkTS侧获取的参数的数量，napi_value可理解为ArkTS value在native方法中的表现形式。
      size_t argc = 1;
      napi_value args[1] = {nullptr};

      // 从info中，拿到从ArkTS侧传递过来的参数，此处获取了一个ArkTS参数，即arg[0]。
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
      // 从arg[0]中获取ts侧传递的方法。
      napi_value mul = nullptr;
      napi_get_element(env, args[0], 0, &mul);

      napi_value div = nullptr;
      napi_get_element(env, args[0], 1, &div);

      // 从arg[0]中获取ts侧传递的对象。
      napi_value DataModel = nullptr;
      napi_get_element(env, args[0], 2, &DataModel);

      // 获取对象中的方法。
      napi_value add, sub;
      napi_get_named_property(env, DataModel, "add", &add);
      napi_get_named_property(env, DataModel, "sub", &sub);

      // 创建参数数组。
      napi_value arr[2];
      napi_create_int32(env, 10, &arr[0]);
      napi_create_int32(env, 5, &arr[1]);

      // 创建一个ArkTS number作为ArkTS function的入参。
      napi_value argv = nullptr;
      napi_create_int32(env, 2, &argv);

      // 创建一个初始长度为length的数组result。
      napi_value result;
      if (napi_ok != napi_create_array_with_length(env, 4, &result)) {
          return nullptr;
      }

      // napi_call_function函数可以传递多个参数，传递函数的入参个数、类型、返回值类型不一致都适用此方法。
      napi_value resultAdd;
      // 调用方法add。
      // napi_call_function传递两个参数。
      napi_call_function(env, nullptr, add, 2, arr, &resultAdd);
      napi_set_element(env, result, 1, resultAdd);
      // 调用方法sub
      napi_value resultSub;
      napi_call_function(env, nullptr, sub, 2, arr, &resultSub);
      napi_set_element(env, result, 2, resultSub);

      // 调用方法mul。
      // napi_call_function传递一个参数。
      napi_value resultMul;
      napi_call_function(env, nullptr, mul, 1, &argv, &resultMul);
      napi_set_element(env, result, 3, resultMul);

      // 调用方法div。
      napi_value resultDiv;
      napi_call_function(env, nullptr, div, 1, &argv, &resultDiv);
      napi_set_element(env, result, 4, resultDiv);

      return result;
  }

  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          {"test", nullptr, Test, nullptr, nullptr, nullptr, napi_default, nullptr}
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
      .nm_priv = ((void *)0),
      .reserved = {0},
  };

  extern "C" __attribute__((constructor)) void RegisterEntryModule(void) { napi_module_register(&demoModule); }
  ```
* index.ets：文件中创建一个arr数组，存放两个匿名函数及一个DataModel对象（DataModel中存在两个方法）。

  ```ts
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import testNapi from 'libentry.so';
  import dataModel from '../pages/DataModel';

  let value: number = 10;

  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column() {
          Text('test')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              let arr: Object[] = [];
              arr[0] = () => {
                return value * 2;
              };
              arr[1] = () => {
                return value / 2;
              };
              arr[2] = dataModel;
              let ret = testNapi.test(arr);
              hilog.info(0x0000, 'testTag', 'Test NAPI test ret = %{public}d', ret[1]);
              hilog.info(0x0000, 'testTag', 'Test NAPI test ret = %{public}d', ret[2]);
              hilog.info(0x0000, 'testTag', 'Test NAPI test ret = %{public}d', ret[3]);
              hilog.info(0x0000, 'testTag', 'Test NAPI test ret = %{public}d', ret[4]);

            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* DataModel.ets：导出DataModel类。

  ```ts
  class DataModel {
    add(a: number, b: number): number {
      return a + b;
    }

    sub(a: number, b: number): number {
      return a - b;
    }
  }

  export default new DataModel();
  ```
