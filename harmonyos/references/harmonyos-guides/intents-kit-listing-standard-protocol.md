---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-standard-protocol
title: 意图标准协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > 意图标准协议上架指导
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:34dc00a98dd1a7b57979aa2c66d3f8fe06c615d8dd1c0fec44d3d13cda8227cb
---

该配置需开发者完成自测后，先将携有对应意图信息的App在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见[应用开发准备](application-dev-overview.md)。

## 意图注册配置操作步骤

1. 进入意图注册配置入口。

   1. 登录[华为开发者联盟](https://developer.huawei.com/consumer/cn/) ，选择“管理中心 > 生态服务 > 智慧服务 > 小艺开放平台”，在管理中心找到小艺开放平台。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/AWDc-iWCQfOc6yxR6exJLA/zh-cn_image_0000002820526773.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CB40693D056D0EAD8E66C9EBC19927144B50F4CBC149939ED9D5F2C54620D83)
   2. 点击“立即体验”按钮，进入项目管理页面。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/8EaTgrueQeKVeV2zBVyfLg/zh-cn_image_0000002820406773.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=FA7EA693989D4DB0A5BABCE38236DBEFCE0DC20A831D7DD05BA7A38B411DEE69)
   3. 在资源库中点击“意图框架”页签，即可到达意图注册配置操作入口。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/W5KTtf1BTM2od4IX38qXug/zh-cn_image_0000002791726794.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2C68C457C013EF144313C3F1B3CCE7D6FDEEB0CF219CDCB7E6C0B3F25C98FF3)
2. 选择意图集：携有意图声明文件的应用在AGC**正式上架**后可**自动生成**一条草稿态的记录，记录中包含开发者在意图配置文件中声明的所有**端侧意图**。如果本次接入意图框架也涉及到使用**云侧意图**，则需要在意图集内手动进行云侧意图的配置（配置方式参考下文意图配置部分）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/jtH0nchTRV2TMk1GOsrpaw/zh-cn_image_0000002791566822.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EFED2C01EAA575085E7AA7A730314D763ABAB3B6DEBC70C1134009C82F42C18)
3. 基本信息编辑：点击对应的意图集记录的“编辑”按钮，进入基本信息编辑页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/ODlHpCS1S-O1H_4V92grYw/zh-cn_image_0000002820526775.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5E59B8A9C71CF03C74846923668D826180C5DC63E5706D4821D32324B1A9765)

   此处的版本号和版本描述为智慧分发配置的版本信息，用于开发者记录和识别智慧分发配置版本变更，与APP软件包版本无关，意图注册名称与APP名称保持一致。开发者补充完基本信息后点击“保存”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/RFer8MLqTOmdMdTa0JKtMw/zh-cn_image_0000002820406775.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F1785D3BF4C63346384559171B0FCC257A2D7C89E763BC562E2BC35422F4C38)
4. 意图配置：切换至“意图”页签，点击“保存”会触发刷新，需检查接入特性所依赖的全量意图是否在此页面都已列出。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/SKK1HEVPTCi-nt2CivLArg/zh-cn_image_0000002791726796.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=51489C0929ABE049A95B019A30E2E4AFC819CAF93012C7DEF39FAA2893A9243A)

   * 端侧意图：“端云类型”为端侧的意图，在APP软件包中定义，此处会自动呈现。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/w1KWZ0gJRiC48IsDYc8mDQ/zh-cn_image_0000002791566824.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=F05C7298C6069A95A31115EECB75DC0890A373A3BB8F92531F270C17CC005665)
   * 云侧意图：“端云类型”为云侧的意图，需在此页面手动添加。可参照如下步骤配置：

     1. 点击“添加”，进行意图新增。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/yv0GBkzDR5S-jZOV6ze8rg/zh-cn_image_0000002820526777.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8920B155493A2B3BE814670DB37CA84A37D97DFC9270508D66EA848ED80A7E4)
     2. 选择云侧意图分类，搜索意图名称，勾选所需意图进行添加。

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/eTR6rW1ASKSNWOlI8CPYpw/zh-cn_image_0000002820406777.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=29F7CEE46D8EAB651415A8A6B0342D203D7AB44BBCE2C0C16A130C4DC3CD46F6)
     3. 添加完成后，需录入接口信息配置，具体信息如下：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/95dPHdGzQrGokck3YhY0lw/zh-cn_image_0000002791726798.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=26E4F0324AE133666A82BD1C17B83B90E13CBF67C93FC091203CE02905D462F0)

        + API：即开发者的URL地址信息，供华为侧服务器进行云侧意图调用。
        + 认证方式：如果涉及接口鉴权，则选择认证方式（例如AK/SK认证）并配置密钥信息；如果不涉及则选择不认证。
        + 个人数据授权：该信息是指华为侧服务器携带对应信息访问开发者服务器，当有个性化推荐诉求时需要填写，默认不填写；比如选中“用户授权的用户唯一标识”（即SID），则华为侧服务器访问开发者服务器时会携带SID，开发者服务器则可以识别用户返回个性化的数据用户推荐展示。
   * 如仍未全部列出，检查软件包中意图注册配置文件是否漏配，若漏配则在意图配置文件中补充配置，并重新在AGC进行应用上架/升级，完成后在小艺开放平台进行意图注册。
   * 如果提示声明意图不存在，开发者可以继续点击保存走完本次流程，但相应意图和关联特性不会生效；如需使该云侧意图生效，请按照[Intents Kit接入流程](intents-access-flow.md)中的能力申请步骤，表述意图使用的场景提交审核。审核成功后，根据审核成功的反馈提示，重新操作该意图的配置即可。
5. 检查完成：如果特性依赖的所有意图都已列出，检查意图名称、意图调用配置和意图共享配置等是否正确，正确则点击“保存”，进入下一步。
6. 选择“发布”页签，进入配置检查页面。点击“开始检查”，检查接入特性和其关联的意图是否正确。

   * 如果正确会同时生成特性以及abilityId，若开发者接入特性的方案涉及此参数（例如事件推荐场景），则意图共享中请求字段的abilityId参数需要填写当前界面的abilityId值。特性检查无误后，点击“提交审核”。
   * 若提示特性undefined，则说明华为意图框架后台未配置该特性。如需使该特性生效，请按照[Intents Kit接入流程](intents-access-flow.md)中的能力申请步骤，表述意图使用的场景提交审核。审核成功后，根据审核成功的反馈提示，重新操作该特性的配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/kywUHHPWSFu4iO73sHSloQ/zh-cn_image_0000002791566826.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=0509BEBBAB393A4D2B3D7687950A20806E717A980E387F854F8207021647124A)
7. 审核：提交审核后，该条记录状态变为“上架审核中”，一般审核周期为3-5个工作日，审核通过后状态变为“已上架”，至此意图标准协议上架配置已完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/wWMlTnvoSaOcCKNqwYa3BQ/zh-cn_image_0000002820526779.png?HW-CC-KV=V1&HW-CC-Date=20261119T014826Z&HW-CC-Expire=31536000000&HW-CC-Sign=10332A846CFDE00429E2452F3792C2A75B57228CE9C05382E475B52211174DD5)
8. 若开发者后续有新意图上架，可在同一条意图记录上进行编辑后提交，操作流程同上述步骤，未提交审核不影响已经注册的意图。
