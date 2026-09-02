---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-19
title: napi_load_module_with_info使用限制和注意事项
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > napi_load_module_with_info使用限制和注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:13bd9bb4da7d352db92b955a5ad2dddb703ab3d96d002410ec710058c55717d6
---

## 问题现象

[napi\_load\_module\_with\_info](../harmonyos-references/napi.md#napi_load_module_with_info)支持开发者在C++侧加载工程内模块及文件，该接口在使用时有哪些使用限制和注意事项？

## 解决方案

* 参数说明：

  | 参数名 | 含义说明 |
  | --- | --- |
  | path | 要加载的文件路径/模块名。如：“entry/src/main/ets/Test”。 |
  | module\_info | app.json5中配置的工程名/待加载模块所在的HAP下module.json5中配置的模块名的路径拼接，如：“com.example.application/entry”。 |
* 异常返回值说明及处理方法：

  | 返回值名 | 含义说明 | 异常处理方法 |
  | --- | --- | --- |
  | napi\_invalid\_arg | env/result为nullptr。 | 检查传入的参数，确保参数值准确不为空。 |
  | napi\_generic\_failure | 模块加载失败。 | 检查文件路径/模块信息是否准确，确保目标路径下文件存在。 |
  | napi\_pending\_exception | 调用接口前有未捕获的ArkTS异常。 | 可以参考官方文档中清除异常接口[napi\_get\_and\_clear\_last\_exception](../harmonyos-guides/use-napi-about-error.md#napi_get_and_clear_last_exception)和调用前检查异常接口[napi\_is\_exception\_pending](../harmonyos-guides/use-napi-about-error.md#napi_is_exception_pending)来定位异常发生的位置。 |

**说明** 

* 加载本地工程模块内文件时，要求path以moduleName开头。
* 因为应用间的hsp包也可以通过napi\_load\_module\_with\_info接口加载，所以module\_info参数中必须指定bundleName和moduleName。
* 编译构建后，HAR模块被打包到各个模块之中，其入口模块仍然是HAP模块。所以在调用HAR模块时，path的模块名称要填HAP模块中oh-package.json5中定义的依赖HAR的名称，而不是HAR模块的实际名称。
* 如果在HAP/HSP中直接或间接使用了三方包，该三方包中使用napi\_load\_module\_with\_info接口加载其他模块A，则需要在HAP/HSP中也添加A的依赖。
* 在加载非模块内文件时，需要对调用模块的build-profile.json5进行配置：

  ```txt
  buildOption->arkOptions->runtimeOnly->packages->oh-package.json5文件中dependencies配置的依赖名。
  ```
* 在[napi\_create\_ark\_runtime](../harmonyos-references/napi.md#napi_create_ark_runtime)接口创建的运行时环境中使用时，若希望加载的模块不被系统回收，可以通过[napi\_create\_reference](../harmonyos-references/napi.md#napi_create_reference)方法将模块存储起来。
* 在ohosTest中使用时，需要将加载路径改为“entry/src/ohosTest/ets/test/Ability.test”，module\_info中的模块名改成entry\_test。

## 总结

与[napi\_load\_module](../harmonyos-references/napi.md#napi_load_module)仅支持在主线程使用相比，napi\_load\_module\_with\_info不仅支持在主线程中使用，也可以在[新创建的ArkTS基础运行时环境中使用](../harmonyos-guides/use-napi-ark-runtime.md)。

napi\_load\_module\_with\_info支持加载hap/hsp/har/native模块等多种场景，具体使用可以参考[使用示例](../harmonyos-guides/use-napi-load-module-with-info.md#使用示例)。

在实现模块加载时，推荐优先使用napi\_load\_module\_with\_info接口。
