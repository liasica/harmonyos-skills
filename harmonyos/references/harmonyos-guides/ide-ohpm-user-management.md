---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:45+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:a5fcd0e29c4c4a19dc845c9bb7a792b24a2bb410a4f65427c6dc80e7dcb0378e
---

用户管理页面可以新增用户、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/yU1jUYaKT86CMoSJwAfVLw/zh-cn_image_0000002561751203.png "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入新增用户的用户名和密码，新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/XBkSjtTkSFmpmb9q4R_DhQ/zh-cn_image_0000002530911264.png "点击放大")
2. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/1ZcmAunKSem3Dv_tM7I9eg/zh-cn_image_0000002530911262.png "点击放大")
3. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/azFdAy9vTqyfNJRyaLoeCQ/zh-cn_image_0000002561831181.png "点击放大")
4. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框，由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/gfTHac_bRlGYZm6GovIJBg/zh-cn_image_0000002561751201.png "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/iDGbuG9dQWqGoiPatsJfbQ/zh-cn_image_0000002530751274.png "点击放大")

   5. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/x8JGtG8oSlWTrQxqCa_h1g/zh-cn_image_0000002530911260.png "点击放大")
