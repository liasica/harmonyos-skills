---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-lifecycle
title: 管理ArkTS卡片生命周期
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 管理ArkTS卡片生命周期
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62db96961b9bfb31892cdd64ac8f7c7116f69f996f5ca50fc930e752bc93c9ce
---

创建ArkTS卡片，需实现[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期接口。

1. 在EntryFormAbility.ets中，导入相关模块。

   ```typescript
   // entry/src/main/ets/entryformability/EntryFormAbility.ts
   import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   import { Configuration, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在EntryFormAbility.ets中，实现[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期接口，其中在onAddForm的入参[want](../harmonyos-references/js-apis-app-ability-want.md)中可以通过[FormParam](../harmonyos-references/js-apis-app-form-forminfo.md#formparam)取出卡片的相关信息。

   ```typescript
   // entry/src/main/ets/entryformability/EntryFormAbility.ts
   const TAG: string = 'EntryFormAbility';
   const DOMAIN_NUMBER: number = 0xFF00;

   export default class EntryFormAbility extends FormExtensionAbility {
     onAddForm(want: Want): formBindingData.FormBindingData {
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
       hilog.info(DOMAIN_NUMBER, TAG, want.parameters?.[formInfo.FormParam.NAME_KEY] as string);
       // 卡片使用方创建卡片时触发，卡片提供方需要返回卡片数据绑定类
       let obj: Record<string, string> = {
         'title': 'titleOnAddForm',
         'detail': 'detailOnAddForm'
       };
       let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
       return formData;
     }

     onCastToNormalForm(formId: string): void {
       // 当前卡片使用方不会涉及该场景，无需实现该回调函数
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
     }

     onUpdateForm(formId: string): void {
       // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
       let obj: Record<string, string> = {
         'title': 'titleOnUpdateForm',
         'detail': 'detailOnUpdateForm'
       };
       let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
       formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
         hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
       });
     }

     onChangeFormVisibility(newStatus: Record<string, number>): void {
       // 卡片使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
     }

     onFormEvent(formId: string, message: string): void {
       // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
       hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);
       // ···
     }

     onRemoveForm(formId: string): void {
       // 删除卡片实例数据
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
       // 删除之前持久化的卡片实例数据
       // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
     }

     onConfigurationUpdate(config: Configuration) {
       // 当前formExtensionAbility存活时更新系统配置信息时触发的回调。
       // 需注意：formExtensionAbility创建后10秒内无操作将会被清理。
       hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
     }

     onAcquireFormState(want: Want): formInfo.FormState {
       // 卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态。
       return formInfo.FormState.READY;
     }
   }
   ```

**说明** 

FormExtensionAbility进程不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务，在生命周期调度完成后会继续存在10秒，若在10秒内未收到新的生命周期回调，则进程将自动退出。针对可能需要10秒以上才能完成的业务逻辑，建议[拉起主应用](arkts-ui-widget-event-overview.md)进行处理，处理完成后使用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)通知卡片进行刷新。
