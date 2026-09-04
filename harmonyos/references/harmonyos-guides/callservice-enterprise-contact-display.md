---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/callservice-enterprise-contact-display
title: 企业联系人信息来去电页面显示
breadcrumb: 指南 > 应用服务 > Call Service Kit（通话服务） > 企业联系人信息来去电页面显示
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:05+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:57556bad6c374402bc27e45e9934ffdc18748fade0d82c5087d61360ab2942d7
---

本功能仅供企业应用开发者接入。

## 场景介绍

来去电时，页面显示已安装企业应用的联系人信息，方便用户识别来去电人信息，快速回应，增强企业内部沟通效率。

**说明** 

来去电页面或横幅仅展示一个联系人信息，对于多个应用里存在相同联系人的情况，按照应用包名的字典序排序，展示首个查询结果。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [onQueryCallerInfo](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#onquerycallerinfo)(phoneNumber: string)：Promise<CallerInfo> | 查询联系人信息接口。 |
| [queryNumberIdentifySwitchState](../harmonyos-references/callservicekit-numberldentify.md#querynumberidentifyswitchstate) (context: Context):SwitchState | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |
| [isSupportEnterpriseNumberIdentify](../harmonyos-references/callservicekit-numberldentify.md#issupportenterprisenumberidentify)(context: Context): Promise<boolean> | 查询是否已开通企业来电显示权限。 |

## 申请接入

企业来电显示能力使用受限，如需接入，需要在AGC网站申请对应权限。

1.登录[AGC网站](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)，选择“开发与服务”。

2.在项目列表选择项目，并在应用列表下选择需要申请企业来电显示的应用。

3.进入“项目设置 > 开放能力管理”页面，点击“企业来电显示”对应的“申请”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/iu343FKTTnq9b88qHXdmoA/zh-cn_image_0000002712245096.png)

4.请根据实际业务需求在弹框中填写对应信息，完成后，点击右上角“提交”，提交后将在3个工作日内回复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/v_cWklsMRkSzuMt-DXiFIA/zh-cn_image_0000002742004045.png)

## 替换调试Profile

当企业来电显示能力申请成功后，需要重新[申请调试Profile](../app/agc-help-add-debugprofile-0000001914423102.md)。并且在DevEco Studio中替换新申请的调试Profile。

## 开发步骤

1. 在工程内创建一个[ExtensionAbility](extensionability-overview.md)类型的自定义组件并继承[CallerInfoQueryExtensionAbility](../harmonyos-references/callservicekit-callerinfoquery-extension-ability.md#callerinfoqueryextensionability)，完成onQueryCallerInfo方法的复写。

   说明：

   由于调用onQueryCallerInfo方法时，系统先创建应用的AbilityStage实例，请勿在AbilityStage中添加过于复杂耗时的逻辑，避免调用超时。

   代码示例：

   ```typescript
   import { CallerInfoQueryExtensionAbility, CallerInfo } from '@kit.CallServiceKit';

   export default class EntryCallerInfoQueryExtAbility extends CallerInfoQueryExtensionAbility {
    // 来去电时由系统通话应用主动调用该接口查询企业联系人信息
     async onQueryCallerInfo(phoneNumber: string): Promise<CallerInfo> {
       return new Promise<CallerInfo>((resolve, reject) => {
         let isSuccess = true;
         // 在此处实现根据号码查询企业联系人的业务逻辑
         if (isSuccess) {
           // 查询成功，返回结果
           resolve({
             contactName:'xxxx',
             employeeId:'xxxx',
             department:'xxxx',
             position:'xxxx'
           });
         } else {
           // 查询失败，返回错误原因
           reject('error reason');
         }
       });
     }
   }
   ```
2. 在应用配置文件module.json5中注册extensionAbilities，具体详见[module.json5配置](module-configuration-file.md)。

   配置文件示例：

   ```json
   {
       "extensionAbilities": [
         {
           "name": "EntryCallerInfoQueryExtAbility",
           "srcEntry": "./ets/callerinfoquery/EntryCallerInfoQueryExtAbility.ets",
           "type": "callerInfoQuery"
         }
       ]
   }
   ```

   * type标签需设为"callerInfoQuery"，表示该拓展类型为CallerInfoQueryExtensionAbility。
   * srcEntry标签表示上述ExtensionAbility组件所对应的代码路径。
3. 在调试设备上，前往“电话”，点击右上角的“更多”图标，前往“设置”>“陌生号码和信息识别”，或者通过[应用跳转陌生号码和信息识别页面](callservice-enterprise-app-redirection.md)，打开对应企业应用的号码识别功能开关，进行调试。
