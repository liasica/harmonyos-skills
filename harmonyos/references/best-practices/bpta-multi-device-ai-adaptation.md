---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-ai-adaptation
title: AI辅助多设备应用开发
breadcrumb: 最佳实践 > 一次开发，多端部署 > AI辅助多设备应用开发
category: best-practices
scraped_at: 2026-11-14T08:54:10+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:2959cb7ed04666793c35c29c162e39ff75d4970a62608f694c4f1cd1de0119f8
---

## 概述

随着HarmonyOS终端产品形态多样化和规模增长，多设备适配难度持续加大，传统一多开发方式在应对多端适配时存在如下痛点：

* 需要为不同断点场景提供响应式布局，适配复杂度高。
* 适配场景多，涉及安全区避让、尺寸换算、布局约束等，逐项处理工作量大。

本文以一款简单新闻阅读应用为例，介绍如何用DevEco Code + AI Skill辅助一多开发：基于现有直板机代码，AI自动完成多设备适配，降低开发成本、提高开发效率。

## 使用AI Skill辅助多设备适配开发

### 多设备适配AI Skill定义

HarmonyOS多设备适配Skill集是由1个总入口、6个专属场景Skill和1个验证流程文档组成的分层Skill集合，旨在面向多设备适配场景提供AI辅助开发能力。总入口负责意图识别、阶段判定和场景路由，6个专有场景Skill分别覆盖屏幕窗口尺寸、折叠状态、系统避让区、交互方式、自然方向、硬件能力6个适配维度，开发者只需要用自然语言描述适配需求即可自动路由到对应场景并输出工程化方案。

| Skill | 名称 | 定位 | 使用设备 |
| --- | --- | --- | --- |
| 多设备适配总场景入口 | [hmos-multidevice-scenario-entry](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-scenario-entry) | 意图识别和场景路由的总入口 | phone/tablet/tv/2in1/wearable |
| 屏幕窗口尺寸适配 | [hmos-multidevice-screen-window-size](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-screen-window-size) | 响应式布局、自适应布局、窗口变化监听 | phone/tablet/tv/2in1/wearable |
| 设备折叠状态适配 | [hmos-multidevice-fold-state](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-fold-state) | 开合连续、折痕避让、悬停适配 | phone/tablet/tv/2in1/wearable |
| 设备避让区适配 | [hmos-multidevice-avoid-areas](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-avoid-areas) | 系统栏/挖孔区/软键盘避让、沉浸式适配 | phone/tablet/tv/2in1/wearable |
| 交互方式适配 | [hmos-multidevice-interaction-methods](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-interaction-methods) | 触摸/鼠标/键盘/手写笔交互归一 | phone/tablet/tv/2in1 |
| 设备自然方向适配 | [hmos-multidevice-natural-orientation](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-natural-orientation) | 窗口/屏幕方向与自然方向判定 | phone/tablet/tv/2in1/wearable |
| 硬件调用适配 | [hmos-multidevice-hardware-access](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/tree/main/06-solutions/multi-device/hmos-multidevice-hardware-access) | 硬件能力检测与相机适配 | phone/tablet/tv/2in1/wearable |

### 使用说明

使用多设备适配Skill时，开发者无需记忆每个Skill名称或手动选择场景，只需用自然语言描述当前的多设备适配需求（例如：“双折叠展开后出现大图大字体现象”或“平板上字体只展示一列”），入口Skill会自动识别意图、判定所属阶段并路由到对应的专有场景Skill。

| 标签 | 阶段 | 总入口关注点 |
| --- | --- | --- |
| REQ | 需求分析 | 问题边界、设备范围、主适配维度 |
| DEV | 开发 | 主代码落点在哪个场景，是否需要多个场景联合 |
| FIX | 问题修复 | 根因属于哪个适配域，是否存在连带回归域 |
| VAL | 功能验证 | 验证矩阵应覆盖哪个场景，是否需要交叉验证 |

命中场景后，Skill会读取内置的参考文档和决策树，按统一字段规范输出结构化方案，包括设备约束、代码修改点、实现注意事项、修复计划和测试用例等，涉及多个适配场景时，Skill会同时命中主场景和次场景并输出方案。进入验证阶段涉及折叠设备多形态验证时，所有Skill统一路由到[多设备验证指南](https://gitcode.com/HarmonyOS_Skills/harmonyos-agent-skills/blob/main/06-solutions/multi-device/hmos-multidevice-scenario-entry/references/multi-device-verification.md)执行标准流程。

### 差异对比

以下为本文案例——《简单新闻阅读应用》，在使用多设备AI Skill前后的对比：

| 状态 | 直板机效果图 | 双折叠展开态效果图 | 平板效果图 |
| --- | --- | --- | --- |
| 使用AI Skill适配前 |  |  |  |
| 使用AI Skill适配后 |  |  |  |

## AI适配多设备开发步骤

本章以《简单新闻阅读应用》为实例，基于AI Skill完成从直板机到多设备形态的适配工作。该应用当前页面整体基于Tabs、List、WaterFlow组件构建，存在三处典型的一多适配缺口：未处理沉浸式布局与安全区避让、未针对不同设备的窗口尺寸做响应式适配、未声明多设备下的窗口显示方向。

### 开发步骤

1、使用DevEco Code作为AI工具，启动DevEco Code并选择[Agent模式](../doccenter-deveco-studio/ide-deveco-code-agent.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/zsg0tCiWTXqff9NDd7HS2w/zh-cn_image_0000002789073558.png?HW-CC-KV=V1&HW-CC-Date=20261114T005410Z&HW-CC-Expire=31536000000&HW-CC-Sign=3EA2CD71E080D211E2BACA3E249787083CDC554D438BB7782B0D3340FDA73584)

对于刚接触多设备适配的开发者，建议选择Build模式，通过自然语言描述需求，由入口Skill自动路由到对应的场景Skill进行处理，快速完成适配。

对于有一定多设备开发经验的开发者，建议选择Plan + Build模式，可根据实际需求直接调用对应的场景Skill，对部分布局或功能进行针对性适配。

2、配置多设备相关Skill，详情可参考[配置Skill](../doccenter-deveco-studio/ide-deveco-code-common-configure.md#section13208205414819)。

将多设备相关Skill下载并存放在DevEco Code能扫描到的位置，包括：

* 项目配置：.deveco/skills/<skill-name>/SKILL.md
* 用户配置：C:/Users/用户名/.config/deveco/skills/<skill-name>/SKILL.md
* 项目Agent兼容：.agents/skills/<skill-name>/SKILL.md
* 用户Agent兼容：C:/Users/用户名/.agents/skills/<skill-name>/SKILL.md

具体放置流程可参考[创建自定义Skill](../doccenter-deveco-studio/ide-deveco-code-common-configure.md#section4684243316)，通过在DevEco Code对话框输入\*\*/skills\*\*可查看所有Skill，下图为多设备Skill配置成功的效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/cjmUmQyMSLS5JoS9HhbMVA/zh-cn_image_0000002818072971.png?HW-CC-KV=V1&HW-CC-Date=20261114T005410Z&HW-CC-Expire=31536000000&HW-CC-Sign=B38395450378F4D2595239620EA42D4821F2FC41D3C9B4AC4C4993609CD101C2)

3、在DevEco Code中用自然语言描述多设备适配需求。

以Build模式进行快速适配为例，该工程需要适配的主要问题如下：

* 该工程当前仅支持手机，需要在平板上也可以运行。
* 直板机的底部Tabs，在平板、三折叠三屏态等大屏下应该以侧边栏的形式展示。
* 首页新闻瀑布流，直板机一列，双折展开态两列，平板、三折叠三屏态等大屏下应该三列。
* 所有设备应当实现窗口沉浸，并合理避让顶部状态栏和底部导航条。
* 所有设备应当选择合理的窗口旋转策略。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/LdyxwZ44Tku2eQUEDpOlIQ/zh-cn_image_0000002788913630.png?HW-CC-KV=V1&HW-CC-Date=20261114T005410Z&HW-CC-Expire=31536000000&HW-CC-Sign=0877015567D333098EB0A7884D92C553AEDBD69E6B51A63486F682F54518B4BB)

4、由AI自动完成多端适配代码的编写与修改。

入口Skill自动分析需求，判定适配阶段，路由到对应的场景Skill，由场景Skill结合源码完成适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/KHg8pgb8QsS3AgNp44Asmw/zh-cn_image_0000002817953045.png?HW-CC-KV=V1&HW-CC-Date=20261114T005410Z&HW-CC-Expire=31536000000&HW-CC-Sign=6A3C634996D7B4879071740F9654A02F56B55A19C6C92050AA16E98916479033)

5、由AI自动执行多端适配测试并预返工。

多端批量检测布局适配问题、编译问题、开合问题等，提前修复。涉及折叠屏开合的内容，会连接至多设备验证指南，对折叠态、展开态、三屏态、悬停态进行额外的布局适配验证。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/WyNV_pYYSU6jLYDFmV1i5Q/zh-cn_image_0000002789073560.png?HW-CC-KV=V1&HW-CC-Date=20261114T005410Z&HW-CC-Expire=31536000000&HW-CC-Sign=81B3A6F30FE012C25434345AAF8577AABE7A5E59FBBD3643CC585C840C17E851)

## 示例代码

[基于ArkUI实现简易新闻阅读应用](https://gitcode.com/HarmonyOS_Samples/NewsReader)
