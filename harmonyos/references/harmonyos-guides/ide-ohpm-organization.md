---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:7c99b7e9d7e0e051c9d73f886a7311a7bcac18b6e402036532bce58a078530c1
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的首个上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/GldqS7OOQl-u8-OUHN3b_w/zh-cn_image_0000002779405348.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=400C48C77AAED79259D8794C62810B456F36C7F49517EBAA92F52CC50BF1D9A5 "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/1SR7O_-4R5m74jCeFgZJng/zh-cn_image_0000002808884991.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=02F6CB4078CC1ECC5C4049747FF157562C002C35811BE6C8C3555A4CCE3DB8B4 "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/7sOUrC1RQqOYSZm6A5QGeA/zh-cn_image_0000002808764889.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C6DCC2D00E39E47CE747CA550A6BCD1B34245B77F3E4F859CB4CC7F1863CB1F "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/92f-BrB6QPyYsMNz87udVQ/zh-cn_image_0000002808764869.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=4ED370F5DF1576043E77C6F6B35CD840BD185DF80D923C5F414AE6C0738D4401 "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/XXaepRmMSTCYrxYljhBeCw/zh-cn_image_0000002779565316.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=232453F8D6305106332206645F41B5BEC36ED17E20C68C0EF6859C3601C831CF "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/_Yich9qLTviZ58atr_8SmA/zh-cn_image_0000002808764865.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=1497DD48514037FED3B3BA615D24876FC81493FC4729689F7C993CAEE142E600 "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/pWfxx872Q-moHUSpPQOxEg/zh-cn_image_0000002779565328.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=48C2086F0B321773A10BF5EF0456D91A0ED0B0B4EA29D324728F8BE5E1748A7C "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/3vaNwTA7TC2yR_s-ZaByww/zh-cn_image_0000002808884965.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=F90FED78DBB02E80D9B687351E1E3D24E00356F31A739881238B0D73754A0976 "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/LMPCKDI_RKeQWn4cOfTM2Q/zh-cn_image_0000002808764843.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=16ADD439250CE5030EC23CE4E785B0CA9DED1119DE52F98D176F57CC6CB7BF05 "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/u51kv2TjTPKOuijsu2-iRA/zh-cn_image_0000002808764911.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=E271635E450ABC3C50AC5417B15B5B7566960368501194F727389807BC622A71 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/-EYkELuBRZi2xJMojNdUTQ/zh-cn_image_0000002808884979.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF086DCF3F4D37962E1209A18474896DDFC25D9E3EAC999B0C6B212EB4732053 "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/CFV9_lfARjql29r8eYPt4Q/zh-cn_image_0000002808764881.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=89A41C1A204C8A351F7D55FF62642CBAC7B4D67CC300E19CAC1226125C837D7A "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/iDyL8BHzS5uudXyskEgPXQ/zh-cn_image_0000002808884941.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=2956D7AC33DDC2DFCFED6DDAC0ABFA12FF8B99F96A27C2A46373322AE3A33EDC "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Y887A0mDRjO4v20LPTE81w/zh-cn_image_0000002808884957.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=564B49AF7049887C4BFAA2FBF2DA06005C2BEE2E3E0D67B68BF902A274571AAB "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/zuTKhwt0RaqzidXUMZAebg/zh-cn_image_0000002779405342.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=975837AFA99123B73F1EB8DB48F0824D98A5B30557ECD641C5095914CB0A0593 "点击放大")
