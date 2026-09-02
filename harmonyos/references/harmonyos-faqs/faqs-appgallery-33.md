---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-33
title: AGC审核驳回：在同意隐私政策前，应用获取了用户的个人信息
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC审核驳回：在同意隐私政策前，应用获取了用户的个人信息
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:e84a5bdf503294cbbcd71e0378f70f7c326b110cb9c311d5ada2c302a688f6b9
---

## 问题现象

应用开发完毕后提交上架，应用市场反馈“在用户同意隐私政策前，您的应用获取了用户的个人信息（xxx），不符合相关法律法规要求。修改建议：请在用户同意隐私政策后，再申请获取用户个人信息及权限。”如何解决该问题？

## 背景知识

* [应用权限管控概述](../harmonyos-guides/app-permission-mgmt-overview.md)：根据授权方式的不同，权限类型可分为以下两种：
  + [system\_grant（系统授权）](../harmonyos-guides/permissions-for-all.md)：不会涉及用户或设备的敏感权限；系统会在用户安装应用时，自动把相应权限授予给应用。
  + [user\_grant（用户授权）](../harmonyos-guides/permissions-for-all-user.md)：会涉及到用户或设备的敏感权限；需要在应用商店的详情页面，向用户展示所申请的权限。
* [选择申请权限的方式](../harmonyos-guides/determine-application-mode.md)：应用在访问数据或者执行操作时，需要评估该行为是否需要应用具备相关的权限。如果确认需要目标权限，则需要在应用安装包中申请目标权限。每一个权限的权限等级、授权方式不同，申请权限的方式也不同，开发者在申请权限前，需要先判断应用能否申请目标权限。
* [应用隐私保护](../best-practices/bpta-app-privacy-protection.md)：隐私是用户的基本权利，HarmonyOS重视用户隐私。隐私保护措施能降低个人信息滥用风险，保护用户财产和利益。
* [abilityAccessCtrl.createAtManager](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)：获取访问控制模块对象，访问控制管理。
* [requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)：用于UIAbility/UIExtensionAbility拉起弹框请求用户授权。

## 解决方案

在HarmonyOS开发中，系统和用户授权的权限需要开发者完成以下准备操作：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/D9d6VRvGRECTAdyFB7BZ8A/zh-cn_image_0000002678026887.png "点击放大")

1. **权限声明**：

   开发者需在应用的配置文件[module.json5](../harmonyos-guides/module-configuration-file.md)中声明所需的系统授权权限。

2. **隐私声明**：
   * **权限说明：** 在隐私政策中明示应用需要获取的所有权限，例如：本应用需要网络权限（ohos.permission.INTERNET）以加载在线内容。
   * **首次启动弹窗：** 应用首次运行时需通过弹窗[向用户申请授权](../harmonyos-guides/request-user-authorization.md)展示隐私政策，用户同意隐私政策前应用不应该有任何调用权限API的行为。

   若未在隐私政策中提前向用户声明用到的权限，或是声明了权限但未在用户同意后就获取信息，那将会被应用市场驳回：“在用户同意隐私政策前，您的应用获取了用户的个人信息（xxx），不符合相关法律法规要求”。
3. **动态申请权限（仅用户授权权限需要）**
   * **首次弹窗：** 系统自动弹出授权对话框，用户可选择允许或拒绝。
   * **拒绝处理：** 如果用户拒绝授权，应用将无法再次通过requestPermissionsFromUser()拉起弹框。用户需要在系统设置中手动授权。应用也可以通过调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，直接拉起权限设置弹框，引导用户授权。

     **说明** 

     需要在module.json5中配置对应权限，配置权限详细代码请见：[声明权限](../harmonyos-guides/declare-permissions.md)。

## 常见FAQ

Q：使用的是系统授权权限，而且在隐私政策中说明了权限与使用场景，用户同意前也没有提前获取数据，为什么应用市场还是驳回了：在同意隐私政策前，应用获取了用户的个人信息？

A：可以尝试在互动中心向应用市场要调用信息，确保不是审核误报。

Q：应用上架审核意见中有“登录界面，隐私政策显示默认勾选”问题，但在应用登录界面是有用户协议及服务条款弹窗，同意与否会与隐私政策的勾选关联，所以不存在默认勾选的问题。

A：由于弹窗将隐私政策的勾选遮盖，导致无法确认其默认勾选状态，可以使用以下方案进行修复：

方案一：将弹窗底部抬高，避免遮挡隐私政策的勾选。

方案二：弹窗的同意状态不与隐私政策的勾选关联，让用户手动选择隐私政策的勾选。

Q：应用审核提示OAID违规使用，未申请隐私权限的场景获取了OAID，但代码review和hilog均未发现违规使用，如何定位？

A：可以通过以下步骤排查：

1. 全局搜索：在项目代码中全局搜索getOAID、AdvertisingIdClient、APP\_TRACKING\_CONSENT等关键词，确认所有调用点。
2. 审查第三方SDK初始化：将所有第三方SDK的初始化代码，全部延迟到用户点击隐私协议"同意"按钮之后执行。
3. 模拟审核环境：在手机设置中，将应用权限全部关闭，然后在不点击隐私弹窗的情况下，直接运行应用，通过hilog观察是否有OAID相关的错误或调用日志。
4. 使用Profiler工具：使用DevEco Studio的Profiler工具，抓取应用启动时的函数调用栈，查看是否有非预期的OAID获取行为。通过以上步骤，通常可以定位到是哪个模块在用户授权前触发了OAID获取。如果排查后仍无法定位，建议提供完整的hilog日志（包含时间戳和进程ID）给技术支持，以便进一步分析。

## 总结

开发者需在配置文件中正确声明系统授权权限，并在隐私政策中透明化处理。对于低敏感权限（如网络），系统自动授予，但仍需遵循最小化原则和用户告知义务；对于高敏感权限（如位置），在低敏感权限的基础上还需要弹窗给用户进行动态权限申请。
