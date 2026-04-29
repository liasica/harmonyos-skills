---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ceb59eface3a6ac841936ac8750f2d000f58763c54d639b952203073fb3b7ee
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 登录<https://developer.huawei.com/consumer/cn/> ，通过“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，点击“立即体验”进入意图注册入口，需使用与应用上架相同的账号登录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/3cg38ONNSlCTSFEsEr22xA/zh-cn_image_0000002589245631.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=C2D6C803A7E1CB0D3CE12E3880A60F1929CFE5D1BDDAAB7B52D83F56EF17BFF6)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/ORIVMrWzQJyYres_HAkTAA/zh-cn_image_0000002558765822.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=E1FB5A1F437FD83CE3821500CD74C10967D7A15B57298C6D517E0B2557BC6271)
2. 点击注册意图新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/W-NZgzr3RVWQ77tWzLopWw/zh-cn_image_0000002558606176.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=CDC4C62F7C3D0D5514054AA06CE10AEFC34F39746C9BD92A97EFEE752656C2AC)

   1. 点击新增注册意图，填写注册信息进行创建。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/e6RFFajtTc-dbRWchnRVRw/zh-cn_image_0000002589325703.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=03504D1168694FC53676A3A9973C00CC0CA8D563542C0BB7CC09968DC56BE581)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/eaD5Mu0tR3uFA7ExR9iGzg/zh-cn_image_0000002589245643.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=E19AC193E9FEF87B923107C7BC1476FE6CBEFD2626707B7A4BD09C9599FDB4C8)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/M61-01m0QuuzhGgqYlsrIw/zh-cn_image_0000002558765834.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=7B5A025F60E678807D6F2FE51B66FF1EC0B6A876329D15E20C682C1C953ABE74)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入）并确定。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/xgxiZrbMTz2PVSqcG-A7pg/zh-cn_image_0000002558606178.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=48986BD4CCAF0DFD03F2B7B1E9FB14D32F6B541FB017690791666C70EC445F9D)
   3. 展开已创建的意图，并填入自定义输入、输出参数，点击保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/lumvswMsRPOPL91wBlQIvw/zh-cn_image_0000002589325705.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=FE90751D4695FFFFCB2946092B94F0D01C1F7CDCA52A04C999A35EC5CFDFD8BD)
4. 添加意图使用样本（意图样本用于提升模型对意图识别的准确率）。

   1. 意图使用样本可通过新增/批量导入进行上传。
   2. 若无需添加意图使用样本，打开是否已提供线下样本开关即可。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/vwBu7CW5Qc6Lm1ZvJtdluA/zh-cn_image_0000002589245645.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=68B756ECA9B0065CF4716CFA8D73E6E982291E9A983F25679D4360DD357438F4)
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击编辑用户组。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/H1YH8P37R3yJeReUyDJ_4w/zh-cn_image_0000002558765836.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=A52203E3A2942624AFAE1CA7A83C508242E7C1721D38DED79C8A550EDA9EA6D2)
   2. 点击新增组，输入新用户组名称（名称自定义）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/IPc8kNdqRJageDVRXktoBg/zh-cn_image_0000002558606180.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=7E4441ADFF12EC7237FDC8F0D9AC47BB7C0F5CD44C8D68BBCE19A01419B12362)
   3. 选择已新增用户组，点击查看进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kr5z7fMvQHOc0KPeKBnl5g/zh-cn_image_0000002589325707.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=8AB1C1DE814E67FBC775D5BD8D34D556999649C78911D3DE0D8CA1A91449A890)
   4. 点击添加用户，选择账号类型为邮箱/手机号码，填入后点击确定（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/_vU363F0TG6rXCO8nAqCzQ/zh-cn_image_0000002589245647.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=78C251FD6567C72FEFE91802B211DE0D49C1838C5798E13C3077B0D14E09C45E)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/1QfZwJqXRomMepsVWszJlQ/zh-cn_image_0000002558765838.png?HW-CC-KV=V1&HW-CC-Date=20260429T054336Z&HW-CC-Expire=86400&HW-CC-Sign=B903B80D6C8FF945959E0C48A8F70AEF08E75851FEBC9B924F1CBF7B1A195998)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，通过小艺进行自验证。

   1. 开发者预期：用户可通过小艺打开应用内页面并传递参数。
   2. 开发者验证：正常跳转目标落地页并收到对应参数。
