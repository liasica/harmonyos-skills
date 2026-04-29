---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-frame-case
title: 案例：使用Frame模板分析应用卡顿问题
breadcrumb: 指南 > 优化应用性能 > 卡顿丢帧分析 > 案例：使用Frame模板分析应用卡顿问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:32+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:5c825856c0c4af6505e031b182aa00e7dc784ce27d17425b2b0923d0a9a92f72
---

本案例介绍如何判断应用存在卡顿帧，再通过调用栈和trace信息分析应用运行逻辑，找出应用卡顿的原因。

应用卡顿分析基础功能请参考[Frame分析](ide-insight-session-frame.md)。

## 分析步骤

分析应用卡顿类问题步骤如下：

1. 确认是否存在卡顿帧。
2. 若存在卡顿帧，根据调用栈和trace等信息进一步确定问题点。

## 分析Frame数据

### 分析应用是否存在卡顿

1. 框选Frame泳道，窗口下方的“Statistics”区域中会以进程维度对选定时间段内的Frame信息进行统计，当Jank Count大于0时，说明存在卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/01tkrbg5TvCS6MWHo_rAJg/zh-cn_image_0000002530913404.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=D25BFCB65FD2153C0A8AEB61AFEE5EAE266DCD2591ED3FC89979C763A9260E48 "点击放大")
2. 找到“Statistics”页签中存在卡顿帧的进程，点击进程名称后方跳转按钮，跳转到“Frame List”页签。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/f7VFTQgwTgiOOxC2CSrK5A/zh-cn_image_0000002530753402.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=28D2A4D903FF7E2CF8D14C4D5C972382855AFD44645717A7E57E81EA66970FBA "点击放大")
3. “Frame List”页签会展现该进程对应的Frame列表。在“Frame List”页签中对卡顿丢帧类型（Jank Type）进行升序排序，单击“Frame List”页签中任意一卡顿帧，直接跳转到该帧且泳道上该帧被反选。

   说明

   * 在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
   * AppDeadlineMissed：App侧的卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/vqGyetyqToS8RnSKGzcOFA/zh-cn_image_0000002530753404.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=A90F185CF3B97E4EB79ABC7801137D74FBDDE112E3CC9E39F2C8B541EE13B03E "点击放大")
4. 点选该卡顿帧，窗口下方的“Details”区域中显示卡顿帧的关键信息。右侧应用进程前方跳转按钮可以跳转到应用进程Trace。
   * Expected Duration：一帧绘制的期望耗时。与fps的大小有关，如fps为120，对应的Vsync周期为8.3ms，即App侧/Render Service侧的帧耗时，一般需要在8.3ms以内。
   * Actual Duration：一帧绘制的实际耗时。

   如下图，可以看到该帧的期望耗时为8ms 330μs，实际耗时为44ms54μs，远远超过了期望耗时，因此被识别为卡顿帧。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ov2ubt19T-OrUP1_S0-74A/zh-cn_image_0000002561753341.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=9FD4BF8EAF57CB6400F7B8D89750A95E31814809DBF00A2E3EA8CC98598DC555 "点击放大")
5. 框选该异常帧时间范围，结合ArkTS Callstack泳道、Callstack泳道和Trace等信息进一步分析异常点。

### 案例：分析应用卡顿原因

1. 找到并框选要分析的异常帧，查看ArkTS Callstack泳道分析ArkTS侧耗时函数。优先查看主线程调用栈，即线程号与进程号一致的ArkVM子泳道。可以看到ArkTS侧一些方法的耗时。
2. 查看下图调用栈，除(program)外，其他调用栈耗时小于一帧绘制的期望耗时8.3ms（被调优的设备fps为120），因此该卡顿帧主要分析调用栈(program)的耗时。

   (program)代表程序执行进入纯Native代码阶段，该阶段无ArkTS代码执行，也无ArkTS调用Native或者Native调用ArkTS情况，一般很难通过这里分析出有效的信息，需要切换到Callstack泳道看具体的调用栈信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Drm4igZFSXScRe2TNoaKPA/zh-cn_image_0000002530753408.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=A12EB3001A452410815BF14CC10A94A8EB3A6AA65DC01EF6744B5391779513EB "点击放大")
3. 切换到Callstack泳道，查看Callstack泳道的主线程（线程号与进程号一致）子泳道，滑动观察下方Heaviest Stack区域“%”列中占比最大的函数调用栈，Category中亮色代表开发者调用栈，灰色代表系统调用栈，可以看出下图中耗时主要在系统侧的so，无法识别具体异常原因，接下来进一步分析应用进程Trace。

   说明

   也可通过底部的“Call Trees”选择框来隐藏系统调用栈，减少干扰信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/g0G4jW48S_-hckmgvnu2pQ/zh-cn_image_0000002561833327.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=CC4F032DA24B0B4305AF791943A5D408D6B1465F2E3DEF60BE3A88915FF60318 "点击放大")
4. 切换到应用进程Process泳道，查看主线程（线程号与进程号一致）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/MfVcbsiZT1ObLLIsHEvBgA/zh-cn_image_0000002530913408.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=8DA52E691AF434380778B27A3295B685B86CD3528E058C3E26CBAD9D6EAB0DE5 "点击放大")
5. 窗口下方详情区可查看到Trace统计信息列表，逐层展开耗时最长的Trace，定位到主要耗时是在3次H:CreateImagePixelMap。接下来进一步分析这3次H:CreateImagePixelMap耗时的原因。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/B-IlGQL6T-WnYcaem0H_Mw/zh-cn_image_0000002561753345.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=1AB92604A842A6465BDB872F558EBE29C4B1226DECE5A3D47D52293DF7BB7906 "点击放大")
6. H:CreateImagePixelMap和图片加载相关，再结合业务代码查看，可以看到是因为同步加载网络图片，建议修改为异步加载。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/oIJjOfRtQYSMk4l-hotcVA/zh-cn_image_0000002561833331.png?HW-CC-KV=V1&HW-CC-Date=20260429T054730Z&HW-CC-Expire=86400&HW-CC-Sign=44948711DB9453C346E9C7F30011A70637040350E65DAF73B12E7AD9E40C09A9 "点击放大")

   说明

   一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。不建议图片加载较长时间时使用同步加载。
