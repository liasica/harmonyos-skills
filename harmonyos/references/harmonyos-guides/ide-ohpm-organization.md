---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:83ffc9ca1a977e42ef9ac22bee3d60ea447987b9ab4393ef590ef1713061ea5c
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的首个上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/0zEgJeskSwWOEZ4DscRTIg/zh-cn_image_0000002779405348.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=243AF3F041EC0BAC7C434EEF562EFCD2420AFA28C410668500F46A978A07E9A6 "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/jGgN_2uYTWW0PsWYZdGCbQ/zh-cn_image_0000002808884991.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA80034B2092896042A245FD854B400012FBF80F0DDE6FAEB7A376AC8EA0F8A3 "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/t_AJQDLwTX6JFKDUImzdtA/zh-cn_image_0000002808764889.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E2E350693C2BF8C4B79B8A83A92207BD5FC5B4039AC1C1EAED8A333A5EB24DF3 "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/BojifQ0DQ7egWp7wRI_6oA/zh-cn_image_0000002808764869.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=618626CF76114B2BDF0884CE54730872629065CC6243F04AF8C599F43367B1CA "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/epBw7SSmSym-WAM8nog2Fg/zh-cn_image_0000002779565316.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC430C5605AAF19CDC163601ABB90C4EE03030E18FE16D3F797E9F33E6C3DF36 "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Un9pwmB-SOuvqpKBFfWg-w/zh-cn_image_0000002808764865.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=153F8A8892769D3ACB2076F7E1C74FC7534470BCC3B1C778B864E29A096D232D "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/bZESHvC0RMGoKlVz5wvcog/zh-cn_image_0000002779565328.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DF961DEAD9035F6207B3760F5C47E588072E7ACDF6AAE0F742578198D16E8DF "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/SkaMmm9lRmyCQgSq7KQ65w/zh-cn_image_0000002808884965.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5671CD48FE94137381B15ED17FFD24CA3F7A29DB3001C423AA6611686E344F7D "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/PlX2h7N_Q7GD36aXCTcB_w/zh-cn_image_0000002808764843.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EBF1F7D40DC91F5FBCDC13FF8FD39E344E2F8F822BC891500D96E7AD2A191D2 "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/xrFeze0UR3uWCnp1cECwKw/zh-cn_image_0000002808764911.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=403F952C55742F839D8D7F1DE0605E80C05419D4C02A31A19C87B5AA269C77F4 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/7668wlzcRGKhPnkIn7JDtg/zh-cn_image_0000002808884979.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=615D2C697E547480219FCE35D279A33C719BFB3021F9CDE8690F777CD0948370 "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/IS452bTZSEGP3u7qspyqGg/zh-cn_image_0000002808764881.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBDF71B9460102CBA778200FB9E316163ED9EF794B81B006AD90EF4C3E516F80 "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/umIiZiqqRNygOzXLj9SBKA/zh-cn_image_0000002808884941.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=A332BDFD5FC1380DD8925FC7B6DF51348B30F10DEDB47F34265C3501241FCC67 "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/pInQMXoySNu1bbgS2VWXMQ/zh-cn_image_0000002808884957.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7753554C14F8492ACA6ACFB9F5CF2B5EF0310715316047642096F973E5DB6986 "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/6_jjQmn0QPSV4GJbu4LcCg/zh-cn_image_0000002779405342.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=571239930A029BE217F450E049F1F2F15C9D76CD117C55C18B1CE7D851C220EC "点击放大")
