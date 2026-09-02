---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-function-flow-runtime-3
title: NAPI使用线程安全函数相关问题
breadcrumb: FAQ > 应用框架开发 > NDK开发 > 任务并发调度（Function Flow Runtime） > NAPI使用线程安全函数相关问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:47ddde48d75938bd6440d836b6c419a6168dccdf087dceef415e62427131706e
---

## 问题现象

调用napi\_create\_threadsafe\_function创建ArkTS回调接口和线程安全回调函数，传入线程安全回调函数的ArkTS侧回调接口函数地址为0，无法正确获取到ArkTS侧回调函数的原始值。线程安全回调函数代码如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/rnAhld0YRcCY1xZlRBCaOQ/zh-cn_image_0000002659258291.png "点击放大")

运行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/oJqeq56HQ9SdQTettuoXmA/zh-cn_image_0000002659138351.png "点击放大")

## 背景知识

Node-API线程安全开发主要用于异步多线程之间共享和调用场景中使用，以避免出现竞争条件或死锁。例如以下场景：

* 异步计算：如果需要进行耗时的计算或IO操作，可以创建一个线程安全函数，将计算或IO操作放在另一个线程中执行，避免阻塞主线程，提高程序的响应速度。
* 数据共享：如果多个线程需要访问同一份数据，可以创建一个线程安全函数，确保数据的读写操作不会发生竞争条件或死锁等问题。
* 多线程开发：如果需要进行多线程开发，可以创建一个线程安全函数，确保多个线程之间的通信和同步操作正确无误。

[napi\_create\_threadsafe\_function](../harmonyos-references/napi.md#napi_create_threadsafe_function)：该接口主要用于创建线程安全对象，在创建的过程中，会注册异步过程中的关键信息：ArkTS回调接口callback和线程安全回调函数call\_js\_cb等。参数说明如下：

```cpp
/**
* @brief 用于创建一个线程安全的函数，该函数可以在多个线程中调用，而不需要担心数据竞争或其他线程安全问题
*
* @param env 指向NAPI环境的指针，用于创建和操作Javascript值
* @param func 指向JavaScript函数的指针
* @param async_resource 异步资源，通常是一个表示异步操作的对象
* @param async_resource_name 指向资源名称的指针，这个名称将用于日志和调试
* @param max_queue_size 一个整数，表示队列的最大大小，当队列满时，新的调用将被丢弃
* @param initial_thread_count 无符号整数，表示在创建线程安全函数时，初始的线程数量
* @param thread_finalize_data 一个指向在所有线程之前需要清理的数据
* @param napi_finalize thread_finalize_cb 回调函数，当所有线程完成时被调用，用于清理资源
* @param context 指向上下文的指针，这个上下文将被传递给call_js_func函数
* @param call_js_cb 指向回调函数的指针，这个函数将在Javascript函数被调用时被调用
* @param result 指向napi_threadsafe_function结构的指针，这个结构将被填充为新创建的线程安全函数
*/
napi_status napi_create_threadsafe_function(napi_env env,
                                            napi_value func,
                                            napi_value async_resource,
                                            napi_value async_resource_name,
                                            size_t max_queue_size,
                                            size_t initial_thread_count,
                                            void* thread_finalize_data,
                                            napi_finalize thread_finalize_cb,
                                            void* context,
                                            napi_threadsafe_function_call_js call_js_cb,
                                            napi_threadsafe_function* result);
```

## 问题定位

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/usWvA9QsRjyydHY2WITzQg/zh-cn_image_0000002629059000.png "点击放大")

根据代码分析，发现ArkTS侧回调接口传入到线程安全函数的第三个参数，此参数关联async\_hooks，用来追踪异步资源的API。

## 分析结论

根据napi\_create\_threadsafe\_function线程安全函数参数说明，ArkTS应用侧传入的回调接口应该传入到第二个参数。

## 修改建议

ArkTS应用侧传入的回调接口参数传入到napi\_create\_threadsafe\_function函数的第二个参数。通过线程安全回调函数CallJs执行，通过napi\_call\_function调用ArkTS回调接口，从而将异步计算结果反馈到ArkTS应用侧，用于应用侧UI刷新。示例代码如下：

```cpp
static napi_value StartThread(napi_env env, napi_callback_info info)
{
    size_t argc = 1;
    napi_value jsCb = nullptr;
    CallbackData *callbackData = new CallbackData(); // 异步任务完成时释放
    napi_get_cb_info(env, info, &argc, &jsCb, nullptr, nullptr);

    // 创建一个线程安全函数
    napi_value resourceName = nullptr;
    napi_create_string_utf8(env, "Thread-safe Function Demo", NAPI_AUTO_LENGTH, &resourceName);
    napi_create_threadsafe_function(env, jsCb, nullptr, resourceName, 0, 1, nullptr, nullptr, nullptr, CallJs,
                                    &callbackData->tsfn);

    // 创建一个异步任务
    // ExecuteWork会执行在一个由libuv创建的非JS线程上，此处使用napi_create_async_work是为了模拟在非JS线程场景使用napi_call_threadsafe_function接口向JS线程提交任务
    napi_create_async_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work);

    // 将异步任务加入到异步队列中
    napi_queue_async_work(env, callbackData->work);
    return nullptr;
}
```
