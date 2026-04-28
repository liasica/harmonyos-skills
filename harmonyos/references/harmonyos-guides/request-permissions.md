---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-permissions
title: 申请授权
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > PageAbility组件开发指导 > 申请授权
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c9629c0645fc2aef23b680f135b3ff54fcc34b18b1adaf4e385a2d1c7fc03f9
---

应用需要获取用户的隐私信息或使用系统能力时，例如获取位置信息、使用相机拍摄照片或录制视频等，需要向用户申请授权。

在开发过程中，开发者首先需要明确涉及的敏感权限，并在config.json中声明这些权限。然后在运行时通过requestPermissionsFromUser接口，以动态弹窗的方式向用户申请授权。

在config.json声明需要的权限，在module下添加"reqPermissions"，并写入对应权限。

例如申请访问日历权限：

1. 需要申请ohos.permission.DISTRIBUTED\_DATASYNC权限，配置方式请参见[声明权限](declare-permissions.md)。
2. 同时需要在应用首次启动时弹窗向用户申请授权，使用方式请参见[向用户申请授权](request-user-authorization.md)。
