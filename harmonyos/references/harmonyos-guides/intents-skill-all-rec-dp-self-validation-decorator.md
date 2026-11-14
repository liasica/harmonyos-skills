---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:40+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:2f4cf4f754ac0925c6ef9088f64655696ef23cc6f2f0a290734524fa2dcd4365
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/AkSX-1cUR4yaXqO2qvKnsQ/zh-cn_image_0000002817507913.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=51D7349475AA0B18497CBA0F52C4E5EBACE7A77242CC2E813916F9F1DB2698B1)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Rm2PGSzkQ7a7aEBBl_SosA/zh-cn_image_0000002788308482.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=33ED1A2861DBF2A731643BA19AC68E8622EA8291BFE0E5354F3B597D3FB1FD9A)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/xbOGLrELSjapDV7sr_3ovw/zh-cn_image_0000002817427845.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=D604350E044296C5C964B38BB4B7F9C9395495431C651F93CF34CE5A28411829)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/v190w5f7SJShUBNavRz0Jw/zh-cn_image_0000002788468426.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=70E02ECB9165EDCA0256380DD558C9B21C7378C923AE88D256C21DBE121043E7)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/J92hDBjiQpurNIXjZ2EKQg/zh-cn_image_0000002817507915.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FC85CB31209AA86D58FBFE3F304B54EFF54A382BDF8A14D6C805AA4BBDDA768)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/kcBwC6AySdGm7UtZ0ClynQ/zh-cn_image_0000002788308484.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B47EAE8B3016E89A73365C609564FE4D560DBAB6EBA52196451EE40D1D34538)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册名称 | 填写应用名称。 |
      | APP名称 | 填写应用名称。 |
      | 关联APP | 选择需要进行测试的应用。 |
      | 支持的设备类型 | 选择手机、平板、PC。 |
      | 版本号 | 开发者自定义，仅支持正整数。 |
      | 版本描述 | 开发者自定义，该内容不对外展示。 |
      | 图标 | 尺寸：72px\*72px（1:1）  格式：png、jpg、jpeg  样式要求：方角、不透明背景 |
3. 添加意图。

   1. 切换至意图页签，点击“添加”，进行添加意图。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/cTHCJnopSsen-hc2rdTE7w/zh-cn_image_0000002817427847.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=03106BD8EA26538F0ADB6CCC78FE72F85BD97A600675A68BC7F7B72779760510)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/RiGxJrezR7eSnQ5aYq3tfw/zh-cn_image_0000002788468428.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C9CB7E3F74D5D8A90A9ADB7FFF3A867B84CCABAA33707C989D1B6BBB1E10B80)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/WFCOBUDPTd2bzDWHMFJycQ/zh-cn_image_0000002817507917.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=F942C60CEA771A8C59FBA49B3360E2CF87836F2404415681AE294F947C615E77)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/prdN3lWiQk-tWcl-sDD3cg/zh-cn_image_0000002788308486.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C7777456F2A9B8E635A55A973C34D72A9741F56DAED3E5F8BEB8A32AD5249BA)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/PxeBuF5-QQWi98bo8eTMZA/zh-cn_image_0000002817427849.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=DEF5A34E068E47354AED99DA9AFB1DDDA18DDF78EE4E6D1D8C892226FC21D59B)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/QPCAcQAEQw6JAIKuVJvXsg/zh-cn_image_0000002788468430.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=0663E6E1EFB3BFC6DB6CD2A74EB465154B174E7B030BF913112F014397BDF26E)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/PxzRLoclTpG4tMl28IZT3g/zh-cn_image_0000002817507919.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC9AEAAE418F8AEA4BED47D6EF71AB8996136598222962BCAE3F9C984E5F2C4F)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/K2WAYtW0QumivR1_Sgoumw/zh-cn_image_0000002788308488.png?HW-CC-KV=V1&HW-CC-Date=20261114T004840Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C864DD06AF37C116533AEA87A3637D39E486AF214B3109027D16B28EAB744E4)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
