---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-network-performance-issue-localization
title: 网络性能问题定位指导
breadcrumb: 最佳实践 > 性能 > 性能分析 > 网络性能问题定位指导
category: best-practices
scraped_at: 2026-11-24T12:47:51+08:00
doc_updated_at: 2026-11-24
content_hash: sha256:33da8a7f5da026c7edf3133c0561fea7e3455030b5b8d7982e99a8d29ff1dc52
---

## 概述

网络性能问题指应用进行HTTP/HTTPS网络请求时，因某一环节耗时过高而导致的响应慢、卡顿、加载超时等现象。

问题定位的核心思路是：利用DevEco Profiler的Network模板把“感觉慢”变成“哪段慢”（参考文档[网络诊断：Network分析](../doccenter-deveco-studio/ide-profiler-network.md)）。在应用运行过程中采集HTTP协议栈的网络信息与流量信息。将请求耗时按五个阶段单独展示，并给出每个请求携带的Request/Response头、Body、Cookie等具体内容，从而精准定位耗时瓶颈，再针对性地优化时延问题。

## 问题定位流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/JbxO9mb8Tla9A-euZLDh-g/zh-cn_image_0000002793523586.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4D4624E27A49038AE62B64A5D627C79795F536928313F7CEC861DE4193ACBFC)

1. 录制并操作应用：使用DevEco Profiler的Network模板录制网络请求，执行操作复现网络请求问题。
2. 查看Network Traffic：查看网络流量消耗信息，定位异常流量的时段与数据包。
3. 查看Network Request泳道：定位高耗时域名 → 定位高耗时请求 → 查看五阶段细分耗时 → 查看请求信息 → 查看Callstack调用栈 → 实施对应优化。
4. 重新录制验证：修改代码后重新录制Network数据，对比修复前后耗时，确认耗时达标；未达标则回到步骤3继续迭代。

## 网络卡顿案例分析

### 案例介绍

在触发请求后，需要等较长时间拿到响应数据，影响后续视图渲染。

### 分析流程

第1步：录制请求信息

DevEco Profiler → 选择设备与应用进程 → 选择Network模板 → 创建Session → 启动录制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/-y8PZJ4ZSo2_GvY-aIaOJw/zh-cn_image_0000002793683574.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=97763509F2A85907CDD72A110DE3ABE617481750CF2028E81EBED9016B9FD999 "点击放大")

第2步：查看Network Traffic泳道

在时间轴区域找到Network Traffic泳道，其中红色柱状表示上行/发送流量（Bytes Transmitted），绿色柱状表示下行/接收流量（Bytes Received）。

选中Network Traffic泳道后，在底部Summary标签页查看按网络接口（Network Interfaces）维度统计的流量消耗，字段包括：

| 字段 | 含义 |
| --- | --- |
| Network Interfaces | 网络接口（如wlan0，即Wi-Fi网卡） |
| Average In / Bytes In / Packets In | 平均下行流量 / 下行总流量 / 下行数据包数 |
| Average Out / Bytes Out / Packets Out | 平均上行流量 / 上行总流量 / 上行数据包数 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Dv9PR6T8RXGygy1nwVnbiw/zh-cn_image_0000002822483489.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=8343D60956AA6469C91D5697888C348A436ADC4F86DACB56973D88FE989F34B7 "点击放大")

切换到Details标签页，查看按时间戳排序的周期上报网络数据。字段包括：上报时间戳（Timestamp）、持续时间（Duration）、下行流量（Bytes In）、下行流量包数（Packets In）、网络接口、上行流量（Bytes Out）、上行流量包数（Packets Out）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/svqxQCe7QTG7IeiDgh1Kqw/zh-cn_image_0000002822363493.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A8B253CE841827D0C377780FB7CF677142E2EE00ACBA815A63D496094B07431 "点击放大")

选中Network Traffic泳道最高的柱子 → 选中ArkTS Callstack泳道 → 查看调用栈 → 双击调用栈跳转到具体代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/dRrtq2kiRdm9KcIZq07GbQ/zh-cn_image_0000002793523588.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B8331FA35C036AC80F4496356A14E5456EA1466E818AAC30D6F90E3ED83F987 "点击放大")

第3步：查看Network Request信息

该泳道用于查看录制过程中发生的网络请求数量与耗时分布：选中Network Request泳道 → 查看Summary区域。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/8fYIff6uSpixdYTnJnuHOQ/zh-cn_image_0000002793683576.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D224F9F745D508D14FE1B881EDE48140094E92EDDF00D68E07D7D2D00EE2CB "点击放大")

Summary标签页可用于查看按域名（Domain）维度统计的请求耗时，字段包括：

| 字段 | 含义 |
| --- | --- |
| Domain | 请求域名 |
| Thread / Count | 发起请求的线程 / 请求条数 |
| Avg Duration / Max Duration | 该域名下请求的平均 / 最大总耗时 |
| DNS/TCP/TLS/等待响应/接收数据（平均/最大）耗时 | 该域名下各阶段耗时统计 |

第4步：定位高耗时域名

在Summary区域按“平均耗时”或“最大耗时”列降序排序，找出耗时最高的域名并记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/x-ZoRH6gTuCKFXkDqJEDSA/zh-cn_image_0000002822483493.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=E772F8709FBD6AE343C647C7D9677279581CD5744F849428F2C437385FBE1C1D "点击放大")

第5步：定位高耗时请求

选中高耗时域名泳道 → 查看Details区域 → 按“总耗时”列降序排序，找出耗时最高的请求并记录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/dGrxmTpEQ4CpDqhYZJP88A/zh-cn_image_0000002822363495.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=5535478ACE980BA1376B051703D5B29C549B815A2CF9B599EE886B293ED8D608 "点击放大")

每条请求的信息含义如下：

| 字段 | 含义 |
| --- | --- |
| Request ID / Thread | 请求唯一标识 / 发起线程（如OS\_NET\_HttpWork[62082]） |
| URL / Effective URL | 请求地址 / 重定向后的地址 |
| IP Address | 实际连接的服务端IP（如98.88.155.171） |
| Duration | 请求从发起到完成的总耗时 |
| DNS Duration / TCP Duration / TLS Duration | 前三阶段耗时 |
| Waiting For Response / Receiving Response | 后两阶段耗时 |
| Method / Status Code / HTTP Version | 请求类型（GET/POST等）、HTTP状态码、协议版本 |

第6步：查看五阶段细分耗时

两种查看方式如下：

* 方式一（推荐）：将鼠标悬停在Network Request泳道上该请求的耗时方块上，弹出Tooltip展示各阶段耗时。
* 方式二：在底部Details面板中选中该请求，查看各阶段耗时列。如下图所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/gCGSBhWGRfSZDsQbsIm1AQ/zh-cn_image_0000002793523592.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A972C0D8D2552599E07A63153758FC4F79FB91DFE652FCF484A9388E9CD38AA "点击放大")

  结论：总耗时约1s 374ms，请求等待和接收响应阶段耗时过长，即从请求发出到全部接收完成时间过长。

第7步：查看请求信息

选择Details中某条数据后，泳道区域将以虚线框展示其耗时方块，右侧More区域展示该请求的Request Headers、Response Headers、Response Body。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/nckqczWETk-q5e0TSU8Cuw/zh-cn_image_0000002793683578.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FD77CD1991EE2C69EBC91A55298A371B2A83C2FA01F5A76892738B261028E00 "点击放大")

通过Callstack定位到具体的请求代码：在具体的请求泳道中选中耗时长的部分 → 选中左侧ArkTS Callstack → 查看调用栈 → 双击跳转代码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/qlwZJYAcRDWIGhHr5wmHbw/zh-cn_image_0000002822483495.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=67E7F5C5E7BA6B589D3009BC154DE61864698D18B9220B894C51DA90C11FECA1 "点击放大")

第8步：实施对应优化

根据定位到的异常阶段，对照下表选择对应的优化方案。优化落地时注意区分：

服务端问题（TTFB高、响应体大）：优化服务端性能、CDN、缓存、压缩；

客户端问题（DNS/TCP/TLS慢）：通过代码配置HTTPDNS、连接池、TLS1.3、请求合并等。

| 特征识别 | 具体表现 | 优化方案 |
| --- | --- | --- |
| DNS阶段>100ms | 首次请求耗时较长，后续相同域名请求正常 | 检查域名解析是否首次解析、DNS服务器响应是否正常 |
| TCP阶段耗时高，且连接复用率低 | 每次请求都建立新连接，耗时波动大 | 检查是否新建连接、服务器响应是否正常 |
| TLS阶段>200ms | HTTPS请求首次慢，后续正常但每次握手仍然耗时 | 检查证书配置是否合理、是否复用了session |
| 请求等待阶段耗时高（TTFB高） | 请求发出后等待较长时间才收到第一个字节 | 检查服务器处理时间、是否存在排队 |
| 接收响应阶段耗时高 | 响应体较大，下载耗时长 | 检查响应数据量大小、网络带宽 |

### 重新录制验证

1. 经第6步五阶段耗时分析，接收响应阶段耗时占比最高，最终确认为网络时延较高，调整网络后，重新编译并安装应用到设备，再次抓取数据。
2. 重复“分析流程”中第2步至第6步，定位到同一请求，记录修复后的五阶段耗时。如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/d_gunOs5RWCDUJQc9v-ynQ/zh-cn_image_0000002822363497.png?HW-CC-KV=V1&HW-CC-Date=20261124T044751Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1696DABF218452FA6D5B43BDA1296037F8014997ACC1F155BE30759BA6BA4BE "点击放大")

## 总结

对于常见的网络性能问题，主要流程就是首先借助DevEco Profiler创建Network模板获取定位问题的全量数据，随后可通过对Network Traffic和Network Request定位到异常的请求数据，比对常见场景进行排查并做出相应优化，最终再次获取数据验证问题是否修复。

## 示例代码

* [网络性能问题定位分析同源示例代码](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/tree/master/NetworkPerformanceIssueLocate)
