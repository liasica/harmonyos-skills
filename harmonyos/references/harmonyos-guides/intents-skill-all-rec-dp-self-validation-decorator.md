---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:54+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8b150b085c80ae726004459d7a5f68cd92607740dd0e3f1075858cbbb822eb9c
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/kMJAv6JtSkKhK9_qaq8VIA/zh-cn_image_0000002717612252.png)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/3S3cnl2zTyiFDv4KG9OcuQ/zh-cn_image_0000002747292205.png)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ATiKUnY8R9CoqctAgCVNeQ/zh-cn_image_0000002747212121.png)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/Y_oR_lA1QGmYQDSEvLreog/zh-cn_image_0000002717772186.png)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/enJT8b0DRi6UX9JExmcPyA/zh-cn_image_0000002717612254.png)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/Q5wTQXaFS5CA4jZmh3ymvw/zh-cn_image_0000002747292207.png)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/Ox6Utlf8RDy1Cw9xHuuizg/zh-cn_image_0000002747212123.png)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/atnAhDBjSxCud8kOqppv6Q/zh-cn_image_0000002717772188.png)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/mDevk7W4QDit-cQ449AuuA/zh-cn_image_0000002717612256.png)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/dfCrYaAvRnCDxGjlPYmU7Q/zh-cn_image_0000002747292209.png)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/zyqFDiBQRWWTcWJKkrQD0w/zh-cn_image_0000002747212125.png)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/AhxLYKbITaK1uiD8ZWghCg/zh-cn_image_0000002717772190.png)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/aMCYuRexT5S4FcNPM-ulGw/zh-cn_image_0000002717612258.png)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/7XFfX4mVTVKRw-A3P0G5VA/zh-cn_image_0000002747292211.png)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
