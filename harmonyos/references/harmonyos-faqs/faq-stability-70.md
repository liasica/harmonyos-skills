---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-70
title: NDK工程bad_variant_access崩溃分析和解决
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > NDK工程bad_variant_access崩溃分析和解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f966dd1af7a76076725a4ad657f681f5d9b5a5d0800d4812c0f94cacb410d635
---

## 问题现象

HarmonyOS NDK工程运行出现崩溃，报错信息如下：

```txt
LastFatalMessage:terminating due to uncaught exception of type std::bad_variant_access: bad_variant_access
Thread name:m.example.application
#00 pc 0000000000199e1c /system/lib/ld-musl-aarch64.so.1(raise+228)(6b9883f518515f73e093bce9a89a2548)
#01 pc 0000000000146f8c /system/lib/ld-musl-aarch64.so.1(abort+20)(6b9883f518515f73e093bce9a89a2548)
#02 pc 00000000000b06c8 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(7d8a9e90f79938a689894d03db6e4557bd538eb3)
#03 pc 0000000000098b38 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(7d8a9e90f79938a689894d03db6e4557bd538eb3)
#04 pc 00000000000af834 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(7d8a9e90f79938a689894d03db6e4557bd538eb3)
#05 pc 00000000000b28e4 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(7d8a9e90f79938a689894d03db6e4557bd538eb3)
#06 pc 00000000000b2860 /data/storage/el1/bundle/libs/arm64/libc++_shared.so(__cxa_throw+124)(7d8a9e90f79938a689894d03db6e4557bd538eb3)
```

## 背景知识

在C++17中引入了一个非常有用的类型std::variant，使用前需要包含头文件：

```
#include <variant>
```

std::variant是一个类型安全的联合体，可以存储固定集合中的任意类型的值。这使得std::variant成为处理那些可能需要存储不同类型数据的情况的理想选择。

std::variant与union联合体很像，主要区别如下：

* 类型安全：与传统的C联合体（union）不同，std::variant在类型安全方面提供了显著的改进。它能保证在任何时候都只包含其能持有的类型之一，并且提供了丰富的接口来检查和访问存储的数据。
* 自动管理：std::variant自动处理类型的构造、析构和赋值，确保资源的正确管理。访问控制：提供了安全的方式访问存储的数据，例如std::get、std::visit等函数。

## 问题定位

从崩溃信息中terminating due to uncaught exception of type std::bad\_variant\_access: bad\_variant\_access可以看到主要原因在于访问std::variant的时候出的问题。于是全局搜索使用std::variant变量的地方，查看使用方法发现在使用variant的地方没有进行保护，导致出现类型转换错误的时候出现崩溃，示例如下：

```
using VarObject = std::variant<int, std::string, MyClass>;
VarObject v1 = 42;
VarObject v2 = "Hello";
VarObject v3 = MyClass(100);
...
auto a = std::get<MyClass>(v2); // 转换错误，发生崩溃
...
```

## 分析结论

* 当使用std::get<T>访问std::variant时，如果当前存储的类型与请求的类型不匹配，会抛出std::bad\_variant\_access异常。
* std::variant的std::get<T>在类型不匹配时抛出的异常（std::bad\_variant\_access），如果未使用try-catch捕获，异常会向上传播到未被捕获的异常处理程序，触发std::terminate，导致程序终止（表现为“崩溃”）。

## 修改建议

* **方案一：预先检查类型。**

  使用std::holds\_alternative<T>检查当前存储的类型：

  ```
  if (std::holds_alternative<MyClass>(v)) {
      auto s = std::get<MyClass>(v); // 安全访问
  } else {
      // 处理其他类型
  }
  ```
* **方案二：使用std::get\_if安全获取指针。**

  std::get\_if返回指针，类型不匹配时返回nullptr：

  ```
  if (auto* p = std::get_if<MyClass>(&v3)) {
      p->Print();
  } else {
      // 处理其他类型
  }
  ```
* **方案三：使用std::visit统一处理所有类型。**

  通过访问者模式处理所有可能的类型，避免直接访问错误类型：

  ```
  std::visit([](auto&& arg) {
      using T = std::decay_t<decltype(arg)>;
      if constexpr (std::is_same_v<T, MyClass>) {
          // 处理MyClass
          arg.Print();
      } else if constexpr (std::is_same_v<T, std::string>) {
          // 处理String
          OH_LOG_INFO(LOG_APP, "MyClass visit is String %{public}s.", arg.c_str());
      } else {
          // 处理其他类型
      }
  }, v3);
  ```
* **方案四：异常处理（不推荐作为首选方案）**

  使用try-catch捕获异常：

  ```
  try {
      std::get<MyClass>(v3).Print(); // 输出: MyClass: 100
  } catch (...) {}
  ```
