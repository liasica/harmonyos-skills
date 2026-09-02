---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-32
title: 应用使用过程中自动退出
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用使用过程中自动退出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:98839bd4547fe62a7acdffd35f18dd32719076bb3900bfcf93dbea8eef37528c
---

## 问题现象

应用在使用过程中出现自动退出的情况，该如何定位？

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)：无需ROOT设备，即可准确、高效地采集到应用运行时的CPU、GPU等性能数据，了解应用的性能状况。

## 问题定位

1. 查看faultlogger目录下的AppFreeze日志，主线程发生卡死，当前任务从08:19:21.148开始执行，到08:19:27.416还未执行结束，执行时间超过6s。

   ```txt
   Main handler dump start time: 2025-07-03 08:19:27.416
   mainHandler dump is:
    EventHandler dump begin curTime: 2025-07-03 08:19:27.416
    Event runner (Thread name = , Thread ID = 61389) is running
    Current Running: start at 2025-07-03 08:19:21.148, Event { send thread = 62421, send time = 2025-07-03 08:19:21.148, handle time = 2025-07-03 08:19:21.148, trigger time = 2025-07-03 08:19:21.148, task name = , caller = [native_safe_async_work.cpp(PostTask:451)] }
    History event queue information:
   ```
2. 搜索关键字TID:进程ID(PID)，获取应用栈信息，3s栈和6s栈因为超时获取失败。

   ```txt
   Failed to dump normal stacktrace for 61389
   Reason:
   normal stack:failed to fully dump due to timeout
   Tid:61389, Name:com.hx.example
   #00 pc 00000000001cc674 /system/lib/ld-musl-aarch64.so.1
   #01 pc 00000000001d2658 /system/lib/ld-musl-aarch64.so.1
   #02 pc 00000000000a291c /system/lib/ld-musl-aarch64.so.1
   #03 pc 000000000014ab24 /data/storage/el1/bundle/libs/arm64/libentry.so
   #04 pc 0000000000149164 /data/storage/el1/bundle/libs/arm64/libentry.so
   #05 pc 00000000002a21e4 /data/storage/el1/bundle/libs/arm64/libentry.so
   #06 pc 0000000005d22478 /data/storage/el1/bundle/libs/arm64/libkn.so
   #07 pc 0000000005d206b0 /data/storage/el1/bundle/libs/arm64/libkn.so
   #08 pc 0000000005d6d884 /data/storage/el1/bundle/libs/arm64/libkn.so
   ```
3. 使用HiSmartPerf工具抓取该过程的Trace信息，观察到处理onAreaChange接口时间达到16s，远远超过一般的耗时（us级）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/C7P5_Wh-QvuSvPWl9M63lQ/zh-cn_image_0000002658794247.png "点击放大")

## 分析结论

[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)接口耗时太长导致应用卡死，随后自动退出。

## 修改建议

将[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)接口中的耗时业务放到子线程处理，参考文档[使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)。
