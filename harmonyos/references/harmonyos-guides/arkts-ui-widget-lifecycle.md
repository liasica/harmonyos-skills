---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-lifecycle
title: 管理ArkTS卡片生命周期
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 管理ArkTS卡片生命周期
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:26+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:435f69d72fd0fd3683a45fc122c9a9b4211bd1263136ec53fc7d9ba861ff81a4
---

创建ArkTS卡片，需实现[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期接口。

1. 在EntryFormAbility.ets中，导入相关模块。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ts
   2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   3. import { Configuration, Want } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在EntryFormAbility.ets中，实现[FormExtensionAbility](../harmonyos-references/js-apis-app-form-formextensionability.md)生命周期接口，其中在onAddForm的入参[want](../harmonyos-references/js-apis-app-ability-want.md)中可以通过[FormParam](../harmonyos-references/js-apis-app-form-forminfo.md#formparam)取出卡片的相关信息。

   ```
   1. // entry/src/main/ets/entryformability/EntryFormAbility.ts
   2. const TAG: string = 'EntryFormAbility';
   3. const DOMAIN_NUMBER: number = 0xFF00;

   5. export default class EntryFormAbility extends FormExtensionAbility {
   6. onAddForm(want: Want): formBindingData.FormBindingData {
   7. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onAddForm');
   8. hilog.info(DOMAIN_NUMBER, TAG, want.parameters?.[formInfo.FormParam.NAME_KEY] as string);
   9. // 卡片使用方创建卡片时触发，卡片提供方需要返回卡片数据绑定类
   10. let obj: Record<string, string> = {
   11. 'title': 'titleOnAddForm',
   12. 'detail': 'detailOnAddForm'
   13. };
   14. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   15. return formData;
   16. }

   18. onCastToNormalForm(formId: string): void {
   19. // 当前卡片使用方不会涉及该场景，无需实现该回调函数
   20. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onCastToNormalForm');
   21. }

   23. onUpdateForm(formId: string): void {
   24. // 若卡片支持定时更新/定点更新/卡片使用方主动请求更新功能，则提供方需要重写该方法以支持数据更新
   25. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onUpdateForm');
   26. let obj: Record<string, string> = {
   27. 'title': 'titleOnUpdateForm',
   28. 'detail': 'detailOnUpdateForm'
   29. };
   30. let formData: formBindingData.FormBindingData = formBindingData.createFormBindingData(obj);
   31. formProvider.updateForm(formId, formData).catch((error: BusinessError) => {
   32. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] updateForm, error:' + JSON.stringify(error));
   33. });
   34. }

   36. onChangeFormVisibility(newStatus: Record<string, number>): void {
   37. // 卡片使用方发起可见或者不可见通知触发，提供方需要做相应的处理，仅系统应用生效
   38. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onChangeFormVisibility');
   39. }

   41. onFormEvent(formId: string, message: string): void {
   42. // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
   43. hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);
   44. // ···
   45. }

   47. onRemoveForm(formId: string): void {
   48. // 删除卡片实例数据
   49. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onRemoveForm');
   50. // 删除之前持久化的卡片实例数据
   51. // 此接口请根据实际情况实现，具体请参考：FormExtAbility Stage模型卡片实例
   52. }

   54. onConfigurationUpdate(config: Configuration) {
   55. // 当前formExtensionAbility存活时更新系统配置信息时触发的回调。
   56. // 需注意：formExtensionAbility创建后10秒内无操作将会被清理。
   57. hilog.info(DOMAIN_NUMBER, TAG, '[EntryFormAbility] onConfigurationUpdate:' + JSON.stringify(config));
   58. }

   60. onAcquireFormState(want: Want): formInfo.FormState {
   61. // 卡片提供方接收查询卡片状态通知接口，默认返回卡片初始状态。
   62. return formInfo.FormState.READY;
   63. }
   64. }
   ```

说明

FormExtensionAbility进程不能常驻后台，即在卡片生命周期回调函数中无法处理长时间的任务，在生命周期调度完成后会继续存在10秒，若在10秒内未收到新的生命周期回调，则进程将自动退出。针对可能需要10秒以上才能完成的业务逻辑，建议[拉起主应用](arkts-ui-widget-event-overview.md)进行处理，处理完成后使用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)通知卡片进行刷新。
