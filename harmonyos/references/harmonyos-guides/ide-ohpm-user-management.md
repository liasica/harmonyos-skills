---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:77b5e76ff67ff26b91ace7a9cb6963ee3ccb6f437fbe4dd382de0a8a5f82ccc3
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/9-Z1CLMOSkylKh6RwDyNqQ/zh-cn_image_0000002808884765.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=0EE63E846036ABBED6D48A090BFA27C8866740C4FB36FC06C3CBA0AFF6CFC91C "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/lEDeCnQCRfGoqYfYVlRyBw/zh-cn_image_0000002808884771.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E86440332F9618B4B9E27A784EBD609678E760FBA12F65DAA3D3878EF3ED2808 "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ubf_BSofSxC6m4y7F7AaOQ/zh-cn_image_0000002779565072.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5DA5557BBA9D8A79FB74CB54946BAEED69A0A196583CBE4731792B752EC8BED0 "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/aW_5Kjm6QFOw2IcoWeV6wA/zh-cn_image_0000002808884745.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B368637E9F62367E63E011A69B15C8E271908AC30ACD7C030F982C89F0DF02D "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/u28pVeTXSCmhYrI_rg_LKg/zh-cn_image_0000002808764677.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B61B34D59258909BFB39CE4B2EFC16173401A4424DA50EA607B265E39B1CC801 "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/LmRqS9VlSG-D3JsKmMpiCw/zh-cn_image_0000002808884779.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=84E06CA0A4BE06FDA2139BE14B828A5A245C201A341D587B377FBF449151EEA1 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/sRcNxbp2Q1CI94FBLrjRUw/zh-cn_image_0000002779405142.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=05ED08ED2A6B2D47BFBBF31FD0C457850700753E79A09F71B22815999DBEA4D7 "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/w_Rvrq-5Q5Cenent4BwZRA/zh-cn_image_0000002779405088.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A29BD9617E2AF2520832F65616A1CDC4254DEF4D79FF5329C4592801AF480C0 "点击放大")
