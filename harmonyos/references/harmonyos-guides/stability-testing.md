---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stability-testing
title: 稳定性测试
breadcrumb: 指南 > 应用测试 > 专项测试 > DevEco Testing > 稳定性测试
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c3092c6ae61859bd84a3b5c5117ddae64ac268b9f1a8d792724e5a66cfa8cb09
---

## 稳定性基础质量测试

**稳定性基础质量测试：**根据应用稳定性建议，检测应用运行过程中是否存在应用崩溃、资源过载、内存泄漏等异常情况。

**创建任务**

进入DevEco Testing客户端，在左侧菜单栏选择“测试服务”找到“稳定性测试”，点击“稳定性基础质量测试”服务卡片，即进入任务创建界面。用户按需配置任务参数，点击创建任务即开始测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/4Mh-2PXDTDGn9bfpvUQMXA/zh-cn_image_0000002663932205.png "点击放大")

任务名称：用于标识任务，工具会根据时间生成默认任务名，支持自定义修改。

备注信息：按需填写任务备注信息，便于快速筛选报告。

测试设备：选择一个待测设备和待测应用，系统版本支持 HarmonyOS 5.0及以上版本。

选择应用：可选择测试设备上已安装的应用；或安装新的应用，即在测试设备上安装新的应用包。

是否卸载应用：选择卸载应用后，测试时会进行卸载无残留检测，测试任务结束后将自动卸载被测应用。

是否开启多线程检测：打开后，系统支持检测应用多线程安全问题（例如：多个线程并发写入操作）。

是否开启[MemDebug](../best-practices/bpta-stability-hwasan-detection.md#section10791454125320)模式：打开开关以后，会打开被测应用的内存越界检测开关，可以辅助发现和定位内存越界类问题。

**说明** 

**稳定性基础质量测试最佳测试时长建议设置为8****小时**。

**控件黑名单**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/MIG3DMETT6u1_QxZnfL-Ow/zh-cn_image_0000002633693040.png "点击放大")

控件黑名单通过指定控件的关键字（控件感知语义或layout中控件text属性值）和控件Xpath进行正则匹配识别黑名单控件；黑名单控件在遍历中不会进行操作；屏蔽的黑名单控件在遍历过程中会在应用页面中置灰。

1、关键字：可以填写页面内可交互控件选框中的关键字，例如“购物车”、“我的订单”等。

2、XPath：可通过UIViewer工具或已有的遍历图谱文件获取控件的XPath，将展示对应XPath图片；XPath最大支持30个。

**说明** 

**1、关于控件黑名单中“XPath”信息也可以通过探索测试报告中的遍历地图获取**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/zVQWfciRSgS3cQtenllHqg/zh-cn_image_0000002664012247.png "点击放大")

点击遍历地图中的关联线条；即可在右侧查看该跳转事件详情。

**指定入口（非必选项）：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/0s2UuUPSSbiomEpSqSSqtw/zh-cn_image_0000002633693046.png "点击放大")

1、DeepLink：可以选择DeepLink链接跳转至应用特定页面作为入口页。DeepLink可支持多个，每次触发随机跳转其中一个DeepLink。

2、入口切换策略：

按固定概率切换：根据设定的概率来决定是否切换入口，每次操作以指定的概率随机选择执行一个DeepLink跳转。

按固定周期切换：根据设定的周期来切换入口，固定时间周期随机选择执行一个DeepLink跳转。

**测试执行**

创建任务后，将会跳转到执行页，进入测试环境初始化阶段。待测试环境初始化完成，待测应用被启动。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/AyUbgIpGTj6pEP2Aqz21oQ/zh-cn_image_0000002663932193.png "点击放大")

测试过程中，在测试页面可以看到测试进度、检测状态、实时投屏及执行日志。

**查看报告**

测试完成后，自动生成测试报告。报告包含任务信息、结果统计、检测规则。

任务信息中，可查看当前应用信息、任务执行时长及详细的环境参数（配置信息及环境信息），点击打开目录按钮支持导出 html 的报告文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/GjDBpO5tTnmtCIkRnYSXKA/zh-cn_image_0000002633693020.png "点击放大")

测试概览中，包含结果统计及检测规则，可直观查看本次任务中，测试项检测结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/o4JkcJGbSymQtr5X3ISZxA/zh-cn_image_0000002663932217.png "点击放大")

检测不通过或检测异常的规则项，点击查看详情即可查看异常问题详情，包含检测项概览、测试截图、问题列表。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/s7ikupXBSuaBqgwHBGLwkw/zh-cn_image_0000002633533124.png "点击放大")

点击查看按钮，支持查看测试过程中的日志，用户可结合问题描述及日志详情进一步分析。

**说明** 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->稳定性测试->稳定性基础质量测试->任务创建页->测试指南中查询。

更多应用稳定性体验优化建议及问题定位，请查阅：[应用稳定性体验建议](experience-suggestions-stability.md) 及 [CppCrash故障定位指导](../harmonyos-faqs/faq-stability-10.md)

## 内存泄漏测试

**被测设备准备**

* 系统版本支持 HarmonyOS 7.0及以上版本。
* 确保手机性能状态正常，包括网络连接通畅、非高温、非低电量（推荐>80%），以及其他可能对性能表现产生影响的变量。
* 取消各类锁屏密码，确保自动化能完成上滑解锁。
* 应用图标在桌面可见（自动化会翻页查找不同桌面，但不会打开文件夹）。
* 对待测应用进行必要的预置操作，包括权限授予、用户协议确认、账号登录等等，以保障自动化遍历可顺利进行。

**任务创建**

**选择应用**

应用支持情况说明：

* 目前主要支持以下应用类型：
* ArkUI控件（含ReactNative框架开发）应用。
* 使用Flutter3.7.12及之后版本开发的应用。
* 除以上支持的应用类型，浏览器类应用、纯Web开发的应用及其他三方自研框架的自定义控件暂不支持。
* 待测试应用包需要调试证书签名。

**注意** 

若应用具备监听截图并展示功能，建议在测试前关闭该功能模块，以避免干扰测试流程及影响测试数据准确性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/eyNm_pTJRzeF729_qL9z0A/zh-cn_image_0000002664012253.png "点击放大")

**a.**选择已安装的应用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/Y2iDFi4_QD6g-VJ1ZlW9_A/zh-cn_image_0000002633533118.png "点击放大")

**b.**安装新的应用

点击按钮，在弹窗中选择应用安装包，支持.hap、.zip格式安装包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/HtAesGrQSmGXPGCXrRgxjA/zh-cn_image_0000002663932187.png)

**模式选择：**

* 自主遍历：服务可自主探索遍历应用。
* 自定义场景：需自行操作应用进行测试。

**是否录屏**：自定义场景模式下可选择是否录屏。开启录屏将保存全部场景录屏，关闭录屏则不保存录屏文件

**测试时长**：

自主遍历模式：应用内点击、滑动等操作的总执行时长，用户可根据需求自定义测试时长，默认为10小时，最小支持10分钟，最大10080分钟。预估每小时任务需要2G磁盘空间，磁盘空间不足时会给出提示信息。

自定义场景模式：应用场景执行总执行时长，用户可根据需求自定义测试时长，默认为1小时，最小支持10分钟，最大10080分钟。预估每小时任务需要2G磁盘空间，磁盘空间不足时会给出提示信息（同上）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/D-6Fq_G1TSuRQUEACGN4Hg/zh-cn_image_0000002633693050.png)

**高级配置**

仅自主遍历模式支持高级配置，默认关闭。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/IaSEsn2VRuqhD9iTfgg_vQ/zh-cn_image_0000002664012259.png "点击放大")

**控件黑名单：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/d__xOEYBTqqUot_ahqab-g/zh-cn_image_0000002663932199.png "点击放大")

通过指定控件的关键字（layout中控件text属性值）和控件XPath进行匹配，识别黑名单控件。黑名单控件在遍历过程中不会被操作。

图谱选择：根据所选应用选择在图谱管理工具中定义的图谱。

黑名单选择：根据所选图谱选择在图谱管理工具中定义的黑名单控件。

1、关键字：可以填写页面内可交互控件选框中的关键字，会有对应关键字图片展示。例如“购物车”、“影音娱乐”等；关键字最大支持30个。

2、XPath：可通过UIViewer工具或已有的遍历图谱文件获取控件的XPath，将展示对应XPath图片；XPath最大支持30个。

**指定入口：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/h9ph762IRMGRTa71ZCx4mg/zh-cn_image_0000002633533142.png)

* DeepLink：可以选择DeepLink链接跳转至应用特定页面作为入口页。DeepLink可支持多个，每次触发随机跳转其中一个DeepLink。
* 入口切换策略：
  + 按固定概率切换：根据设定的概率来决定是否切换入口，每次操作以指定的概率随机选择执行一个DeepLink跳转。
  + 按固定周期切换：根据设定的周期来切换入口，固定时间周期按输入Deeplink顺序选择执行一个DeepLink跳转。

**任务执行**

**自主遍历**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/c6huOy7jTY6EVLAfAP6KQw/zh-cn_image_0000002633533106.png)

进度：实时显示任务的整体进度。

测试场景：实时显示当前操作的场景名称。

检测结果统计：实时统计测试过程中发现的内存泄漏问题。

日志：实时打印测试过程日志。

**自定义场景**：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/CGD-0WhnSwONziLbmfVCfg/zh-cn_image_0000002633693056.png "点击放大")

进度：实时显示任务的整体进度。

应用内存占用：实时监控并可视化应用内存的动态变化。

场景开始：定义监控场景名称和执行时长，点击场景开始按钮后，工具才会启动内存数据的抓取，在场景到达执行时间结束或手动结束场景后，分析内存问题。

调用信息：实时呈现各场景下的内存泄漏问题及其对应的代码调用栈。

日志：实时记录任务执行过程中的系统日志与操作反馈。

**操作详情**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/XlMz7aDNQnuI8bhVShWv7w/zh-cn_image_0000002633693048.png "点击放大")

场景开始：待环境初始化完成，用户可添加场景以启动测试流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/evrAeHbJQ9Gplxp2j9Ui-A/zh-cn_image_0000002633533112.png "点击放大")

场景结束：场景可按设定时间自动结束，或手动终止；结束后进入分析模式，允许用户继续添加后续场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/c7-n288PRsCddd6eyLCcMA/zh-cn_image_0000002633693026.png "点击放大")

任务分析完成后可查看当前场景是否存在问题，不通过的场景将显示场景下内存增长最大的调用栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/FYH60MXMS_22mwQgeFVk9Q/zh-cn_image_0000002664012241.png "点击放大")

点击场景名称，可以看到场景下的所有问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/jajRPWSmRoGePaIaaIsJww/zh-cn_image_0000002664012269.png "点击放大")

GC：按钮点击后，会执行hidumper --mem-jsheap pid --gc命令触发指定应用进程GC。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/ldPImP76QTeRRbYoRYzsQw/zh-cn_image_0000002633693032.png "点击放大")

结束采集：点击按钮终止监控任务。系统将等待所有剩余场景的分析完成后，自动停止任务并生成最终报告。

**查看报告**

基础信息

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/_FgUchFtRSKsIWFQkxKuFQ/zh-cn_image_0000002664012267.png "点击放大")

* 任务数据：任务名称、开始时间、持续时间、执行人。
* 应用数据：应用包名、应用版本、API版本。
* 备注：备注信息支持自定义修改。
* 环境参数：支持查看任务下发的参数。
* 执行日志：支持查看任务执行过程中的日志，支持日志级别的筛选。
* 打开目录：点击打开任务数据文件夹。

自主遍历：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/HalXrxKbRVWYhKJz4A5szA/zh-cn_image_0000002663932213.png "点击放大")

概览部分会展示本次的测试结论，包括如下部分：

* 遍历执行时长：本次测试遍历操作所使用的时长。
* 覆盖场景数：本次测试遍历过程中触发的场景数量。
* 问题场景数：存在内存泄漏问题的场景数量。
* 内存泄漏问题总数：内存泄漏问题总数。

自定义场景：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/gJTuxarvSMyDSf0e7cltQw/zh-cn_image_0000002663932179.png "点击放大")

概览部分会展示本次的测试结论，包括如下部分：

* 场景监控时长：本次测试所有场景使用时长。
* 覆盖场景数：本次测试监控过程中触发的场景数量。
* 问题场景数：存在内存泄漏问题的场景数量。
* 内存泄漏问题总数：内存泄漏问题总数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/EvdYf-9nQcWig_Zhzup6EA/zh-cn_image_0000002633533130.png "点击放大")

点击覆盖场景数可查看所有场景详情。

**资源数据**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/R5X8daflSL-Pf_eHlQyb_g/zh-cn_image_0000002664012265.png "点击放大")

测试过程中内存指标的资源占用情况。

详情见[HiSmartPerf Device性能使用指导](smartperf-guidelines.md)

|  |  |
| --- | --- |
| **指标** | **说明** |
| TotalMem | 应用占用的整体物理内存 |
| GLMem | 应用占用的gpu内存 |
| GraphMem | 应用占用的图形内存 |
| ArkTsMem | 应用占用的arkts内存 |
| NativeMem | 应用使占用的Native内存 |
| AnnoPageMem | 应用使占用的匿名页内存 |
| FilePageMem | 应用使占用的文件页内存 |
| AshMem | 应用使占用的AshMem |
| StackMem | 进程使用的栈内存 |
| AvailbleMem | 整机可用内存 |
| FreeMem | 整机空闲内存 |

**说明** 

更多测试服务详情，请前往DevEco Testing客户端->测试服务->稳定性测试->内存泄漏测试->任务创建页->测试指南中查询。
