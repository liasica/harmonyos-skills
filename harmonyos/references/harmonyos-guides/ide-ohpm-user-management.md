---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:b3c09b8654029b90ef6d1a567baf1a2e75c3d929334eb28a1462770e83df2ecc
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/eGs3bScfQJe01XpcOeN0NA/zh-cn_image_0000002808884765.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB2CBA3EEB22122E9B9DECAE4C878AC96024E5CA9777FDE89E4782ED2CB7DE64 "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ZgEiJh0qRNCSSI30wXebZQ/zh-cn_image_0000002808884771.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EC9073B8F4009E9F3EB40454F5EC80C600A0938970C7B1B8C6888817E96ECF6 "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/LSHeM7PhRdS9eio8QI9s4w/zh-cn_image_0000002779565072.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE2C3CCC64712223BF28CCF3A1D5F220005E56529FC5F418D9EA89543DD8BD13 "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/olBNPid3Rui15nw8c0ZiqQ/zh-cn_image_0000002808884745.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=7428682646C8C49779C5F871FC2A001CBB672405D86E835AE38F0D83A0F03762 "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/aLRD9ifZTZK9LLQ04q1KCQ/zh-cn_image_0000002808764677.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=A24C9E3689492028146AC4D07D7BFBA79226E241BC912E551528EDBF3B42D757 "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/gYIbYQdhTVGrzEwDVXxJ-g/zh-cn_image_0000002808884779.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=0CB22DC257DFBD39FCCEE689B338D6FED8D2CDB3AED3FB6277B942BE2556C332 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/y7UVkDvSQdOv_LDbZ3pAEQ/zh-cn_image_0000002779405142.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=33EE84574568894D94416E38A9487CC1B057E7595AE97C1E3B525525920C3DC4 "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jXFfGHz5QQ-RUYeqzHBDbg/zh-cn_image_0000002779405088.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=CFA30A22CC683076E8A5440D2D0384042A916EA604B8317DB6F20623D57C969C "点击放大")
