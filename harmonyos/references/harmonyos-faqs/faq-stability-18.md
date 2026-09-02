---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-18
title: 线程泄漏问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 线程泄漏问题定位
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:b8eb4d964b26c7e0a298272e469884877e57e057c8e1b7ed89ed4a4a516512a1
---

## 问题现象

应用在使用过程中出现闪退。

## 背景知识

* 线程泄漏：60s一次遍历进程，获取进程的总线程数，超过阈值（700个）时抓取详细线程名信息，同步上报泄漏，参考文档[实现原理](../harmonyos-guides/resource-leak-guidelines.md#实现原理)。
* 线程泄漏日志规格可以参考[线程泄漏日志规格](../harmonyos-guides/resource-leak-guidelines.md#线程泄漏日志规格)说明。
* 详细分析方法可见[线程泄漏分析方法](../best-practices/bpta-stability-leak-way.md#section282262074411)。

## 问题定位

1. 从日志中可以看出，应用进程的总线程数达到了703个，超过了阈值700个。

   ```screen
   time: 2024/12/20 23:41:08
   pid: 55855
   vss: 57201248
   rss: 478548
   process: com.hx.example
   summary: 703
   Top 10 Thread Name:
   621 com.hx.example
   9  ThreadPoolForeg
   8  OS_FFRT_3_2
   6  ThreadPoolSingl
   5  OS_GC_Thread
   3  gpu-work-client
   2  OS_NET_HttpWork
   ```
2. 查看应用线程堆栈信息，可以看到线程都处于等锁状态unique\_lock，并且线程全部归属于libpdfservice.z.so库创建\_\_thread\_proxy。

   ```screen
   Tid:2478, Name:com.hx.example
   #00 pc 00000000001b6510 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #01 pc 00000000001b8514 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #02 pc 00000000000c1124 /system/lib64/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+20)(dfedb06268d7f896c86362ced8e6c5c77e36a0da)
   #03 pc 00000000000e6980 /system/lib64/module/hms/officeservice/libpdfservice.z.so(void* std::__h::__thread_proxy[abi:v15004]<std::__h::tuple<std::__h::unique_ptr<std::__h::__thread_struct, std::__h::default_delete<std::__h::__thread_struct>>, DocumentBaseST::DocumentBaseST(IPDF_Document*)::$_0>>(void*)+324)(d02bcdfd65731d541761e17057ebf133)
   #04 pc 00000000001bac20 /system/lib/ld-musl-aarch64.so.1(start+236)(fbb1eb526bb54f59c5dc4f2521b68e52)
   Tid:3591, Name:com.hx.example
   #00 pc 00000000001b6510 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #01 pc 00000000001b8514 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #02 pc 00000000000c1124 /system/lib64/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+20)(dfedb06268d7f896c86362ced8e6c5c77e36a0da)
   #03 pc 00000000000951ac /system/lib64/module/hms/officeservice/libpdfservice.z.so(void std::__h::condition_variable_any::wait<std::__h::unique_lock<std::__h::mutex>>(std::__h::unique_lock<std::__h::mutex>&)+108)(d02bcdfd65731d541761e17057ebf133)
   #04 pc 0000000000092dd8 /system/lib64/module/hms/officeservice/libpdfservice.z.so(coro::thread_pool::executor(unsigned long)+156)(d02bcdfd65731d541761e17057ebf133)
   #05 pc 0000000000094d2c /system/lib64/module/hms/officeservice/libpdfservice.z.so(void* std::__h::__thread_proxy[abi:v15004]<std::__h::tuple<std::__h::unique_ptr<std::__h::__thread_struct, std::__h::default_delete<std::__h::__thread_struct>>, coro::thread_pool::thread_pool(coro::thread_pool::options)::$_0>>(void*)+68)(d02bcdfd65731d541761e17057ebf133)
   #06 pc 00000000001bac20 /system/lib/ld-musl-aarch64.so.1(start+236)(fbb1eb526bb54f59c5dc4f2521b68e52)
   Tid:2478, Name:com.hx.example
   #00 pc 00000000001b6510 /system/lib/ld-musl-aarch64.so.1(__timedwait_cp+192)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #01 pc 00000000001b8514 /system/lib/ld-musl-aarch64.so.1(__pthread_cond_timedwait+188)(fbb1eb526bb54f59c5dc4f2521b68e52)
   #02 pc 00000000000c1124 /system/lib64/libc++.so(std::__h::condition_variable::wait(std::__h::unique_lock<std::__h::mutex>&)+20)(dfedb06268d7f896c86362ced8e6c5c77e36a0da)
   #03 pc 00000000000e6980 /system/lib64/module/hms/officeservice/libpdfservice.z.so(void* std::__h::__thread_proxy[abi:v15004]<std::__h::tuple<std::__h::unique_ptr<std::__h::__thread_struct, std::__h::default_delete<std::__h::__thread_struct>>, DocumentBaseST::DocumentBaseST(IPDF_Document*)::$_0>>(void*)+324)(d02bcdfd65731d541761e17057ebf133)
   #04 pc 00000000001bac20 /system/lib/ld-musl-aarch64.so.1(start+236)(fbb1eb526bb54f59c5dc4f2521b68e52)
   ```

## 分析结论

应用创建大量线程且都处于等锁状态导致线程泄漏。

## 修改建议

降低线程池大小，避免大量线程同时存在，更多参考[线程泄漏问题优化建议](../best-practices/bpta-stability-leak-opt.md#section10137113593613)。

确保锁得到正确的管理，在异常分支提前返回时释放互斥锁。更多参考[优化建议1：多线程操作锁时，需要合理使用lock\_guard这类自动控制持锁和释放锁的管理方式](../best-practices/bpta-stability-app-freeze-opt.md#section395763916392)。
