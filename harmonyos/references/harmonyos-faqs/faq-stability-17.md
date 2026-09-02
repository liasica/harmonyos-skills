---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-17
title: 应用刷新页面时出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用刷新页面时出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:059e929ccd6179597e52eff1033d34ffff2bb230a3b23aa2f1eea86ef9bc3d6a
---

## 问题现象

刷新页面时，应用出现闪退现象。

## 背景知识

* 地址越界问题是指访问了不合法的地址，导致程序运行出现异常，通常表现为应用崩溃（crash）。其故障原因为释放后使用（use after free）、重复释放（double-free）、栈溢出（stack-overflow）、堆溢出（heap-overflow）等，参考[地址越界类问题分析方法](../best-practices/bpta-stability-address-illegal-way.md)。
* 地址越界问题通常表现为应用崩溃闪退（crash），没有显式的故障特征可以直接确定是地址越界问题。地址越界问题判断依据包括：问题多次低概率持续发生，崩溃栈顶无规律，同一个崩溃栈顶源码无规律。
* 地址越界问题分类可以参考[地址越界事件介绍](../harmonyos-guides/hiappevent-watcher-address-sanitizer-events.md)。

## 问题定位

1. 查看崩溃堆栈，可以发现每次产生崩溃栈都不一样，无规律，预计发生了地址越界问题。

   ```screen
   Process name:com.hx.example
   Process life time:8s
   Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x00424b7474326a9d 
   Fault thread info:
   Tid:63354, Name:com.hx.example
   #00 pc 000000000002b9ec /data/storage/el1/bundle/libs/arm64/libutunnel.so(token_report_handler(int, int, void*)+56)(95e2a68a228022f77283aefa824ad2d9381307a7)
   #01 pc 000000000002aab8 /data/storage/el1/bundle/libs/arm64/libutunnel.so(msg_idle_cb(uv_idle_s*)+32)(95e2a68a228022f77283aefa824ad2d9381307a7)
   #02 pc 000000000001db98 /system/lib64/platformsdk/libuv.so(uv__run_idle+228)(7f3f0c53ff27176dc061e331a1525b34)
   #03 pc 0000000000017000 /system/lib64/platformsdk/libuv.so(uv_run+360)(7f3f0c53ff27176dc061e331a1525b34)
   #04 pc 000000000002abd8 /data/storage/el1/bundle/libs/arm64/libutunnel.so(thread_func(void*)+228)(95e2a68a228022f77283aefa824ad2d9381307a7)
   #05 pc 00000000001bada8 /system/lib/ld-musl-aarch64.so.1(start+236)(c05a4bdaf3657c3186f06e417c4fa802)
   ```

   ```screen
   Process name:com.hx.example 
   Process life time:7s 
   Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x006b6b5b016cd3c8  
   Fault thread info: 
   Tid:44438, Name:com.hx.example 
   #00 pc 0000000002ee5f88 /system/lib64/platformsdk/libace_compatible.z.so(87e797bd4d27e4b60838ea50d45176d8) 
   #01 pc 00000000008fd07c /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::TaskExecutorImpl::OnPostTask(std::__h::function<void ()>&&, OHOS::Ace::TaskExecutor::TaskType, unsigned int, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>> const&, OHOS::Ace::PriorityType) const+252)(87e797bd4d27e4b60838ea50d45176d8) 
   #02 pc 0000000002ee42ac /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiXComponentBridge::~JsiXComponentBridge()+272)(87e797bd4d27e4b60838ea50d45176d8) 
   #03 pc 0000000002ee4410 /system/lib64/platformsdk/libace_compatible.z.so(OHOS::Ace::Framework::JsiXComponentBridge::~JsiXComponentBridge()+16)(87e797bd4d27e4b60838ea50d45176d8)
   ```
2. 地址越界问题可以通过[使用HWAsan检测内存错误](../best-practices/bpta-stability-hwasan-detection.md)等工具检测出。
3. 开发态配置好HWAsan后，调试当前应用。当程序出现内存错误时，弹出HWAsan log信息，点击信息中的链接即可跳转至引起内存错误的代码处，以下示例可供参考。

   ```screen
   Module name:com.hx.example
   Version:1.0.0
   Pid:36316
   Uid:20020251
   Reason:use-after-free
   ==appspawn==36316==ERROR: HWAddressSanitizer: tag-mismatch on address 0xXXXX at pc 0x0069136867e4
   READ of size 4 at 0xXXXX tags: c4/26 (ptr/mem) in thread T0
       #0 0x69136867e4  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x67e4) (BuildId: d35146dc167c816454c7e906c4aa5fb00d0f5c7d) <-- 故障链接
       #1 0x691368665c  (/data/storage/el1/bundle/libs/arm64/libentry.so+0x665c) (BuildId: d35146dc167c816454c7e906c4aa5fb00d0f5c7d)
       #2 0x5efeabec44  (/system/lib64/platformsdk/libace_napi.z.so+0x3ec44) (BuildId: 37dfa4be8ab42a21d0511559b6a4b6de)
   ```

   ```screen
   // 错误示例
   static int TestUAF() 
   {
       int* a = new int[2]{1, 2};
       delete[] a; 
       int sum = a[0] + a[1]; // 引起内存错误代码行，使用已经被释放的内存
       return sum;
   }
   ```

## 分析结论

应用访问了不合法的地址导致出现闪退。

## 修改建议

[使用HWAsan检测内存错误](../best-practices/bpta-stability-hwasan-detection.md)，修复引起内存错误的代码。
