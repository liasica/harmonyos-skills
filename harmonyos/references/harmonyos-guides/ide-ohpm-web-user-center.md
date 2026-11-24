---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-web-user-center
title: 个人中心主页
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 个人中心主页
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:20+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2375c27b4040b4ef5bc364e3a1bee58f420486344249f364b7140a180e859583
---

个人中心主页是ohpm-repo私仓的核心管理页面，整个系统在此进行集中管理和操作，页面效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/in-Q0mVGRa2CXX3X6vt8uw/zh-cn_image_0000002779565248.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=A70AD40A92879C5EE24C797539E72881437CF7CCE710906E58F936E6004F343B "点击放大")

**区域1**：个人信息区域，显示登录用户的信息。其中有编辑、复制发布码和修改密码三个功能。

* 编辑：ohpm-repo从6.0.1版本开始，支持编辑个人的邮箱和手机号。
* 复制发布码：点击后可将用户的发布码publish\_id复制到剪贴板中。使用ohpm命令行工具发布包时，如果采用证书认证方式，必须配置发布码，其详细发布流程见：[使用命令行工具发布](ide-ohpm-repo-quickstart.md#section182904013257)。
* 修改密码：点击后可以修改用户的密码。

**注意** 

为保障账户安全，请勿使用简单或重复密码，并定期更换密码。

**区域2**：后台管理区域，显示区域4的相应菜单的操作面板。

**区域3**：登录注册区域，用户登录后将鼠标放在此区域的用户名位置会弹出功能菜单，选择退出登录即可更换账户重新登录，其他功能与区域4相同。

**区域4**：功能菜单区域，展示个人中心的用户管理、仓库管理、包权限管理、认证管理、组织管理，操作日志和系统设置七大功能，点击相应功能后会在区域2显示该功能的具体操作面板。管理员拥有全部菜单权限，普通用户拥有认证管理、包权限管理、组织管理权限。

* 管理员菜单：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/OKvIEOu6TOGVuP3-muU35Q/zh-cn_image_0000002779405262.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA505C7E832F48FAAA58BD6EF4D26A26FE5F1E0A2F119CE5FCD4572FC87B4F2E "点击放大")
* 普通用户菜单：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/gH8__j9URiiYtqqYYvqBOQ/zh-cn_image_0000002779405274.png?HW-CC-KV=V1&HW-CC-Date=20261124T044220Z&HW-CC-Expire=31536000000&HW-CC-Sign=30E6FE52F42D3CBE321550860BA7315E625197821DAE61F3B32D5F2E4CED80F6 "点击放大")
