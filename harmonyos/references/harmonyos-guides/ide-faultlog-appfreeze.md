---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-faultlog-appfreeze
title: 查看AppFreeze（应用冻屏）日志
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 查看AppFreeze（应用冻屏）日志
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:31+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:400c9aabaf7a494e3a1ed3c6c7d8a7fcf370ca2520443b6340fcf6f1d470dbcc
---

从DevEco Studio 6.0.0 Beta2版本开始，支持对AppFreeze类型的FaultLog，进行结构化展示和日志过滤。关于AppFreeze日志的检测原理、日志规格等信息请查看[AppFreeze（应用冻屏）检测](appfreeze-guidelines.md)。

1. 打开FaultLog窗口，双击appfreeze日志，**Fault Info**右侧会出现**Fault Analysis**页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ufAdo_1FTHWL7cN4RwI1gQ/zh-cn_image_0000002808766989.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=92A631C4E1AD4163FD0EC2C6A0D26AE92F32A7933729F3011E30AEEA16D32C63)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。
   * 页面上方的字段对应了FaultLog中的字段，具体对应关系请参考[字段说明](ide-faultlog-appfreeze.md#section6678213185017)。
   * 页面下方包含Stacks、Logs、Binder Communication、System等页签，具体如下。
     + **Stacks**：展示线程的堆栈信息，具体请参考[查看堆栈信息](ide-faultlog-appfreeze.md#section6334533115019)。
     + **Logs**：展示FaultLog中的HiLog日志，具体请参考[查看HiLog日志](ide-faultlog-appfreeze.md#section7265205715018)。
     + **Binder Communication：**从DevEco Studio 6.1.1 Beta1版本开始，新增Binder Communication页签，对应AppFreeze日志中的[对端信息（与当前故障进程通信的进程信息）](appfreeze-guidelines.md#对端信息与当前故障进程通信的进程信息)，用于展示进程间通信的调用信息、各进程Binder资源信息，具体请参考[查看Binder通信信息](ide-faultlog-appfreeze.md#section61431112125119)。
     + **System**：从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，具体请参考[查看高负载CPU/内存日志信息](ide-faultlog-appfreeze.md#section145027295519)。
     + **Sampling Stack**：从DevEco Studio 6.1.1 Beta1版本开始，新增Sampling Stack页签，对应[AppFreeze增强日志中的堆栈信息](appfreeze-guidelines.md#appfreeze应用冻屏增强日志信息采样栈)，用于查看采样栈数据，标记可疑问题栈，具体请参考[查看采样栈数据信息](ide-faultlog-appfreeze.md#section1731022185212)。
     + **3s/6s Compare**：从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，具体请参考[查看3s/6s堆栈日志](ide-faultlog-appfreeze.md#section699194455215)。
     + **Main Thread Task Queue**：从DevEco Studio 6.1.1 Beta1版本开始，新增Main Thread Task Queue页签，对应AppFreeze日志中的[EventHandler信息](appfreeze-guidelines.md#日志主干通用信息)，用于展示主线程的任务队列，包括历史任务和待调度任务，具体请参考[查看主线程任务队列信息](ide-faultlog-appfreeze.md#section3149310135314)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/_lTRxpyOSEmH2ioG2Ka-MA/zh-cn_image_0000002779567410.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA92DC50CE2B8CA5A48E3D854639F173E5B6082DBDE9285206AD8478BC7DC16E)

## 字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

**表1**

| **Fault Analysis**的字段 | 说明 |
| --- | --- |
| Occurrence time | FaultLog发生的时间，对应FaultLog中的Timestamp字段。 |
| Analysis time | 触发日志结构化展示的时间，即双击日志文件的时间。 |
| Frontend | 是否是前台应用，对应FaultLog中的Foreground字段。 |
| Bundle name | 包名，对应FaultLog中的Module name字段。 |
| Device type | 设备类型。 |
| App build number | 应用构建号，对应FaultLog中的VersionCode字段。 |
| App version | 应用版本，对应FaultLog中的Version字段。 |
| Device model | 设备信息，对应FaultLog中的Device info字段。 |
| System version | 系统镜像版本，对应FaultLog中的Build info字段。 |
| Freeze type | 冻结类型，对应FaultLog中的Reason字段。 |
| Note | 从DevEco Studio 6.1.1 Beta1版本开始，如果AppFreeze是系统高负载导致的，会显示Note字段，对应FaultLog中的NOTE字段。 |

## 查看堆栈信息

Stacks页签用于查看AppFreeze中的堆栈信息，并以线程为单元进行折叠，点击展开按钮，可以展开对应线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/xOd-QAayQVedLZFJxXZbeA/zh-cn_image_0000002779407438.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C64679DAC940B8C4059817130DA9E1EAAA7038465B71CA7E6A6AAE911CE42D9)

图中标注1的勾选框是展开应用堆栈，标注2的勾选框是展开系统堆栈，两个勾选框一共组成了四种状态，具体如下表。

**表2**

| 勾选框勾选状态 | 说明 |
| --- | --- |
| 1、2都不勾选 | 展示所有线程，线程处于折叠状态。 |
| 1、2都勾选 | 展示所有线程，线程处于展开状态。 |
| 只勾选1 | 只展示应用线程，线程处于展开状态。 |
| 只勾选2 | 只展示系统线程，线程处于展开状态。 |

## 查看HiLog日志

Logs页签用于查看AppFreeze中的HiLog日志，支持日志级别的过滤和搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/YAoDg8_XQL2Y119d74glvg/zh-cn_image_0000002808766995.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=82E0CCC71F29196DEED2F82A0463CF6076BCB4D324CD45789F114A6930731FE6)

## 查看Binder通信信息

从DevEco Studio 6.1.1 Beta1版本开始，新增Binder Communication页签，对应AppFreeze日志中的[对端信息（与当前故障进程通信的进程信息）](appfreeze-guidelines.md#对端信息与当前故障进程通信的进程信息)。

Binder Communication页签包含以下内容：

① 查看进程间通信的调用信息及等待时间的情况，包括binder通信方式、发起进程/线程、接收进程/线程等。

② 查看各进程Binder资源信息，包括进程ID/名称、当前IPC请求数、已启动IPC线程数、最大IPC线程数等，当进程资源紧张时会高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/d1awn170TpGEyw8RrbmAIw/zh-cn_image_0000002808887073.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BED45404F2C654A786FF202CD10E57188F5C49EABFE4424ABD6EF6F481A5545F "点击放大")

## 查看高负载CPU/内存日志信息

从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，有助于分析高负载和AppFreeze之间的关联关系。

如下是CPU的相关日志。

①：柱状图表示对应时间点的CPU使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示CPU总使用率、CPU使用率top5的进程号（Pid）和对应的CPU使用率。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/dWtVkrDBR-qkw30D3WOY_g/zh-cn_image_0000002808887077.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=74C841E5C3758A86F518DFF2386A8EFD54959FDA73E9951F4446FE65B3E33A24 "点击放大")

如下是内存的相关日志。

①：柱状图表示对应时间点的内存使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示内存使用率、内存占用top5的进程和对应的内存大小。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/AYt4dy6KTdKdU6WGDRrb4g/zh-cn_image_0000002779407436.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=01FC0149C39D02BC34DB02F84DACA92BDAC9BB002FEA01769D6FB3C86A5D09B8 "点击放大")

## 查看采样栈数据信息

从DevEco Studio 6.1.1 Beta1版本开始，新增Sampling Stack页签，对应[AppFreeze增强日志中的堆栈信息](appfreeze-guidelines.md#appfreeze应用冻屏增强日志信息采样栈)，用于查看采样栈数据，标记可疑问题栈。

当设备版本低于API 26.0.0时，查看采样栈数据之前，需要在AppScope/app.json5文件中配置如下环境变量，获取AppFreeze增强日志。当设备版本为API 26.0.0及以上时，无需配置环境变量。

```json5
"appEnvironments": [
  {
    "name": "DFX_APPFREEZE_LOG_OPTIONS",
    "value": "mainthread_sampling:enable"
  }
]
```

Sampling Stack页签默认展示堆栈水平条形图，按照堆栈的出现频率从高到低排序，条形图最后的数字是堆栈出现的次数，并通过不同颜色标识应用堆栈和系统堆栈，可通过左上角的勾选框选择查看对应的堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Lt2NHcNwTTKt3oCgCCWnsw/zh-cn_image_0000002808766997.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=33EFAC1DE4B9862F246236D0A137CA9712B15D6EAB87D79D15DDC447E6E5D2DA)

点击切换图表类型按钮，可切换到堆栈火焰图，并通过不同颜色标识堆栈类型，其中红色代表异常堆栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/qvTB-o-ZTwGpvf6JawYccQ/zh-cn_image_0000002808887067.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A92DBE893DEDEDD35C275F11AA8BC29F37BDC71689E470086CF10351EC564ED)

## 查看3s/6s堆栈日志

从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，并标识栈帧中可能的故障处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/0OiFLusYRkaSbNCgZgGMmA/zh-cn_image_0000002779407428.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=A2B8A2B02598E5364030E0164CD950E1E8F2DEC0A0DA7B279EC1FD47931D6801)

如果不是THREAD\_BLOCK\_6S类型的AppFreeze问题，不会展示3s/6s Compare页签。

## 查看主线程任务队列信息

从DevEco Studio 6.1.1 Beta1版本开始，新增Main Thread Task Queue页签，对应AppFreeze日志中的[EventHandler信息](appfreeze-guidelines.md#日志主干通用信息)，用于展示主线程的任务队列，包括历史任务和待调度任务。

① 在历史任务概览中，可查看每个任务的名称、耗时、优先级等信息，并通过不同颜色标识正常耗时任务、长耗时任务和当前调度任务，默认展示无响应的任务。

② 在待调度任务概览中，展示了5种级别的任务占比情况，点击饼图可跳转到对应的任务详情。

③ 在任务详情中，可切换不同页签，查看历史任务和待调度任务的详情，支持对任务进行排序和搜索。

④ 支持切换查看3s和6s时间点的任务信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/p9KZm2KqTLuYCXh1GwtTSQ/zh-cn_image_0000002779407430.png?HW-CC-KV=V1&HW-CC-Date=20261124T044231Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E4743777D30F121BE5741756C7A1BD1655A8EED186AAE966854F6C3DBD99FA8)
