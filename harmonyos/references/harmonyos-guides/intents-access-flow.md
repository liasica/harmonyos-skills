---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-access-flow
title: Intents Kit接入流程
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > Intents Kit接入流程
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:08e3b5dbaf03f6c5f82b28490ef42ce93f22fdb090fb6b162bc8eef029a6561f
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/wSdbL7pGSlOaL2zAVHrEKA/zh-cn_image_0000002815400229.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B6E56D8B2C34AED0BF6446B4C5D988971509A062C6294CE327ED6B02CDACC35)

**阶段一：意向**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 选择特性确定意图 | 开发者根据想达成的用户体验，确定好涉及的系统入口和特性类型，基于已发布的特性列表选择需实现的意图。如果已发布的特性列表中没能找到合适的意图，则只需要确定好系统入口和特性类型即可。 | 开发者想实现“歌曲续听推荐”的特性，根据智慧分发特性的场景描述，该特性属于小艺建议系统入口下的习惯推荐特性类型，需要实现“播放歌曲”意图。 | [歌曲续听推荐](../service/intents-ai-distribution-characteristic-0000001901922213.md) |
| 能力申请 | 确定好特性后，开发者在AppGallery Connect平台上提交对应特性类型的能力申请。 | 见下文图示。 | / |

**能力申请步骤**

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”，在项目列表选择项目。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/xfFvqqCGQCWpEhEamAcc9Q/zh-cn_image_0000002786520654.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB7B0CF16A193A965E88CE90CDD0D47BF492AA596252A57DCFAFEB11E0C7C1A0)
2. 选择项目后，选择需要申请开通能力的应用。
3. 进入“项目设置 > 开放能力管理”页面，点击“意图框架”对应能力的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/rQQ9n2HYTym1Nl-gJFeO8g/zh-cn_image_0000002786360726.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C37846F19B37A98B3352E005395B15AE093F3B82ACAD7609454C3AD600867E6F)
4. 参考“申请原因”中的模版，提供必要的申请信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/tU5SBx-MRJW3zRe_9FkLJA/zh-cn_image_0000002815560147.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=03901CA03635EC60D00FA51245C26168ADE691254184492704057553A1EC132D)
5. 返回“开放能力管理”页面，原“申请”变为“申请中”，1~3个工作日内反馈申请结果。申请结果请留意互动中心的“服务开通申请”信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/YDUVVR3RR_6TR7Wgwe7kng/zh-cn_image_0000002815400231.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A2602D0B757B10B40BB190F09214272E2F004848FF50A48489D55DC1EC00765)

**阶段二：开发**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 意图调试申请 | 申请能力通过后，开发者可根据审核成功的反馈提示，提供测试应用的信息，用于开通意图调试权限。 | 1. 应用名称：华为音乐。  2. 应用包名：com.xxxx。  3. 接入意图名称：“播放歌曲”。  4. 应用图标：jpg、png……。  5. APP ID：1234567。  6. Client ID：1234567。  7. 华为账号（UID）：1234567、7654321……。 | 见各特性类型  习惯推荐：[开发者测试](intents-habit-rec-dp-self-validation.md)  事件推荐：[开发者测试](intents-event-rec-dp-self-validation.md)  技能调用：[开发者测试](intents-skill-all-rec-dp-self-validation-con.md) |
| 意图声明文件中注册意图 | 在DevEco Studio中开发时，注册对应的意图。 | 注册“播放歌曲”意图。 | [意图注册](intents-habit-rec-access-programme.md#意图注册) |
| 开发实现意图共享 | 开发应用/元服务的意图共享接口，使其可以通过HarmonyOS接口完成意图数据共享。 | 开发“播放歌曲”意图中的意图共享接口。 | [端侧意图共享](intents-habit-rec-access-programme.md#端侧意图共享) |
| 开发实现意图调用 | 开发应用/元服务的意图调用接口，使其可以通过HarmonyOS接口被正确调用。 | 开发“播放歌曲”意图中的意图调用接口。 | [端侧意图调用](intents-habit-rec-access-programme.md#端侧意图调用) |

**阶段三：验证**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 端到端验证特性 | 使用华为侧提供的测试能力完成目标特性的端到端联调测试，联调测试完成后，提交智慧分发配置至审核。 | 在设备上对应入口进行“华为音乐-歌曲续听推荐”的特性端到端测试，测试完成后点击提交智慧分发配置。 | / |

**阶段四：上架**

| **任务** | **任务描述** | **示例** | **指导文档** |
| --- | --- | --- | --- |
| 应用市场上架软件包（应用/元服务） | 开发完成并打包好软件包后，在应用市场上传软件包。 | 打包“华为音乐”软件包并通过应用市场上架。 | [应用市场上架流程](../app/agc-help-release-0000002235870050.md) |
| 意图框架注册 | 在小艺开放平台进行意图注册配置并提交审核。由华为工程师审核，一般审核周期为3-5个工作日，审核通过后状态变为"已上架"。 | 注册“播放歌曲”意图。 | [意图标准协议上架指导](intents-kit-listing-standard-protocol.md) |
