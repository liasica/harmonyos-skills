---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-58
title: C++代码如何配置trace打点数据
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > C++代码如何配置trace打点数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:d93ecad3b77ab928245b63f6141498c926b8db9836df6d03b9d5b4bb42e08568
---

## 问题现象

在C/C++项目开发过程中，如何配置trace打点数据？具体包括如何使用同步跟踪打点接口和异步跟踪打点接口标记耗时任务，以及如何通过hitrace命令行工具或Profiler工具查看打点信息。

## 背景知识

开发者可以在代码中调用HiTraceMeter接口进行trace打点，然后使用[hitrace命令行工具](../harmonyos-guides/hitrace.md)获取程序运行时产生的打点信息，从而了解程序运行的进程、线程、时间戳、cpu等信息，以帮助开发者进行问题分析和性能调优等活动。

HiTraceMeter提供ArkTS和C/C++两种接口，开发者可根据实际开发语言选择合适的接口。

* [使用HiTraceMeter跟踪性能（ArkTS）](../harmonyos-guides/hitracemeter-guidelines-arkts.md)
* [使用HiTraceMeter跟踪性能（C/C++）](../harmonyos-guides/hitracemeter-guidelines-ndk.md)

## 解决方案

OH\_HiTrace\_StartTraceEx用于标记一个同步跟踪耗时任务的开始。同步跟踪打点接口OH\_HiTrace\_StartTraceEx和OH\_HiTrace\_FinishTraceEx必须配对使用。

OH\_HiTrace\_StartAsyncTraceEx标记一个异步跟踪耗时任务的开始。用于在异步操作前调用进行开始打点，异步跟踪开始和结束数据由于不是顺序发生的，所以解析时需要通过一个唯一的taskId进行识别。必须和OH\_HiTrace\_FinishAsyncTraceEx配对使用，参数name和taskId相同的开始与结束打点相匹配，构成一个异步跟踪耗时任务。

* OH\_HiTrace\_StartTraceEx和OH\_HiTrace\_FinishTraceEx配套使用，要用cpu insight才能看到trace信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/NTx7vmLAT4iCwDFQ9EFq1A/zh-cn_image_0000002677871739.png "点击放大")
* OH\_HiTrace\_StartAsyncTraceEx和OH\_HiTrace\_FinishAsyncTraceEx配套使用，Time insight和cpu insight都可以看到trace信息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4bC_gXSwSuq5nNT77pHCIg/zh-cn_image_0000002677872197.png "点击放大")
* 如果是配合ArkTS/HarmonyOS排查函数耗时，用OH\_HiTrace\_StartAsyncTraceEx和OH\_HiTrace\_FinishAsyncTraceEx进行打点，然后使用Profiler的Time insight模板就可以看到。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/BMotM155TVCld1vKGc_ZVw/zh-cn_image_0000002647792546.png "点击放大")
* 运行hitrace打点，要在这里添加libhitrace\_ndk.z.so。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/R-5SXBzlT2yFRA7HTPss_g/zh-cn_image_0000002647792624.png "点击放大")

## 常见FAQ

Q：通过OH\_HiTrace\_StartAsyncTraceEx、OH\_HiTrace\_FinishAsyncTraceEx等接口打点后，在Time Profile中看不到User trace信息怎么办？

A：建议通过IDE中抓取Time/CPU的Profiler trace信息来显示打点信息。若仍无法看到，请升级IDE版本到26.0.0 beta1版本后再尝试。
