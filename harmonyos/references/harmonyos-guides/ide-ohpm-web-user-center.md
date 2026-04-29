---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-web-user-center
title: 个人中心主页
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 个人中心主页
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:44+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:05ee3fa44fcfe96eb88ec29d55161f2db1f8395e808d9aa4fc79308d42135bd8
---

个人中心主页是ohpm-repo私仓的核心管理页面，整个系统在此进行集中管理和操作，页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/6bYD8a0cQd2viTStzXowYw/zh-cn_image_0000002530751308.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=453975799E325ECB1A1E1F191C2F5AC9F8A645114AD292C28B05E14312160393 "点击放大")

* 区域1：个人信息区域，显示登录用户的信息。其中有复制发布码和修改密码两个功能。
  + 复制发布码：点击后可将用户的发布码publish\_id复制到剪贴板中。使用ohpm命令行工具发布包时，如果采用证书认证方式，必须配置发布码，其详细发布流程见：[使用命令行工具发布](ide-ohpm-repo-quickstart.md#zh-cn_topic_0000001792256157_使用命令行工具发布)。
  + 修改密码：点击后可以修改用户的密码。

  注意

  为保障账户安全，请勿使用简单或重复密码，并定期更换密码。
* 区域2：后台管理区域，显示区域4的相应菜单的操作面板。
* 区域3：登录注册区域，用户登录后将鼠标放在此区域的用户名位置会弹出功能菜单，选择退出登录即可更换账户重新登录，其他功能同区域4。
* 区域4：功能菜单区域，展示个人中心的用户管理、仓库管理、包权限管理、认证管理、组织管理，操作日志和系统设置七大功能，点击相应功能后会在区域2显示该功能的具体操作面板。管理员拥有全部菜单权限，普通用户只拥有认证管理、包权限管理、组织管理权限。
  + 管理员菜单：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/aXtRhwGtTaCBwVZC5ShBng/zh-cn_image_0000002561751251.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=E4F6F135876731C89B3AAB35F332E877EB9DEB017943C64A284C4DCC8C150067 "点击放大")
  + 普通用户菜单：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/6A7w1XbGSQuqkQDn22C1cA/zh-cn_image_0000002561831229.png?HW-CC-KV=V1&HW-CC-Date=20260429T054443Z&HW-CC-Expire=86400&HW-CC-Sign=A2722D72B6574CBFE2B775A52FABAF90B22D9061E217FEAD28C887B5939880F9 "点击放大")
