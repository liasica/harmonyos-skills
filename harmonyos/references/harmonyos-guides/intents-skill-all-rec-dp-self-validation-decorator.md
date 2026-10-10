---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-10-11T07:22:47+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:0d0ce7605df4223a802e16e14892eddab6824244666d7ec9660b35980c6abc80
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/3Xcm-n1NTaqtRmO_a5bXQQ/zh-cn_image_0000002784664139.png)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/W83dmIgHRCKTVbkDO-iiTA/zh-cn_image_0000002755025206.png)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/mkezizC0TsqZSlh749by-w/zh-cn_image_0000002755185092.png)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/i7sVvmtqTOybrnP8TomDWw/zh-cn_image_0000002784583959.png)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/p1eSHsvITT6_o5lEGnmKMQ/zh-cn_image_0000002784664141.png)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/v8KPYls-QvqphaE5a_cKRQ/zh-cn_image_0000002755025208.png)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/h0ax6KVRRhKLHhSmrhL0wQ/zh-cn_image_0000002755185094.png)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/NozUz7C2SzyDfoRFXAjbAg/zh-cn_image_0000002784583961.png)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/lRSKrvHhR_2-ZZpdx6TouA/zh-cn_image_0000002784664143.png)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/j0GAKxGnQNGlnsyeYCYDVA/zh-cn_image_0000002755025210.png)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/1ZJg-mRoQWOfTUrHSec1cw/zh-cn_image_0000002755185096.png)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/t_vOIg9kQ2yZlQUOKPQLrA/zh-cn_image_0000002784583963.png)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/VW3nyoBPTZqb6i8N5vpmew/zh-cn_image_0000002784664145.png)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/pK6QTfqASQa23-KkG1JSqg/zh-cn_image_0000002755025212.png)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
