---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-faultlog-cppcrash
title: 查看Cpp Crash（进程崩溃）日志
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 查看Cpp Crash（进程崩溃）日志
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1d3939be76fef6a9c96c603e891837942af30c14b1008c65e7cc8b8efbd0fcc7
---

从DevEco Studio 6.0.0 Beta1版本开始，支持对Cpp Crash类型的FaultLog，进行结构化展示和日志过滤。

1. 打开FaultLog窗口，双击cppcrash日志，**Fault Info**右侧会出现**Fault Analysis**页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/MyBR4_k4TPSaAGac-ld-mA/zh-cn_image_0000002808766393.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBF74FE6D03161563A6DA7580AE25A54D052B704AE67EE7423077C2F1C65A494)
2. 点击**Fault Analysis**页签，会展示结构化的日志信息。
   * 页面上方的字段对应了FaultLog中的字段，具体对应关系请参考[字段说明](ide-faultlog-cppcrash.md#section4735122283511)。
   * 页面下方包含Stacks和Logs两个页签。
     + **Stacks**：展示线程的堆栈信息，具体请参考[查看堆栈信息](ide-faultlog-cppcrash.md#section145813141354)。
     + **Logs**：展示FaultLog中的HiLog日志，具体请参考[查看HiLog日志](ide-faultlog-cppcrash.md#section656352444818)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/FxprcdqrTHqNZh0a-9PaDw/zh-cn_image_0000002779406832.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=53F4673F2A5DDA0093E53DD8ACDFEA8E262C8BF47DEBD76437A408B81257BAE7 "点击放大")

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
| Abnormal signal | 异常信号，对应FaultLog中的Reason字段。 |

## 查看堆栈信息

Stacks页面包含了FaultLog中的堆栈信息，并以线程为单元进行折叠，点击展开按钮，可以展开对应线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-tg7RktKQvyyNbhYwihCfw/zh-cn_image_0000002779406836.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=89F0796276956EBA00B81F5E9ADE10F7F4857B7248A34B57FA13CC63CA65073C "点击放大")

图中标注1的勾选框是展开应用堆栈，标注2的勾选框是展开系统堆栈，两个勾选框一共组成了四种状态，具体如下表。

**表2**

| 勾选框勾选状态 | 说明 |
| --- | --- |
| 1、2都不勾选 | 展示所有线程，线程处于折叠状态。 |
| 1、2都勾选 | 展示所有线程，线程处于展开状态。 |
| 只勾选1 | 只展示应用线程，线程处于展开状态。 |
| 只勾选2 | 只展示系统线程，线程处于展开状态。 |

## 查看HiLog日志

Logs页面展示了FaultLog中的HiLog日志，支持日志级别的过滤和搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/5IMlRWTMTQy4VmDdF7mmEQ/zh-cn_image_0000002779566812.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C299BD89D1CA7E8852E03C28B271495F81662B4EB0C8BF7EABE8FD4B48EFA087 "点击放大")
