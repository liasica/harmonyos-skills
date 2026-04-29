---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-standard-protocol
title: 意图标准协议上架指导
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 意图框架上架配置指导 > 意图标准协议上架指导
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3c5282650f2a79765aab2940ccad2b07471236d69981cbb35a078011f2efee27
---

该配置需开发者完成自测后，先将携有对应意图信息的App在AppGallery Connect（以下简称AGC）完成应用上架，具体操作步骤参见<https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-overview>。

## **意图注册配置操作步骤**

1. 账号登录：

   1. 通过“<https://developer.huawei.com/consumer/cn/> > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口，需使用与应用上架相同的账号登录。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/NB3CkFMISjSU5HnI9cHeoA/zh-cn_image_0000002589245631.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=064C30E2F74FBF47EC02F4C19161F0C9F7C90130941267ADFC81E2DF00324AB5)
   2. 点击“立即体验”即可进入意图注册入口。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/UOt6KNYpS1G5yWHUSY_Krg/zh-cn_image_0000002558765822.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=9A138C4EB25AC2C0334C9BD6D5A0C4EDE7FD788AC23836618E0FCE17D99BB39D)
2. 选择意图集：在“小艺开放平台”首页“意图集（插件）”中，携有意图声明文件的应用在AGC**正式上架**后可**自动生成**一条草稿态的记录，记录中包含开发者在意图配置文件中声明的所有**端侧意图**（云侧意图需手动新增，见下图）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/Tg_YZ_XQSLae7TSOIJS1aA/zh-cn_image_0000002558606166.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=72F6551899D608CE0AABAD92AE4E15CEFE791948383869E49DE78C01D6784505)
3. 基本信息编辑：点击对应的意图集记录的“编辑”按钮，进入基本信息编辑页面，开发者补充完基本信息后点击“保存”即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/iLl7DIuWRciusy15JwbaZw/zh-cn_image_0000002589325693.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=EDCDAA3B5810982A8C2209EDF1CD2A7D06F423341FEFB44CFF3E7BF02663E907)

   此处的版本号和版本描述为智慧分发配置的版本信息，用于开发者记录和识别智慧分发配置版本变更，与APP软件包版本无关，意图注册名称与APP名称保持一致。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/kKHFemoqSI2iGGIVZQeWhw/zh-cn_image_0000002589245633.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=6CB295E11DFF33E14967FD1394C344A185F194B36D99636062A4F76DE34D4001)
4. 意图检查：切换至“意图”页签，点击“保存”会触发刷新，需检查接入特性所依赖的全量意图是否在此页面都已列出，同时打开意图使用样本中“是否已提供线下样本“开关。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Fatst4a-RjCQnUteItLN_w/zh-cn_image_0000002558765824.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=2A7DA401022DF547BF485DBCE9583539AD14CDF138163A8AC2EB5961650789EF)

   1. 其中，“端云类型”涉及端的意图需在APP软件包中定义，此处会自动呈现。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/LzLiNbrSStGyFih2gj-ZUQ/zh-cn_image_0000002558606168.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=D9C6BE1F55410BD1FD8943E85CDF1A1344AE3E84275022C70D6A00FF24E7C773)
   2. “端云类型”仅涉及云的意图需要需手动添加该意图。可参照如下步骤配置：

      1. 点击添加进行意图新增。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/3QdGbkRnQiyDWbkw0druiQ/zh-cn_image_0000002589245635.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=6691491789512178DFC2E3B3609A975A65247C3446190EFA76E7AC9D666D037E)
      2. 选择云侧意图分类，搜索意图名称，勾选所需意图进行添加（若没有找到对应意图可联系华为工程师，检查是否未配置该意图）。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ngFuV6VmSui1QERqKhm_BA/zh-cn_image_0000002589325695.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=C73FBB027806C23DC5F41632F862FF968371898CC3BB0AF703A387B7D278193F)
      3. 添加完成后，需录入接口信息配置，具体信息如下：

         1. API：即开发者的URL地址信息，供华为侧服务器进行云侧意图调用。
         2. 认证方式：如果涉及接口鉴权，则选择认证方式（例如AK/SK认证）并配置密钥信息；如果不涉及则选择不认证。
         3. 个人数据授权：该信息是指华为侧服务器携带对应信息访问开发者服务器，当有个性化推荐诉求时需要填写，默认不填写；比如选中“用户授权的用户唯一标识”（即SID），则华为侧服务器访问开发者服务器时会携带SID，开发者服务器则可以识别用户返回个性化的数据用户推荐展示。

         ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ej-ZPZsYQ0eYKdeHGJmjMg/zh-cn_image_0000002558765826.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=F2809B8FC5F83A803F26B5E1487D88A6C4E70EC2C8B9977088F05D9BB9D0198F)
   3. 如仍未全部列出，检查软件包中意图注册配置文件是否漏配，若漏配则在意图配置文件中补充配置，并重新在AGC进行应用上架/升级，完成后在小艺开放平台进行意图注册。
   4. 如果提示声明意图不存在，则说明华为意图框架后台未配置该意图。开发者可以继续点击保存走完本次流程，但相应意图和关联特性不会生效；可联系华为工程师，检查是否未配置该意图。
5. 检查完成：如果特性依赖的所有意图都已列出，检查意图名称、意图调用配置和意图共享配置等是否正确，正确则点击“保存”，进入下一步。
6. 发布选择“发布”页签，进入配置检查页面。

   1. 点击“开始检查”，检查接入特性和其关联的意图是否正确，如下图所示。生成特性时会同时生成abilityId，若开发者接入特性的方案涉及此参数，则事件推荐请求字段abilityId参数需要填写当前界面的abilityId值。若提示特性undefined，则联系华为工程师，检查是否未配置该特性。
   2. 配置检查完成后点击“提交审核”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/bZE7-rSBTFGkKqEHY3r1OA/zh-cn_image_0000002558606170.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=E81A123BB79234324A4E9C423607C76BC628552B54599BD7EA4383562661B8AC)
7. 审核：提交审核后，在“小艺开放平台> 意图集中”，该条记录状态变为“上架审核中”，一般审核周期为3-5个工作日，审核通过后状态变为“已上架”，至此意图注册及特性选择已完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/yDewmA59Rx-yw82Cb_VvBQ/zh-cn_image_0000002589325697.png?HW-CC-KV=V1&HW-CC-Date=20260429T054338Z&HW-CC-Expire=86400&HW-CC-Sign=F8C7F3EF2E27A7474951B82DA24F65EE11B839221B099575827AD830515D690B)
8. 新增意图：若开发者有新意图上架，可在同一条记录上进行编辑后提交，操作流程同上述步骤，未提交审核不影响已经注册的意图。
