---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-system-settings
title: 系统设置
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > ohpm-repo私仓搭建工具 > 页面功能介绍 > 系统设置
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9fc338ad995f98b14edf1a4a035a7ed4b1f7cc8755f0e801571e32b6cd846198
---

系统设置是ohpm-repo系统层面的管理，当前支持"oh-package.json5检查规则"和"系统安全"两大功能。

## oh-package.json5检查规则

oh-package.json5检查规则是ohpm-repo对上传包的oh-package.json5文件进行校验的规则管理。当前主要针对category，repository和name三个字段设定规则。

**category白名单：**若其为空，系统将不会对category字段进行校验。若配置了值，则category字段的值就必须存在于白名单中。

**repository是否必填**：决定repository字段在oh-package.json5文件中是否必须存在。如果设置为是，那么在上传包时，oh-package.json5文件中就必须包含repository字段。

**name****字段是否必须包含组织名**：oh-package.json5文件中name字段是否必须包含组织名，如果设置为是，则上传包时，则name字段必须包含组织名，无组织包名将会上传失败。

页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/K09LPXd5Q6C7OPRFy4NUZg/zh-cn_image_0000002561751227.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=5410C17786C10FC96EC55CB14A92624FA17C405F5D79B7129419AD1E9B564DE7 "点击放大")

## 系统安全

系统安全页面中有两部分配置项：重置系统密钥和配置是否支持匿名访问。页面效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/c8xLTnyDTmC9BPItk55SYQ/zh-cn_image_0000002530751290.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=3BDDD8BC6D1E43825CFF5C61B038FA7CA3A56A372253FA13B720C01A0B46A54D "点击放大")

1. 重置系统密钥

   系统密钥用于重新加密ohpm-repo服务中用户上传的公钥和uplinks的网络代理口令信息。多实例部署ohpm-repo时不支持重置系统密钥。点击重置系统密钥，将出现重置提示，如果确定重置，需要点击按钮“是”，将出现密码输入框，由于重置系统密钥是敏感操作，故需要输入当前登录账户的密码进行再次认证，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/CtyecCNWQKy_RnbjjCCgxA/zh-cn_image_0000002561831211.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=477D7F1C686FD05F675981B7E2234031331746CD32B7C33DD4D07BA01A807CBE "点击放大")
2. ohpm-repo匿名访问配置

   ohpm-repo从5.0.5版本开始支持配置匿名访问功能。默认情况下，ohpm-repo支持匿名访问。如果需要配置不支持匿名访问，需要点击按钮“否”后提交，页面效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/hRhgK5l3QE2XeSliMN82og/zh-cn_image_0000002561831205.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=631C7864E1C6490B679C0B1611BA66F8B3696E8C878AFD83249F89AFBE66E9E3 "点击放大")

   * 当配置禁用匿名访问后，用户未登录状态下，不能够访问ohpm-repo管理界面首页中的包列表页面和包详情页面，只有登录后才能正常访问；首页也不能注册用户，只有登录选项。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/jgTE2TpVRKSdyHNh1zL8Vw/zh-cn_image_0000002561751233.png?HW-CC-KV=V1&HW-CC-Date=20260427T235449Z&HW-CC-Expire=86400&HW-CC-Sign=646F4D8D76AB574F7E21155E76888199FC0D080761119340D5B55C9D6935F31B "点击放大")
   * 配置禁用匿名访问后，当没有在.ohpmrc文件中正确配置AccessToken认证信息时，ohpm没有权限执行需要读权限的install，info和update命令。必须在.ohpmrc文件中正确配置读写/只读AccessToken认证信息。
   * 配置禁用匿名访问后，如果使用ohpm-repo5.0.5版本以前的[认证插件](ide-custom-auth-plugin.md)模板，必须升级认证插件内容，额外添加方法authWithReadOnly，实现只读AccessToken认证方法。
