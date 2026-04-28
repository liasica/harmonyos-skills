---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-faq-about-stability
title: 稳定性相关问题汇总
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API常见问题汇总 > 稳定性相关问题汇总
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:901c243d8614867dd2941c36e641f3d1492248022cc974df32ef7a39e5a12978
---

## 应用运行过程中出现高概率闪退怎么进行定位解决

* 具体问题：在使用Node-API开发过程中，应用运行过程中出现高概率闪退，出现cpp crash栈，栈顶为系统库libark\_jsruntime.so，崩溃栈前几帧也有libace\_napi.z.so，怎么进行定位解决？

复现概率高，每次崩溃栈略有区别，但是共性都是：崩溃栈顶是系统库的libark\_jsruntime.so或者libace\_napi.z.so。

* 崩溃信息如下：

```
1. Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x00000136 probably caus
2. Fault thread info:
3. Tid:15894, Name:e.myapplication
4. #00 pc 002b8dd4 /system/lib/platformsdk/libark_jsruntime.so
5. #01 pc 0024d3e1 /system/lib/platformsdk/libark_jsruntime.so
6. #02 pc 0024d0d9 /system/lib/platformsdk/libark_jsruntime.so
7. #03 pc 002eac5d /system/lib/platformsdk/libark_jsruntime.so
8. #04 pc 00428d0f /system/lib/platformsdk/libark_jsruntime.so
```

* 定位问题：

使用Node-API时如果出现高概率闪退，崩溃栈顶在系统库libark\_jsruntime.so，一般是开发者Node-API接口使用不当导致。

* 以下定位问题的思路，可作为参考：

1. 排查是否存在多线程安全问题（概率较大）。

   DevEco Studio中提供了相关开关，开启开关后，重新编译打包并运行，看看崩溃栈是不是符合下面这个文档的描述，如果是，那就是在使用Node-API时，存在多线程安全问题。

   [常见多线程安全问题](../best-practices/bpta-stability-ark-runtime-detection.md#section19357830121120)

   DevEco Studio开关：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/aHsATN85TPG3XJqh90-HDA/zh-cn_image_0000002552799724.png?HW-CC-KV=V1&HW-CC-Date=20260427T235412Z&HW-CC-Expire=86400&HW-CC-Sign=28B10201686FBD26D3AD8973A87440420E828D36B9A46ECEF3957E33F0572B2E)
2. 使用Node-API接口时入参非法导致。

* 这种情况一般是崩溃栈上的so会很浅，so调用了某个具体的Node-API接口，比如调用了napi\_call\_function之类的接口，然后Node-API又调到了libark\_jsruntime的so，然后直接崩溃在libark\_jsruntime里面。

示例栈结构如下。

```
1. #01 /system/lib/platformsdk/libark_jsruntime.so
2. #02 /system/lib/platformsdk/libark_jsruntime.so
3. #03 /system/lib/platformsdk/libace_napi.z.so(napi_set_named_property+170) -- Node-API的so，该位置显示具体调用报错的接口
4. #04 /data/storage/el1/bundle/libs/arm/libentry.so -- 你的so
```

* 如果是入参问题，一般so在崩溃栈上的位置比较浅（不会跑到#10这种离栈顶很远的位置），不过也可以按照这个思路进行排查。
* 排查思路参考：

a. 排查有没有napi\_value未初始化，还没赋值成功，直接作为非法入参传递给接口了。

b. 排查有没有在这个易错API列表里面找到相应的篇章。

可参考文档：

[方舟运行时API](../best-practices/bpta-stability-coding-standard-api.md#section1219614634615)。

## 线程池中并发调用ArkTS方法如何处理线程安全问题

* 现有个场景，ArkTS中有个类方法，对这个方法创建了napi\_ref引用，现想在C++线程池中并发地调用ArkTS方法，有以下几个问题：

1. 可以在C++创建的线程池中调用napi\_ref缓存的ArkTS类方法吗？
2. 回调到ArkTS要怎么确保线程安全？

对于问题一：

只能在C++线程中将ArkTS任务抛回ArkTS线程，这时候并不是同步调用，而是一个抛任务的动作。

需要注意的是，这个ArkTS方法真正的执行动作只能在ArkTS线程中完成，即，只能方法运行在对应的ArkTS线程上。

对于问题二：

上面提到，C++线程都是抛任务到ArkTS线程，进而执行ArkTS方法。关于线程安全，可参考[使用Node-API接口进行线程安全开发](use-napi-thread-safety.md)。

另外，开发过程中也可以打开[方舟多线程检测](../best-practices/bpta-stability-ark-runtime-detection.md#section75786272088)开关，这个开关可以拦截多线程安全问题。

## napi\_value内容产生变化

* 具体描述：在一个程序初始化的时候，保存了env和一个method（napi\_value），这个method在刚刚创建的时候有进行check，napi\_typeof的结果是napi\_function，符合预期。程序运行一段时间后，使用保存的env和method再去调用，发现method check不过了，此时不是一个napi\_function了，保存与使用时均处于同一主线程，要如何解决？
* 排查建议：

1. 确认是否napi\_value出了scope还在使用，导致use-after-scope问题。

   可参考文档：

   [方舟运行时API](../best-practices/bpta-stability-coding-standard-api.md#section1219614634615)。
2. 保存时建议使用napi\_ref，而不是直接保存napi\_value。

## 是否存在获取最新napi\_env的方法

* 具体描述：Native 层在较深的调用层级中需调用 ArkTS 方法，无法逐层传递 napi\_env，直接缓存会导致崩溃。

```
1. #00 /system/lib/platformsdk/libark_jsruntime.so(panda::JSValueRef::IsFunction)
2. #01 /system/lib/platformsdk/libace_napi.z.so(napi_call_function)
3. #02 /data/storage/el1/bundle/libs/arm/libentry.so
4. ...
```

* 参考方案：

1. 关于保存napi\_env：

   Node-API没有提供直接获取napi\_env的能力，只能通过逐层函数调用传递。一般不推荐保存napi\_env，有两个原因：

   其一，napi\_env退出时候如果没有被使用方感知到，很容易出现use-after-free问题；

   其二，napi\_env和ArkTS线程是强绑定的，如果napi\_env放在其它ArkTS线程使用，就会有多线程安全问题。

   可参考文档：

   [napi\_env禁止缓存的原因是什么](../harmonyos-faqs/faqs-ndk-73.md) 。
2. 该问题的关键在于：

   如果要强行保存env，必须感知env是否退出，可以使用napi\_add\_env\_cleanup\_hook的回调进行感知。同时，在开发过程中打开多线程检测开关，避免出现多线程安全问题。

   可参考文档：

   [常见多线程安全问题](../best-practices/bpta-stability-ark-runtime-detection.md#section19357830121120)。
3. 对于崩溃问题本身，该崩溃可能发生在调用napi\_call\_function时，入参 func 有问题，即非法入参，开发者可排查napi\_value是否被缓存。这种情况可能是napi\_value被缓存后，napi\_value超出napi\_handle\_scope作用域导致失效。

   如果有类似逻辑，需使用napi\_ref进行存储，napi\_ref可以延长生命周期。

* 可参考文档：

  [napi\_create\_reference、napi\_delete\_reference](use-napi-life-cycle.md)

  [方舟运行时API](../best-practices/bpta-stability-coding-standard-api.md#section1219614634615)

## napi\_add\_env\_cleanup\_hook调用报错该如何处理

* 具体问题：napi\_add\_env\_cleanup\_hook/napi\_remove\_env\_cleanup\_hook调用报错，该如何处理？

napi\_add\_env\_cleanup\_hook 和 napi\_remove\_env\_cleanup\_hook 调用报错，常见原因和特征日志如下，均为接口使用不当导致。

1. 在env所在的ArkTS线程外使用上述两个接口，导致多线程安全问题。特征报错日志current napi interface cannot run in multi-thread。
2. 调用napi\_add\_env\_cleanup\_hook时，重复使用同一个args注册不同的回调函数，导致后续注册失败问题。该接口第三个入参args是作为接口内部map的key值，当重复注册同一个args的回调时，后续注册动作将会失败，仅第一次注册才会成功。注册失败可能导致后续业务功能异常或崩溃。特征报错日志AddCleanupHook Failed。
3. 调用napi\_remove\_env\_cleanup\_hook时，尝试通过一个不存在（或已被删除）的args删除回调函数，该接口调用失败，出现特征报错日志RemoveCleanupHook Failed。

常见错误场景示例如下：

```
1. void AddEnvCleanupHook(napi_env env)
2. {
3. napi_add_env_cleanup_hook(env, [](void* args) -> void {
4. // cleanup function回调
5. }, env); // env是个通用的数据，即使此处没有重复注册，可能会被其它地方所提前注册，导致该处注册失败。
6. }

8. static napi_value Test(napi_env env, napi_callback_info info)
9. {
10. //第一次注册
11. AddEnvCleanupHook(env);
12. //第二次重复注册
13. AddEnvCleanupHook(env);
14. return nullptr;
15. }
```

* 修复建议：

1. 对于多线程安全问题，需确保调用接口的线程在env所在的ArkTS线程上。
2. 对于注册失败的问题，需由使用者明确待注册的函数。需要保证key值（也就是napi\_add\_env\_cleanup\_hook的第三个入参）是唯一的即可。
3. 对于删除失败的问题，需要使用者确保args已注册过且未被删除。

相关参考资料链接：

[使用Node-API接口注册和使用环境清理钩子](use-napi-about-cleanuphook.md)

[方舟运行时API](../best-practices/bpta-stability-coding-standard-api.md#section1219614634615)

## napi\_open\_handle\_scope与napi\_close\_handle\_scope进行生命周期相关开发典型错误场景

* 具体问题：使用napi\_open\_handle\_scope与napi\_close\_handle\_scope接口管理ArkTS对象时出现稳定性问题，该如何处理？

napi\_open\_handle\_scope 和 napi\_close\_handle\_scope 调用出现稳定性问题，常见原因如下，均为接口使用不当导致。

1. 未配对使用napi\_open\_handle\_scope 和 napi\_close\_handle\_scope，只打开了一个scope而没有关闭，会导致内存泄漏，且可能触发程序崩溃。
2. 未按照与打开scope顺序相反的顺序关闭scope，可能引发踩内存问题。在例如open\_scope1，open\_scope2，close\_scope1，close\_scope2这种场景下，close\_scope1之后指针返回，极有可能覆写scope2中的内存造成踩内存问题。
3. 在native方法中创建的scope未在该方法返回之前被关闭，导致函数重入时scope配对混乱，发生稳定性问题。

常见错误场景示例如下：

```
1. #include "napi/native_api.h"
2. #include <hilog/log.h>

4. // 1. 全局Scope
5. static napi_handle_scope g_globalScope = nullptr;

7. static napi_value CallFunction(napi_env env, napi_callback_info info) {
8. size_t argc = 1;
9. napi_value argv[1] = {nullptr};
10. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

12. napi_valuetype type = napi_undefined;
13. if (argv[0] == nullptr || napi_typeof(env, argv[0], &type) != napi_ok || type != napi_function) {
14. OH_LOG_INFO(LOG_APP, "JS函数参数非法");
15. napi_value errRet = nullptr;
16. napi_create_int32(env, -1, &errRet);
17. return errRet;
18. }

20. if (!g_globalScope) {
21. OH_LOG_INFO(LOG_APP, "【首次调用】全局Scope为空，执行open");
22. napi_open_handle_scope(env, &g_globalScope);
23. // 首次调用：执行JS函数
24. napi_value global = nullptr;
25. napi_get_global(env, &global);
26. napi_value result = nullptr;
27. napi_call_function(env, global, argv[0], argc, argv, &result);
28. return result; // 首次调用直接返回，不执行后续close逻辑
29. } else {
30. // 重入调用：直接返回固定值 + 关闭Scope
31. napi_value result = nullptr;
32. napi_create_int32(env, 10, &result);
33. OH_LOG_INFO(LOG_APP, "【重入调用】全局Scope非空，执行close");
34. napi_close_handle_scope(env, g_globalScope);
35. g_globalScope = nullptr;
36. return result;
37. }
38. }
```

接口声明

```
1. // index.d.ts
2. export const callFunction : (func : Function) => void;
```

ArkTS侧示例代码

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import testNapi from 'libentry.so';

4. function reenterFunc(count = 1) : void{
5. hilog.info(0x0000, 'testTag', `【JS侧】递归`);
6. if (count <= 0) {
7. return;
8. }
9. testNapi.callFunction(() => reenterFunc(count - 1));
10. hilog.info(0x0000, 'testTag', `【JS侧】重入调用`);
11. return;
12. }

14. try {
15. testNapi.callFunction(reenterFunc);
16. hilog.info(0x0000, 'testTag', '【执行完成】');
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', `调用错误：${error.message}`);
19. }
```

CMakeLists.txt

```
1. cmake_minimum_required(VERSION 3.5.0)
2. project(Test)

4. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

6. if(DEFINED PACKAGE_FIND_FILE)
7. include(${PACKAGE_FIND_FILE})
8. endif()

10. include_directories(${NATIVERENDER_ROOT_PATH}
11. ${NATIVERENDER_ROOT_PATH}/include)

13. add_library(entry SHARED napi_init.cpp)
14. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
15. add_definitions( "-DLOG_TAG=\"testTag\"" )
16. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```

* 修复建议：

1. napi\_open\_handle\_scope和napi\_close\_handle\_scope必须配对使用，开发者应当自查。
2. 所有的scope必须按照与打开顺序相反的顺序关闭。
3. 在native方法中创建的所有scope必须在该方法返回之前被关闭。

相关参考资料链接：

[使用Node-API接口进行生命周期相关开发](use-napi-life-cycle.md#napi_open_handle_scopenapi_close_handle_scope)。
