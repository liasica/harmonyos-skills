---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ark-runtime-detection
title: 方舟运行时检测
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 方舟类问题检测 > 方舟运行时检测
category: best-practices
scraped_at: 2026-04-29T14:14:04+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c45b13767bfda41a678d02dd400908006329e7e3d2f59e8f69a081437b6cd462
---

## 方舟多线程检测

在JS运行时环境中，多线程的安全问题是一个重要的考虑因素。由于JavaScript本身是单线程的，对JS对象的任何操作都必须在创建该JS线程的原始线程上进行。如果违反了这一规则，就会导致多线程安全问题。以下是关于如何判断和处理这些问题的一些详细说明。开启多线程检测会有较大性能损耗，请开发者按需开启。

### 原理介绍

* 单线程执行

  JavaScript是单线程执行的语言，这意味着它一次只能在一个线程上执行代码。任何JavaScript对象都只能在创建它们的线程上进行操作。
* N-API（Node-API）接口

  N-API接口直接涉及到JavaScript对象的操作。绝大多数N-API接口（约95%）只能在创建这些对象的JavaScript线程上调用。

* 多线程检测机制

  多线程检测机制会检测当前线程和正在使用的JS虚拟机环境（vm/env）中的JS线程ID是否一致。如果不一致，就表明虚拟机环境被跨线程使用，存在多线程安全问题。

### 常见多线程安全问题

* 非JS线程使用N-API接口

  非JavaScript线程尝试调用N-API接口，可能会导致未定义的行为或崩溃。

  ```
  1. // Index.ets
  2. Text(this.message)
  3. .fontSize($r('app.float.page_text_font_size'))
  4. .fontWeight(FontWeight.Bold)
  5. .onClick(() => {
  6. testNapi.multiCheck();
  7. })
  ```

  ```
  1. // napi_init.cpp
  2. static napi_value MultiCheck(napi_env env, napi_callback_info info)
  3. {
  4. std::thread([](napi_env env) {
  5. napi_value obj = nullptr;
  6. napi_create_object(env, &obj);
  7. }, env).join();

  9. return nullptr;
  10. }
  ```

* N-API接口使用其他线程的env

  一个线程尝试使用另一个线程创建的env（JavaScript环境），这也会导致多线程安全问题。

  ```
  1. // Index.ets
  2. Text(this.message)
  3. .fontSize($r('app.float.page_text_font_size'))
  4. .fontWeight(FontWeight.Bold)
  5. .onClick(() => {
  6. testNapi.saveEnv();
  7. const task = new taskpool.Task(createObject);
  8. taskpool.execute(task);
  9. })
  ```

  ```
  1. // napi_init.cpp
  2. napi_env env_ = nullptr;
  3. static napi_value SaveEnv(napi_env env, napi_callback_info info)
  4. {
  5. env_ = env;
  6. return nullptr;
  7. }
  8. static napi_value CreateObject(napi_env env, napi_callback_info info)
  9. {
  10. napi_value obj = nullptr;
  11. napi_create_object(env_, &obj);
  12. return nullptr;
  13. }
  ```

**如何判断是否发生了多线程安全问题**

如果在运行时遇到以下致命错误信息，这意味着已经发生了多线程安全问题：

```
1. Fatal: ecma_vm cannot run in multi-thread! thread:3096 currentThread:3550
```

当前线程号为3550，而使用的JavaScript线程是由3096线程创建的，这表明虚拟机环境（vm/env）被跨线程使用，从而导致了多线程安全问题。

说明

若未开启多线程检查开关，即使存在错误的多线程写法，运行时也不一定报错。

### 使用约束

方舟多线程检测通过命令行参数开启，点击桌面图标无效。

### 开启方舟多线程检测

可通过以下方式启用方舟多线程检测。

* **方式一**

  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Multi Thread Check**。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/AGGVkOlrQJqY4oDaRBj9_g/zh-cn_image_0000002404045317.png?HW-CC-KV=V1&HW-CC-Date=20260429T061403Z&HW-CC-Expire=86400&HW-CC-Sign=189E246F10C57C145040A58EEA078DB1F21CD7AAB8D1A59AE4BAF4FF84A90071)

* **方式二**

  通过命令行开启。

  ```
  1. hdc shell aa start -a {abilityName} -b {bundleName} -R
  ```

### 使用方舟多线程检测

1. 运行或调试当前应用。
2. 当程序出现多线程安全问题时，会弹出Crash log信息，点击信息中的链接即可跳转至引起多线程安全问题的代码处。

### 方舟异常检测码

若fatal信息为Fatal: ecma\_vm cannot run in multi-thread! thread:20296 currentThread:19953，则发生了多线程安全问题，意为：当前线程号为19953，而使用的js thread是20296创建出来的，跨线程使用VM。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/g81gELANSRSfV3kF7j-9Pg/zh-cn_image_0000002504986012.png?HW-CC-KV=V1&HW-CC-Date=20260429T061403Z&HW-CC-Expire=86400&HW-CC-Sign=469171CD1F151229F8E369FFCBECE258A4A9CC1ECED69227D060E2E03C8EE58C)
