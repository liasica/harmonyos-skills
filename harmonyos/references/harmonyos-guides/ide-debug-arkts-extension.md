---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension
title: extension调试
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > extension调试
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:bab5f19ec8b13ff2a8b18dbcbd49d42f994fbe56087a953f0f6efbc7edfe4d92
---

开发者可通过两种方式对[Extension Ability](extensionability-overview.md)生命周期函数进行调试。

* 应用安装到设备上后，通过等待调试方式进行调试。
* 修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

## 等待调试方式

1. 参考[等待调试](ide-debug-arkts-attach-to-process.md)对当前调试工程进行调试。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/q7zE9vDcSciEu3PH9ZL1Hg/zh-cn_image_0000002808887191.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E1B43A0B1F01DDC9E568DDDF8121E883DB320FF6404357DE27FF61A5DE0AE89)
2. 在Extension Ability生命周期内设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/tTh2mMJaQem1a9974PRrzQ/zh-cn_image_0000002808887189.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FD574A6E61E18B2532B4D5A392658A92592C7541FFCF8E97D9997AE425CBE73)
3. 等待Extension Ability生命周期函数代码调用从而命中断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/wWDBi_3yRlmbkEheV7iqLQ/zh-cn_image_0000002779407550.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3312EFED8DCCC61AD622243913AF13C72DCCECA43E6AF0C362D4E43C7DABF05)

## 修改运行配置方式

1. 在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/EUbYA8EJSeSub6YR9nn4VQ/zh-cn_image_0000002779407548.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F183BEA332B41B59FC4015E213C9F1F9B2C9D93EB2C7C71C5B437CA96186C9E)
2. 选择需要进行调试的Extension Ability。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/rBenQrkeQMeBaeDgqEIvgA/zh-cn_image_0000002808767105.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=7364AFAD9ED5BF0052ECB79B26E86E3800CDD7CD406E24537AE1D87BFB5313F3)
3. 点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/dj1aPr15TgW-nUhoqeHTbg/zh-cn_image_0000002779567526.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EEB084FC0339181741647C2CE126B8A7D0FB76A93B5E31B2580332F2C85205E)，启动调试即可命中 Extension Ability 中的生命周期函数断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/4iwI7FjrTlOHpHNKpDQTYw/zh-cn_image_0000002808767103.png?HW-CC-KV=V1&HW-CC-Date=20261124T044229Z&HW-CC-Expire=31536000000&HW-CC-Sign=00D19081D8F347DD4DAA20D879C463236CE7D36EF4EEAAAE43FDBCC14421829F)
