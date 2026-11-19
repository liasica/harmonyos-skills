---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/notification-banner-default-on
title: 申请通知横幅默开权益
breadcrumb: 指南 > 应用服务 > Notification Kit（用户通知服务） > 申请通知横幅默开权益
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d74c9e2c667f8e36b1a1664f005b1053e254a0da33c6866057776b74bf72a1d9
---

应用的横幅通知开关默认开启。

申请通知横幅默开权益存在以下限制:

1、应用限制：该权益仅对工具类、商务类、效率类、金融理财类、教育类、生活服务类、旅游类、医疗类、运动健康类应用开放。若您的应用不在上述类型中，则不符合申请条件。符合上述类型的应用，请在线上申请时一并在附件中提交应用分类截图。应用分类信息可登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html)网站，在“应用管理”页签中选择“应用上架”->“应用信息”查询。

2、场景限制：使用场景如下，申请后仅在以下场景中使用该能力，且申请时需提供相应功能截图/示意图：

(1) 用于展示用户需要紧急处理的IM消息。

(2) 用于及时展示用户设置的定时类提醒，包括倒计时、日历和闹钟。

(3) 用于展示用户需要立刻处理的订单类信息。

(4) 用于展示用户训练提醒或目标达成。

3、在“新建业务申请”窗口填写申请原因，上传横幅功能场景截图和应用分类信息截图，然后点击“提交”。应用分类信息可登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html)网站，在“应用管理”页签中选择“应用上架”->“应用信息”查询。

## 申请步骤

1. 登录[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/index.html)，选择“应用管理”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/1rIpeBJ3SNG8HyO7Ht_jaQ/zh-cn_image_0000002791726510.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AFA101675527E17FF35A6ED17D5105C8CBD283E972D5EED1FDDE54C2A346BA9)
2. 切换至正确的项目，在项目下的应用列表中选择需要申请通知横幅默开权益的应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/AAJOnzAsS8WHE7Fagosi1w/zh-cn_image_0000002791566538.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC33A22DAD3363B5312AE0C23AE08FB44EFCE26EA89BE1805CE6725287DE60AA)
3. 进入“开放能力管理”页面，点击“通知横幅默开”的“申请”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZhDBPGH7Qz-a1MQsh7880w/zh-cn_image_0000002820526491.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B067CDDA7C3F03B7CB41232215DCA081C5FF143471E81354AE6C30607312C1B)
4. 开发者可参考“申请原因”中的模板，提供申请必须的相关信息，包括应用介绍、使用场景、申请用途、附件、承诺信息，然后点击“提交”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/URKEPpgWTey3FZ90QvIMvA/zh-cn_image_0000002820406491.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACDFAA391A58166427CC189F97F47F2952E62DA96C1ECC30ACD1EB4DFE97034E)
5. 开发者可通过互动中心的“服务申请”消息获取通知横幅默开权益申请结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/aPtmreX_RJev8SVXhNyQWw/zh-cn_image_0000002791726512.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C03C15C2BAAA3498DF64AAF157A5BA00C8AF047FDE7F1BBCD8D3190AA5F7811)
6. 通知横幅默开权益申请通过后，须在“开发者管理”页签下左侧树形菜单的“ID、证书和Profile"->“Profile”菜单，点击“添加”重新生成Profile文件，并下载Profile文件到本地，然后在“[发布应用](ide-publish-app.md)”时，须将该Profile打包到应用包中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/OGF4FVT4T3i-NZPBrM7CGQ/zh-cn_image_0000002791566540.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=D34183788BA91BA1C5A89143CF383BF03E24532E31A7DFD271CA7580A52DA08B)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/pvQdSK71Se2X0mET_jLEJg/zh-cn_image_0000002820526493.png?HW-CC-KV=V1&HW-CC-Date=20261119T014812Z&HW-CC-Expire=31536000000&HW-CC-Sign=239F38A59A0B9165B0BF96B9F52CAECDDFA036B08D7F435A4A7B5FBA15149483)
