---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-49
title: Profiler监控SDK运行的性能时，如何延长录制时间
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > Profiler监控SDK运行的性能时，如何延长录制时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e142a97557360a431004c869e51fe5a42cb91c41c500bc300f16738cb73f07f0
---

## 问题现象

使用Profiler监控SDK运行的性能时，录制时间一般7到8分钟会话就结束了，如何延长录制时间。

## 背景知识

* [DevEco Profiler](../best-practices/bpta-optimization-overview.md#section2012922312284)提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据，自顶向下逐层展开分析，并可借助DevEco Profiler跳转到代码位置，结合代码进行白盒分析，明确不合理的负载出现位置，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率。
* DevEco Profiler提供了基础的[内存场景分析Allocation](../harmonyos-guides/ide-insight-session-allocations.md)，您可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

## 解决方案

系统用户目录下(C:\Users\xxxxxx)\AppData\Local\Huawei\DevEcoStudio**xx**(**xx**为版本号)\.insight，修改配置文件config.json5：

* 如果使用的Allocation模板，默认是Memory、All Heap & Anonymous VM、All Heap、All Anonymous VM、System Resources五个泳道，需要修改MemUsage、AllHeapAndAllAnonymousVM、AllHeapUnit、AllAnonymousVmUnit、SystemResources字段下scene为0相应的restrainedDuration值，根据需要调整（单位：秒）。
* 如果是CPU模板，默认是CPU Core（CpuPlaceholderUnitV101）和Process（CpuProcessPlaceholderUnit）这两个泳道，需修改CpuPlaceholderUnitV101和CpuProcessPlaceholderUnit字段下restrainedDuration的值，两个字段restrainedDuration值不同时，录制时间取两者最小值（单位：秒）。
