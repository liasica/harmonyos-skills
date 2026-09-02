---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-1
title: ArkTS与Native C++间数据传递异常
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > ArkTS与Native C++间数据传递异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:471be9347c7c07ca11bb7fed91d6cd8b6479a47a365df003a39831346842aad0
---

## 问题现象

在ArkTS与Native C++通过Node-API接口进行数据传递时，经常会遇到一些数据传递前后不一致甚至报错的问题，如：

* **场景一**：ArkTS向C++传递数据问题：

  通过napi\_get\_value\_string\_utf8传递长string时，C++获取不到字符串内容。
* **场景二**：C++向ArkTS传递数据问题：
  + 通过napi\_create\_external\_arraybuffer异步传递Buffer，在ArkTS侧获取不到内容。
  + 通过napi\_create\_buffer\_copy创建并复制数据到Buffer对象时报错：

    ```txt
    Create failed, current size: 2.969184 MiB, limit size: 2.000000 MiB
    ```
  + 通过napi\_create\_typedarray创建并赋值Unicode字符串数据时报错：

    ```txt
    C03F00/ArkCompiler com.examp...lication E RangeError: The newByteLength is out of range.
    ```

## 背景知识

* [支持的Node-API接口](../harmonyos-guides/napi-data-types-interfaces.md#支持的node-api接口)：HarmonyOS Node-API接口在Node.js提供的模块基础上扩展，支持的数据类型和相关接口的用法及示例可参考文档。
* [使用Node-API接口进行线程安全开发](../harmonyos-guides/use-napi-thread-safety.md)：创建一个线程安全的JavaScript函数。主要用于在多个线程之间共享和调用，而不会出现竞争条件或死锁，确保多个线程之间的通信和同步操作正确无误。
* [使用Node-API的napi\_create\_external\_buffer接口进行Buffer相关开发](../harmonyos-guides/use-napi-about-buffer.md#napi_create_external_buffer)：external\_buffer使用现有的Node-API模块内存块，而不需要额外的拷贝。

## 问题定位

* **场景一**：

  C++侧获取不到ArkTS传入的string，可能导致的原因有两种：

  + 参数传入的string的内容是否为空。
  + string的长度特别长。

  可以通过ArkTS侧的源码排查，属于上述哪种情形。
* **场景二**：
  + 异步回调ArkTS收不到数据，通过代码排查是否使用了external\_arraybuffer，在External Buffer释放的地方加上日志，通过日志的时间戳检查C++侧数据是否在被取出时已经被释放。
  + C++创建和复制数据到Buffer时出错报错，通过检索日志中包含limit size: 2.000000 MiB错误信息，判断拷贝的数据超过了2M的限制，在源码中找到Buffer拷贝的数据，确认其大小。
  + 通过typedarray传递ArrayBuffer时，检索日志包含is out of range，则是数组越界导致，通过代码排查计算类型大小×length判断是否超出了数组的大小。

## 分析结论

* **场景一**：

  ArkTS传入的字符串长度超过限制，无法通过napi\_get\_value\_string\_utf8传递，该接口获取字符大小由底层内存决定，Node-API无法设置和更改。
* **场景二**：
  + external\_arraybuffer不会拷贝内存，而是复用Node-API模块内存块，通过异步回调方式传递数据时，若C++侧数据释放了，ArkTS将获取不到数据。
  + napi\_create\_buffer\_copy最大支持2M数据（2097152字节），超出报错。
  + Unicode字符占用2字节，napi\_create\_typedarray以类型napi\_int16\_array传递Unicode字符时，2\*length超过数据长度时，出错。

## 修改建议

* **场景一**：

  传输长string时，建议以Buffer传递，通过napi\_get\_buffer\_info来获取从TS层传来的Buffer，再转成string。
* **场景二**：
  + 使用External ArrayBuffer复用Node-API内存时，确保在结果回调前内存不释放，或者使用线程安全函数。
  + 传递Buffer数据控制数据在2M内，超出时，推荐使用napi\_create\_arraybuffer接口创建的ArrayBuffer对象，该接口没有数据大小限制。
  + 创建ArrayBuffer对象时，计算检查数据类型长度，避免数据内存越界。
