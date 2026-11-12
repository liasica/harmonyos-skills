---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-dp-self-validation-decorator
title: 装饰器接入方式自测试方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 开发者测试 > 装饰器接入方式自测试方案
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:960e5c4cebce0ca9e313ab3fd7b623b4b2099cc8eb1f4bb3ae4444103c7fd0d2
---

从6.0.0(20)开始，Intents Kit向开发者提供意图调用调试能力。开发者完成代码开发之后，功能正式上架应用市场前，可以在HarmonyOS 5及以上的设备上面进行自验证，调试分为两个步骤：环境准备和联调验证。

## 环境准备

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/w65i8fcoRq2__v_yDYrFmQ/zh-cn_image_0000002786360748.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1120C8FE7F5E3CB0FAF23E07AAD7A5EF5ABB9BFEF669E99B261320FE1A873C0A)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/YAgrMAa4T9--YW8uUYYPYg/zh-cn_image_0000002815560169.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4897246B3EA8A9FA67EA56F749CEF40EE578F05C3D29817A94DC6CC87777C3EB)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/iUmg0AzfQparKN_QvBmJPQ/zh-cn_image_0000002815400253.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBA0072E19B7F9C5CF4D74DD407E6213B2B419A313D5468A007A26D5F772C2AE)
2. 点击“注册意图”，新增意图集。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/9Rdnn2teRBm1YHoURDHS8Q/zh-cn_image_0000002786520678.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=58650F8C1FC628FBAAF693BB53C387BE98173AB9CEECA551355A9CEB40188D5D)

   1. 填写意图注册信息，点击“创建”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/_CRxPbV3QHCT1X1gvVszdw/zh-cn_image_0000002786360750.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDC5A018D6C552924A9A85719D27C94F00D0472E92443EFBFD66354E38796487)

      | 名称 | 描述 |
      | --- | --- |
      | 意图注册协议类型 | 选择意图标准协议。 |
      | 意图集（插件）名称 | 需唯一标识。 |
      | 分类 | 开发者根据自定义意图选择对应垂域。 |
   2. 编辑意图集基本信息并保存。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/e-RcfJeSSJKsgJnevNSlcA/zh-cn_image_0000002815560171.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=34747E6432D63A79A76A0940B5061754506B480D1B7DC0923FF2AE9989F9338F)

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

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/H81W6Nd1QD6QyfMHu5Gi6A/zh-cn_image_0000002815400255.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=67882F6EDD1A3D1C8A46C7CABD34ED3A253AC951A631E1F3DBC2F16416EA3B82)
   2. 选择自定义意图并填入意图信息（根据接入方案进行填入），填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/QD2YT4XTSqqfVJ6IUTfwjA/zh-cn_image_0000002786520680.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=945D150D2BE6BCC59D8D7A69B48C3EA3D800560FD5A5418DC06FF913BC8683F3)
   3. 展开已创建的意图，新增自定义意图输入参数和自定义意图输出参数，新增完毕后点击“保存”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/RiBn52UZS9mdLgqLcFnP_w/zh-cn_image_0000002786360752.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBD5EC6CFB0280AB999254064F5CFCBDEAD6EB33FCCC64B313DED5B819B94E95)
4. （可选）新增/批量导入意图使用样本，用于提升模型对意图识别的准确率。

   ```screen
   ![decorator-test-11](figures/decorator-test-11.png)
   ```
5. 添加账号至真机测试用户组。

   1. 切换至测试页签，点击“编辑用户组”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/gThY-rkxRYq0l9Lorcwq9w/zh-cn_image_0000002815560173.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F64E2D9B262A3E85006EB38F9AA6DF98419F697D40EF5AC91233F3273B693B36)
   2. 点击“新增用户组”，填写用户组名称，填写完成后点击“确定”。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/kuWJ7vamQGqJLmLYHhLY6w/zh-cn_image_0000002815400257.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A167F674808157546DC88C4E24A425B0E4EDA1CCA22D24BE940C3F5FB2AC83A4)
   3. 选择已新增好的用户组，点击“管理用户”进入。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/DTUvhMV5Qve7qqTurJmVSA/zh-cn_image_0000002786520682.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=83BB5CEEF98A76F0A1A8EFBF319B4A5D591E7636A8B328FBF881E1F8D2B1F205)
   4. 点击“邀请用户”，填写测试用户的账号信息，账号类型支持选址邮箱或手机号码，填入后点击“确定”（测试用户须为该项目团队下的成员）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Fa1wxAAqTD-gfDC4Mex20Q/zh-cn_image_0000002786360754.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=753B086559E65B5278574044F07D9EC474038B36B285835D28CB54E232CFE4BC)
   5. 返回测试页签，选择所创建的真机测试用户组进行保存，点击开始测试准备，开发者即可通过HarmonyOS 6.0.0(20)版本及以上的设备在小艺进行端到端测试。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/qlRz6w9dSBek0MEMA3ZEtg/zh-cn_image_0000002815560175.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=583EB8BE93B2A675208B5BEF866526B8607FF0FDCB4E6B6B5C160405B777C828)

## 联调验证

1. 开发者需确认调试设备系统版本为HarmonyOS 6.0.0(20)及以上。
2. 在调试设备上登录已添加真机测试用户组的华为账号。
3. 检查小艺App是否为应用市场最新版本（需升级至最新版）。
4. 长按电源键/语音唤起小艺，输入测试语料，验证是否能正常打开应用内页面并传递参数。
