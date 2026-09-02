---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-3
title: 如何对多个C++源文件中接口进行导出声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何对多个C++源文件中接口进行导出声明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:530f95391a813ee858dd6ed6ce9cc08ea2ba5fdba7dd001ad1d524b0e51316ee
---

**问题现象**

DevEco Studio创建的默认C++工程中是只有一个hello.cpp，想在C++侧加一个 a.cpp文件，并且希望可以从a.cpp文件中导出一个函数给ArkTS侧调用，具体如何实现？

**解决措施**

首先需要引入对应的a.cpp对应的头文件a.h，然后在初始化函数Init中进行接口映射，最后通过index.d.ts文件将接口导出。参考代码如下：

在NumberType.cpp文件中实现Add函数业务功能。

```cpp
#include "NumberType.h" // Import header file
// NumberType is the class name, and Add is its function 
napi_value NumberType::Add(napi_env env, napi_callback_info info) {
    // ... Business Function Implementation Code
    // ...
}
```

在hello.cpp文件中引入头文件并初始化函数Init中进行接口映射。

```ts
#include "NumberType.h"
#include "napi/native_api.h"

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    /* Associate the externally provided interface with the written method, for example, associate add with the Add 
     * method. 
    */ 
    napi_property_descriptor desc[] = {
        { "add", nullptr, NumberType::Add, nullptr, nullptr, nullptr, napi_default, nullptr }
    };
    // napi_define_properties construct a return value that contains a list of methods that correspond. 
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
```

在接口声明文件（index.d.ts）中对要传递给ArkTS侧的函数进行导出。

```ts
export const add: (a: number, b: number) => number;
```

**参考链接**

[基于XComponent组件实现图像绘制功能](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-XComponent)
