---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:41282dc72b6638f135bb3e72b92bf2080899a2065b3050ded5fa7c8715ec1c16
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/azXTNJ0ER9i8D0YLHstrTg/zh-cn_image_0000002731381195.png "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Z3Cmi1vaRla05LirWC0CYw/zh-cn_image_0000002731381539.png "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/F1Oov488T5akJpeG3hq6fg/zh-cn_image_0000002731541119.png "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/ENP4YqdvSaOEsE7p3_Nsmg/zh-cn_image_0000002731381545.png "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/B_jnyJwtTYCpjaRJ1pevjQ/zh-cn_image_0000002701661934.png "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/F3uiquw5R-C23RkVAYfW4g/zh-cn_image_0000002731381557.png "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/x14gerqYQMyPU0t1ZGyhCQ/zh-cn_image_0000002701821858.png "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/AFNtUL7dSiW1mbvYrevpgg/zh-cn_image_0000002701661958.png "点击放大")
