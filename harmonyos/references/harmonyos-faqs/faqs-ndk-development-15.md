---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-15
title: native如何通过父类创建子类并返回到ArkTS侧
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > native如何通过父类创建子类并返回到ArkTS侧
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f417c9f37b6cc87ca921ab5af786cfe944693b0d760f072c4a528204acc56d02
---

## 问题现象

C/C++侧同时创建了父类和子类，可以通过父类方法创建子类，ArkTS侧如何调用此类native实现获取到子类实例。

## 背景知识

* [napi\_new\_instance](../harmonyos-guides/use-napi-about-class.md#napi_new_instance)：通过给定的构造函数实例化一个对象，将这个对象返回ArkTS侧使用。
* [napi\_define\_class](../harmonyos-guides/use-napi-about-class.md#napi_define_class)：用于定义一个ArkTS类。该函数允许在Node-API模块中创建一个ArkTS类，并将类的方法和属性与相应的Node-API模块关联起来。
* [napi\_wrap](../harmonyos-guides/use-napi-about-class.md#napi_wrap)：在ArkTS object上绑定一个native对象实例。

## 解决方案

代码示例：

1. native侧Parent类为父类，Child类为子类。

   ```screen
   extern class Child;

   class Parent {
     public:
       void DoSomething();
     Child *CreateChild();
   };

   class Child : Parent {
     public:
       void DoSomething();
   };
   ```

   通过napi方法[napi\_define\_class](../harmonyos-guides/use-napi-about-class.md#napi_define_class)定义ArkTS侧的Parent类和Child类并导出。

   ```screen
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor parentDesc[] = {
           {"doSomething", nullptr, ParentDoSomething, nullptr, nullptr, nullptr, napi_default, nullptr},
           {"createChild", nullptr, ParentCreateChild, nullptr, nullptr, nullptr, napi_default, nullptr}
       };

       napi_property_descriptor childDesc[] = {
           {"doSomething", nullptr, ChildDoSomething, nullptr, nullptr, nullptr, napi_default, nullptr}
       };

       napi_value parentConstructor = nullptr;
       napi_define_class(env, "Parent", NAPI_AUTO_LENGTH, ParentConstructor, nullptr, sizeof(parentDesc) / sizeof(parentDesc[0]),
                         parentDesc, &parentConstructor);
       napi_set_named_property(env, exports, "Parent", parentConstructor);

       napi_value childConstructor = nullptr;
       napi_define_class(env, "Child", NAPI_AUTO_LENGTH, ChildConstructor, nullptr, sizeof(childDesc) / sizeof(childDesc[0]),
                         childDesc, &childConstructor);
       napi_set_named_property(env, exports, "Child", childConstructor);
       return exports;
   }
   EXTERN_C_END
   ```

   Index.d.ts中导出的定义：

   ```screen
   export class Parent {
     constructor()

     doSomething(): void

     createChild(obj: ESObject): Child
   }

   export class Child {
     constructor()

     doSomething(): void
   }
   ```
2. 执行native侧的ParentCreateChild函数。
   1. 通过[napi\_new\_instance](../harmonyos-guides/use-napi-about-class.md#napi_new_instance)在native端创建一个Child类的实例（也就是Child的native对象）。
   2. 该Child实例会被包装成一个可被ArkTS使用的对象（通过[napi\_wrap](../harmonyos-guides/use-napi-about-class.md#napi_wrap)绑定）。
   3. 最后，该Child实例被返回给ArkTS侧的createChild()方法。

      **说明** 

      * 在native层创建Child实例，通过[napi\_wrap](../harmonyos-guides/use-napi-about-class.md#napi_wrap)包装并绑定，最终返回给ArkTS侧使用。

      ```screen
      static napi_value ParentCreateChild(napi_env env, napi_callback_info info)
      {
        size_t argc = 1;
        napi_value args[1] = {nullptr};
        napi_value jsthis;
        Parent *instanceParent = nullptr;
        bool bRet = false;
        napi_value result = nullptr;
        napi_status status;

        status = napi_get_cb_info(env, info, &argc, args, &jsthis, nullptr);
        if (status != napi_ok) {
          OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_get_cb_info fail.Status:%{public}d", status);
          return nullptr;
        }

        status = napi_unwrap(env, jsthis, reinterpret_cast<void **>(&instanceParent));
        if (status != napi_ok) {
          OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_unwrap fail.Status:%{public}d", status);
          return nullptr;
        }

        status = napi_new_instance(env, args[0], 0, nullptr, &result);
        if (status != napi_ok) {
          OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_new_instance fail.Status:%{public}d", status);
          return nullptr;
        }

        Child *instanceChild = instanceParent->CreateChild();

        status = napi_wrap(env, result, reinterpret_cast<void *>(instanceChild), DerefChild, NULL, NULL);
        if (status != napi_ok) {
          // 主动释放内存
          OH_LOG_INFO(LOG_APP, "ParentcreateChild ChildConstructor napi_wrap fail status:%{public}d", status);
          delete instanceChild;
        }

        return result;
      }
      ```
3. ArkTS侧的调用逻辑：

   ```screen
   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message = 'Welcome';
               let parent = new testNapi.Parent();
               let child = new testNapi.Child();
               parent.doSomething();
               child.doSomething();
               let newChild: testNapi.Child = parent.createChild(testNapi.Child);
               newChild.doSomething();
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

**完整实现如下：**

ArkTS侧实现：

```screen
import testNapi from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.message = 'Welcome';
            let parent = new testNapi.Parent();
            let child = new testNapi.Child();
            parent.doSomething();
            child.doSomething();
            let newChild: testNapi.Child = parent.createChild(testNapi.Child);
            newChild.doSomething();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

native侧实现：

```screen
#include "hilog/log.h"
#include "napi/native_api.h"

#define LOG_TAG "test"
extern class Child;

class Parent {
public:
    void DoSomething();
    Child *CreateChild();
};

class Child : Parent {
public:
    void DoSomething();
};
void Parent::DoSomething() { OH_LOG_ERROR(LOG_APP, "Parent DoSomething"); }

Child *Parent::CreateChild()
{
    Child *instance = new Child();
    return instance;
}

void Child::DoSomething() { OH_LOG_ERROR(LOG_APP, "Child DoSomething"); }

static napi_value Add(napi_env env, napi_callback_info info)
{
    size_t argc = 2;
    napi_value args[2] = {nullptr};

    napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

    napi_valuetype valuetype0;
    napi_typeof(env, args[0], &valuetype0);

    napi_valuetype valuetype1;
    napi_typeof(env, args[1], &valuetype1);

    double value0;
    napi_get_value_double(env, args[0], &value0);

    double value1;
    napi_get_value_double(env, args[1], &value1);

    napi_value sum;
    napi_create_double(env, value0 + value1, &sum);

    return sum;
}

static void DerefParent(napi_env env, void *data, void *hint)
{
    // 可选的原生回调，用于在ArkTS对象被垃圾回收时释放原生实例
    OH_LOG_INFO(LOG_APP, "Node-API DerefItem");
    Parent *obj = reinterpret_cast<Parent *>(data);
    if (obj != nullptr) {
        delete obj;
    }
}

static void DerefChild(napi_env env, void *data, void *hint)
{
    // 可选的原生回调，用于在ArkTS对象被垃圾回收时释放原生实例
    OH_LOG_INFO(LOG_APP, "Node-API DerefItem");
    Child *obj = reinterpret_cast<Child *>(data);
    if (obj != nullptr) {
        delete obj;
    }
}

static napi_value ParentConstructor(napi_env env, napi_callback_info info)
{
    napi_value undefineVar = nullptr;
    napi_get_undefined(env, &undefineVar);
    napi_value jsInstance = nullptr;
    if (napi_get_cb_info(env, info, nullptr, nullptr, &jsInstance, nullptr) != napi_ok) {
        return undefineVar;
    }

    Parent *instance = new Parent();

    napi_status status = napi_wrap(env, jsInstance, reinterpret_cast<void *>(instance), DerefParent, NULL, NULL);
    if (status != napi_ok) {
        // 主动释放内存
        OH_LOG_INFO(LOG_APP, "ParentConstructor napi_wrap fail");
        delete instance;
    }
    OH_LOG_INFO(LOG_APP, "ParentConstructor success");
    return jsInstance;
}

// 定义类Parent的方法
static napi_value ParentDoSomething(napi_env env, napi_callback_info info)
{
    napi_value jsthis;
    Parent *instance = nullptr;
    bool bRet = false;
    napi_value result = nullptr;
    napi_get_cb_info(env, info, nullptr, nullptr, &jsthis, nullptr);

    napi_unwrap(env, jsthis, reinterpret_cast<void **>(&instance));

    instance->DoSomething();
    return result;
}

static napi_value ParentCreateChild(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value args[1] = {nullptr};
    napi_value jsthis;
    Parent *instanceParent = nullptr;
    bool bRet = false;
    napi_value result = nullptr;
    napi_status status;

    status = napi_get_cb_info(env, info, &argc, args, &jsthis, nullptr);
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_get_cb_info fail.Status:%{public}d", status);
        return nullptr;
    }

    status = napi_unwrap(env, jsthis, reinterpret_cast<void **>(&instanceParent));
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_unwrap fail.Status:%{public}d", status);
        return nullptr;
    }

    status = napi_new_instance(env, args[0], 0, nullptr, &result);
    if (status != napi_ok) {
        OH_LOG_ERROR(LOG_APP, "ParentcreateChild napi_new_instance fail.Status:%{public}d", status);
        return nullptr;
    }

    Child *instanceChild = instanceParent->CreateChild();

    status = napi_wrap(env, result, reinterpret_cast<void *>(instanceChild), DerefChild, NULL, NULL);
    if (status != napi_ok) {
        // 主动释放内存
        OH_LOG_INFO(LOG_APP, "ParentcreateChild ChildConstructor napi_wrap fail status:%{public}d", status);
        delete instanceChild;
    }

    return result;
}

// 定义类Child的构造函数
static napi_value ChildConstructor(napi_env env, napi_callback_info info)
{
    napi_value undefineVar = nullptr;
    napi_get_undefined(env, &undefineVar);
    napi_value jsInstance = nullptr;
    if (napi_get_cb_info(env, info, nullptr, nullptr, &jsInstance, nullptr) != napi_ok) {
    return undefineVar;
}

    Child *instance = new Child();
    napi_status status = napi_wrap(env, jsInstance, reinterpret_cast<void *>(instance), DerefChild, NULL, NULL);
    if (status != napi_ok) {
        // 主动释放内存
        OH_LOG_INFO(LOG_APP, "ChildConstructor napi_wrap fail");
        delete instance;
    }
    OH_LOG_INFO(LOG_APP, "ChildConstructor success");
    return jsInstance;
}

// 定义类Child的方法
static napi_value ChildDoSomething(napi_env env, napi_callback_info info)
{
    napi_value jsthis;
    Child *instance = nullptr;
    bool bRet = false;
    napi_value result = nullptr;
    napi_get_cb_info(env, info, nullptr, nullptr, &jsthis, nullptr);

    napi_unwrap(env, jsthis, reinterpret_cast<void **>(&instance));

    instance->DoSomething();
    return result;
}

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor parentDesc[] = {
        {"doSomething", nullptr, ParentDoSomething, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"createChild", nullptr, ParentCreateChild, nullptr, nullptr, nullptr, napi_default, nullptr}
    };

    napi_property_descriptor childDesc[] = {
        {"doSomething", nullptr, ChildDoSomething, nullptr, nullptr, nullptr, napi_default, nullptr}
    };

    napi_value parentConstructor = nullptr;
    napi_define_class(env, "Parent", NAPI_AUTO_LENGTH, ParentConstructor, nullptr, sizeof(parentDesc) / sizeof(parentDesc[0]),
                      parentDesc, &parentConstructor);
    napi_set_named_property(env, exports, "Parent", parentConstructor);

    napi_value childConstructor = nullptr;
    napi_define_class(env, "Child", NAPI_AUTO_LENGTH, ChildConstructor, nullptr, sizeof(childDesc) / sizeof(childDesc[0]),
                      childDesc, &childConstructor);
    napi_set_named_property(env, exports, "Child", childConstructor);
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

CMakeLists.txt编译脚本：

```screen
# the minimum version of CMake.
cmake_minimum_required(VERSION 3.5.0)
project(MultipleClass)

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

if(DEFINED PACKAGE_FIND_FILE)
include(${PACKAGE_FIND_FILE})
endif()

include_directories(${NATIVERENDER_ROOT_PATH}
${NATIVERENDER_ROOT_PATH}/include)

add_library(entry SHARED napi_init.cpp)
target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```

## 常见FAQ

Q：如何构建一个ArkTS指定对象并调用其构造方法？

A：可以通过[napi\_new\_instance](../harmonyos-guides/use-napi-about-class.md#napi_new_instance)接口调用给定的构造函数实现对象的实例化。

## 总结

通过[napi\_new\_instance](../harmonyos-guides/use-napi-about-class.md#napi_new_instance)可以在native侧创建一个ArkTS的类实例，调用[napi\_wrap](../harmonyos-guides/use-napi-about-class.md#napi_wrap)方法与native实例进行绑定，再将ArkTS的类实例返回，即可实现通过父类创建子类并返回的效果。
