---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-network
title: 网络诊断：Network分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 网络诊断：Network分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:557984640ddac58e26206b8268d30bfa10362c21a363338fdfa2f4eecc9abe49
---

## 功能介绍

DevEco Profiler提供Network模板，帮助用户在应用运行过程中查看HTTP协议栈网络信息和网络流量信息，HTTP协议栈包括请求分段耗时和请求具体内容，方便对网络问题进行调优。请求耗时按照以下五种阶段进行划分：DNS 解析、TCP连接、TLS连接、请求等待、接收响应，分别展示在各阶段的耗时，可以针对性的优化时延问题。同时，详情信息将展示每个请求中携带的信息，包含Request、Response侧及其携带的Header、Body、Cookie信息，方便网络问题定位。

Network模板支持的泳道包括：Network Traffic、Network Request、User Trace、ArkTS Callstack、Callstack。本文介绍Network Traffic、Network Request泳道，其他泳道的详细信息请参考对应模板内容。

* User Trace、ArkTS Callstack、Callstack泳道的介绍请参考[基础耗时：Time分析](ide-insight-session-time.md)。

**说明** 

* 任务分析前，需创建Network分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。
* 当前Network模板任务仅支持对Network Kit接口中Request 类型接口进行录制和调优。
* 由于隐私安全政策，已上架应用市场的应用不支持录制Network分析模板。

## 查看网络流量消耗信息

点击**Network Traffic**泳道，可在下方数据区查看录制过程中发生的网络流量消耗情况。

* **Summary**区域可以查看按照网络接口（Network Interfaces）维度统计每个类型的流量消耗，展示信息包含平均下行流量、下行总流量、下行数据包数、网络接口、平均上行流量、上行总流量、上行数据包数。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/2_mTwaSsTD2cFF0XotbZfQ/zh-cn_image_0000002808766185.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2CEC68C97B9F8EDBA25DFF477452C8E4DC4753CB835A272E3C917BA163A7BAC "点击放大")
* **Details**区域将展示按时间戳排序的周期上报的网络数据，每个网络数据包含上报时间戳、持续时间、下行流量、下行流量包数、网络接口、上行流量、上行流量包数。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/JEreOjSZS-Ok32EZRsk_KA/zh-cn_image_0000002779566600.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=3AA05C913FF292FCAC49147E6D72C54CF7F681976AB329B25EE308DBA7C0CB43 "点击放大")

## 查看网络请求各阶段耗时

点击**Network Request**泳道，可在下方数据区查看录制过程中发生的网络请求数量变化。

* **Summary**区域可查看按照域名（Domain）维度统计展示网络请求耗时，展示信息包含域名、线程名称、数量、平均耗时、最大耗时、DNS解析/TCP连接/TLS连接/等待响应/接收数据平均耗时、DNS解析/TCP连接/TLS连接/等待响应/接收数据最大耗时。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/iZn2tuCDTfeW_ezEFAxxdQ/zh-cn_image_0000002808886265.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=25426C9A8805CB4E1374C8473EAD421C05AD97C56CE634EA159FADAE61D169B2 "点击放大")
* 选择任意Domain，**Details**区域将展示请求该Domain的所有网络请求耗时，展示信息包含请求ID、线程名称、请求url、重定向url、IP地址、总耗时、DNS 解析耗时、TCP连接耗时、TLS连接耗时、等待响应耗时、接收响应耗时、请求类型、状态码、使用的版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/jJ3qzN6sSiyLiocRyd777w/zh-cn_image_0000002808886257.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA3FE9FEB92534FFA5846E8DAECB036FD844B91E2BFD4A4C38A4FE87B7A53B8A "点击放大")

  选择Details中某条数据，泳道区域将以虚线框展示其耗时方块，右侧**More**区域展示该请求的Request Headers、Response Headers、Response Body。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/X8rL7EIDRqKR65b51njL8w/zh-cn_image_0000002808766179.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=09F8EC4B14AE840BF202FCD221EC0D3596C128A71F62D9590E00561D714A12BE "点击放大")

  定位到可能造成网络卡顿的网络请求，点选其耗时方块，可以看见该请求各阶段耗时。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/9BiYQwf5STyPQdykBbZdhg/zh-cn_image_0000002779406618.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=14C363D999AD61381BC7B6EE24073CEA345E5D3819CE80116809B129417F9FF0 "点击放大")

## 分析启动过程网络问题

DevEco Profiler的Network分析任务，提供了启动过程网络问题分析能力，协助开发者解决启动过程的网络问题。

针对调测应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用关停，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Network任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/jkTrUwc2RxqV4ahkoS1Ytw/zh-cn_image_0000002779566592.png?HW-CC-KV=V1&HW-CC-Date=20261114T004906Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F0F1E4E0C6FD24CE897A73CC230B7E844B9CB47EC066E5B175140AF16DC3117 "点击放大")按钮。

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同。
