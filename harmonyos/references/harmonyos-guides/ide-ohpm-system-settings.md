---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-system-settings
title: 系统设置
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 系统设置
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:27+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fd7ba68085dcb0e0c5de361866d94c6d842b61d549f8b8ffca8d0bf2690d92f4
---

系统设置是ohpm-repo系统层面的管理，当前支持"oh-package.json5检查规则"和"系统安全"两大功能。

## oh-package.json5检查规则

oh-package.json5检查规则是ohpm-repo对上传包的oh-package.json5文件进行校验的规则管理。当前主要针对category，repository和name三个字段设定规则。

**category白名单：**若其为空，系统将不会对category字段进行校验。若配置了值，则category字段的值就必须存在于白名单中。

**repository是否必填**：决定repository字段在oh-package.json5文件中是否必须存在。如果设置为是，那么在上传包时，oh-package.json5文件中就必须包含repository字段。

**name****字段是否必须包含组织名**：oh-package.json5文件中name字段是否必须包含组织名，如果设置为是，则上传包时，name字段必须包含组织名，无组织包名将会上传失败。

页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ojfBoXG3RkGRY9iLQMgneg/zh-cn_image_0000002808764823.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFC4E9158D4A7F35ADD32479D25F65B0A04B564EC0800F8AC4B8AC224D3A5AC2 "点击放大")

## 系统安全

系统安全页面中有两部分配置项：重置系统密钥和配置是否支持匿名访问。页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/6xkc6z1LRh-ALeSEuAdaBQ/zh-cn_image_0000002808884877.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FAB56FE44D6EFAB293BE9A786806B070DC29E205448958CEEB0E9B6A99A01E1 "点击放大")

1. 重置系统密钥

   系统密钥用于重新加密ohpm-repo服务中用户上传的公钥和uplinks的网络代理口令信息。多实例部署ohpm-repo时不支持重置系统密钥。点击重置系统密钥，将出现重置提示，如果确定重置，需要点击按钮“是”，将出现密码输入框，由于重置系统密钥是敏感操作，故需要输入当前登录账户的密码进行再次认证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/4ognsBwXQ-OhN70XWqzYDw/zh-cn_image_0000002808764785.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FD84EAFA6FFC45BBA01CE4C2936352F898591E328C37DF6BE22928D30273F32 "点击放大")
2. ohpm-repo匿名访问配置

   ohpm-repo从5.0.5版本开始，支持配置匿名访问功能。默认情况下，ohpm-repo支持匿名访问。如果需要配置不支持匿名访问，需要点击按钮“否”后提交，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/5frgfix3R3CGkRdqaNfQjQ/zh-cn_image_0000002808884909.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6E6BB269EC329D24DC0D014E988534DBFAC702A7F7794702512F69DAD0D63E8 "点击放大")

   * 当配置禁用匿名访问后，用户未登录状态下，不能够访问ohpm-repo管理界面首页中的包列表页面和包详情页面，只有登录后才能正常访问；首页也不能注册用户，只有登录选项。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/CVlCZOD4TGWyx-r_nGQL5A/zh-cn_image_0000002808764817.png?HW-CC-KV=V1&HW-CC-Date=20261128T023427Z&HW-CC-Expire=31536000000&HW-CC-Sign=29E05E4AA74F6EF46584633C045EDACC4851A4F3080B948DC402614935013EB4 "点击放大")
   * 配置禁用匿名访问后，当没有在.ohpmrc文件中正确配置AccessToken认证信息时，ohpm没有权限执行需要读权限的install，info和update命令。必须在.ohpmrc文件中正确配置读写/只读AccessToken认证信息。
   * 配置禁用匿名访问后，如果使用ohpm-repo5.0.5版本以前的[认证插件](ide-custom-auth-plugin.md)模板，必须升级认证插件内容，额外添加方法authWithReadOnly，实现只读AccessToken认证方法。
