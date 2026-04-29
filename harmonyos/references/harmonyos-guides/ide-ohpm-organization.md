---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:48+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3ff1f31ec16cbc46c435ae87f2b0cc12b303bbfabc983f5639456cbbcf28e251
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。

其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。

注意

在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

同时在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的第一任上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Vh9-PTwXQxmdspTCgLmGNA/zh-cn_image_0000002530751342.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=F71274B54E1DE77C519F7AEB3776487B79452733305353E0ECEC55013AC8B5AE "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/YlLXNg7aRci7eeBYr0CisQ/zh-cn_image_0000002561831267.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=02DE78CBC44B114A4AE1875AA902526AF945DC0FFB15C0FDC787829B97825AB7 "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/qlLwbq5XRBmzKFZYcTpjTw/zh-cn_image_0000002561751297.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=79DF8FCE586673D586FE0AE192F69CA356396F2B05C9992892EB8589710768EC "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/bLZOesVZRfK9cvoIS6ZgPA/zh-cn_image_0000002561831221.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=85F51E1CBC32F24E1D8D94BD4A053F196AFBC1AFA607898CA9C50C275BFA42FA "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/SiiuPYOVTBWgBRL2Up6gTQ/zh-cn_image_0000002561751263.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B983B143F664FE897C9233A5BDFEFA16B33E77DE974451DCB47FD0DDA51D2FF2 "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/kH3emWa4RCSokXCRl6ahnQ/zh-cn_image_0000002530751314.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=8C72738031B3B42749D471B5E18EFF204CC7B8573CCE8430B1E3BA893B24DF98 "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-0IN2zC8Ra-ouvWGqdMLhQ/zh-cn_image_0000002530751302.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B685C4E3E8F7CE6811B96B3335FBEA43067A3538E9D3BE6BFD0932833527857C "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/3PiighoQTryUTukDrzisiA/zh-cn_image_0000002530751312.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=BB5E245176CB8DE2346634BD9765DC156D2D19F8222D712B9951DD05E86FFB93 "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/-opxE1TzQ0y27eseh188FQ/zh-cn_image_0000002530751306.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=275E42F768F9430DA27EB42747F5D18FC8C889C57627B2F175AE371E92F9033C "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/YCcE7skqSGyJ9vgwiC50qg/zh-cn_image_0000002530911322.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=7735572C35E189A717CA4A09201DEF2BC99FDB5D0AC86E81B6460E4433439CD8 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/5yhxAtQaQZOexa-YjU6Scg/zh-cn_image_0000002561751277.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=B8EB27840F7CE2C56A8CD15618B308353612C57451850E9D72D7F440EA7E07D7 "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/_bOCgC7TSTOLTiG72FWYRg/zh-cn_image_0000002530751362.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=102EE01CF0DED0104E0866D74AD4326325783D49613D2822CE657D87199C06BE "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/9Yk2qeyUQD2vmYUD2gGHrQ/zh-cn_image_0000002530911310.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=90E147478E60E29A12E87E5C0E48B1163E3C40B3C42C1D0679053AE86DF8A79B "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/5rqNDbtRSlK7gDuibdacTw/zh-cn_image_0000002561751247.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=6E5430CA60E655A8FDA4D169B6A173E268AB4F8E809540EA54C677C0D01A0F75 "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/MaUKDvUAR8GLu9PlbNUsqg/zh-cn_image_0000002561831225.png?HW-CC-KV=V1&HW-CC-Date=20260429T054444Z&HW-CC-Expire=86400&HW-CC-Sign=10A646C7A43C18B910B60EAADF258AA8CE3D6207933E7591638E4BC1E81A390B "点击放大")
