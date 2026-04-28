---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/declare-permissions-in-acl
title: 申请受限权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 申请受限权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87127d2878598ca88afcb8fef45194bf67b92a49a021ddd6b5151946f5ae6e82
---

受限开放的权限通常是不允许三方应用申请的。如果有特殊场景需要使用，请提供相关申请材料到应用市场（AppGallery Connect，简称为AGC）申请相应权限证书。

在申请前，请审视是否符合受限权限的使用场景。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合特殊场景的应用被允许申请受限权限。

注意

在应用上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如检测到应用软件包涉及获取受限权限，应用开发者需为每个受限权限项填写相应的权限说明，并上传视频说明使用场景，详情请见[发布HarmonyOS应用](../app/agc-help-release-app-guide-0000002287176372.md)。

如果应用未申请相应的权限证书，却试图在配置文件中声明此类权限，将会导致应用安装失败。

## 申请步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/4GU0-o46Q7GGa5Kc9zcrbw/zh-cn_image_0000002552958358.png?HW-CC-KV=V1&HW-CC-Date=20260427T234201Z&HW-CC-Expire=86400&HW-CC-Sign=4B0AACA305094C8BE6164E8F21AFDDD3F3E91E9BB14AEA7256FD2010ECE77E56)

针对上图中的数字标注，补充说明如下：

1. 开发者可根据[受限开放权限列表](restricted-permissions.md)，确认自己准备申请的权限，是否受限开放，仅受限开放权限需要经过应用市场审核。
2. 每个受限开放权限的介绍、可用场景及其建议方案均可参考[受限开放权限列表](restricted-permissions.md)。

   说明

   开发者**必须查询[受限开放权限列表](restricted-permissions.md)确认开发的应用是否符合使用场景，如果不符合要求，应用的上架申请将被驳回**。
3. 在应用市场（[AGC](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)）侧申请Profile文件并同步申请使用相应受限权限。

   申请的Profile文件，将用于后续的应用签名信息配置。申请Profile的操作需在应用市场（AGC）完成，详细步骤请参阅[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。

   应用因特殊场景要求使用受限开放权限，请务必在申请发布Profile“添加Profile页面”时，申请使用相应权限，否则应用将在审核时被驳回。

   注意

   * 请确保应用申请受限开放权限时提供的场景和功能信息准确。
   * 如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响您的应用上架。

   说明

   * 在调试阶段，除下述方式外，还可以通过DevEco Studio自动签名完成申请。在自动签名的过程中，将由DevEco Studio完成向AGC申请受限权限的步骤，开发者可直接使用，具体请参考[自动签名-操作步骤](ide-signing.md#section151231211105010)。
   * 在发布阶段，必须根据[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)完成受限权限的手动申请。
4. 在配置文件中[声明权限](declare-permissions.md)。
5. 通过[权限列表](restricted-permissions.md)中的“**授权方式**”字段，判断是否需要用户授权。
6. （可选）如果权限的授权方式为user\_grant（用户授权）时，还需要通过弹窗[向用户申请权限](request-user-authorization.md)。
