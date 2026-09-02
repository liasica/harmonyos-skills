---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-12
title: HarmonyOS应用ArkTS老年代空间超限引发OOM内存溢出的定位与解决方案
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > HarmonyOS应用ArkTS老年代空间超限引发OOM内存溢出的定位与解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:677a423964ac353f0ee04bd49747baf6337d2e07438128f33c3d8a470d6cb902
---

## 问题现象

应用使用过程中，经常性闪退和无响应。

## 背景知识

* 内存溢出(Out Of Memory，简称OOM)是指应用系统中存在无法回收的内存或使用的内存过多，最终使得程序运行要用到的内存大于能提供的最大内存。
* [Heap](../harmonyos-guides/gc-introduction.md#heap)中分为不同的空间，当某个空间的内存达到上限后再次分配内存时会产生OOM问题。
* 可以通过[Snapshot分析模板](../harmonyos-guides/ide-insight-session-snapshot.md)去定位OOM问题。
* 由于隐私安全政策，已上架应用市场的应用不支持使用Snapshot分析模板。

## 问题定位

1. 查看faultlogger目录下的崩溃日志，从日志中可以看出执行AllocateHugeObject函数时抛出OOM异常。

   老年代和大对象空间初始化时均设定为Heap剩余未分配空间的大小，默认手机设备主线程OldSpaceSize上限接近350MB。所以应用分配的内存超过了350M就会出现OOM。

   ```txt
   Process life time:2688s
   Reason:Signal:SIGABRT(SI_TKILL)@0x01317bbb000035ed from:13805:20020155
   LastFatalMessage:[gc] HandleUncatchableError:590 Out of Memory
   Fault thread info:
   Tid:13805, Name:com.hx.example
   #00 pc 000000000019a3dc /system/lib/ld-musl-aarch64.so.1(raise+228)(952d1375b95e66d7b43a1e752f4866bd)
   #01 pc 000000000014754c /system/lib/ld-musl-aarch64.so.1(abort+20)(952d1375b95e66d7b43a1e752f4866bd)
   #02 pc 00000000005252a0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::EcmaVM::HandleUncatchableError()+540)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #03 pc 0000000000524560 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::BaseHeap::ThrowOutOfMemoryError(panda::ecmascript::JSThread*, unsigned long, std::__h::basic_string<char, std::__h::char_traits<char>, std::__h::allocator<char>>, bool)+872)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #04 pc 0000000000172494 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::AllocateHugeObject(unsigned long)+296)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #05 pc 0000000000172570 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::Heap::AllocateOldOrHugeObject(panda::ecmascript::JSHClass*, unsigned long)+84)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #06 pc 000000000060eef0 /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewTaggedArrayWithoutInit(unsigned int, panda::ecmascript::MemSpaceType)+196)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #07 pc 0000000000613c0c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::ObjectFactory::NewTaggedArray(unsigned int, panda::ecmascript::JSTaggedValue)+72)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #08 pc 00000000006c0e4c /system/lib64/platformsdk/libark_jsruntime.so(panda::ecmascript::RuntimeStubs::NewTaggedArray(unsigned long, unsigned int, unsigned long)+116)(4ba0b19dff34c54f62fc9ad6efc9db72)
   #09 pc 0000000000403658 /system/lib64/module/arkcompiler/stub.an(RTStub_CallRuntime+40)
   ```
2. 找到稳定复现场景，通过Snapshot分析模板拍摄内存快照，对比操作前后的内存快照，找到泄漏对象。

## 分析结论

应用内存溢出，分配的内存超过空间上限。ArkTS的[SharedHeap](../harmonyos-guides/gc-introduction.md#sharedheap结构)对大对象的空间分配存在阈值上限，手机设备默认分配的空间上限接近350MB，单次申请的对象超过该上限会触发OutOfMemoryError导致应用闪退。

## 修改建议

方案一：通过[Snapshot分析模板](../harmonyos-guides/ide-insight-session-snapshot.md)分析泄漏对象，修复内存溢出问题。

方案二：单次申请内存较大时，尝试分多次申请，将大数据拆分为小批次，每批次处理完毕后及时释放。

方案三：若必须处理数百MB的数据，可将这部分内存放到Native堆，使用Native堆进行存储，通过NAPI只将结果摘要传回ArkTS层。
