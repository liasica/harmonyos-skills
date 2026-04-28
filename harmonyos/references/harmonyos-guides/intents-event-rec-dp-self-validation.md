---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-dp-self-validation
title: 开发者测试
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 开发者测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f9c6a3cc4a2d82d8a728312ee1feeb54914535fbb3df0b75023e68f5cad5e805
---

Intents Kit向开发者提供真机测试能力，即开发者可连接设备进行调测。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS NEXT设备上面进行自验证，打磨体验。真机测试分为三个步骤：基础信息提供，环境准备，联调验证。

## 基础信息提供

达成开发意向后，开发者发送邮件到邮箱（hagservice@huawei.com）或者联系华为意图框架接口同事，向华为提供测试应用的信息。

| **序号** | **基础信息** | **描述** |
| --- | --- | --- |
| 1 | 应用名称 | 应用市场上架的应用名称。 |
| 2 | 应用包名 | 应用市场上架的应用包名。 |
| 3 | 接入意图名称 | 开发者意向接入的意图名称（中英文）。 |
| 4 | 应用图标 | 应用的图标，具体要求如下：  图标背景：非透明。  比例&尺寸：1:1，72px\*72px。  大小：不超过1M。  格式：png、jpg、jpeg。 |
| 5 | APP ID | 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，在“开发与服务 > 我的项目 > 项目设置 > 常规 > 应用-APP ID”中获取。 |
| 6 | Client ID | 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，在“开发与服务 > 我的项目 > 项目设置 > 常规 > 应用 > OAuth 2.0客户端ID(凭据) > Client ID”中获取。 |
| 7 | 华为账号（UID） | 参考[附录A获取UID](intents-appendix-a-get-uid.md)。 |

## 环境准备

准备一台装有HarmonyOS Next版本的手机设备，系统版本最低要求为 Developer Beta 3，并按照以下顺序依次执行，不能更换执行顺序。

1. 保持设备联网，并且设备时间和实际北京时间保持一致。
2. 点击桌面的小艺建议卡片。此时卡片显示的是“欢迎使用小艺建议”，点击卡片打开小艺的隐私页面，并选择“同意”。如果此前已经同意过小艺的隐私协议，此步骤可以跳过。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/-o6duRRhSVGOJg6cx59EKw/zh-cn_image_0000002552959312.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=59E4786E3E3586CCD61DB5104B710C79360E35A9293843D3CC199B1A367275F1)
3. 打开开发者调试模式：进入设置 > 机型 > 关于手机，连续点击软件版本7次，弹出“开启“开发者模式””，点击“确认开启”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/fWBuJptGT9-b7EB_4hkt4Q/zh-cn_image_0000002583479313.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=CC643511F1CEF5417D86EAC078E8078651ACF1372C6E6CEA2C6A591A902DFABD)
4. 长按电源键唤醒小艺，将半屏态小艺向上拉升至全屏态，点击左上角返回上层，返回后点击右上角的头像，进入“设置”，找到并进入应用网络设置，打开“WLAN下自动更新”开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/gw0T1HN-TWiIcKqYTXnUDw/zh-cn_image_0000002552799664.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=ED6EE52119C8380ECAF29CE45249EF7276245EFEBDFF17EB25EF1EE3897E3FF9)
5. 在上一步页面中下滑，点击“个性化推荐”，进入后打开“个性化推荐”的开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Ma-nZz4rSQeLQGH4taxaYg/zh-cn_image_0000002583439359.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=FC6106F748362EE901A1BCA0DF8C320FD42B158C822425186A73A38A5E1DF263)
6. 进入设置 > 系统 > 开发者选项 > 意图框架调试，打开意图框架调试开关，如果下方显示已切换至真机模式并且测试应用包名在“本设备支持测试应用”下，则代表真机模式切换成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZFHOQdVERR201HIPxOY1VA/zh-cn_image_0000002552959314.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=06549665EBD79C9CEBBCAFEBF0B5B685729AE4E26BA939F81374AE7CFC39B91F)

   【提示】如果出现意图框架调试打开后，设备长时间无法出现“已切换至真机模式”或者出现“已切换至真机模式”但没有包名的时候，可以尝试以下操作：

   1. 登出华为账号，再登录之后重新开启意图框架调试开关。
   2. 在小艺对话中点击右上角头像，设置 > 服务管理 > 注销服务 > 注销服务，然后返回桌面重新点击小艺建议的卡片，将展示“欢迎使用小艺建议”的卡片刷新成有服务推荐的卡片，最后重新开启意图框架调试开关。
7. 完成以上所有步骤，即可进行联调。

## 联调验证

1. 事件共享：开发者登录应用即可[获取云侧事件捐赠的SID](intents-event-rec-access-programme.md#获取sid)，然后触发事件推送，将事件内容同步到华为云，具体操作可参考[开发者指南-事件推荐方案章节](intents-event-rec-access-programme.md)。

   【举例】某出行类APP接入意图框架航班提醒的特性。用户通过APP购买了机票，触发开发者云调用华为事件通知接口（https://insightintent-simenv.cloud.huawei.com/open-ability/v2/service-events/notify），将用户航班事件推送至华为云，接口响应成功。
2. 卡片渲染：点击桌面上的小艺建议卡片中任意服务，然后返回桌面，会触发小艺建议卡片强制上云刷新。出卡条件是以事件的生效时间进行偏移，具体出卡条件和卡片的样式可以参考具体特性的场景说明文档（确定开发意向后由华为侧提供）。

   【举例】航班提醒是提前24小时提醒用户，如果用户航班起飞时间是8月15日20:00，则8月14号20:00起可查询到该事航班信息，在此之前无法查询到信息。
3. 意图调用：点击小艺建议卡片中的模板卡片，在测试应用冷启动或热启动的场景下都能够跳转至测试应用的目标页面，则说明意图调用的过程是正确的。

   【举例】点击小艺建议卡片中的模板卡片，会跳转至该用户的购票详情页面。
