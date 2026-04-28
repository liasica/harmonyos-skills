---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-standard-protocol
title: 意图标准协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > 意图标准协议上架指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d0e173cc00b565d01a5898ff5a7896678917039ca407235c7de784a2f8aeb5a
---

该配置需开发者完成自测后，先将携有对应意图信息的App在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview>。

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口，需使用与应用上架相同的账号登录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/g974qhJfRMW_T9jtPt71yw/zh-cn_image_0000002552959320.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=A96195FBFF703F4A4B99F4F871803A891404052499ACAF8F6173A5367E1A315C)
   2. 点击“立即体验”即可进入意图注册入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/XTKijCS9Tr2rEhmVM7kiDw/zh-cn_image_0000002583479321.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=6534FE6203CFCD5DA9504F0527884B87974097DA4BBFC0B900E2DCB3A13AD051)
2. 选择意图集：在“小艺开放平台”首页“意图集（插件）”中，携有意图声明文件的应用在AGC**正式上架**后可**自动生成**一条草稿态的记录，记录中包含开发者在意图配置文件中声明的所有**端侧意图**（云侧意图需手动新增，见下图）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/tkHQC5BOSGWq3hknSV5ZPw/zh-cn_image_0000002552799672.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=B688056712B54B8AD198839BFD11D97A55687258BF64F4E7ED616FE935654547)
3. 基本信息编辑：点击对应的意图集记录的“编辑”按钮，进入基本信息编辑页面，开发者补充完基本信息后点击“保存”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6YTKF04bSmiEQQpj9Kr-6Q/zh-cn_image_0000002583439367.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=0BBF786B32D6AA656EF39B82C477B5D487EE49AF26D5E66CC5F234FE82F41C3A)

   此处的版本号和版本描述为智慧分发配置的版本信息，用于开发者记录和识别智慧分发配置版本变更，与APP软件包版本无关，意图注册名称与APP名称保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/i8S3cfiCTGGNQLirtx-xNA/zh-cn_image_0000002552959322.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=D4D4EE4E0251A39B1B95D418CB437EE267A8B952B41C0DE8E79361E0188FF92B)
4. 意图检查：切换至“意图”页签，点击“保存”会触发刷新，需检查接入特性所依赖的全量意图是否在此页面都已列出，同时打开意图使用样本中“是否已提供线下样本“开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/C_WCgVqySSijg5xEngYlig/zh-cn_image_0000002583479323.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=2FB1E3342CF35E05FB0B6BB070BC627D4090FA6B2DD279C3E08F006E10FC4562)

   1. 其中，“端云类型”涉及端的意图需在APP软件包中定义，此处会自动呈现。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/itN6n2v2Qc6dNR2mroZQig/zh-cn_image_0000002552799674.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=572780A2E0A90F76B889FD741A62D572E8973365DB10EDC264020BC19ED34705)
   2. “端云类型”仅涉及云的意图需要需手动添加该意图。可参照如下步骤配置：

      1. 点击添加进行意图新增。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/yA0Uus-5Sj2q73aYaHkOPA/zh-cn_image_0000002552959324.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=B6223EB951A27F751B926AA58D0C81B320C8198719D880D55F03A2F0FB897EF2)
      2. 选择云侧意图分类，搜索意图名称，勾选所需意图进行添加（若没有找到对应意图可联系华为工程师，检查是否未配置该意图）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/9Jys-6xTQSKuKlkKj7yDAw/zh-cn_image_0000002583439369.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=5839A9B86FC3C01EF95828E7ED4B1DECF345C9F98136025882C5A01C38413F2B)
      3. 添加完成后，需录入接口信息配置，具体信息如下：

         1. API：即开发者的URL地址信息，供华为侧服务器进行云侧意图调用。
         2. 认证方式：如果涉及接口鉴权，则选择认证方式（例如AK/SK认证）并配置密钥信息；如果不涉及则选择不认证。
         3. 个人数据授权：该信息是指华为侧服务器携带对应信息访问开发者服务器，当有个性化推荐诉求时需要填写，默认不填写；比如选中“用户授权的用户唯一标识”（即SID），则华为侧服务器访问开发者服务器时会携带SID，开发者服务器则可以识别用户返回个性化的数据用户推荐展示。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/vqcFor6SQ22GKl_eA1WB8w/zh-cn_image_0000002583479325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=1590F2464847B8DC2C5C96F2AB37CFE53D0F16ECE3C8FF3C1B034BBF7E46B326)
   3. 如仍未全部列出，检查软件包中意图注册配置文件是否漏配，若漏配则在意图配置文件中补充配置，并重新在AGC进行应用上架/升级，完成后在小艺开放平台进行意图注册。
   4. 如果提示声明意图不存在，则说明华为意图框架后台未配置该意图。开发者可以继续点击保存走完本次流程，但相应意图和关联特性不会生效；可联系华为工程师，检查是否未配置该意图。
5. 检查完成：如果特性依赖的所有意图都已列出，检查意图名称、意图调用配置和意图共享配置等是否正确，正确则点击“保存”，进入下一步。
6. 发布选择“发布”页签，进入配置检查页面。

   1. 点击“开始检查”，检查接入特性和其关联的意图是否正确，如下图所示。生成特性时会同时生成abilityId，若开发者接入特性的方案涉及此参数，则事件推荐请求字段abilityId参数需要填写当前界面的abilityId值。若提示特性undefined，则联系华为工程师，检查是否未配置该特性。
   2. 配置检查完成后点击“提交审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/0xEDko5GRfSFTjxjdEoBfg/zh-cn_image_0000002552799676.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=135B6F75EA143887FC51E7A0FF0818D640F73F3880BEAA70CA7C1578D3B57CA1)
7. 审核：提交审核后，在“小艺开放平台> 意图集中”，该条记录状态变为“上架审核中”，一般审核周期为3-5个工作日，审核通过后状态变为“已上架”，至此意图注册及特性选择已完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/ijhChspATd26nueisRNj0Q/zh-cn_image_0000002583439371.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=63EEEA7B41F13FF70C951EEC8E32CF37E3E3074D7595EA5AEA074089B551C7E8)
8. 新增意图：若开发者有新意图上架，可在同一条记录上进行编辑后提交，操作流程同上述步骤，未提交审核不影响已经注册的意图。
