---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-7
title: AGC上提交审核时提示检测到当前软件包的user_grant类型权限与隐私声明不一致
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > AGC上提交审核时提示检测到当前软件包的user_grant类型权限与隐私声明不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:09086de285e9444590e926f0a0ceeae7f2fa8144e2ce623b817841d5bf31bc6f
---

## 问题现象

应用提交审核时提示：检测到当前软件包的user\_grant类型权限与隐私声明不一致，请修改后重新提交。

## 解决方案

请参考下述步骤进行排查。

1. 查看项目module.json5文件的requestPermissions标签，列出其中的隐私权限。
2. 排查是否使用了已废弃权限，例如[ohos.permission.WRITE\_MEDIA](../harmonyos-guides/permissions-for-all-user.md#ohospermissionwrite_media)权限。需要根据文档说明使用替换方案。
3. AGC平台上打开隐私协议，查看设备权限调用模块中包含的隐私协议，与步骤（1）结论对比，并修改一致。
4. 若问题没有解决，在AGC提交审核界面查看应用隐私说明模块列举的权限，与隐私协议中权限对比，并修改一致。（软件包存在部分权限通过其他包引入，没在module.json5文件中声明，需要判断是否有必要引入该包。）
5. 检测是否使用了隐私协议服务，和配置的权限是否和软件包中一致。

补充说明，若隐私政策声明中设备权限调用展开为空，通常是因为软件包中声明了user\_grant权限但隐私声明中未同步声明。建议按以下方向处理：

* 若业务确实需要对应权限（如读写日历），在发布侧隐私声明的设备权限调用中补充对应权限，并填写用途说明，用途应与module.json5中requestPermissions的reason保持一致。
* 若当前版本未实际使用该权限，从requestPermissions中移除对应权限，重新打包后再提交。
* 重新提交前，确认requestPermissions中的权限清单与隐私声明设备权限调用中的权限清单完全一致。
* 若在发布侧补充权限后设备权限调用仍为空，检查是否选择了正确的应用、包名和版本，或重新上传包后刷新隐私声明配置。

另外，针对常见的不一致场景，可按以下方式处理：

* 权限只在软件包中声明（如WRITE\_MEDIA）：优先从requestPermissions中删除。READ\_MEDIA/WRITE\_MEDIA从API Version 22起已废弃，保存/选择图片、视频、文件建议改用Picker、保存控件或新的媒体访问能力。
* 权限只在隐私政策中声明（如LOCATION\_IN\_BACKGROUND）：若应用没有后台定位功能，从隐私政策/AGC权限声明中删除；若确实需要后台定位，在module.json5中声明LOCATION\_IN\_BACKGROUND，同时补齐前台定位权限、权限申请原因、使用场景，并按后台定位要求申请定位类长时任务，参考[位置权限申请](../harmonyos-guides/location-permission-guidelines.md)。
* 检查所有模块：不只看entry，还要查feature/HSP/HAR、三方SDK等配置，确认最终打包产物里没有残留权限。
* 修改后clean/rebuild，重新上传包，并同步更新隐私政策权限清单。

## 总结

正常情况下，在架应用包体不变，设备权限也不会改变，所以在架应用不能直接修改隐私声明的权限。参照[配置隐私声明（HarmonyOS应用）-设备权限调用](../app/agc-help-privacy-policy-app-0000002282162168.md#section743894110535)模块进行相关权限的配置。
