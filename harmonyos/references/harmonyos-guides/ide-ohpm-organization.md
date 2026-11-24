---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:20+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:7a9df9d103c7f94c4a2b20a50594c3001cd0dd480aeb00448ba86dac4f088105
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的首个上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/PfIwg4bnTXC_DJJHwnnX2A/zh-cn_image_0000002779405348.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=9DA7D4AA4E2357438B628E46B538840188A99BEF37E634094A224F72B3D4B11F "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/T3UXKHghQauHY0QozXS1Yg/zh-cn_image_0000002808884991.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F6136546C0833D8D9D8BD257B752FF2749269D528F87DFB2543CC3E52DC69A1 "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/e20ojTX7TsSzD4YK4o02GA/zh-cn_image_0000002808764889.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4A3D6AA6CD83743773EB6841E6D9CCB77966B85831E2B12B4A654BB65995F94A "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/5rRGxSkkTEWNC3cDjtzgZQ/zh-cn_image_0000002808764869.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=59518DDE26C9C462F2E9E92A580021E0A0A85DF0172DA25F05FE62BC3E528189 "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/Iw7RZgLqTfyVCBJhMjizvg/zh-cn_image_0000002779565316.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEED2EF334BA9BC0707C824BF4A991C0209A3B9E14E722C6613469F094AA9897 "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/m2igI_DTQfqnc1rymj-TAg/zh-cn_image_0000002808764865.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DC0ECC2747AD7802FF29A25B78270AEA0ADBBA4ED47507061119B4C5797A46F "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/vMDq-T_hQCeSmZhkoLQNmQ/zh-cn_image_0000002779565328.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B75049C4756E33B86B6DAEB51A0AB78009FE49A76895FD662416EA93BF948788 "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Y_pHBhTaTD-F6006bR8AuA/zh-cn_image_0000002808884965.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD521ED377D09EF28294D65EBD84FE665F4AB333BFC94F452E87202884BA8EED "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UD10hDThQQiWNBSXh2vkiQ/zh-cn_image_0000002808764843.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA6CE095029C5EBAB3034E6A792B58037A97503D64185026304D29E21A751200 "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/3ulOXZlHRL2vFu1oqjYRTQ/zh-cn_image_0000002808764911.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=03852A1E9DD6B58E3F80AF1BD19E32A487D433A5C7ADF434C60C9BA9AF2FDBF7 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/N5sh5PHGQam5SciSY2aqog/zh-cn_image_0000002808884979.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EB668B9565DA804DE4184F0A275F3990D6CCC1C3D89F48C6F4CF4EA959CE200 "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/W2zd_hLSQem9m0Ao_1s4ZA/zh-cn_image_0000002808764881.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFD579AAAC619458CCDBEAF67D18B3525078DBA3E791556FFE7E6C52F63CFE59 "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Fbwb2YX_SmGpYTItvueJGA/zh-cn_image_0000002808884941.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A707534F316F2CB02692F9FB5C413AFDCA153AF3E1D46B8C5C52725E3C0E56D1 "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/-70pFoRETG2U5zzjH42sPQ/zh-cn_image_0000002808884957.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EE5D36D9EE6250E05EEFA8F0D883A0110DBDF15633E7B3C1E5DEC8510310568 "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/gg391m6QSTSLlbgA9Q018A/zh-cn_image_0000002779405342.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=5310588865E9BB3BDAAA79F702A539804499484C460BD33C2CDD69BB41BC8A26 "点击放大")
