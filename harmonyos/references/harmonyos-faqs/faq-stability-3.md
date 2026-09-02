---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-3
title: 用户打开视频播放时，应用发生闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 用户打开视频播放时，应用发生闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2cd30df752de287d96cf9d8341ece72dde15434848ae9b55514cb5262737942
---

## 问题现象

应用播放视频时，无法播放直接闪退。

## 背景知识

* CppCrash进程崩溃检测基于操作系统信号机制，目前支持的崩溃信号参考[Cpp Crash（进程崩溃）检测](../harmonyos-guides/cppcrash-guidelines.md)。
* JsCrash异常根据不同的异常场景，在Reason字段进行了分类，分为Error、TypeError、SyntaxError、ReferenceError、RangeError等错误类型。参考文档[JS Crash（进程崩溃）检测](../harmonyos-guides/jscrash-guidelines.md)。
* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。

## 问题定位

1. 闪退问题首先排查是否出现JsCrash，CppCrash以及AppFreeze文件，查看faultlogger目录，是否生成了形如jscrash-应用包名/cppcrash-应用包名/appfreeze-应用包名的故障日志。如果存在则进入对应日志查看故障信息。
2. 在日志内查看对应信息：
   * 故障分类是CppCrash，故障根因是SIGSEGV。

     从故障日志可以看出，栈顶基础库ld-musl-aarch64的调用链sprintf->vfprintf->printf\_core->strnlen，这是在操作格式化字符串到缓冲区，下一个栈帧是libplay\_logic\_library.so，PlayerOption对象执行toString方法，当PlayerOption对象中的成员变量未正确初始化，调用toString方法时，就会在栈顶strnlen函数(计算字符串长度)出现空指针异常。

     ```screen
     Process name:com.hm.example
     Process life time:4832s
     Reason:Signal:SIGSEGV(SEGV_MAPERR)@0x0000007e00000000
     Fault thread info:
     Tid:22654, Name:com.hm.example
     #00 pc 00000000000a4f10 /system/lib/ld-musl-aarch64.so.1(strnlen+16)(2af53e742fb0df4341adb4e9ae0f0054)
     #01 pc 00000000001a6830 /system/lib/ld-musl-aarch64.so.1(printf_core+2180)(2af53e742fb0df4341adb4e9ae0f0054)
     #02 pc 00000000001a5e24 /system/lib/ld-musl-aarch64.so.1(vfprintf+188)(2af53e742fb0df4341adb4e9ae0f0054)
     #03 pc 00000000001a4b84 /system/lib/ld-musl-aarch64.so.1(sprintf+212)(2af53e742fb0df4341adb4e9ae0f0054)
     #04 pc 000000000003f934 /data/storage/el1/bundle/libs/arm64/libplay_logic_library.so(PlayerOption::toString()+404)(2d78355f9595418980b6aace1ea3685860608a19)
     ```
   * 故障分类是JsCrash，故障原因是TypeError。

     异常信息是Error message：Cannot read property XXX of undefined。

     ```screen
     Reason:TypeError
     Error name:TypeError
     Error message:Cannot read property length of undefined
     Stacktrace:
     Cannot get SourceMap info, dump raw stack:
         at anonymous (entry|entry|1.0.0|src/main/ets/pages/MediaPlayer.ts:569:1)
     ```

     从异常信息可以看出，变量不是预期的类型。
   * 故障分类是AppFreeze。

     从日志中可以看出当前故障模块进程号是：47988，故障原因是THREAD\_BLOCK\_6S(应用主线程卡死)，故障发生的时间点是20240627092725。

     ```screen
     Pid:47988
     Uid:20020143
     Reason:THREAD_BLOCK_6S
     appfreeze: com.hm.example THREAD_BLOCK_6S at 20240627092725
     DisplayPowerInfo:powerState:AWAKE
     ```

     在日志中搜索关键字THREAD\_BLOCK\_3S和THREAD\_BLOCK\_6S，找到Tid:应用进程号,Name:应用包名下的堆栈信息。

     ```screen
     Tid:47988, Name:com.hm.example
     #00 pc 000000000056a540 /data/storage/el1/bundle/libs/arm64/libijkffmpeg.z.so(av_buffer_unref+60)(0e10837e2bdb99cbff68006c6e49e517)
     #01 pc 000000000026364c /data/storage/el1/bundle/libs/arm64/libijkffmpeg.z.so(av_packet_unref+88)(0e10837e2bdb99cbff68006c6e49e517)
     #02 pc 0000000000031524 /data/storage/el1/bundle/libs/arm64/libijkplayer.so(packet_queue_flush+80)(190419e211fa912da795fa2ee2cb02b1685dd3d6)
     #03 pc 000000000003ce60 /data/storage/el1/bundle/libs/arm64/libijkplayer.so(decoder_abort+72)(190419e211fa912da795fa2ee2cb02b1685dd3d6)
     ```

     两个堆栈信息完全一致，堆栈的栈顶为libijkffmpeg.z.so，需要结合代码对该so库进行后续的分析和排查。

## 分析结论

* 故障根因是SIGSEGV。

  调用so库时产生非法内存访问，导致出现闪退。
* 故障根因是JsCrash-TypeError。

  异常信息是Error message：Cannot read property XXX of undefined。变量不是预期的类型，不能调用对应的属性，导致JsCrash闪退。
* 故障根因是THREAD\_BLOCK\_6S。

  故障so库业务时间过长被判定为应用卡死，为了保证系统可恢复，用户能正常使用，系统会杀死应用。

## 修改建议

* 故障根因是SIGSEGV。

  故障so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
* 故障根因是JsCrash-TypeError。

  异常信息是Error message：Cannot read property XXX of undefined。

  在使用变量前进行校验，检查变量是否存在对应的属性。
* 故障根因是THREAD\_BLOCK\_6S。

  故障so库使用[hstack](../harmonyos-guides/ide-command-line-hstack.md)解析崩溃栈后结合具体代码进行分析。
