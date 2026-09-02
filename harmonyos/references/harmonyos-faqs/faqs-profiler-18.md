---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-18
title: DevEco Profile的SnapShot无法抓取ArkTS snapshot数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > DevEco Profile的SnapShot无法抓取ArkTS snapshot数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62a2a985b9b55eb78bb38d5230da825206ab89c2023f9c30e1eae790664ecfcf
---

## 问题现象

参考Snapshot模板数据步骤进行操作录制，操作第4步快照拍摄，ArkTS snapshot无数据（未显示紫色条块）。

* DevEco Studio版本：5.0.11.100。
* 工程机版本：5.0.1.130(SP8C00E130P5P4patch03)。
* SDK版本：API17。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/TkyA8MVaTXqUfq9EX69tYg/zh-cn_image_0000002628409542.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QNkpkGBITLS0IIcIVQmTmA/zh-cn_image_0000002628569440.png "点击放大")

## 背景知识

[Snapshot分析](../harmonyos-guides/ide-insight-session-snapshot.md)：针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

## 问题定位

* 排查是否是已上架应用市场的应用：由于隐私安全政策，已上架应用市场的应用不支持使用Snapshot分析模板。
* 排查操作步骤是否错误：先连接工程机后，将工程启动，定位到需要分析的页面，然后参考[录制Snapshot模板数据](../harmonyos-guides/ide-arkts-memory-leak-analysis.md#section292715574272)步骤进行操作录制。
* 排查DevEco Studio版本和工程机版本是否使用配套的版本：DevEco Studio版本号前2位与工程机版本保持一致后，SDK版本所对应的DevEco Studio版本，详细参考[对应的版本概览](../harmonyos-releases/overview-allversion.md)。
* 点击快照按钮无反应，则在DevEco Studio工具栏中选择“Help > Edit Custom VM Options…”，排查配置参数Xmx是否过小导致快照录制不出来。

## 分析结论

DevEco Studio配置参数Xmx设置为2048m，较小导致快照录制不出来。

## 修改建议

在DevEco Studio工具栏中选择“Help > Edit Custom VM Options…”打开配置文件，增大“-Xmx”参数后的值。如果配置文件中未包含“-Xmx”参数，请手动添加，例如：-Xmx2048m。2048m表示虚拟机可使用的内存量。
