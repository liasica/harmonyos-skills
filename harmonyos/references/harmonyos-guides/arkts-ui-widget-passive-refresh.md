---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-passive-refresh
title: ArkTS卡片被动刷新
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > ArkTS卡片被动刷新
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:553b2d3505e9aab923c6bba65cee975626ff53c8f35eb0ce3c4f1af9e9c56233
---

本文主要提供被动刷新的开发指导，刷新流程请参考[被动刷新概述](arkts-ui-widget-interaction-overview.md#被动刷新)。

## 卡片定时刷新

当前卡片框架提供了如下两种按时间刷新卡片的方式：

* 定时刷新：表示在一定时间间隔内调用[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)的生命周期回调函数自动刷新卡片内容。可以在[form\_config.json](arkts-ui-widget-configuration.md#配置文件字段说明)配置文件的updateDuration字段中进行设置。例如，可以将updateDuration字段的值设置为2，表示刷新时间间隔为2个30分钟，即1小时。

  ```
  1. {
  2. "forms": [
  3. {
  4. "name": "UpdateDuration",
  5. "description": "$string:widget_updateduration_desc",
  6. "src": "./ets/updateduration/pages/UpdateDurationCard.ets",
  7. "uiSyntax": "arkts",
  8. "window": {
  9. "designWidth": 720,
  10. "autoDesignWidth": true
  11. },
  12. "isDefault": true,
  13. "updateEnabled": true,
  14. "scheduledUpdateTime": "10:30",
  15. "updateDuration": 2,
  16. "defaultDimension": "2*2",
  17. "supportDimensions": [
  18. "2*2"
  19. ]
  20. }
  21. ]
  22. }
  ```

  说明

  在使用定时刷新时，需要在form\_config.json配置文件中设置updateEnabled字段为true，以启用周期性刷新功能。
* 下次刷新：表示指定卡片的下一次刷新时间。可以通过调用[setFormNextRefreshTime](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidersetformnextrefreshtime)接口来实现。最短刷新时间为5分钟。例如，可以在接口调用后的5分钟内刷新卡片内容。

  ```
  1. // entry/src/main/ets/updatebytimeformability/UpdateByTimeFormAbility.ts
  2. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
  3. import { hilog } from '@kit.PerformanceAnalysisKit';
  4. import { BusinessError } from '@kit.BasicServicesKit';
  5. import { Want } from '@kit.AbilityKit';

  7. const TAG: string = 'UpdateByTimeFormAbility';
  8. const FIVE_MINUTE: number = 5;
  9. const DOMAIN_NUMBER: number = 0xFF00;

  11. export default class UpdateByTimeFormAbility extends FormExtensionAbility {
  12. onAddForm(want: Want): formBindingData.FormBindingData {
  13. // 卡片使用方创建卡片时触发，返回卡片数据绑定类
  14. let formData: Record<string, Object | string> = {};
  15. return formBindingData.createFormBindingData(formData);
  16. }

  18. // ...
  19. onFormEvent(formId: string, message: string): void {
  20. // 当卡片提供方的postCardAction接口的message事件被触发时调用
  21. hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${JSON.stringify(message)}`);
  22. try {
  23. // 设置过5分钟后更新卡片内容
  24. formProvider.setFormNextRefreshTime(formId, FIVE_MINUTE, (err: BusinessError) => {
  25. if (err) {
  26. hilog.error(DOMAIN_NUMBER, TAG,
  27. `Failed to setFormNextRefreshTime. Code: ${err.code}, message: ${err.message}`);
  28. return;
  29. } else {
  30. hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in setFormNextRefreshTiming.');
  31. }
  32. });
  33. } catch (err) {
  34. hilog.error(DOMAIN_NUMBER, TAG,
  35. `Failed to setFormNextRefreshTime. Code: ${(err as BusinessError).code},
  36. message: ${(err as BusinessError).message}`);
  37. }
  38. }

  40. onAcquireFormState(want: Want): formInfo.FormState {
  41. // 卡片使用方查询卡片状态时触发该回调，默认返回初始状态。
  42. return formInfo.FormState.READY;
  43. }

  45. }
  ```

在触发定时、下次刷新后，系统会调用FormExtensionAbility的[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)生命周期回调，在回调中，可以使用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)进行提供方刷新卡片。onUpdateForm生命周期回调的使用请参见[卡片生命周期管理](arkts-ui-widget-lifecycle.md)。

**约束限制：**

1. 定时刷新有配额限制，每张卡片每天最多通过定时方式触发刷新50次，定时刷新次数可以通过修改[卡片配置项updateDuration字段](arkts-ui-widget-configuration.md#配置文件字段说明)、或调用[setFormNextRefreshTime](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidersetformnextrefreshtime)接口两种方式进行设置，当达到50次配额后，无法通过定时方式再次触发刷新，刷新次数会在每天的0点重置。
2. 当前定时刷新使用同一个计时器进行计时，因此卡片定时刷新的第一次刷新会有最多30分钟的偏差。比如第一张卡片A（每隔半小时刷新一次）在3点20分添加成功，定时器启动并每隔半小时触发一次事件，第二张卡片B(每隔半小时刷新一次)在3点40分添加成功，在3点50分定时器事件触发时，卡片A触发定时刷新，卡片B会在下次事件（4点20分）中才会触发。
3. 定时刷新在卡片可见情况下才会触发，在卡片不可见时仅会记录刷新动作和刷新数据，待可见时统一刷新布局。
4. 如果使能了卡片代理刷新，定时刷新和下次刷新不生效。

## 卡片定点刷新

当前卡片框架提供了如下两种定点刷新卡片的方式：

* 单定点刷新：表示在每天的某个特定时间点自动刷新卡片内容。可以在form\_config.json配置文件中的scheduledUpdateTime字段中进行设置。例如，可以将刷新时间设置为每天的上午10点30分。

  ```
  1. {
  2. "forms": [
  3. {
  4. "name": "ScheduledUpdateTime",
  5. "description": "$string:widget_scheduledUpdateTime_desc",
  6. "src": "./ets/scheduledupdatetime/pages/ScheduledUpdateTimeCard.ets",
  7. "uiSyntax": "arkts",
  8. "window": {
  9. "designWidth": 720,
  10. "autoDesignWidth": true
  11. },
  12. "isDefault": true,
  13. "updateEnabled": true,
  14. "scheduledUpdateTime": "10:30",
  15. "updateDuration": 0,
  16. "defaultDimension": "2*2",
  17. "supportDimensions": [
  18. "2*2"
  19. ]
  20. }
  21. ]
  22. }
  ```
* 多定点刷新：表示在每天的多个特定时间点自动刷新卡片内容。可以在form\_config.json配置文件中的multiScheduledUpdateTime字段中进行设置，例如，可以将刷新时间设置为每天的上午11点30分和下午4点30分。

  ```
  1. {
  2. "forms": [
  3. {
  4. "name": "ScheduledUpdateTime",
  5. "description": "$string:widget_scheduledUpdateTime_desc",
  6. "src": "./ets/scheduledupdatetime/pages/ScheduledUpdateTimeCard.ets",
  7. "uiSyntax": "arkts",
  8. "window": {
  9. "designWidth": 720,
  10. "autoDesignWidth": true
  11. },
  12. "isDefault": true,
  13. "updateEnabled": true,
  14. "scheduledUpdateTime": "10:30",
  15. "multiScheduledUpdateTime": "11:30,16:30",
  16. "updateDuration": 0,
  17. "defaultDimension": "2*2",
  18. "supportDimensions": [
  19. "2*2"
  20. ]
  21. }
  22. ]
  23. }
  ```

在触发定点刷新后，系统会调用FormExtensionAbility的[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)生命周期回调，在回调中，可以使用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)进行提供方刷新卡片。onUpdateForm生命周期回调的使用请参见[卡片生命周期管理](arkts-ui-widget-lifecycle.md)。

说明

1. 当同时配置了定时刷新updateDuration和定点刷新scheduledUpdateTime时，定时刷新的优先级更高且定点刷新不会执行。如果想要配置定点刷新，则需要将updateDuration配置为0。
2. multiScheduledUpdateTime的配置最多可设置24个时间。
3. 同时配置了单定点和多定点刷新，多定点刷新配置生效，单定点刷新配置不生效。
4. 考虑到向前兼容的问题，尽量保留scheduledUpdateTime字段，不要直接删除。

**约束限制：**

1. 定点刷新在卡片可见情况下才会触发，在卡片不可见时仅会记录刷新动作和刷新数据，待可见时统一刷新布局。
