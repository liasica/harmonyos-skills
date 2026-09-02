---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-11
title: 从napi导出的C++类如何在ArkTS侧被派生
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 从napi导出的C++类如何在ArkTS侧被派生
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4edb048de0580fcbf5e9251eeefe9692861863c33d141d4eb3ffbe494f532e3e
---

## 问题现象

从napi导出的C++类，支持在ArkTS侧被派生吗?

如果支持的话，如何在ArkTS侧派生使用从napi导出的C++类，并提供示例Demo。

## 解决方案

napi导出的C++类，支持被派生。

在index.d.ts中，已经提供了ts层的c++接口，所以需要将ArkTS需要使用的C++类，在index.d.ts中声明，才能转为ArkTS侧的父类。

**方法一：使用[AKI](https://gitcode.com/openharmony-sig/aki)的JSBIND\_CLASS接口将C++类绑定到JavaScript环境，再在ArkTS侧用extends继承****：**

1. C++侧：akiusepractice.cpp中定义使用的类结构。

   ```cpp
   #include <aki/jsbind.h>
   #include <hilog/log.h>
   #undef LOG_DOMAIN
   #undef LOG_TAG
   #define LOG_DOMAIN 0x3200  // 全局domain宏，标识业务领域
   #define LOG_TAG "MY_TAG"   // 全局tag宏，标识模块日志tag

   // 类/结构体
   struct Person {
       Person(int mage, std::string mname, double mweight) : age(mage), name(mname), weight(mweight)
       {
           OH_LOG_INFO(LOG_APP, "AkiInfo: Person: age %{public}d", mage);
       }

       std::string sayHello()
       {
           OH_LOG_INFO(LOG_APP, "AkiInfo: SayHello");
           return "hello from Native";
       }
       int age;
       std::string name;
       double weight;
   };

   // 全局函数
   Person MakePerson()
   {
       Person person(91, "aki", 128.8);
       return person;
   }

   // Aki JSBind语法糖
   JSBIND_GLOBAL()
   {
       JSBIND_FUNCTION(MakePerson);
   }

   JSBIND_CLASS(Person)
   {
       JSBIND_CONSTRUCTOR<int, std::string, double>();
       JSBIND_METHOD(sayHello);
       JSBIND_PROPERTY(age);
       JSBIND_PROPERTY(name);
       JSBIND_PROPERTY(weight);
   }

   // TODO：知识点：使用JSBIND_ADDON注册OpenHarmony Native插件，可从JavaScript import导入插件。注册AKI插件名:即为编译*.so名称，规则与NAPI一致。这里注册AKI插件名为:akiusepractice
   JSBIND_ADDON(akiusepractice)
   ```
2. 桥接层：index.d.ts中声明使用的C++类。

   ```ts
   export class Person {
     constructor(age:number, name:string, weight:number);
     sayHello: () => string;
     age: number;
     name: string;
     weight: number;
   }

   export const MakePerson: () => Person;
   ```
3. 在指定路径下（如：项目根路径/entry），输入如下命令安装ohpm har包依赖，该命令会自动将AKI依赖添加到build-profile.json5中。

   ```shell
   cd entry
   ohpm install @ohos/aki
   ```
4. 在CMakeLists.txt中链接AKI库。

   ```ts
   # 设置AKI根路径
   set(AKI_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../../../oh_modules/@ohos/aki)
   # 将CMAKE_MODULE_PATH变量的值设置为AKI_ROOT_PATH变量的值，这样CMake在查找自定义模块时会查看这个路径。
   set(CMAKE_MODULE_PATH ${AKI_ROOT_PATH})
   # 用于查找并加载名为"Aki"的库
   find_package(Aki REQUIRED)
   # 创建并编译一个akiusepractice库
   add_library(akiusepractice SHARED pluginPlan.cpp)
   # 将Aki::libjsbind库链接到akiusepractice
   target_link_libraries(akiusepractice PUBLIC Aki::libjsbind libhilog_ndk.z.so)
   ```
5. ArkTS侧：index.ets中使用派生类。

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so';
   import libAki from 'libakiusepractice.so'; // 导入自定义AKI插件

   const DOMAIN = 0x0000;

   class Man extends libAki.Person {
     sayWord() {
       console.info('AkiInfo ArkTS Hello! Hello!');
     }
   }

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Button(this.message)
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message = 'Welcome';
               hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
             })
           Button("aki")
             .onClick(()=>{
               let man = new Man(99, "aki", 128.8);
               man.sayWord();
               hilog.info(DOMAIN, 'testTag', 'AkiInfo Get: %{public}s', man.sayHello());
               libAki.MakePerson();
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

* **方案二****：****通过napi\_define\_class建立ArkTS类与C++侧的映射关系，并将对应的对象挂载到export上导出，后用extends继承。**
  1. C++侧：napi\_init.cpp中定义使用的类结构。

     ```cpp
     /*
      * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
      */
     #include "napi/native_api.h"
     #include <hilog/log.h>
     #include <string>

     // 定义C++的类
     class MyDemo {
     public:
         MyDemo(){};
         explicit MyDemo(std::string name);
         std::string m_name;
         double Add(double a, double b);
         double Sub(double a, double b);
     };

     MyDemo::MyDemo(std::string name)
     {
         this->m_name = name;
     }

     double MyDemo::Add(double a, double b)
     {
         return a + b + 1000;
     }

     double MyDemo::Sub(double a, double b)
     {
         return a - b + 1000;
     }

     // ArkTS对象构造器
     static napi_value JsConstructor(napi_env env, napi_callback_info info)
     {
         // 创建Napi对象
         napi_value jDemo = nullptr;
         size_t argc = 0;
         napi_value args[1] = {0};
         // 获取构造函数的入参
         napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
         // 参数通过args[0]获取
         char name[50];
         size_t result = 0;
         napi_get_value_string_utf8(env, args[0], name, sizeof(name) + 1, &result);
         // 创建C对象
         MyDemo *cDemo = new MyDemo(name);
         OH_LOG_INFO(LOG_APP, "%{public}s", (cDemo->m_name).c_str());
         // 设置JS对象name属性
         napi_set_named_property(env, jDemo, "name", args[0]);
         // 将JS对象与C++对象绑定
         napi_wrap(
             env, jDemo, cDemo,
             // 定义回调函数，用于回收JS对象，用于销毁C++对象并防止内存泄漏
             [](napi_env env, void *finalize_data, void *finalize_hint) {
                 MyDemo *cDemo = (MyDemo *)finalize_data;
                 delete cDemo;
                 cDemo = nullptr;
             },
             nullptr, nullptr);
         return jDemo;
     }

     // ArkTS对象add函数
     static napi_value JsAdd(napi_env env, napi_callback_info info)
     {
         size_t argc = 2;
         napi_value args[2] = {nullptr};
         napi_value jDemo = nullptr;
         napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
         MyDemo *cDemo = nullptr;
         // 将ArkTS对象转换为C对象
         napi_unwrap(env, jDemo, (void **)&cDemo);
         // 获取ArkTS传递的参数
         int value0;
         napi_get_value_int32(env, args[0], &value0);
         int value1;
         napi_get_value_int32(env, args[1], &value1);
         int cResult = cDemo->Add(value0, value1);
         napi_value jResult;
         napi_create_int32(env, cResult, &jResult);
         return jResult;
     }

     // ArkTS对象sub函数
     static napi_value JsSub(napi_env env, napi_callback_info info)
     {
         size_t argc = 2;
         napi_value args[2] = {nullptr};
         napi_value jDemo = nullptr;
         napi_get_cb_info(env, info, &argc, args, &jDemo, nullptr);
         MyDemo *cDemo = nullptr;
         // 将ArkTS对象转换为C对象
         napi_unwrap(env, jDemo, (void **)&cDemo);
         // 获取ArkTS传递的参数
         int value0;
         napi_get_value_int32(env, args[0], &value0);
         int value1;
         napi_get_value_int32(env, args[1], &value1);
         int cResult = cDemo->Sub(value0, value1);
         napi_value jResult;
         napi_create_int32(env, cResult, &jResult);
         return jResult;
     }

     static napi_value Add(napi_env env, napi_callback_info info)
     {
         size_t requireArgc = 2;
         size_t argc = 2;
         napi_value args[2] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         napi_valuetype valuetype0;
         napi_typeof(env, args[0], &valuetype0);
         napi_valuetype valuetype1;
         napi_typeof(env, args[1], &valuetype1);
         int value0;
         napi_get_value_int32(env, args[0], &value0);
         int value1;
         napi_get_value_int32(env, args[1], &value1);
         MyDemo *demo = new MyDemo();
         // 调用类的成员函数
         int result = demo->Add(value0, value1);
         napi_value sum;
         napi_create_int32(env, result, &sum);
         delete demo;
         return sum;
     }

     static napi_value Sub(napi_env env, napi_callback_info info)
     {
         size_t argc = 2;
         napi_value args[2] = {nullptr};
         napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
         napi_valuetype valuetype0;
         napi_typeof(env, args[0], &valuetype0);
         napi_valuetype valuetype1;
         napi_typeof(env, args[1], &valuetype1);
         int value0;
         napi_get_value_int32(env, args[0], &value0);
         int value1;
         napi_get_value_int32(env, args[1], &value1);
         MyDemo *demo = new MyDemo();
         // 调用类的成员函数
         int result = demo->Sub(value0, value1);
         napi_value num;
         napi_create_int32(env, result, &num);
         delete demo;
         return num;
     }

     EXTERN_C_START
     static napi_value Init(napi_env env, napi_value exports)
     {
         napi_property_descriptor desc[] = {
             { "add", nullptr, Add, nullptr, nullptr, nullptr, napi_default, nullptr },
             {"sub", nullptr, Sub, nullptr, nullptr, nullptr, napi_default, nullptr}
         };
         napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);

         // 通过napi_fine_class建立ArkTS类和C++端的映射关系，然后将相应的对象挂载到export上
         napi_property_descriptor classProp[] = {{"add", nullptr, JsAdd, nullptr, nullptr, nullptr, napi_default, nullptr},
                                                 {"sub", nullptr, JsSub, nullptr, nullptr, nullptr, napi_default, nullptr}};
         napi_value jDemo = nullptr;
         const char *jDemoName = "MyDemo";
         // 建立ArkTS构造函数与C++方法之间的关联
         napi_define_class(env, jDemoName, sizeof(jDemoName), JsConstructor, nullptr,
                           sizeof(classProp) / sizeof(classProp[0]), classProp, &jDemo);
         napi_set_named_property(env, exports, jDemoName, jDemo);
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
  2. 桥接层：index.d.ts中声明使用的C++类。

     ```ts
     declare namespace testNapi {
       const add: (a: number, b: number) => number;
       const sub: (a: number, b: number) => number;
       // 定义ArkTS接口
       class MyDemo {
         constructor(name:string)
         name: string
         add(a: number, b: number): number
         sub(a: number, b: number): number
       }
     }
     export default testNapi;
     ```
  3. ArkTS侧：index.ets中使用派生类。

     ```ts
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import testNapi from 'libentry.so';

     class Employee extends testNapi.MyDemo { // 继承C++的类
       salary: number = 0;
       calculateTaxes(): number {
         return this.salary * 0.42;
       }
     }

     @Entry
     @Component
     struct Index {

       build() {
         Row() {
           Column() {
             Text('Hello World')
               .fontSize($r('app.float.page_text_font_size'))
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                 let em = new Employee('abc');
                 hilog.info(0x0000, 'testTag', 'Employee 1000 + 8 + 9 = %{public}d', em.add(8,9));
                 hilog.info(0x0000, 'testTag', 'Employee 1000 + 10 - 3 = %{public}d', em.sub(10, 3));
               })
           }
           .width('100%')
         }
         .height('100%')
       }
     }
     ```

## 总结

napi导出的C++类，支持被派生。
