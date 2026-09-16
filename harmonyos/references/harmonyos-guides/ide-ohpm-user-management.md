---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-09-17T06:46:53+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:32bbab2081a34b671dc44854a6fb1bc506114dca27cf836d611b2fa08b22a13f
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/uVhuqaMsT2GBH8fB42pe5Q/zh-cn_image_0000002731381195.png "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fNIFoUAlQF6ZGfIF3h_iEA/zh-cn_image_0000002731381539.png "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/1WhO7XKqT4KKMJrSLJfrQw/zh-cn_image_0000002731541119.png "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/cgFlEVdSSFKCdAP4qQrfiQ/zh-cn_image_0000002731381545.png "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/tYSDHAz6TUe00jM9AnQQdw/zh-cn_image_0000002701661934.png "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/8SsNuxvcRK-kaVF8xHe7ag/zh-cn_image_0000002731381557.png "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/4HjM-B4yQs6lZxH1HGJMQg/zh-cn_image_0000002701821858.png "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/PQUZdRWdRfmpG3ALzoB5kA/zh-cn_image_0000002701661958.png "点击放大")
