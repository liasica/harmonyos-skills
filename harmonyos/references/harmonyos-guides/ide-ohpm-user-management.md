---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-user-management
title: 用户管理
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 用户管理
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:48+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:786d0b9f7a2e6cd333a13877f1d33a3025b661fc565b08fd1f8c5a616f169d69
---

用户管理页面可以新增用户、编辑用户信息、修改用户类型、重置用户密码，删除用户和搜索用户，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/1qAa61nCSBWkA2BYNWJVlA/zh-cn_image_0000002808884765.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=93DDBEBFD5BB5963A1F82E9D49940F1817EDC5B9D903910DEB17723D944B3ADE "点击放大")

1. 点击“新增”按钮，弹出新增用户面板，输入用户名（必填）、密码（必填）、邮箱（可选）和手机号（可选），新增用户首次登录将强制重置密码。填完用户信息后点击新增即可添加一个新用户，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Ok2BaBtZQ2eZBwNhLFJjXw/zh-cn_image_0000002808884771.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC8A66FDFDD819089989A9E9AB881772D751B20855EF5022072FDAD17BA2D944 "点击放大")
2. ohpm-repo从6.0.1版本开始，新增“编辑用户信息”按钮。

   点击“编辑用户信息”按钮，再点击邮箱或手机号后的勾选框后，即可编辑用户的邮箱或手机号。点击确认修改用户信息，将出现密码输入框，由于管理员修改其他用户的信息是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Qeq9fP9PRyO4uTBaq3w2XA/zh-cn_image_0000002779565072.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0B4976410197CD1DB55513A2A6B736AE1B3541C44637173D8D59E793937F739 "点击放大")
3. 点击“编辑类型”按钮，弹出编辑用户类型面板，在此面板中可以修改用户类型成管理员或用户。点击确认修改用户类型，将出现密码输入框，由于管理员修改其他用户的类型是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/AByI1SJsQa2V3YS9P--qRQ/zh-cn_image_0000002808884745.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=DCBF7412995335EE640C77D435C04D6A4E855BF08211C4CEF071F22E62A3492F "点击放大")
4. 点击“重置密码”按钮，弹出重置用户密码面板，在此面板中可以通过点击生成新密码为用户生成随机新密码，并可通过点击复制图标将新密码复制进剪贴板（只有点击**确定**按钮才会重置密码）。点击确认重置密码，将出现密码输入框，由于管理员对其他用户重置密码是敏感操作，故需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/qq9nuTZdRLaBUd1Muv5zEQ/zh-cn_image_0000002808764677.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D168CEF98895B084F251DB7FF00FCA8F37286890FCBE48E212D37CC59BE13C2 "点击放大")
5. 点击“删除”按钮，弹出删除提示，如果确定删除，需要点击按钮“是”，将出现密码输入框。由于管理员删除用户属于敏感操作，需要输入当前操作账户的密码进行再次验证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/05k1Q9LQRISlD_H1IMWPPw/zh-cn_image_0000002808884779.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=3ACB1BB419716DC9C4200F469AB0ABDF8302BA8152ED7BDD8A14D9D580B18050 "点击放大")

   当被删除的用户是某个三方包的唯一所有者时，禁止被删除。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/FiX_Aa3_TSmMhvJHDQZwOA/zh-cn_image_0000002779405142.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D4C7A87FB5B376205276A6E98F44CBCE2A6A8CB2EF07809266F01F0F1501C24 "点击放大")
6. 点击搜索框，支持指定用户类型（系统管理员/普通用户）和用户名模糊搜索，搜索页面效果如下图所示（以指定用户类型为系统管理员，用户名为admin为例）：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/5TLyvlRwREi7OTl8fAsXkA/zh-cn_image_0000002779405088.png?HW-CC-KV=V1&HW-CC-Date=20261114T004847Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8397A92B40872826F6F6C2D590CECB75AEB0479A9E59269B462AEBAB1B9A069 "点击放大")
