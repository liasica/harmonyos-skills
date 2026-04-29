---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:45+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:4cb61b9562743ac593fa02f5569d550527f3ba2bf3740340af1a542ffcf165e6
---

用户管理页面可以新增用户、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/yU1jUYaKT86CMoSJwAfVLw/zh-cn_image_0000002561751203.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=FEE840785F0A741177A8CE388993BB2C187F2CB514D0E4FA01BC71E18C44E362 "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入新增用户的用户名和密码，新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/XBkSjtTkSFmpmb9q4R_DhQ/zh-cn_image_0000002530911264.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=2093083685027BD15DF4915655E5A343E36401F678C8089B77CD06A4ADD5E275 "点击放大")
2. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/1ZcmAunKSem3Dv_tM7I9eg/zh-cn_image_0000002530911262.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=765ABC46F73D653A2DB3372A9B75DF1A3CF30AB4BEB2128103C6E73506E79BE3 "点击放大")
3. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/azFdAy9vTqyfNJRyaLoeCQ/zh-cn_image_0000002561831181.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=3C9EB487AB130398F5289B82A13A93C41DF9DDDD01A34DBFF8DA448A51E86B62 "点击放大")
4. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框，由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/gfTHac_bRlGYZm6GovIJBg/zh-cn_image_0000002561751201.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=7B7826B29AA623CD4C28DEFDB122B856950853595E4F5007F8F2F8DCC941A634 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/iDGbuG9dQWqGoiPatsJfbQ/zh-cn_image_0000002530751274.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=895F6996ECBDE750CF1AF544D0C81F00561A27A07B7F882DE1E492241A778AE7 "点击放大")

   5. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/x8JGtG8oSlWTrQxqCa_h1g/zh-cn_image_0000002530911260.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=820D6E114D963922ED95E8D07EFB7F814DF7F9211A6E112A603C27989DADB41F "点击放大")
