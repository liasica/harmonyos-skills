---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:20+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:04dbdca1f02c6f8d640100bc462ea0eaf68102a7fd13b3b5bcfa439e6aba8d1b
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/u3BRl6pjRZqU7-IatKsyxw/zh-cn_image_0000002808884765.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F1EA60D7AD581F9FE2DF75EA281D24FFB95289644D91EED9BD52EEFEEA7CC78 "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/RgqNjq93TAGZrGlCvo_9QA/zh-cn_image_0000002808884771.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E35AF146AB51D85DBDBBF9BA29A0E3583542DAADCCD428A4BDA5D94AD85E2933 "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/0bf7AMPSRg6bqDECcbUJMw/zh-cn_image_0000002779565072.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F8C6E8078E80DEE6B71E7153411E0774C398AE63F4BD0CA743D4F771A2E41F6 "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/5x9rh6Z5TDiAPmszqmbDqA/zh-cn_image_0000002808884745.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=E52591A2545B8763A1FDA994C292348F7501D4563DCCA05BD07C78DF4E96143E "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/JH8t-aTmTTCISkAiCSlzFQ/zh-cn_image_0000002808764677.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4358A22E8BD2D0AD30E73D3ED1644C9BEC1CEB86C06AA8094027B92A6576E5A "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/AAiYXJ08Tua206uFd9k6jA/zh-cn_image_0000002808884779.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD046000D1A6E6A4A672F7DBF6CA991AEB40E328884AA7C859B061A7244E09B5 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/e0_VWqHpQZetL0sLCOttGg/zh-cn_image_0000002779405142.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4556F8DC1AE49AA78A09276CCE55AEAB35387A08AD32B48D52D0A330863D0E0 "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Pl3UfAE_Re6rzKL0-Nl3qQ/zh-cn_image_0000002779405088.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=B78934A804692806EAB206F564B91C8B8C702AE361A1CAAD6BDA1363B0678D08 "点击放大")
