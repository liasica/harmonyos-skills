---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-development-21
title: 如何将C++中的复杂类传递至ArkTS
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何将C++中的复杂类传递至ArkTS
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:35+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f23f3ef84c80235f77408fd634be56245efd01bf1254269c35f658c89e0dcd72
---

## 问题现象

1. HarmonyOS项目中，如何从C++侧向ArkTS侧传递包含子对象和对象数组的复合类型？
2. Native侧导出的多个类中包含相同的方法，如何在Index.d.ts文件以及napi\_init.cpp文件中做区分？

## 背景知识

[NDK开发](../harmonyos-guides/ndk-development-overview.md)是HarmonyOS SDK提供的Native API、相应编译脚本和编译工具链的集合，方便开发者使用C或C++语言实现应用的关键功能。

## 解决方案

### 场景一：从C++侧向ArkTS侧传递包含子对象和对象数组的复合类型。

在NDK开发中，当需要从C++向ArkTS传递包含子对象和对象数组的复合类型时，需使用Node-API的对象构建接口，具体示例如下：

1. C++侧传递代码：

   ```cpp
   #include "napi/native_api.h"

   // 创建SubObj对象
   napi_value CreateSubObj(napi_env env, int age) 
   {
       napi_value subObj;
       napi_create_object(env, &subObj);

       napi_value ageValue;
       napi_create_int32(env, age, &ageValue);
       napi_set_named_property(env, subObj, "age", ageValue);

       return subObj;
   }

   // 创建SuperObj对象
   static napi_value CreateSuperObj(napi_env env, napi_callback_info info) 
   {
       // 创建主对象
       napi_value superObj;
       napi_create_object(env, &superObj);

       // 添加基础属性
       napi_value mainAge;
       napi_create_int32(env, 40, &mainAge);
       napi_set_named_property(env, superObj, "age", mainAge);

       // 添加子对象
       napi_value subObj = CreateSubObj(env, 25);
       napi_set_named_property(env, superObj, "subObj", subObj);

       // 创建子对象数组
       napi_value subObjs;
       napi_create_array(env, &subObjs);

       // 向数组添加元素
       for (int i = 0; i < 3; i++) {
           napi_value item = CreateSubObj(env, i + 10);
           napi_set_element(env, subObjs, i, item);    
       }
       napi_set_named_property(env, superObj, "subObjs", subObjs);

       return superObj;
   }

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "createSuperObj", nullptr, CreateSuperObj, nullptr, nullptr, nullptr, napi_default, nullptr }
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
2. Index.d.ts文件接口声明：

   ```ts
   export type SubObj = {
     age: number;
   }

   export type SuperObj = {
     subObj: SubObj;
     subObjs: SubObj[];
     age: number;
   }

   export const createSuperObj: () => SuperObj;
   ```
3. ArkTS接收侧代码：

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so';

   const DOMAIN = 0x0000;

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     superObj = testNapi.createSuperObj();

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               this.message = 'Welcome';
               hilog.info(DOMAIN, 'testTag', 'Main age: %{public}d', this.superObj.age);
               hilog.info(DOMAIN, 'testTag', 'SubObj age: %{public}d', this.superObj.subObj.age);
               hilog.info(DOMAIN, 'testTag', 'First subObj in array: %{public}d',
                 this.superObj.subObjs[0].age);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

### 场景二：从C++侧向ArkTS侧导出多个包含相同方法的类。

Native侧导出多个包含相同方法的类时，可以分别在每个类中单独实现注册函数用于方法导出，完整示例代码如下：

1. Native侧分别实现注册函数：

   ```cpp
   #include "napi/native_api.h"
   #include "hilog/log.h"

   class SameClassOne {
   public:
       static napi_value Constructor(napi_env env, napi_callback_info info);
       static napi_value Add(napi_env env, napi_callback_info info);
       static void Init(napi_env env, napi_value exports);
   };

   class SameClassTwo {
   public:
       static napi_value Constructor(napi_env env, napi_callback_info info);
       static napi_value Add(napi_env env, napi_callback_info info);
       static void Init(napi_env env, napi_value exports);
   };

   napi_value SameClassOne::Constructor(napi_env env, napi_callback_info info) 
   {
       OH_LOG_INFO(LOG_APP, "enter SameClassOne::Constructor");

       napi_value jsthis;
       napi_get_cb_info(env, info, 0, nullptr, &jsthis, nullptr);

       return jsthis;
   }

   napi_value SameClassOne::Add(napi_env env, napi_callback_info info) 
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

   void SameClassOne::Init(napi_env env, napi_value exports) 
   {
       OH_LOG_INFO(LOG_APP, "SameClassOne::Init");
       napi_status result = napi_ok;
       napi_property_descriptor desc[] = {
           {"Add", nullptr, SameClassOne::Add, nullptr, nullptr, nullptr, napi_default, nullptr}};

       napi_value sameClassOne;
       result = napi_define_class(env, "SameClassOne", NAPI_AUTO_LENGTH, SameClassOne::Constructor, nullptr,
                                  sizeof(desc) / sizeof(desc[0]), desc, &sameClassOne);

       result = napi_set_named_property(env, exports, "SameClassOne", sameClassOne);

       return;
   }

   napi_value SameClassTwo::Constructor(napi_env env, napi_callback_info info) 
   {
       OH_LOG_INFO(LOG_APP, "enter SameClassTwo::Constructor");

       napi_value jsthis;
       napi_get_cb_info(env, info, 0, nullptr, &jsthis, nullptr);

       return jsthis;
   }

   napi_value SameClassTwo::Add(napi_env env, napi_callback_info info) 
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

   void SameClassTwo::Init(napi_env env, napi_value exports) 
   {
       OH_LOG_INFO(LOG_APP, "SameClassTwo::Init");
       napi_status result = napi_ok;
       napi_property_descriptor desc[] = {
           {"Add", nullptr, SameClassTwo::Add, nullptr, nullptr, nullptr, napi_default, nullptr}};

       napi_value sameClassTwo;
       result = napi_define_class(env, "SameClassTwo", NAPI_AUTO_LENGTH, SameClassTwo::Constructor, nullptr,
                                  sizeof(desc) / sizeof(desc[0]), desc, &sameClassTwo);

       result = napi_set_named_property(env, exports, "SameClassTwo", sameClassTwo);

       return;
   }

   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports) 
   {

       SameClassOne::Init(env, exports);
       SameClassTwo::Init(env, exports);
       return exports;
   }
   EXTERN_C_END

   static napi_module demoModule = {
       .nm_version = 1,
       .nm_flags = 0,
       .nm_filename = nullptr,
       .nm_register_func = Init,
       .nm_modname = "library",
       .nm_priv = ((void *)0),
       .reserved = {0},
   };

   extern "C" __attribute__((constructor)) void RegisterLibraryModule(void) { napi_module_register(&demoModule); }
   ```
2. 在Index.d.ts文件中声明方法：

   ```ts
   export class SameClassOne {
     constructor();

     Add(a: number, b: number);
   }

   export class SameClassTwo {
     constructor();

     Add(a: number, b: number);
   }
   ```
3. ArkTS侧调用：

   ```ts
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'liblibrary.so';

   const DOMAIN = 0x0000;

   @Component
   export struct MainPage {
     @State message: string = 'Hello World';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               let sameClassOne: testNapi.SameClassOne = new testNapi.SameClassOne();
               let sameClassTwo: testNapi.SameClassTwo = new testNapi.SameClassTwo();
               this.message = 'Welcome';
               hilog.info(DOMAIN, 'testTag', 'sameClassOne 2 + 3 = %{public}d', sameClassOne.Add(2, 3));
               hilog.info(DOMAIN, 'testTag', 'sameClassTwo 3 + 4 = %{public}d', sameClassTwo.Add(3, 4));
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

## FAQ

Q：如何在使用NAPI接口导出两个类的同时定义两个类的继承关系？

A：当前NAPI未提供实现继承对象的方法。可以参考JavaScript修改原型链的方法，达到类似的效果：

```js
// 定义构造函数
function Person(name, age) {
    this.name = name
    this.age = age
}

Person.prototype.running = function () {
    console.info("跑步")
}
Person.prototype.eatting = function () {
    console.info("吃饭")
}

// 定义学生类
function Student(name, age, sno, score) {
    this.name = name
    this.age = age
    this.sno = sno
    this.score = score
}

// 创建一个父类的实例对象(new Person())用这个实例对象来作为子类的原型对象
let p1 = new Person()

Student.prototype = p1

Student.prototype.studying = function () {
    console.info("学习")
}

// 实现方法继承
let stu1 = new Student("hdc", 21, 111, 100)
stu1.running() // 跑步
```
