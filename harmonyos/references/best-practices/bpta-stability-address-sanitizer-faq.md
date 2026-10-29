---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-faq
title: 适配常见问题
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 地址越界类问题检测 > 适配常见问题
category: best-practices
scraped_at: 2026-10-29T08:03:24+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:de5ad8cb0813e31166361d2e267e2120f4ea6fe4a45548ff33516aa993f4472f
---

## HWASan napi int64转换时存在精度丢失

由于ArkTS/JS语言的语法限制，Number类型的数字使用双精度浮点数表示，只能精确表示范围是[-(2^53 - 1), (2^53 - 1)]的数字，也就是54位二进制。一个64位的地址，有效寻址空间只有低40位。在未开启HWASan时，地址高24位为0，因此可以用Number来表示精确的地址。在开启HWASan后，会在地址的高8位打上随机Tag，最后的地址是一个高8位为Tag，低40位为真实地址的64位数，此时再使用双精度来存储该64位地址，会导致精度丢失，使低40位真实地址发生偏移，并由HWASan检测出地址越界的问题。

Node-API中，使用napi\_create\_int64来将一个64位数转换成TypeScript中的Number类型，精度丢失发生在这里；使用三方库aki进行隐式的转换，底层也调用该接口，因此也会存在精度丢失的情况；

要避免这种情况，请在ArkTS/JS侧使用bigint存储超出Number精度的地址。更换Node-API接口为[napi\_create\_bigint\_int64](../harmonyos-guides/use-napi-about-bigint.md#napi_create_bigint_int64)和[napi\_get\_value\_bigint\_int64](../harmonyos-guides/use-napi-about-bigint.md#napi_get_value_bigint_int64)。

## 应用实现了一套类似HWASan的内存检查机制或使用tag作为类型标记来实现了name box机制，和HWASan产生冲突

HWASan使用了地址的高8位来存储Tag，用于检测踩内存问题。应用自身实现的检查机制也在地址的高8位进行了标记和检查，导致2种方法产生了冲突，需要应用选择适配自身方案或者禁用HWASan。

## HWASan报告heap-buffer-overflow，发现栈难以定位且越界的size过大，如何解决？

当HWASan上报类型为heap-buffer-overflow，分析overflow的堆栈后认为该堆栈踩内存概率比较小时，通常表现为size过大，基于日志和业务分析free和use对应的线程，查看该线程的ringbuffer打印。如下检查主线程为`use`的线程，日志中rb:(102300/102300)，表示ringbuffer设置为102300，且已满。

```screen
// T0:线程ID, stack:栈内存范围, sz:栈大小, tls:线程本地存储范围, rb:ringbuffer状态, records:记录数, tid:系统线程ID
Thread: T0 0x005a00002000 stack: [0x007ed30ba000,0x007ed38b9000) sz: 8384512 tls: [0x0059d8b7df20,0x0059d8b7e738) rb:(102300/102300) records(2033100/o:0) tid: 668
```

这种情况下可考虑对HWASan参数进行调参，调参方法可参考[配置参数](bpta-stability-hwasan-detection.md#section1496994494018)，设置heap\_history\_size\_main\_thread大于当前的个数（如上当前为102300）。

## 使用BinXO对无源码动态库文件进行插桩时出现编译告警，该如何处理？

开启HWASan后，使用BinXO对无源码C/C++动态库进行插桩时，编译日志中可能出现BinXO相关告警，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/kPN5VrfPSGulwNja3SJ1kA/zh-cn_image_0000002797298753.png "点击放大")

此类告警不会直接阻塞编译。对于无法完成插桩的动态库，工具会自动跳过该文件，不影响其他符合条件的动态库继续插桩。具体告警说明如下：

| 错误码 | 错误描述 | 处理建议 |
| --- | --- | --- |
| 0x11801002 | 输入文件大小超过规格限制 | 输入文件大小超过BinXO支持的128M限制，无法完成插桩。建议拆分strip减小文件大小后再进行插桩或者通过excludeSoFromBinXO（参考[nativeLib](../doccenter-deveco-studio/ide-hvigor-cpp.md#section15889929155720)）跳过该文件。 |
| 0x11801003 | 输入文件损坏或缺少相关 ELF 信息 | 无需关注，或者通过excludeSoFromBinXO跳过该文件。 |
| 0x11801004 | 输入文件不是 C/C++ 编译而来 | 无需关注，非BinXO规格内的输入文件，或者通过excludeSoFromBinXO跳过该文件。 |
| 0x11801007 | 输入文件不是标准 ELF 文件 | 无需关注，或者通过excludeSoFromBinXO跳过该文件。 |
| 0x1180100A | 生成输出文件处理失败 | 无需关注，该文件无法被BinXO处理，通过excludeSoFromBinXO跳过该文件。 |
| 0x1180100B | 输出文件的临时文件被占用 | 删除或重命名entry\build\default\intermediates\binxo目录下对应的<输出文件名>.temp文件后重新编译。 |
