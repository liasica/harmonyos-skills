---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed419670e1c9dfb2743e51b022e579c21d040c8d50746b1d3cae4e60de21a8bd
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 登录<https://developer.huawei.com/consumer/cn/> ，通过“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，点击“立即体验”进入意图注册入口，需使用与应用上架相同的账号登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/13zOi4uQRuygz5yeL0D6Pw/zh-cn_image_0000002552959320.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=9626DCB2822F91B856490A4A7ADDC08654D96D58246757A90F163CCC82FAB83F)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/C4_vEK9eRkiQoyB5Y7wmeA/zh-cn_image_0000002583479321.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=59D38782E14923201E99C061764133F510DD5A760D6EB1EB583CCC001D6D5226)
2. 点击注册意图新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Pp4A0cYeQUy-PBBoTgCvGA/zh-cn_image_0000002552799682.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=D798556E71C79EC5BA16DB0A3CB64DC57EA71CDD56C502882BCF13D5EBD0BCB9)

   1. 点击新增注册意图，填写注册信息进行创建。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/EFuVQGvlT--AmG820X5k-Q/zh-cn_image_0000002583439377.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=5C8D2A650529CFA27E62CEFE24379C523516C61AB5AA723867BB768C8E214E38)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Gg9aAj0MS0iXdcI-2zzDkA/zh-cn_image_0000002552959332.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=B251D6563E4C55F93E6152CBAB80583857929D5E75770575F308DE743B7F914D)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册名称 | 填写应用名称。 |
      | APP名称 | 填写应用名称。 |
      | 关联APP | 选择需要进行测试的应用。 |
      | 支持的设备类型 | 选择手机、平板、PC。 |
      | 版本号 | 开发者自定义，仅支持正整数。 |
      | 版本描述 | 开发者自定义，该内容不对外展示。 |
      | 图标 | 尺寸：72\*72（1:1）  格式：png、jpg、jpeg  样式要求：方角、不透明背景 |
3. 添加意图。

   1. 切换至意图页签并添加意图。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/GUzJ_u8hSvu2dw4OW4dOuA/zh-cn_image_0000002583479333.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=6057E61D45C35A8A91B4D228E97052D336505BC6F76E8C39C888E1253C3049FA)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入）并确定。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/mcwgbXrHRFyxXtUutNX3fQ/zh-cn_image_0000002552799684.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=7B232B425C315F24EE686622E4E744E26B3C26E1F92F0673E71583E77835AF76)
   3. 展开已创建的意图，并填入自定义输入、输出参数，点击保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/-5tkdKP7TEKEv1DQGEii2A/zh-cn_image_0000002583439379.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=93059503D6BA25A847327200E85E9A8F2CF71D9C6D7F9F3DD38C6230EBFF79E7)
4. 添加意图使用样本（意图样本用于提升模型对意图识别的准确率）。

   1. 意图使用样本可通过新增/批量导入进行上传。
   2. 若无需添加意图使用样本，打开是否已提供线下样本开关即可。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/DANJ7qgkQCuTLlgHhQ_VRg/zh-cn_image_0000002552959334.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=071ED9ED46A6F17F1061D161279FF4BE04F0E92C5303107DE3DFF9CF512CAF26)
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击编辑用户组。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/yC1Li1tBRZ-95q55dhvn1A/zh-cn_image_0000002583479335.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=70A8456E03BBCAEF5F3F0BF34BEDF17E9C21B4525B965401F92010AF44852416)
   2. 点击新增组，输入新用户组名称（名称自定义）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/UAbv7jtaShmHW5NSiobAXw/zh-cn_image_0000002552799686.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=6FA583D6DAF2A7BB6CD75A94D0AEB950720A4F63142F9338B38F2CDFD6448560)
   3. 选择已新增用户组，点击查看进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/t5UtvZxDReGkj9FLvNDPaw/zh-cn_image_0000002583439381.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=FC2F6B4EDC55CABA3A68BCFC05365E34488E20068A033B6322F295868E825F7D)
   4. 点击添加用户，选择账号类型为邮箱/手机号码，填入后点击确定（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/VnYH8hXdRZiYOshN6Rpq-A/zh-cn_image_0000002552959336.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=819383095F773729BBEF0B4167993FA7BAFB4541BB2E9CA2A9C1BB149B86ABE7)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/WLiC-O9mTDqoLD0pmfl9Rg/zh-cn_image_0000002583479337.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=AD11E23E57DE5993AEAB0BA9072D1FA70F72216BE6854C8C455686A8AF1497CA)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，通过小艺进行自验证。

   1. 开发者预期：用户可通过小艺打开应用内页面并传递参数。
   2. 开发者验证：正常跳转目标落地页并收到对应参数。
