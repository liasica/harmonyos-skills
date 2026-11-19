---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:32bf1d762d9bc943effda04542c9f1e6a9273881f1aecd372097ff9f32e5ff02
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/OU5Mi3PDQfqm8J5R7wkryQ/zh-cn_image_0000002820526763.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=99EB745C1503B6EDC53EE459716775E9D2D8E1E904199ADDD6E908E5A356C21A)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/vSMcyqCPR5id9ifVm2YpJA/zh-cn_image_0000002820406763.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=48E4E7281C2E4278942FFB69990762A2EDD9E8DCBD078684EAB515FCA43D951C)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/hO0O9HxHQlK8xW0qbpXxiw/zh-cn_image_0000002791726784.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED26BE074023BD2F38D0FB339C44DB94E8795E1F773EA7B905236FF7B1E5B2BE)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/hXjYPGrESyeMxA-5JIYDNg/zh-cn_image_0000002791566812.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=D436DEA7F93F832EFB6DDEE14615820E0E109DBEE38417BDAF7DCA5628AEDDBB)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/1HEPLd2iSc65nGQQKDiPlw/zh-cn_image_0000002820526765.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A9D7FD273A3F452573DD989DCC49AFC175534C31F2D16D06F76B1C0B80047A7)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/VEfIi-3rTG21b3bNa0HSUA/zh-cn_image_0000002820406765.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CDB53A305DB37DFCC9DD47908534BDF00C3C1504A990FFAC8C845AEC99350D8)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/7KLVqkKJToK9NERw4JvK8w/zh-cn_image_0000002791726786.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FA978A35679D21F4530CC21B8D1FA7FD9A0F65BE1ADF429A61571C50293BF6C)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/9taZ7z0kQoq9Lt01x3v4Gg/zh-cn_image_0000002791566814.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=10C16CB5AEB32D2C462E7AE8AECA675C48FB475E87789FD14DEE499D83448C42)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/VaYl26heRp2Ji6AwvIaBtQ/zh-cn_image_0000002820526767.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF69CF78867FAC54F84633AD1103BA02C5FAF15D5153E12B999FF89416748842)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Xo0nTGFwS7m4JeCgKLtC-w/zh-cn_image_0000002820406767.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=1186E0ACCA4408E62AC74981EB328A70FD5BE312D80E4B660A79D2915182CD53)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/lgprMT_gTjyjfNAbQuhPsg/zh-cn_image_0000002791726788.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=B0C7FE7559AA2893A6EF1A03BDBE37C5AFB3CA6C941200134D362F689C9D08AF)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/id5sQi-kQ56-IPVRavNABg/zh-cn_image_0000002791566816.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=E069692E6436412EEC195D5B346BB7F4F743813812DC9689ABB3AD9B968BDAB7)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/3IChqh46S16Ucy-m7vCSoA/zh-cn_image_0000002820526769.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=55774930BCAF880EF8EE54F0E0EDFABEA49E83A6AE6790C3F4766CBA208360CA)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/1aiC1BNsSyC5ypqvRHtqvg/zh-cn_image_0000002820406769.png?HW-CC-KV=V1&HW-CC-Date=20261119T014921Z&HW-CC-Expire=31536000000&HW-CC-Sign=BD3B02A5AB344DFA592F03FEE75FC2F9B2A46B3A46EC76DB8DD07029785A949F)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
