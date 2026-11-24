---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-network
title: 网络诊断：Network分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 网络诊断：Network分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2667de073d1880176e4bc3e0211666cab31050086372e5414bf25fb4e073c41d
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/sfEk4bqVTcepjOg9aXPWaw/zh-cn_image_0000002808766185.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E936AE55AE6F4AFC20C1AB9E8EE9E6FBF57080C3A2F48D823E44670928DA579 "点击放大")
* **Details**区域将展示按时间戳排序的周期上报的网络数据，每个网络数据包含上报时间戳、持续时间、下行流量、下行流量包数、网络接口、上行流量、上行流量包数。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dhB7IBsyTR2rgFX-yyyUXA/zh-cn_image_0000002779566600.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B82F426C1FD45C2DA56CB88D4E3BEDF6858D159E3720B7133D90F757F6FF09D6 "点击放大")

## 查看网络请求各阶段耗时

点击**Network Request**泳道，可在下方数据区查看录制过程中发生的网络请求数量变化。

* **Summary**区域可查看按照域名（Domain）维度统计展示网络请求耗时，展示信息包含域名、线程名称、数量、平均耗时、最大耗时、DNS解析/TCP连接/TLS连接/等待响应/接收数据平均耗时、DNS解析/TCP连接/TLS连接/等待响应/接收数据最大耗时。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/6nWZMBugSQ-K6DcN1BDk5A/zh-cn_image_0000002808886265.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=550032C3177A41108244EAC69EAB1097ACCD5E7F0618FA6D5CA1AA20417E618E "点击放大")
* 选择任意Domain，**Details**区域将展示请求该Domain的所有网络请求耗时，展示信息包含请求ID、线程名称、请求url、重定向url、IP地址、总耗时、DNS 解析耗时、TCP连接耗时、TLS连接耗时、等待响应耗时、接收响应耗时、请求类型、状态码、使用的版本。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/er4jPwDYR4KwJI2fueaq4g/zh-cn_image_0000002808886257.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=27AA9A12F78D3D3658F0D5BA0D557C9F9AD85099BDD276F6752FE2EBCEFD256D "点击放大")

  选择Details中某条数据，泳道区域将以虚线框展示其耗时方块，右侧**More**区域展示该请求的Request Headers、Response Headers、Response Body。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/bKSSkbJIQim_vd24VA4C7g/zh-cn_image_0000002808766179.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=72110B2FE1898C4F197BFBF953292789DA5C08DF486FAB3F8DE255EBD575CEFD "点击放大")

  定位到可能造成网络卡顿的网络请求，点选其耗时方块，可以看见该请求各阶段耗时。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/peJonHoHRAaNKUCj5hSATw/zh-cn_image_0000002779406618.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E0E3775B81EF3A2B42487AB2B1478293824AF93144263E73FA9A18477ACF0C0 "点击放大")

## 分析启动过程网络问题

DevEco Profiler的Network分析任务，提供了启动过程网络问题分析能力，协助开发者解决启动过程的网络问题。

针对调测应用的当前运行情况，DevEco Profiler对其做如下处理：

* 如选择的是已安装但未启动的应用，在启动该分析任务时，会自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。
* 如选择的是正在运行的应用，在启动该分析任务时，会先将应用关停，再自动拉起应用，进行数据录制，结束录制后可正常进入解析阶段。

具体操作方法为：在任务列表中单击Network任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/wfyMlYTRTEefSPfiZgVoYA/zh-cn_image_0000002779566592.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D0D8151388BD3D82AF5C7CC2A2FACF8E7FF0DBB0C44C46F02257A494AFABB91 "点击放大")按钮。

在分析结束后，呈现出的数据类型以及相应的处理方法，与非启动过程的分析相同。
