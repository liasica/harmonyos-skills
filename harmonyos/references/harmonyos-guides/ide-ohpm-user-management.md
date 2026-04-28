---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:46+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:14c46c4664a539e8ec9e97d17f1a2ba47ef9624e896446b7c02acb89a0e1747d
---

用户管理页面可以新增用户、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/fxjmfQTGRJuAcXEBkZWFhg/zh-cn_image_0000002561751203.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=3A8867930972CAC8B422B4E06E993AA5B576CD47B5B3A3B488944CA1177F4819 "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入新增用户的用户名和密码，新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/JZ6uf948S2e6Yo4do8V6BA/zh-cn_image_0000002530911264.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=AAC39CC90974CD3C83AE4740767845568394FB0F17BB595B1025DA51B6576853 "点击放大")
2. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/a2Q9RJIqQpeaKknWhZv_dw/zh-cn_image_0000002530911262.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=E8D094601379A30ADC206331445221324257E23052681F29348E2D30350B1F44 "点击放大")
3. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/wqMQzMHLQoK-70LjBiC4CA/zh-cn_image_0000002561831181.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=1CF7CF3E56B1201639B3F48697C9B47E12C9320C0853275FC56A1FAFD60F03B6 "点击放大")
4. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框，由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/uaEhupTqSFyy78i_Kfhm7g/zh-cn_image_0000002561751201.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=57111405B79F939F1EC742CB8357E66F2DD1070DA9133864303F62157EC79245 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/syv1RnmQRQuDnHFS8Sj8OA/zh-cn_image_0000002530751274.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=6B3B7694BDE5DF7DEE5C785E64446F642447E37A1B06B1431DBBEE2EB67C85F7 "点击放大")

   5. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/X78GyMoaSGmYQ3bA_YAVkA/zh-cn_image_0000002530911260.png?HW-CC-KV=V1&HW-CC-Date=20260427T235445Z&HW-CC-Expire=86400&HW-CC-Sign=7CA39E0962A41F90AD556455F03C9BDF9E6BC1538CD2CE683D74A5EEFB1FF944 "点击放大")
