---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:53+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f05be4bdbaf8dfc7fe69e9c5df30296b3863655c834dd54ef26cb96424191588
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。

其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。

注意

在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

同时在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的第一任上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/FPhAlKzpQcmnpdLgG1Z4oA/zh-cn_image_0000002530751342.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=607ECCD7F7F08230D4B2EBBCC465EBF50F42330455567C20ED68584A423C59D3 "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/sFQwotg6S_C0qsJk8ARXNQ/zh-cn_image_0000002561831267.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=6BFE804B7C0F1B35015E111E5B5B662B9946308299CBEF812A721B213225AA0D "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/iXjoqgO1QhKNoPGmQKegdg/zh-cn_image_0000002561751297.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=705B74937AAF409CE4B8CC9C0ADEF48FE61861A28075F67CB5F4481775602C59 "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/dutkIEzGSJyrrKjOQlWwng/zh-cn_image_0000002561831221.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=19A9DB023D61BAE7001F5BC2E29744EF10AE523872526D7885DDD967EC06E74C "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/Fn5znU9vS66z-mgqw33TLw/zh-cn_image_0000002561751263.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=6A675D07CC4FD95045649F2E03C62EED9283293AED333213AF12EBFB7EAAD2BD "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ZZevrXHlSaCC413Wr3R8zg/zh-cn_image_0000002530751314.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=EE82B054459C672429DE631CD0B7B7708820325D208C071A80C730A8922DA5F4 "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/u1o0X3fvS26-erHsGRCa2A/zh-cn_image_0000002530751302.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=BF69E22D7D4DBFA3C45FF011FAE83DDA7969C902EA92DEBE6020C09BF216B7AC "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/RXGJ80mSRbutWFvQhBkyTA/zh-cn_image_0000002530751312.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=BD50D74BFE8CAFED0ECC54627A864BE52028E6027FA93D4A4FC54FAB67D138A2 "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/kps5QE4kTjCTvY9eCX5pOA/zh-cn_image_0000002530751306.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=3A74B69FC78560C3010C2BFCF82DB5D4F5E0C54F67610516D07B7EABFBB1396E "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/4Qo1OK0yTmCw_PDP5ISs4g/zh-cn_image_0000002530911322.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=A00DBB98C411E06616E3C1B1BA398FF70A4A5E9279364C6B9D17073AF96079E9 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/AjYFHhA0RymKoAI5105WVQ/zh-cn_image_0000002561751277.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=8464CC5A386DCAC1772BEC5659E6B93F40BF1DE0C74312DCBA2FB5419911E44F "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/KTGPEtpMT7OFHeewzvB_MA/zh-cn_image_0000002530751362.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=08F0E77E778347E53D3A8EF94400323477E04E54EB5B908F5BE34BB9881E0095 "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/toBqzFdkQgGbSTEfGoeXCg/zh-cn_image_0000002530911310.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=889EAA0B76969B5C5D11B4D5B5A7F29A8E2C983964AD05DBAFBC7C33D430200D "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/ChhoXGw-ROK8sdch2iTZRQ/zh-cn_image_0000002561751247.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=B92B182414DDD30F287772B2070BDD8F0400730737FD0E86076BE1577360165A "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/QEek42tCQ1qOvrKce6Ttzw/zh-cn_image_0000002561831225.png?HW-CC-KV=V1&HW-CC-Date=20260427T235450Z&HW-CC-Expire=86400&HW-CC-Sign=A146AB86DB03E319B06D8C58F05E8556EB65909B34623155535456F8D2B57AD0 "点击放大")
