---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-standard-protocol
title: 意图标准协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > 意图标准协议上架指导
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:47+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:7e487e0af41b68286301711eee12442f672b982809bed9086bc0af72993067d9
---

该配置需开发者完成自测后，先将携有对应意图信息的App在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见[应用开发准备](application-dev-overview.md)。

## 意图注册配置操作步骤

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/8ZlNAO_HS0WW0WvKjYKhCA/zh-cn_image_0000002821838381.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCFB4BD02BD749700B5B9BAB0578D279621F976468DD8666C1DD4DEB31B42E43)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/e2XnrQVpSduE6N3GWm5mLg/zh-cn_image_0000002821758383.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B8CC2336B0190A4D3EBBD2F44EBB8CD461D5BA2059866AED4E8BBCB4FF22EE6)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Q-z3DsYuRhSs2Z-0nHxYog/zh-cn_image_0000002793038446.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=E28F5EB2D5743871B15057B87AC4A0B807FC28D78A1C044F4BC36633948D7ED5)
2. 选择意图集：携有意图声明文件的应用在AGC**正式上架**后可**自动生成**一条草稿态的记录，记录中包含开发者在意图配置文件中声明的所有**端侧意图**。如果本次接入意图框架也涉及到使用**云侧意图**，则需要在意图集内手动进行云侧意图的配置（配置方式参考下文意图配置部分）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pug-4I9QROCijEk0y0T35w/zh-cn_image_0000002792878476.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E81B8857EFCCB6B030C47692A5E7ED4AF4162A1442DD654C21C91108C45DA1A)
3. 基本信息编辑：点击对应的意图集记录的“编辑”按钮，进入基本信息编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/VT-5Zh18Ree2hhuntk9mRg/zh-cn_image_0000002821838383.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=83734D3EC7161501C1377366E6E42AED0DD23FE3F34B31E9642D7F836CC9F3E8)

   此处的版本号和版本描述为智慧分发配置的版本信息，用于开发者记录和识别智慧分发配置版本变更，与APP软件包版本无关，意图注册名称与APP名称保持一致。开发者补充完基本信息后点击“保存”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/KCwTXVZqRrqrRrST1LA20Q/zh-cn_image_0000002821758385.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=5062484B488BE60A217EDA47B079AC4EBC97B60FB1CBF2832919B87E53D88651)
4. 意图配置：切换至“意图”页签，点击“保存”会触发刷新，需检查接入特性所依赖的全量意图是否在此页面都已列出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/EVLpFJZyRl-1yv5rQ4e1rQ/zh-cn_image_0000002793038448.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD8ED5403F7587C39513F2E2806D148B351CC05E42566C9E2E889DF93A601997)

   * 端侧意图：“端云类型”为端侧的意图，在APP软件包中定义，此处会自动呈现。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/3JDruEUrQE-ktgXMFREg_Q/zh-cn_image_0000002792878478.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FFC11736CDAECF02EAC3B10E161DF7B6477839CCD18D70D25E026C20E0EE1F2)
   * 云侧意图：“端云类型”为云侧的意图，需在此页面手动添加。可参照如下步骤配置：

     1. 点击“添加”，进行意图新增。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/SbshA7K_STyviMF4BEe_yA/zh-cn_image_0000002821838385.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=2949A291900C43024B5E0C59D7B49855FC0253EE72B522BCE2363B626CA1A11C)
     2. 选择云侧意图分类，搜索意图名称，勾选所需意图进行添加。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/a6qm3trkTWCYTxmUzae-Yg/zh-cn_image_0000002821758387.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=F59BD864F932816ECFA0A4F268512E7A085839C6EFB24329CCAB588B407B4515)
     3. 添加完成后，需录入接口信息配置，具体信息如下：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/pXXy5sdcSuCKCHtPFmfQrg/zh-cn_image_0000002793038450.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=D67E3845D6CA9368C7047677BE52125304194C6F4453A2889936D1263DB83C85)

        + API：即开发者的URL地址信息，供华为侧服务器进行云侧意图调用。
        + 认证方式：如果涉及接口鉴权，则选择认证方式（例如AK/SK认证）并配置密钥信息；如果不涉及则选择不认证。
        + 个人数据授权：该信息是指华为侧服务器携带对应信息访问开发者服务器，当有个性化推荐诉求时需要填写，默认不填写；比如选中“用户授权的用户唯一标识”（即SID），则华为侧服务器访问开发者服务器时会携带SID，开发者服务器则可以识别用户返回个性化的数据用户推荐展示。
   * 如仍未全部列出，检查软件包中意图注册配置文件是否漏配，若漏配则在意图配置文件中补充配置，并重新在AGC进行应用上架/升级，完成后在小艺开放平台进行意图注册。
   * 如果提示声明意图不存在，开发者可以继续点击保存走完本次流程，但相应意图和关联特性不会生效；如需使该云侧意图生效，请按照[Intents Kit接入流程](intents-access-flow.md)中的能力申请步骤，表述意图使用的场景提交审核。审核成功后，根据审核成功的反馈提示，重新操作该意图的配置即可。
5. 检查完成：如果特性依赖的所有意图都已列出，检查意图名称、意图调用配置和意图共享配置等是否正确，正确则点击“保存”，进入下一步。
6. 选择“发布”页签，进入配置检查页面。点击“开始检查”，检查接入特性和其关联的意图是否正确。

   * 如果正确会同时生成特性以及abilityId，若开发者接入特性的方案涉及此参数（例如事件推荐场景），则意图共享中请求字段的abilityId参数需要填写当前界面的abilityId值。特性检查无误后，点击“提交审核”。
   * 若提示特性undefined，则说明华为意图框架后台未配置该特性。如需使该特性生效，请按照[Intents Kit接入流程](intents-access-flow.md)中的能力申请步骤，表述意图使用的场景提交审核。审核成功后，根据审核成功的反馈提示，重新操作该特性的配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/FQFHmaCLRcqXEI9Al9kHLA/zh-cn_image_0000002792878480.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEBF0490940A769FA3C82EB28192FDFC8BB0A021A9991DF7DB862F58E6F016A7)
7. 审核：提交审核后，该条记录状态变为“上架审核中”，一般审核周期为3-5个工作日，审核通过后状态变为“已上架”，至此意图标准协议上架配置已完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/eT-3o1c9Rc2Is4GweJwN4g/zh-cn_image_0000002821838387.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=94110ADCA66B64265B97CB7772F47A61BD43C9B5090F36163720B0A91B22DBD6)
8. 若开发者后续有新意图上架，可在同一条意图记录上进行编辑后提交，操作流程同上述步骤，未提交审核不影响已经注册的意图。
