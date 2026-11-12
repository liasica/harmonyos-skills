---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-stability-basic-quality-test-6
title: 如何获取和查看DevEco Testing稳定性测试日志
breadcrumb: FAQ > DevEco Testing > 专项测试 > 稳定性基础质量测试 > 如何获取和查看DevEco Testing稳定性测试日志
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:f3c56022b9ae5bdc99e51b3994e990a85aa649fd29e135ca5382b7e31b8be51b
---

## 问题现象

使用DevEco Testing进行稳定性测试，执行完成后如何获取和查看稳定性测试日志？

## 解决方案

[稳定性基础质量测试](../harmonyos-guides/stability-testing.md#section1661194962815)日志存在于hilog和faultlog日志中，其中faultlog为Crash时的堆栈日志，hilog是这整个运行过程中的全量日志。

1. 稳定性测试获取日志途径：
   * 稳定性测试报告中检测异常项，详细日志点击查看，如图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/SrUMt-5MQ8uBWv1UHgcjrg/zh-cn_image_0000002632552628.png?HW-CC-KV=V1&HW-CC-Date=20261112T233218Z&HW-CC-Expire=31536000000&HW-CC-Sign=09542958B884F808879BFC3FB63E984ED2A55C88A449261CB891433895BFDC26 "点击放大")
   * 日志详情-定位日志，点击查看，跳转到对应日志，如图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/IGm9SlumTD-pjrY15bDL8g/zh-cn_image_0000002663031767.png?HW-CC-KV=V1&HW-CC-Date=20261112T233218Z&HW-CC-Expire=31536000000&HW-CC-Sign=E028C651EE35CAAD2F0284E57DDD7FB3AB1B91C7883C136A1F883C33E52BDFF4 "点击放大")

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/JZuzQuoETNOI-rtZOmes5A/zh-cn_image_0000002662871817.png?HW-CC-KV=V1&HW-CC-Date=20261112T233218Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B72143CAD5C363E4439EF21949F81EAB186F91A3F0D5E8C4988B1E22E9706B4 "点击放大")
   * DevEco Testing稳定性测试，发生内存泄漏，如需获取profiler日志，需要执行测试前在“开发者选项”中打开“系统资源泄漏日志”开关（打开或关闭开关均需重启设备），参考[订阅资源泄漏事件](../harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts.md#步骤二订阅资源泄漏事件)。
2. 稳定性日志分析：

   稳定性分析将稳定性划分为地址越界、资源泄漏、应用冻屏（AppFreeze）和应用崩溃四大类。分析方法可参考文档[稳定性分析](../best-practices/bpta-stability-analysis.md)。
