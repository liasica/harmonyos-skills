---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-organization
title: 组织管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 组织管理
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:a6d5b63078475e02016e6f43c3ddab583f2599d53e615c540d27c6e63740620c
---

在ohpm中包的命名格式为@<group>/<package\_name>或者<package\_name>。其中group是组织，package\_name是包名。当想要上传一个含有组织（例如@ohos/axios）的包时，在ohpm-repo中需要先创建出该组织（例如ohos）才能进行上传。在发布HAR/HSP包时，建议将组织名称包含在包名（package\_name）中，便于管理和识别三方库。

在ohpm-repo中，只有组织成员才能上传该组织的包，如果一个包没有组织，那么后续版本更新只能由该包的首个上传者上传。组织管理用于管理组织信息。

* 管理员用户的组织管理页面：可以查看所有组织的信息，编辑任何组织的管理员信息。此外，还能添加新组织、搜索现有组织，以及编辑和删除负责管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/6ybWI-GzQIOnMmXb9_zRig/zh-cn_image_0000002779405348.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=455B6FD2F4FDD74C8A5F0BAB6AED10E0852B421D8C60AE454F678183A896F393 "点击放大")

* 普通用户的组织管理页面：只能够看到当前用户所属组织的信息，能够查看和搜索组织，编辑和删除所管理的组织。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/Fa5unpzvSQm4G7n2wvqnHw/zh-cn_image_0000002808884991.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=7BDCD6932E412276CC09FFCCDA14FA4BD95D918DF69973AD0C37B07E975C744F "点击放大")

1. 点击“新增”组织按钮，需要管理员用户权限，弹出添加新组织面板，可以新建一个组织，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/t1JxUrNlQna54KHRiRu13g/zh-cn_image_0000002808764889.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=434743B130546E98EDE489BACCDB7B978FF8B068DE36D0CCBE02C32A2E8CF6BB "点击放大")
2. 点击“详情”按钮，进入组织详情面板。包含描述、包、成员三个页签，其中描述页签是展示组织的基本信息；包页签展示该组织下仓库所上传的所有包信息；成员页签用于组织管理员对组织内成员的管理，可以输入用户名去添加成员或将成员移除出组织。
   * 描述：展示组织的基本信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/mok5mniASyapn1unmFLTEg/zh-cn_image_0000002808764869.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=1707C9768C9E706FC7AF69E8829E9A1B17D82B01EA5E2ADB40CB5F1F2C5D32A7 "点击放大")
   * 包：展示该组织下仓库所上传的所有包信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/SHcpLjo_Qg-Vzx_peUNXcg/zh-cn_image_0000002779565316.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=258DF51F1671ADEB010D29A4B9F1B47FCC60E9B1838CA5AB544F8BAB2AB0DF78 "点击放大")
   * 成员：组织管理员对组织内成员的管理，可以输入用户名去添加一位成员进入组织和将成员移除出组织；组织成员只有查看组织成员列表权限。
     + 组织管理员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/LpxiVRvbTJSLD8SCesHjDg/zh-cn_image_0000002808764865.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E1E3522D9EE8B84D9467AF8006FDDF62E81F5997C9CC029EA4C1571273706A5 "点击放大")

     + 组织成员页面：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/cCZLNnlHSgG-tL-6Dd-srg/zh-cn_image_0000002779565328.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFF8B2937C612EBCF359A905DE312A5596A594C2EA2B1E5DD7F725ECDFC672AF "点击放大")
     + 点击“新增成员”按钮：需要组织管理员权限，输入用户名，能够把该用户添加到组织中，成为组织成员。当组织成员添加后，成员用户将自动具有组织下所有包的维护者权限。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/-fznNqnySvau1Kd-oD4DeQ/zh-cn_image_0000002808884965.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=2300872022B2F6BB564BBD1FC2CCDB0D2E8F0790328B401C969F9885F966D24A "点击放大")
     + 点击“删除”组织成员按钮：需要组织管理员权限。如果删除的成员是组织管理员，且没有其他组织管理员，则不允许删除，一个组织必须有至少一个组织管理员。当删除组织成员是普通成员时，如果当前用户对组织下的包具有维护者权限，权限将被删除；当删除的组织成员是组织管理员时，如果当前用户对组织下的包具有所有者权限，权限将被删除。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/fRmVThH9R426EZVpsCuR3Q/zh-cn_image_0000002808764843.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=66BBB054A97A0459187CF82FC887B63142E8753F974CA7650B39FDE6AEC2B5EA "点击放大")

3. 点击“编辑组织”按钮，需要组织管理员权限。进入编辑面板，可以修改组织的名称和描述，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许修改名称：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/uECdfYxJShK4k0KkgZnf9w/zh-cn_image_0000002808764911.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FBC763D4137FE42671F0DCA0F86D1AD6219664D16E9072E63866188A8434DF3 "点击放大")
4. 点击“编辑组织管理员”按钮，进入组织管理员详情页面，需要管理员用户权限。能够查看组织的管理员列表，并且对组织管理员进行新增或删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/CVVxLUjdTRC9KAW8Drv2kQ/zh-cn_image_0000002808884979.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AB0B070D67EDCA02076F447B7069992D095F6E4182EDCF8C35F60838B514F21 "点击放大")

   * 点击“新增组织管理员”按钮，输入用户名将用户添加为组织管理员。当成功添加组织管理员后，当前用户将自动具有组织下所有包的所有者权限。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/OmXJqZxZSpGi1U6VQtnqtw/zh-cn_image_0000002808764881.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=175FDFB9FFC0B5939DA7C0F088D0B7161E92B9666A74D5169BEE0534A8275452 "点击放大")
   * 点击"删除"组织管理员按钮，当组织管理员只有一个时，则不能被删除，一个组织必须有至少一个组织管理员。如果当前用户对组织下的包具有所有者权限，权限将被删除。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/HJCO0HjBSjeU9AgSciXUMw/zh-cn_image_0000002808884941.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=591D5AF02C2495931FE194636A02B48DCFAE259D2402736C6F247BC9DD9332EE "点击放大")
5. 点击“删除”组织按钮，如果ohpm-repo内已经有该组织的包（组件数量不为0），则不允许删除组织。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/NjvfLjsWT1mbI33i4fDbig/zh-cn_image_0000002808884957.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9698780576890AF8F5F44475F67BCBBD64F7D1A730FFA72045CF7921BA8358D "点击放大")
6. 点击搜索组织，组织搜索可以根据组织名称和组织管理员名称搜索。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/QIF4_xE7Sh6HSzSWTK7kNw/zh-cn_image_0000002779405342.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FF7FDC45B2E54919241452A2CFF17A3277E7D8E9773C311BC475F021C08C797 "点击放大")
