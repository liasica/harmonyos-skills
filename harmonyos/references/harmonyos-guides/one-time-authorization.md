---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/one-time-authorization
title: 向用户申请单次授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 向用户申请单次授权
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:16+08:00
doc_updated_at: 2026-07-17
content_hash: sha256:fa38fb132901d92157008c090c70fe639391a8320d452e944d62e74d50bfdfe0
---

基于授权最小化原则，防止应用获取和滥用用户数据。针对部分应用敏感权限，在弹窗向用户申请授权时，新增“允许本次使用”的授权选项。

开发者在开发应用时，无需额外配置，仍然调用requestPermissionsFromUser()[向用户申请授权](request-user-authorization.md)。系统会根据该能力[支持的权限](one-time-authorization.md#支持范围)，弹出对应的弹窗。

授权弹窗如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/C-HEFT-tTeeOqfXDRWtMrw/zh-cn_image_0000002742123403.png)

同时，用户可以在“设置”中修改授权。修改路径：设置 > 隐私 > 权限管理 > 应用 > 目标应用 > 位置信息。

## 支持范围

当前仅支持以下权限，当应用向用户申请这些权限时，弹窗将显示“允许本次使用”的选项；在设置中修改这些权限时，系统将显示“每次询问”的选项。

* 剪贴板：["ohos.permission.READ\_PASTEBOARD"](restricted-permissions.md#ohospermissionread_pasteboard)
* 模糊位置：["ohos.permission.APPROXIMATELY\_LOCATION"](permissions-for-all-user.md#ohospermissionapproximately_location)
* 位置：["ohos.permission.LOCATION"](permissions-for-all-user.md#ohospermissionlocation)
* 后台位置：["ohos.permission.LOCATION\_IN\_BACKGROUND"](permissions-for-all-user.md#ohospermissionlocation_in_background)

## 使用限制

* 当用户点击“允许本次使用”按钮后，应用将获得临时权限。

  + 当应用切换至前台、应用展开卡片且处于当前屏幕可见即[卡片可见](arkts-ui-widget-lifecycle.md)或者[设置后台长时任务](continuous-task.md)的时候（当前仅支持定位导航长时任务），应用的临时权限会一直保持。

    其他情况下启动计时器，十秒后取消临时权限。若需再次获取，必须重新授予。
  + 当应用切换到后台，开始十秒计时，如果在计时期间，应用处于卡片可见状态或者设置了后台长时任务，计时停止。

    当卡片不再可见或长时任务结束时，再次启动十秒计时，计时结束后，取消临时授权。

    如下图样例所示，小艺建议处于卡片可见状态：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/3LUgGr6_TDi_dvzN-RieoA/zh-cn_image_0000002712244490.png)
* 当用户在权限设置中选择“每次询问”时，应用将获得模糊位置和位置临时权限。取消临时授权的操作与此相同。
