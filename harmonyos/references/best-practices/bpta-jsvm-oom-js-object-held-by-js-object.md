---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-jsvm-oom-js-object-held-by-js-object
title: JS对象长期被JS持有导致内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > JSVM OOM故障模式说明 > JS对象长期被JS持有导致内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:2264e9affe297d2c04f43ea35f5ce0138a57db5be5ebf104f92f5bd2397cb7fd
---

JS引擎通过GC机制在JS代码执行结束后释放JS对象所占内存，若想在JS代码执行期间及时释放内存，需由开发者管理JS对象的生命周期。本文通过两种场景分析JS对象内存占用过高导致引擎OOM的问题，并利用堆快照文件展示此类情况的堆内存特征。

## 根因描述

* 在函数内部创建的对象，其生命周期与函数相同；当使用Array、Map、Set、Object、Class等占用内存较大的对象，并结合循环、递归等语法时，容易导致OOM。
* 闭包函数可引用外部临时对象，使对象生命周期延长至与闭包函数相同；当闭包加入微任务队列时，对象生命周期进一步延长至微任务执行完毕。若对象数量过多、单个对象内存占用过大或微任务队列积压，容易导致OOM。

## 内存泄漏分析方法

1. 获取问题场景的Heap Snapshot，使用Chrome浏览器的DevTools展示各类JS对象在内存中的占比。
2. 按内存占比从高到低排序，关注Stack roots、Micro tasks的占用情况。
3. 开发者可结合源码，逐个分析对象的内存占用合理性，定位导致OOM的对象。

## 关键字

在Heap Snapshot引用链中找到以下关键字：

* Stack roots：指函数内部创建的临时变量，在生成Heap Snapshot时归入Stack roots。
* Micro tasks：指通过Promise或queueMicrotask语法加入微任务队列的任务，在生成Heap Snapshot时归入Micro tasks。

## 案例一：创建过大的临时对象导致堆内存泄漏

以下为负向用例，用于说明创建过大的临时变量会造成堆内存泄漏。用例在foo()函数内创建了两个占用内存较大的临时对象，在foo()函数执行结束前，这两个对象所占用的内存都不会释放，导致堆内存使用量保持较高水平。

```javascript
const char *SRC_CALL_NATIVE_STACK = R"JS(
    function foo()
    {
        let largeArray1 = new Array(1024 * 1024 * 20).fill(0);
        heapMgmtTest();
        let LargeArray2 = new Array(1024 * 1024 * 20).fill(0);
    }
    foo();
)JS";

static int32_t TestJsvmStack()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmStack");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;
    JSVM_Value result;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);

    // Execute JS code.
    JSVM_Script script;
    JSVM_Value jsSrc;
    CheckRet(OH_JSVM_CreateStringUtf8(env, SRC_CALL_NATIVE_STACK, JSVM_AUTO_LENGTH, &jsSrc), env);
    JSVM_Status status = OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    if (status != JSVM_OK) {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: Stack compile failed");
    } else {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: Stack compile success: ret is %{public}d", status);
    }
    Check(OH_JSVM_RunScript(env, script, &result));

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);
    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmStack([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmStack();
    return nullptr;
}
```

heapMgmtTest()函数封装了OH\_JSVM\_TakeHeapSnapshot()的调用细节。首次创建临时对象后，调用heapMgmtTest()导出堆内存快照，开发者可通过分析该快照，了解JS函数内临时对象在堆内存快照中的特征，以辅助分析此类问题。

### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](bpta-overview-of-jsvm-oom-fault-modes.md#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。

1. 打开Chrome浏览器，按F12打开DevTools。

2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/QWagjX3sTZC43g-eYyT-Ww/zh-cn_image_0000002707578265.png)

3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见100%的内存分布在Array对象中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/WFlJzE9wTv6DsQhYe4mfkQ/zh-cn_image_0000002677658554.png)

4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/4gJfcERUSraHm4oJbwM2FQ/zh-cn_image_0000002707458415.png)

可见大量内存被Stack roots引用，表明当前内存分布主要集中在栈上局部变量。

5. 结合内存快照中给出的对象类型以及其他信息，梳理内存泄漏对象的生命周期是否合理，是否可以被优化。

### 预防建议

由函数内分配的临时对象引发的OOM，需要检视JS代码，是否在栈上进行了大量的内存分配（如超大数组分配、扩容等），或者是函数递归调用，导致栈上内存始终无法被回收并持续进行累积，最终导致OOM发生。开发者需要梳理业务逻辑，为临时对象给出合理的作用范围与生命周期，降低临时对象的内存占用峰值。

## 案例二：微任务长时间引用临时对象导致内存泄漏

以下为负向用例，用于说明微任务长时间引用临时对象会造成内存泄漏。该用例在longLivedClosure闭包函数内引用了foo()函数内创建的临时对象bigObject，并将longLivedClosure加入微任务队列。foo()函数执行结束后，longLivedClosure成为bigObject的唯一引用，在longLivedClosure执行完成前，bigObject所占内存不会释放，堆内存使用量将保持较高水平。

```javascript
const char *SRC_CALL_NATIVE_MICRO_TASK = R"JS(
    function foo()
    {
        // Create a sufficiently large local object inside the function.
        let bigObject = new Array(1024 * 1024 * 20).fill(0);
        let longLivedClosure = () => {
            // Reference this large object inside the closure.
            console.log(`bigObject length: ${bigObject.length}`);
        };
        // Enqueue the closure into the microtask queue.
        Promise.resolve().then(longLivedClosure);
    }
    // After the foo function finishes execution, its reference to the large object ends,
    // and the closure in the microtask queue becomes the only reference to the large object.
    foo();
    heapMgmtTest();
)JS";

static int32_t TestJsvmMicroTask()
{
    OH_LOG_INFO(LOG_APP, "TestJsvmMicroTask");
    JSVM_InitOptions initOptions = {0};
    JSVM_VM vm;
    JSVM_Env env = nullptr;
    JSVM_VMScope vmScope;
    JSVM_EnvScope envScope;
    JSVM_HandleScope handleScope;
    JSVM_Value result;

    // Initialize the JS engine instance.
    if (g_aa == 0) {
        g_aa++;
        Check(OH_JSVM_Init(&initOptions));
    }

    // Prepare the JSVM environment.
    Check(OH_JSVM_CreateVM(nullptr, &vm));
    Check(OH_JSVM_OpenVMScope(vm, &vmScope));
    Check(OH_JSVM_CreateEnv(vm, sizeof(descriptor) / sizeof(descriptor[0]), descriptor, &env));
    CheckRet(OH_JSVM_OpenEnvScope(env, &envScope), env);
    CheckRet(OH_JSVM_OpenHandleScope(env, &handleScope), env);

    // Execute JS code.
    JSVM_Script script;
    JSVM_Value jsSrc;
    CheckRet(OH_JSVM_CreateStringUtf8(env, SRC_CALL_NATIVE_MICRO_TASK, JSVM_AUTO_LENGTH, &jsSrc), env);
    JSVM_Status status = OH_JSVM_CompileScript(env, jsSrc, nullptr, 0, true, nullptr, &script);
    if (status != JSVM_OK) {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: MicroTask compile failed");
    } else {
        OH_LOG_INFO(LOG_APP, "JSVM OOM Test: MicroTask compile success: ret is %{public}d", status);
    }
    Check(OH_JSVM_RunScript(env, script, &result));

    // Destroy the JSVM environment.
    CheckRet(OH_JSVM_CloseHandleScope(env, handleScope), env);
    CheckRet(OH_JSVM_CloseEnvScope(env, envScope), env);
    Check(OH_JSVM_DestroyEnv(env));
    Check(OH_JSVM_CloseVMScope(vm, vmScope));
    Check(OH_JSVM_DestroyVM(vm));
    return 0;
}

static napi_value RunTestJsvmMicroTask([[maybe_unused]] napi_env env, [[maybe_unused]] napi_callback_info info)
{
    TestJsvmMicroTask();
    return nullptr;
}
```

heapMgmtTest()函数封装了OH\_JSVM\_TakeHeapSnapshot()的调用细节。foo()函数执行后，微任务尚未开始执行，此时调用heapMgmtTest()导出堆内存快照，开发者可通过分析该快照了解微任务队列持有临时对象在堆内存快照上的特征，以辅助分析类似问题。

### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](bpta-overview-of-jsvm-oom-fault-modes.md#section08171224103515)章节中介绍，本节介绍通过Chrome浏览器DevTools分析Heap Snapshot文件的流程。

1. 打开Chrome浏览器，按F12打开DevTools。

2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Cp4SlWUSQWWsNa_rRMgKUw/zh-cn_image_0000002677818404.png)

3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见98%的内存分布在bigObject对象中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/o09zmtqfRPe6sfROWagQLg/zh-cn_image_0000002707578267.png)

4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/CteqFLauSJC1o-aXxynuUA/zh-cn_image_0000002677658556.png)

可见大量内存被Micro tasks引用，表明当前内存分布集中在微任务所引用的变量。

5. 结合内存快照中给出的对象类型以及其他信息，梳理相关Promise或queueMicrotask语法的使用，识别业务逻辑是否存在微任务队列积压、微任务长时间引用外部变量的可能。

### 预防建议

由微任务队列内引发的OOM，需梳理JS代码上下文，分析微任务队列是否长期处于积压状态，或微任务大量持有闭包外的对象引用，且微任务未执行完毕。开发者需对业务场景中Promise或queueMicrotask的使用进行优化。
