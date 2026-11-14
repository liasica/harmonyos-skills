---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu
title: CPU活动分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > CPU活动分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fd3ad5503b508d00a150235a7b0ef262ef483ca16e7c8c2debc014912b5a8d84
---

## 功能介绍

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

CPU模板支持的泳道包括：Energy、CPU Core、Process。本文介绍CPU Core、Process泳道，Energy泳道的详细信息请参考[能耗诊断：Energy分析](ide-profiler-energy.md)。

**说明** 

任务分析前，需创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在[会话区](ide-profiler-session.md)选择**Open File**，导入历史数据。

## 查看各CPU使用情况

1. **CPU Core**泳道显示当前选择调优应用或元服务的CPU的使用率，在泳道右侧**options**下拉列表中选择显示内容：
   * Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
   * Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。

   框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息、状态分类统计信息，以及所有时间片的数据统计信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/sC3BSLL9QdaCLaNSluXvvQ/zh-cn_image_0000002808766625.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDEDC5F88F3FE3C1296EDA69C2FF6E8803F4E33CC1F023F437896121EAA3DDFF "点击放大")
2. 将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。

   **说明** 

   将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/EdnJAWLPRAyR849I0PlfkQ/zh-cn_image_0000002779567040.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CBCDE794F835AC3661F7DDF809D239B09724C2F8D3DBAA59229E4AD67591739 "点击放大")
3. 指定时间片，查看统计信息。
   * 单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/jRtdEr2NT-CtRtSKuh6wXw/zh-cn_image_0000002779407068.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1D48BA10F62C266F6A070D2F2A6869C3A0363E7C81FB6BC3FF81B7E57EE92DC "点击放大")
   * 框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/wEJ_dbjESfyjX9DAaFUG7g/zh-cn_image_0000002808886707.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=365748D9BF61CB3324D5806A07ED4C7CF709293FE6946D5EE468788731BE7E82 "点击放大")
   * 开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/6g_XRF_aSriSJ4SAvZo30A/zh-cn_image_0000002808886705.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CB7DE496D81CB8D7FD403358E6911EAFCEE08D435AFA054C42FF461854C18C2 "点击放大")

## 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/qUOVRNfEQLqpPiiRz8bfmA/zh-cn_image_0000002808766629.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=611A96C0513A28C695F36F8ABA5BFE5B1911201A7B036A826CA20720F7B6F3C5 "点击放大")按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VcusY5HPT1KGWEIw88iHDw/zh-cn_image_0000002808886709.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D76DE859D3749391E03B74ABF758C2DBBD890AF24075FC811A2BAF99EFB34232 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

* 单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ITdwPCTCReuJB_LAKmUPKQ/zh-cn_image_0000002808766623.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D9B8CD92679990B8B3685C2293FB94CA5AFBB861A92A920385ED03CBDCD560F "点击放大")
* 框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。

  **说明** 

  中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/KFdoi1VuSzql5azPmxU9Lw/zh-cn_image_0000002779567048.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDADC04B191D3066269890036F33FEE28B1515CA832F4F6372B2209EF017D9FE "点击放大")
* 框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。

  **说明** 

  并行度（Parallelism）取值范围是[1,CPU核数]，数值越小代表并行度越低。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/KtQMLX_2Qiusjk1cAFnG9A/zh-cn_image_0000002808766627.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1488DB83657B2F486C7F2E0AE41B458BA4DD3854B9F1DDA79942FAD5ABFDAEBC "点击放大")

## 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

* 点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。

  **说明** 

  + 如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
  + 从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/G2PxfmXwTT6EXaPahHauIQ/zh-cn_image_0000002808886703.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=75D7CA2B1C48723F70313F50DE02217814EF486E8BF69B6D18AA3367B4A4A64D "点击放大")
* 框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/l1E05VIFT-2eAHUZXs766g/zh-cn_image_0000002808766621.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=925EA74CF670DF94A80A29BAA836500F2DB3C507A4D158AE9B87755F21F2B217 "点击放大")
