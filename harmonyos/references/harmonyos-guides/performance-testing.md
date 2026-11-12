---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-testing
title: 性能测试
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 性能测试
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b63b26f0d94bba8cc7f5bcea5466575ca426a044694d639c058f4d11d24eb7a
---

## 性能基础质量测试

**性能基础质量测试：**基于应用性能测试标准，提供了一套包含智能遍历算法和性能指标分析的解决方案，用于评估应用性能。该测试服务通过模拟用户操作行为，对应用进行长时间、高频次的页面遍历，实时采集性能数据，并生成全面、专业的测试报告。

应用的设计、开发及测试过程中推荐参考[应用性能体验建议](performance-experience-suggestions.md)。

**服务使用场景：**

用户在进行整包性能评估测试时，可以使用本服务通过指定应用启动次数与遍历操作时长，对应用进行性能测试。

**检测能力**：

性能基础质量测试提供了响应时延、完成时延、卡顿、音视频和黑白块五大类性能指标的检测能力，具体如下：

|  |  |  |  |
| --- | --- | --- | --- |
| **指标类型** | **指标名称** | **单位** | **指标说明** |
| 响应时延 | 点击响应时延 | 毫秒 | 时间起点：点击离手；  时间终点：界面发生变化。 |
| 响应时延 | 滑动响应时延 | 毫秒 | 时间起点：手指滑动；  时间终点：界面发生变化。 |
| 完成时延 | 加载完成时延 | 毫秒 | 时间起点：应用首页铺满全屏；  时间终点：应用首页所有占位符加载完成。 |
| 完成时延 | 点击完成时延 | 毫秒 | 时间起点：点击离手；  时间终点：转场页面所有占位符加载完成。 |
| 卡顿 | 最大丢帧 | 次 | 动效时间内，连续丢失的最大帧数。 |
| 卡顿 | 卡顿率 | 毫秒/秒 | 动效时间内，累计丢帧时间/动效时长。 |
| 音视频 | 起播时延 | 毫秒 | 时间起点：点击或滑动离手；  时间终点：视频播放首帧。 |
| 音视频 | 视频卡顿 | 次 | 视频播放过程中的卡顿情况，卡顿时长大于100ms视为1次卡顿。 |
| 黑白块 | 启动白屏时长 | 毫秒 | 时间起点：启动动效开始；  时间终点：启动过程中白屏消失。 |
| 黑白块 | 滑动占位符加载指数 | 毫秒/秒 | 页面滑动过程中占位符存在的累计时间。 |

**创建任务**

打开DevEco Testing客户端-测试服务-性能测试-性能基础质量测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/cA59viPgQGGASzrcGBNdEw/zh-cn_image_0000002663932283.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=7A45607448E8117FAFD7F4A0435EDF02FA6331BF1E361937E5A72388C57E6DD6 "点击放大")

性能基础质量测试支持选择已安装的应用，或选择待测应用的安装包后进行测试。

**说明** 

应用支持情况说明：

* 冷启动测试：支持所有应用。
* 应用内操作测试：遍历目前主要支持以下应用类型：
  + ArkUI控件（含ReactNative框架开发）应用。
  + 使用Flutter3.7.12及之后版本开发的应用。
  + 除以上支持的应用类型，其他三方自研框架的自定义控件暂不支持。

（1）已安装的应用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/FqI6YRV8TuCo4mZy9iClyg/zh-cn_image_0000002716047331.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7249A59ECA03EB5FEBA74C6DCDE4307496A90391CF9CF6722CA0907EB507AFD "点击放大")

（2）安装新的应用

点击按钮，在弹窗中选择应用安装包，支持.hap、.zip格式安装包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/0cyuObpHTZeyn8zKBWjNgQ/zh-cn_image_0000002633693128.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDA9505EF159471BF12933EE232CC92D726068AF4F8D82E9779CF022E721772E "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/qoqO5PjaSO6iutEOKLkQoA/zh-cn_image_0000002633533206.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FD718F986A47D69425A1C140661C593B10EAF1DE7E4B26B996F54B21B4FCC38 "点击放大")

**启动测试次数**

执行冷启动操作的次数，自动化测试过程中会重复执行应用冷启动和退出操作，用来评估应用启动的性能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/GDd1IUaLS4W2p7w4C3Ii7g/zh-cn_image_0000002633693130.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=88C76CF93C96534403F2D45A9C315A79B31AFCDBD0863D647CAFC9CFE1F1E851)

**遍历时长**

应用内点击、滑动等操作的总执行时长，用户可根据需求自定义遍历时长，默认为1小时，最大支持120分钟。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6J34F3eZQ-qKzu3OrRuuIw/zh-cn_image_0000002663932295.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFA4927D6573F1D19896985E578C452EA2F7EE178A7820DB6E7B5F10854D8904 "点击放大")

**高级配置**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/FoUIzmuuS_WitXBmr50hFg/zh-cn_image_0000002633533208.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A69873AFBC006870DC01234E88FD1E407DA0B4A7DADB4C364DA6367D6B40193)

**检测标准**

检测基于用户体验分为三个标准，分别为：

* 极优体验：操作体验快速、流畅，发现更多的性能体验问题（磁盘空间占用会增加)，可选项。
* 较好体验：操作体验良好，发现可感知的性能体验问题，默认选项。
* 一般体验：操作体验较差，发现感知明显的性能体验问题，需重点关注，默认选项。

**指标监控**

自动化遍历执行过程中，被测设备的系统资源指标项采集，当前支持采集CPU、内存、温度、网络、GPU、存储和电量，固定采集CPU和内存，用户自行选择是否采集其他指标项。

**其他配置**

* 后台负载测试：开启后会在自动化遍历结束后，让应用进入后台，采集应用在后台状态下的CPU负载和内存占用，默认采集。
* 保存全部数据：开启后会保存自动化测试过程中产生的所有视频、trace、图片等数据，关闭后只保存影响体验操作的步骤数据。
* 生成IDE分析文件**：**开启后会将报告中的性能问题压缩打包，压缩包可导入 DevEco Studio 的体检工具，进行问题诊断并给出修改建议。

**测试执行**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/11RoRsokQoinBabIFaHnyw/zh-cn_image_0000002633533220.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=214779E33B6A0680B1251FAEFC23A349D4AFDF35821C82389D713583EDB0EE9A "点击放大")

**①：**实时显示任务的整体进度。

**②/③****：**实时显示每个用例的执行状态和分析状态。

**④：**实时打印任务执行时的日志。

**查看报告**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/sCzLoG8IQRCZacQ1eUU-EA/zh-cn_image_0000002664012357.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EC8EBAAC329E9626A2CCFF34AA39BEB64E44C35666671818FA63E84AB0CA92E "点击放大")

**基础信息**

* 任务数据：任务名称、开始时间、持续时间、执行人。
* 应用数据：应用包名、应用版本、API版本。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数以及被测设备的详细信息。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

**整体评估**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/_YhVcjTBTVWkWdPOII5-OQ/zh-cn_image_0000002664012333.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=13DE143BF2F41BD56BBFBBD519E0EA99AC2DD79B57FE0DCD6C6C4074D5931112 "点击放大")

整体评估报告部分会展示本次的测试结论，包括如下部分：

* 测试结论：描述本次测试的结论，包括遍历时长、执行操作次数、发现问题数。
* 报告对比：一键跳转到性能测试报告对比工具，从概览、指标达标率等多维度进行报告对比。
* 性能报告自动分析：一键跳转到性能报告自动分析服务，对该报告中发现的问题进行自动分析。
* 导出IDE体检文件：支持生成体检文件导入到DevEco Studio中进行问题分析定位。详细操作指导请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 问题分布环形图：呈现本次任务发现的总问题数以及各指标性能问题的分布情况。
* 操作类型和问题表单：统计遍历过程中，启动、点击、滑动、观看的操作次数，以及对应指标发现的问题数。
* 一般体验：为了帮助提前识别可能影响应用日常使用的性能体验问题，将所有体验问题进行过滤，聚焦于明显影响用户体验的严重问题，问题数会比所有体验问题少。
* 较好体验和极优体验：为了追求极致性能体验，这两种体验问题的标准比一般体验的标准更严格，上报的问题也会更多，用户可以根据实际情况解决问题。

整体评估表格中的红色数字表示当前体验标准下的问题次数，支持点击查看问题步骤列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ed9tvyviRlqLhphJKcGF9A/zh-cn_image_0000002633533218.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCC9F2E77E3983D4CAF93D340AC7DF2D1E0E8C149F3512A1408E4C6AB9DDECEE "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/ZGx-1OxvSSO--nIOutkBIQ/zh-cn_image_0000002663932303.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=349545EE03917B5B971B28FF96600E78A73F8F01C304CB325324DE21E2571F3B "点击放大")

* 维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。
* 查看详情：点击展开按钮，呈现该操作的帧图片集，点击视频时间数字，能直接定位到具体的图片。

**遍历统计**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/NomRgPuhSdezEO2zu4BsuQ/zh-cn_image_0000002633693140.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=961CC2DB3E8C9C02A2724F92969C575A86BE7357266A2649159998979885682E "点击放大")

**遍历统计会展示应用遍历过程中的操作步骤信息，包括如下信息：**

* 遍历时长：用户在任务创建时指定的遍历时间。
* 启动次数：用户在任务创建时指定的启动测试次数。
* 点击次数：应用遍历过程中，点击操作的总次数。
* 滑动次数：应用遍历过程中，滑动操作的总次数。
* 观看视频：应用遍历过程中，观看视频操作的总次数。
* 图片列表：展示遍历的操作过程。

**资源数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/sP94EK7QQwutOB46USnLQw/zh-cn_image_0000002633693122.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B2AE1FF64D07B935E3526F6933BCE4D047A2CF8D223B12963C1D4CC8D1AD0E0 "点击放大")

资源数据报告部分呈现的是应用在遍历过程中的资源占用情况。

* CPU和内存占用是默认采集，GPU、网络、电量和温度为可选项，可在任务创建页面“高级配置”中勾选。
* 后台CPU和内存的测试需要在任务创建页面打开“后台负载测试”开关，检测应用在后台时，CPU和内存资源的占用情况。
* 峰值步骤：展示当前系统资源指标的最大值，点击可跳转至对应的步骤详情。

**操作详情**

操作详情展示遍历测试过程中的操作步骤信息，整体呈现内容如下所示：

* 应用启动测试：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/atdsBXtXRHuz2fObw9iY_A/zh-cn_image_0000002664012339.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=24A8BD81DF490789C665D0A7782F5E9F67FC39AC80AB42B09D9058F108D3E8BF "点击放大")

展示应用启动测试的步骤信息，包括操作前后截图、测试数据以及维测数据。

操作前&操作后：展示该步骤操作前后的设备截图。

指标项：展示应用启动过程的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示”-”。

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不展示打开按钮。

* 应用内遍历测试：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/83yEGndZQXukV8l_BOqB-g/zh-cn_image_0000002664012351.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=657A0487BAF9F5B31F1E8A2980D1E58C71198E0576B15675D4A3DCEFD5DA528B "点击放大")

展示应用内进行遍历操作的步骤信息，包括操作前后截图、测试数据以及维测数据。

操作前&操作后：展示该步骤操作前后的设备截图。

指标项：展示应用启动过程的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示”-”。

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不展示打开按钮。

* **异常指标信息查看：**

对于超标的检测结果，可以通过点击超标项，查看该步骤的详细信息，展示内容如下图所示（以响应时延为例）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/07P4iVc-QSWcyH7ar8qbGw/zh-cn_image_0000002663932281.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=73613C85348A596BA927ED0A454C6A4834569EDCA3379C4DD6FF2EFE8C567FAF "点击放大")

测试值：表示该步骤的响应时延测试值。

开始时间：表示用户从122这一帧开始操作。

结束时间：表示应用UI在255这一帧开始响应。

图片组：逐帧展示该步骤的操作视频。

**问题定位定界**

**维测数据**

点击打开按钮跳转到问题步骤对应的资源文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/580CejMkRqiKqQfaSiBEvg/zh-cn_image_0000002633693124.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=EA721EB904510231029188DECEAF274802A46724D4D5DC78EF8A153754DA9666 "点击放大")

用户可查看步骤执行全过程的图片和视频，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Or9AdXx5TKCvFV9uFL_a2A/zh-cn_image_0000002664012349.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=417389B0EF370B106F9CB89B08EE6F41A3E7717B1AA95C341D462EEEB059812F "点击放大")

**perfdata数据**

可使用[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) 5.0.3.300及以上版本中的场景化调优工具DevEco Profiler打开及查看该文件，内含步骤执行过程中的trace打点和调用栈信息，也可使用压缩软件解压为单个的trace文件和调用栈文件，解压后的文件可使用[SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host)工具打开。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/H8ziMBdaQnyP9C3leCJSFw/zh-cn_image_0000002664012343.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB4E3E820B86FC5119BAD77BF45E0D14D30E338A38A0E15F9334845E46FDAF9F "点击放大")

**说明** 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->性能测试->性能基础质量测试->任务创建页->测试指南中查询。

更多应用性能优化建议及问题定位，请查阅：[应用性能体验建议](performance-experience-suggestions.md) 及 [最佳实践-性能-性能场景优化案例](../best-practices/bpta-scenario-performance-optimization.md)。

## 场景化性能测试

**服务说明**

场景化性能测试服务提供了一套包含自动化脚本执行和性能指标分析的解决方案，涵盖响应时延、完成时延、卡顿、音视频和黑白块五大类性能指标的检测。

应用的设计、开发及测试过程中推荐参考[应用性能体验建议](performance-overview.md)。

**服务使用场景**

支持一键式测试应用的关键场景和核心路径的性能体验。通过任务报告，用户可查看关键场景上的多维度性能指标表现，精准识别性能体验问题。

**注意** 

**场景化性能测试的性能指标检测能力****与性能基础质量测试一致；详情请查看[性能基础质量测试](performance-testing.md#section12324184817324)。**

**脚本写作**

请参考[自定义性能脚本测试（基于Python)](hypium-perf-python-guidelines.md)。

**任务创建：**

打开DevEco Testing客户端-测试服务-性能测试-场景化性能测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/W81AOkEgSl2jbWTOKRb5RQ/zh-cn_image_0000002663932275.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=1147671C68EB95357E97345A48D547F0EFCCD78FBD8C12ABC5B3422BDE677FE0 "点击放大")

**配置项说明**

**执行轮次**

用例可重复执行多轮提升测试结果的可靠性，最多测试10轮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/L6jFfgEhTcK5DFZnjNjCAA/zh-cn_image_0000002633693120.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=14D03300DE759ABB56BBDB9D318F03189FD5C2A57A3E43F8C9A6371C2A931A01)

**用例工程路径**

存放自动化用例的工程路径。

如果已有用例脚本，可点击创建工程模板，将脚本文件存放到工程根目录的testcases目录下，用例工程路径请选择工程根目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BjPYn19iTaWPeJfw1GZ-JQ/zh-cn_image_0000002633693136.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=210F236CD06D28B2649F2EEF2D501B6A1A19536FDC1CB61A758EB5D186A3ABDB)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/RXgT4jC3RaS2iYONqbL6_A/zh-cn_image_0000002664012345.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF2830F6EE4AE37676B65C61C9C6EDC1C9692584ACEBB72C3A27E29A6AD06ADA)

**高级配置**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/Bdcu4SkETB2qRRC4D_cMeA/zh-cn_image_0000002663932291.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0F051A944DFBB2AB4867E4244CDE1B48ED13CBA722225E6F334C7E6DEADE87E "点击放大")

**检测标准、****指标监控**

与性能基础质量测试一致，可点击[性能基础质量测试](performance-testing.md#section12324184817324)查看。

**其他配置**

保存全部数据：开启后会保存自动化测试过程中产生的所有视频、trace、图片等数据，关闭后只保存影响体验操作的步骤数据。

生成IDE分析文件：开启后会将报告中的性能问题压缩打包，压缩包可导入 DevEco Studio 的体检工具，进行问题诊断并给出修改建议。

**任务执行**

所有用例按照顺序和轮次依次执行，并行分析；任务完成后，会自动生成报告页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/vfxZksGrTE-Fp4Y8anp_uQ/zh-cn_image_0000002663932285.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=91D1E0E98C6CDD84697A07CF178626D409A0E86118085BCBB8000911816EE330 "点击放大")

①：实时显示任务的整体进度。

②/③：实时显示每个用例的执行状态和分析状态。

④：实时打印任务执行时的日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含基础信息、整体评估、资源数据、用例详情等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/H3FxDKg-SX2453JECR_r5A/zh-cn_image_0000002664012335.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C6841ABB356B101C4C758AD28434247DA0CA296A8CBE6324053EA7A15ACD72F "点击放大")

**基础信息**

任务信息：任务名称、工程路径、开始时间、持续时间、执行人。

备注：备注信息支持自定义修改。

环境参数：支持查看任务下发的参数以及被测设备的详细信息。

执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。

打开目录：点击打开任务数据文件夹。

**整体评估**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/bO-kdTEZSxee2MgRoqZAgA/zh-cn_image_0000002633533224.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=939D602E4E73FE516AE34568305A48237570B989F4324A48875CEC00DF9B176C "点击放大")

整体评估包括如下部分：

* 测试结论：描述本次测试的结论，包括执行用例个数、轮数、操作次数及发现问题数。
* 报告对比：一键跳转到报告对比工具，从概览、指标优劣化、用例对比详情等多维度进行报告对比。
* 性能报告自动分析：一键跳转到性能报告自动分析服务，对该报告中发现的问题进行自动分析。
* 导出IDE体检文件：支持生成体检文件导入到DevEco Studio中进行问题分析定位。详细操作指导请查看[导入DevEco Testing的检测报告进行诊断](ide-app-analyzer-testing.md)。
* 问题分布环形图：呈现本次任务发现的总问题数以及各指标性能问题的分布情况。
* 用户场景和问题分布表单：执行状态表示用例场景多轮执行的状态，用例场景展示的是脚本中定义的场景用例名称，后面几列为对应指标发现的问题数。
* 一般体验：为了帮助提前识别可能影响应用日常使用的性能体验问题，将所有体验问题进行过滤，聚焦于明显影响用户体验的严重问题，问题数会比所有体验问题少。
* 较好体验和极优体验：为了追求极致性能体验，这两种体验问题的标准比一般体验的标准更严格，上报的问题也会更多，用户可以根据实际情况对应用进行优化。

**执行状态共有如下几种：**

* 成功：用例所有轮次均执行成功。
* 部分成功：用例部分轮次执行成功，部分轮次失败或者未执行。
* 失败：用例无成功执行轮次。
* 未执行：用例未执行。

整体评估表格中的红色数字是当前体验标准下的问题次数，支持点击查看问题步骤列表：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/RlJWcFwhQYuDd5cPeUBpvg/zh-cn_image_0000002663932279.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=045524481246031A3E6E14DAA2E2B3FA4626CDA94DE252488ECFDFCE86802E7D)

展开后呈现问题的详细信息：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/O00P_cjnTR6HoOSNdr6S2g/zh-cn_image_0000002633533212.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=59E1D72AE7C036AD1319C61EA7825992E9801C807D18EB681B4A9627353C2B9F "点击放大")

维测数据：点击打开按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。

查看详情：点击展开按钮，呈现该操作的帧图片集，点击视频时间数字，能直接定位到具体的图片。

**资源数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Svec7mfnTbOTIxE47r7uMw/zh-cn_image_0000002664012337.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5FB59B9728D34BD6D883E5319A167DAE8FBD2AFEEFFE8F00C90AD87E537808A "点击放大")

资源数据报告部分呈现的是应用在遍历过程中的资源占用情况。

* CPU和内存占用是默认采集，GPU、网络、电量和温度为可选项，可在任务创建页面“高级配置”中勾选。
* 峰值步骤：展示的是当前系统资源指标的最大值，点击可跳转至对应的步骤详情。

**用例详情**

用例详情会展示用例的执行轮次和执行步骤的信息，整体呈现内容如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/BBsdrHncSTaVp4sohwg05A/zh-cn_image_0000002633533216.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=534088D5356733307B2B4DE8C4AC3D3980A1FDE11CC2867AEE6ABAA0E90EB285 "点击放大")

OH\_XXXX：代表用例名称，由脚本进行指定。

用例资源数据： 统计该用例在执行过程中采集到的CPU，内存等资源数据，并针对改用例进行数据汇总计算。

测试步骤：展示用例的步骤信息，默认展示该步骤在多轮测试中的测试数据，对于超过标准的测试值，数据标红显示，支持点击查看问题详情。对于该操作不涉及的指标，显示“-”。

点击步骤左侧的箭头，展开该步骤的详细轮次信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/sQoErGHrQWOXRvtmPAUPFA/zh-cn_image_0000002633693126.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=0FF82809C8B7E35AD211B0D9EC3CF25A408F9D63F4F9072445A1AE90C439DE68 "点击放大")

操作前&操作后：展示该步骤操作前后的信息，用户可以通过前后截图了解操作的场景。

指标项：展示每轮的指标检测结果信息，如果测试值超标，字体标红显示，支持点击查看问题详情。若不涉及，则显示“-”。

维测数据：点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/svLc1XKWSpKYacus9OdlCQ/zh-cn_image_0000002664012355.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=97D7FFB35AC96F4B2E5F5C378B306D54A3BFDABFEEB519782B3D259F3D1262CE "点击放大") 按钮，自动打开该操作的数据文件夹，汇总当前操作的trace、视频、图片等维测数据，协助用户进行问题定位。若该步骤所有测试数据都达到标准，则不会出现该按钮。

对于超标的检测结果，可以通过点击超标项，查看该步骤的详细信息，展示内容如下图所示（以滑动占位符加载指数详情为例）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/VtfeHlPmTTGBIQ93X9lKJQ/zh-cn_image_0000002633533222.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=F326E4760D15B5229AFA4C16BEFF1EA3AEDA7A9DCC9235729A63A425F0AFF274 "点击放大")

开始时间：从3299这一帧开始，页面中出现占位符。

结束时间：在3465这一帧，占位符全部都加载完成。

图片组：逐帧展示该步骤的操作视频。

**问题定位定界**

**维测数据**

点击打开按钮可以跳转到问题步骤对应的资源文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/83koR05nSx-MXE7naD9_AQ/zh-cn_image_0000002663932289.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=76E9210FAF487E31DB842C5A1B4732C1BF380EA2F864EA6288DF6A2091426395 "点击放大")

测试步骤执行全过程的图片和视频如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/N1DConn6R0mf2P7KLsL4Lw/zh-cn_image_0000002663932297.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=803B6CF793129DD00A78854A0DFD6B96685B8257A99B295D2A09C176DC5DD057 "点击放大")

**perfdata****数据**

可使用[DevEco Studio](https://developer.huawei.com/consumer/cn/download/deveco-studio) 5.0.3.300及以上版本中的场景化调优工具DevEco Profiler打开及查看该文件，内含步骤执行过程中的trace打点和调用栈信息，也可使用压缩软件解压为单个的trace文件和调用栈文件，解压后的文件可使用[SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host)工具打开。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/j5auyQWDT9-zm6LQ0gd4og/zh-cn_image_0000002664012353.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=833DA3A4E096BC920780F26ACCCD7EFAD2AE88C5C810D5B171039AF8966290EA "点击放大")

**说明** 

更多场景化性能测试报告解读及常见问题，请前往DevEco Testing客户端->测试服务->性能测试->场景化性能测试->任务创建页->测试指南中查询。

更多应用性能优化建议及问题定位，请查阅：[应用性能体验建议](performance-experience-suggestions.md) 及 [最佳实践-性能-性能场景优化案例](../best-practices/bpta-scenario-performance-optimization.md)。

## 性能指标监控测试

**性能指标监控测试：**为用户提供指定业务场景性能测试能力，选择待测应用后手动操作应用，输出测试过程中应用和整机的性能指标数据。

**任务创建**

打开DevEco Testing客户端-测试服务-性能测试-性能指标监控测试卡片，在任务创建界面按需配置任务参数，点击创建任务后开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/KSW4ZoXpQ6Gv4WA5t_Ruhg/zh-cn_image_0000002633533210.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=BE1B47E703115AB1F743201922B074555FDC413366E5FBFF1B98A76979DE2FD7)

任务名称：用于标识任务，根据时间生成默认任务名，支持自定义任务名称。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择待测设备，待测设备的系统版本建议使用 HarmonyOS 5.0及以上版本。

选择应用：选择已安装在测试设备上的应用或安装新的应用。

指标监控：固定采集CPU和内存，用户自行选择是否采集其他指标项。

参数配置完成后，点击创建任务按钮开始测试。

**测试执行**

创建任务后，跳转到执行页，执行测试环境初始化操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/lIOMu_LSQN-43JrKQGpfPw/zh-cn_image_0000002633533214.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=338AD15AAF2B5A9DA7BE9785518EFBDAB615E24728E5C537CB0AC1A05413690B "点击放大")

等待测试环境初始化完成后，待测应用启动，自动跳转至监控页面，并启动监控，在手工测试场景准备好后，点击右上角的开始图标按钮，出现“开始采集”标识线，开始统计分析数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/8y7k1iT2R-q9ncJprN9AqA/zh-cn_image_0000002664012359.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=358668E9926A081591E7F24B2EE4C3F1D44A04B57C3E2B936E9D7FEFEB973775 "点击放大")

开始采集后，点击开始图标右侧的“记录”图标，可标识场景，并提示“场景开始”。待测场景结束后，再次点击，完成标识场景。概览中单独计算被标识的场景数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/bLsvVtJhR7-QWjpzfJyKYg/zh-cn_image_0000002633693138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=04A56AC46D8FAF9BF10DC3756D3A32A22498F75250C7E67EBD224A838E187048 "点击放大")

在测试过程中，可随时点击“采集 trace”按钮，采集连续30 秒的 trace 信息，单次任务只保留最近10 个 trace 文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/47JwZjihRXyxfDI1kMbGxQ/zh-cn_image_0000002663932293.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FD6BDC4B34FC94F735BABBC0DF07A5262D2D5ECCB9562B67D4B7225529DACCE "点击放大")

结束采集。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/INQc0Iu4SL22AB0i0cT7EA/zh-cn_image_0000002664012347.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=886661524C0BCB1E0CFE7D008C76A7FDE1C96C931EE78E40F50069584B7329BA "点击放大")

**查看报告**

测试报告包括：基本信息、环境参数、执行日志，打开目录及指标数据。

指标数据：包括 FPS、设备 CPU/GPU 的频率、负载监控等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/9Y7HfhTvTd6-PNAyuk6W3Q/zh-cn_image_0000002633693134.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=282D071E9155F485241C8F1E47811E6869F397CC73AC9856AB0D776C47641030 "点击放大")

指标数据介绍：

FPS：应用界面每秒刷新次数。

帧间隔：两帧画面刷新时间的间隔。帧间隔应保持稳定，并与应用帧率负相关。当帧间隔过大时， 设备会出现卡顿现象。

CPU 频率：各个 CPU 核心的实时频率。在 ARM 架构下，相同规格的核心实时频率一致（即大、中、小核分别具有不同的实时频率，但相同的核心的实时频率一致）。

内存占用：应用及整机的各个内存指标测试数据。

GPU 频率：GPU 核心的实时频率。

GPU 负载：GPU 的当前负载。

温度：设备的壳温，前壳温，后壳温，soc 温度。

网络速率：应用测试过程中的网络上下行速率。

Trace：可以通过报告底部的"打开Trace文件"按钮跳转到trace文件目录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/TrjFSgRcQay5mzvzJ7KUDA/zh-cn_image_0000002663932277.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=1874496EA6F80631FED38600F516E6BE24B7E61DB5AF15CB020634353153B0D2 "点击放大")

**说明** 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->性能测试->性能指标监控测试->任务创建页->测试指南中查询。
