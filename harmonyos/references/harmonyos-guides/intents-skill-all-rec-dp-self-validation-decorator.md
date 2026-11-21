---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:47+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:10cfcdb5db96a49bc230c08f4f809b6cc931a9e5c47678ada68bef2eb35d84dc
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/9hWCwf0bT3KV6j58yvY9jg/zh-cn_image_0000002821838371.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=F345FB6E3E817E7B0BBB2D073C165FBBCBE70D31F6A2F87BBFB61FE7BE52AE0B)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2OW38W_iR-O_3lc19NRTIg/zh-cn_image_0000002821758373.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=2784A37CF9C55A97BEBB522EB768DFE2A151195C32EB30F11578D63214804164)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/SPzPY5S3Rx6D8TBxjQW2sQ/zh-cn_image_0000002793038436.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC65F4311B5D5E6B27C7129BD496B32EC6496CCCEE237A3695467910C41AB024)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/qBnEFvTTRqSn3oNkXPOVgg/zh-cn_image_0000002792878466.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=46EC65A7EC02C9702FEEF24DBEEBAF7448B8F7FB79C9BC523751001176832DAD)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/31gTserzT8K2fXJy65r-Dg/zh-cn_image_0000002821838373.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=4DB33DEB757234004C3FA4B3D0041AFE17C89013498583709B619E7DDFE7A7B7)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/VrpreETyTbemOs74wOQprw/zh-cn_image_0000002821758375.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B2CF6389A7E85984E16688265A93EB480C40CEC136B782AA02B8143316F29A3)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/qINX0E-4Qwm4pPc6ePLcVA/zh-cn_image_0000002793038438.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=D661F4764412970014B39470EB31E348C756D5F4F4CA716F74BCC6FE901CB80A)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/RkVFc3teSPSkIMPO33jqyA/zh-cn_image_0000002792878468.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC003CCBC1A8D8AB3C48FA4F6FBCB76AA3182CA0DA7EE7C367E5FD1CDD002E2D)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/EThKSUw8RiO_NbpNbpPYjg/zh-cn_image_0000002821838375.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=75CE3DBC4AB5D387D094EF602DF29A070D3201619DAC689A5123046F90FDFD79)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/59GRLtgzRm2oc8THA161Yg/zh-cn_image_0000002821758377.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=78AF24A7659366AAAE785B4C69E46F3496A6599E4BEDAABF1302183DB7E6EF98)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/LoH2DN-dQ5enktpNIFrXFg/zh-cn_image_0000002793038440.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FA92281A09BE1344E4B71EC44D03B8E7ED49FC5AC712D998C5AC2F1E194FB39)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/cxQ6NGAkTdWAJbiyt20Hkg/zh-cn_image_0000002792878470.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B17C72EC16C4000245803E4CF8F0CDC675E8CA46DCE20BF11704E3D3D095DF1)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/TJTqkF5HR5O9CW0D30wSCg/zh-cn_image_0000002821838377.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C263FB414143D47F1D3E9DC30A5FBE41BFD1D7F72AF3F9238FC3125D7304195)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/2AeLCXPMS82XcKsRLScEaQ/zh-cn_image_0000002821758379.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=47A09B6291C0017297FEBC5CCC3E65A9C2FA6906E5ADCB513FF1671B78627811)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
