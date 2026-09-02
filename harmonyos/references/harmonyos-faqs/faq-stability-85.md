---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-85
title: Profiler录制没有数据
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > Profiler录制没有数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a143cbce08bc16e61e213ad7ca464c1e3a72a9ee7cfcb37f6c897d6ba0268bdb
---

## 问题现象

通过Profiler进行应用性能分析的时候，录制的性能数据有缺失。

## 背景知识

DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，详细内容可参考[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

## 解决方案

* 使用Profiler中的Snapshot、Allocation模板进行内存分析时，Native Heap泳道没有数据。

  检查是否开启了asan，如果开启会导致Profiler无法采集Native数据，参考[文档](faqs-profiler-5.md)关闭asan开关。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/cxU42EUOT8ag22mY9nbKuA/zh-cn_image_0000002628554918.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/_Y77UqiaQLaJuA1kxDf0jw/zh-cn_image_0000002628395016.png "点击放大")
* 使用Profiler中的Network模板，Network Traffic泳道中没有数据。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/kyDKB5kHQjW-IMWWl63WTA/zh-cn_image_0000002658914235.png "点击放大")

  检查是否使用了非request类型接口，当前Network模板任务仅支持对Network kit接口中request类型接口进行录制和调优，参考[文档](../harmonyos-guides/ide-profiler-network.md)设置。
* 使用Profiler中的Snapshot模板时，当DevEco Studio配置项内存设置较小时，会导致快照录制不出来。按如下步骤进行配置调整：
  1. 在工具栏中选择“Help > Edit Custom VM Options…”，打开配置文件。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/mCYDUSOGT2KPSjOKxKtbeg/zh-cn_image_0000002658794285.png "点击放大")
  2. 根据实际需求调整"-Xmx"参数后的值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/kF9IMp-cQJy9nVJpCsaB2g/zh-cn_image_0000002628554924.png "点击放大")
* 如果是mac电脑，在使用Profiler分析性能时，缺少数据，可以执行/usr/sbin/softwareupdate --install-rosetta --agree-to-license命令来尝试修复。
