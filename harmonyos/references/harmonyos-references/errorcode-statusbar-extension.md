---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-statusbar-extension
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 基础功能 > Desktop Extension Kit（桌面拓展服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:36205741b70359ba5fe287e5149aead538d89c16732e10e00bbf4cfa16265186
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1010710001 图片尺寸不符合要求

**错误信息**

The size of the pixelmap exceeds the limit.

**错误描述**

调用添加图标等接口时，传入的图标图片尺寸不符合要求。

**可能原因**

未知原因

**说明** 

当前图标尺寸不做严格限制。

**处理步骤**

请更换传入的图片数据或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710002 菜单项数量超出限制

**错误信息**

The number of menu items or submenu items exceeds the limit.

**错误描述**

调用添加图标等接口时，传入的菜单项数量超出限制。

**可能原因**

* 传入的所有一级菜单项的数量超过限制上限20
* 传入的某个一级菜单项的子菜单项的数量超过上限20

**处理步骤**

请重新设置一级菜单项和二级菜单项或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710003 API调用频繁

**错误信息**

The API is being called too frequently.

**错误描述**

指定API调用频繁。

**可能原因**

addToStatusBar，removeFromStatusBar，updateStatusBarIcon，updateQuickOperationHeight，updateStatusBarMenu等方法时调用间隔小于20ms。

**处理步骤**

请注意设置API的调用间隔或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710004 无前台窗口不允许移除图标

**错误信息**

The icon cannot be deleted when no window is in the foreground.

**错误描述**

前台无应用窗口，不允许调用removeFromStatusBar移除状态栏图标。

**可能原因**

应用退后台后调用了removeFromStatusBar方法。

**处理步骤**

请注意API的调用时机或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710005 字符串长度超出阈值

**错误信息**

The string length exceeds the threshold.

**错误描述**

字串长度超出限制范围。

**可能原因**

* [StatusBarItem](statusbar-extension-manager.md#statusbaritem)中配置的hoverTips字符串长度为0或者大于128。
* 调用[updateStatusBarHoverTips](statusbar-extension-manager.md#statusbarmanagerupdatestatusbarhovertips)方法时传入的字符串长度为0或者大于128。

**处理步骤**

检查传入字符串的长度是否在取值范围中，如果无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710006 菜单项不存在

**错误信息**

Menu item not found.

**错误描述**

对不存在的菜单项进行更新。

**可能原因**

* 调用[updateStatusBarMenuItem](statusbar-extension-manager.md#statusbarmanagerupdatestatusbarmenuitem)时，若传入的item的menuCode未在状态栏的一级菜单项中预先定义，则会导致更新失败。
* 调用[updateStatusBarSubMenuItem](statusbar-extension-manager.md#statusbarmanagerupdatestatusbarsubmenuitem)时，若传入的item的menuCode未在状态栏的二级菜单项中预先定义，则会导致更新失败。

**处理步骤**

请检查待更新的一级或二级菜单项的menuCode是否与现有菜单项的menuCode一致，如果无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010710007 菜单项的menuCode不唯一

**错误信息**

The menuCode of the menu item is not unique.

**错误描述**

菜单项的menuCode不唯一。

**可能原因**

* 调用addToStatusBar时，菜单中的menuCode不唯一。
* 调用updateStatusBarMenu时，菜单中的menuCode不唯一。
* 调用updateStatusBarMenuItem时，待更新的item的子菜单的menuCode不唯一。
  + 子菜单的各menuCode在当前菜单项中不唯一。
  + 子菜单的menuCode是其他菜单项的menuCode。
  + 子菜单的menuCode在其他菜单项的子菜单中存在。

**处理步骤**

请确保所有菜单项的menuCode值保持唯一，合理配置各菜单项的menuCode值以避免冲突，如果无法解决请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1010720001 传入的一级菜单项数据不满足要求

**错误信息**

A menu item contains neither submenu nor menuAction.

**错误描述**

调用添加图标、更新菜单等接口时，传入的一级菜单项数据不满足要求。

**可能原因**

当前传入的某个一级菜单项既不包含[menuAction](statusbar-extension-manager.md#statusbarmenuitem)，也不包含[subMenu](statusbar-extension-manager.md#statusbarmenuitem)。

**处理步骤**

请排查传入的一级菜单项的参数或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210001 菜单分组数量超过限制

**错误信息**

Maximum number of categories reached.

**错误描述**

添加的分组数量超出限制。

**可能原因**

分组最大数量为3，添加的菜单分组数量超过了限制。

**处理步骤**

请重新设置菜单分组的数量或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210002 菜单分组名称重复

**错误信息**

Duplicate category name.

**错误描述**

传入的分组名称和其他分组名称重复。

**可能原因**

调用添加分组和更新分组接口时，传入的分组名称和已存在的分组名称重复。

**处理步骤**

请重新设置菜单分组的名称或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210003 未找到菜单分组

**错误信息**

Category not found.

**错误描述**

调用获取分组、更新分组、删除分组等接口时，未找到对应的菜单分组。

**可能原因**

* 没有添加菜单分组就去获取所有的菜单分组。
* 更新菜单分组时传入的分组Id有误，未找到对应的菜单分组。
* 删除菜单分组时传入的分组Id有误，未找到对应的菜单分组。
* 获取一个分组下的所有任务时传入的分组Id有误，未找到对应的菜单分组。
* 添加菜单任务时传入的分组Id有误，未找到对应的菜单分组。

**处理步骤**

请重新设置已存在的分组Id或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210004 未找到菜单任务

**错误信息**

Quick task not found.

**错误描述**

调用获取任务、更新任务、删除任务等接口时，未找到对应的菜单任务。

**可能原因**

* 删除菜单任务时传入的任务Id有误，未找到对应的菜单任务。
* 获取一个分组下的所有任务时，获取的任务数量为0。
* 更新菜单任务时传入的任务Id有误，未找到对应的菜单任务。

**处理步骤**

请重新设置已存在的任务Id或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210005 分组已经存在

**错误信息**

Group already exists.

**错误描述**

调用新增分组接口时，分组已经存在。

**可能原因**

分组已经增加过，不可重复增加。

**处理步骤**

请检查分组信息或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210006 分组未找到

**错误信息**

Group not found.

**错误描述**

调用删除分组接口时，未找到对应分组。

**可能原因**

分组信息不存在。

**处理步骤**

请检查分组信息或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210007 窗口未找到

**错误信息**

Window not found.

**错误描述**

窗口id不存在。

**可能原因**

窗口id有误。

**处理步骤**

请检查窗口id或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210008 字符串长度超出限制

**错误信息**

The string length exceeds the threshold.

**错误描述**

传入的字符串参数的长度超过限制。

**可能原因**

* 调用[addCustomCategory](desktop-quickbar-extension-manager.md#quickbarmanageraddcustomcategory)方法时传入的字符串长度大于512或者内容为空。
* 调用[updateCustomCategory](desktop-quickbar-extension-manager.md#quickbarmanagerupdatecustomcategory)方法时传入的字符串长度大于512或者内容为空。
* 调用[addQuickTask](desktop-quickbar-extension-manager.md#quickbarmanageraddquicktask)方法时传入的字符串长度大于512或者内容为空。
* 调用[updateQuickTask](desktop-quickbar-extension-manager.md#quickbarmanagerupdatequicktask)方法时传入的字符串长度大于512或者内容为空。

**处理步骤**

请重新设置字符串的内容或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210009 无效的parameter

**错误信息**

Invalid parameter.

**错误描述**

调用接口传入的参数异常。

**可能原因**

* 调用[addQuickTask](desktop-quickbar-extension-manager.md#quickbarmanageraddquicktask)方法时传入的parameters参数的数组大小超过64。
* 调用[updateQuickTask](desktop-quickbar-extension-manager.md#quickbarmanagerupdatequicktask)方法时传入的parameters参数的数组大小超过64。
* 调用[setProgressState](desktop-quickbar-extension-manager.md#quickbarmanagersetprogressstate)方法时传入的state参数范围超出[ProgressState](desktop-quickbar-extension-manager.md#progressstate)。
* 调用[setProgressValue](desktop-quickbar-extension-manager.md#quickbarmanagersetprogressvalue)方法时传入的completed小于0、total小于等于0、completed大于total。

**处理步骤**

请重新设置参数值或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210010 未在快捷栏找到应用图标

**错误信息**

Quick bar icon not found.

**错误描述**

未在快捷栏找到应用图标。

**可能原因**

应用图标未在快捷栏上显示。

**处理步骤**

请在应用图标出现在快捷栏后再调用接口或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1020210011 API接口调用太频繁

**错误信息**

The API is called too frequently.

**错误描述**

短时间内频繁调用API接口。

**可能原因**

[setQuickBarCombineIcon](desktop-quickbar-extension-manager.md#quickbarmanagersetquickbarcombineicon)，[setQuickBarLayeredIcon](desktop-quickbar-extension-manager.md#quickbarmanagersetquickbarlayeredicon)，[setProgressState](desktop-quickbar-extension-manager.md#quickbarmanagersetprogressstate)，[setProgressValue](desktop-quickbar-extension-manager.md#quickbarmanagersetprogressvalue)，[isQuickBarCapabilitySupported](desktop-quickbar-extension-manager.md#quickbarmanagerisquickbarcapabilitysupported)等接口调用间隔小于20ms。

**处理步骤**

请注意设置API的调用间隔或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
