---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-fenceextensionability
title: @ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > @ohos.app.ability.FenceExtensionAbility (FenceExtensionAbility)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0de7fca658a9bb8f04c9bc3a3c0bee018de5d27ac0fcdbb27d2e72545f8da7d9
---

FenceExtensionAbility为开发者提供的地理围栏相关的能力，继承自ExtensionAbility。

说明

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhoneTablet

```
1. import { FenceExtensionAbility } from '@kit.LocationKit';
```

## FenceExtensionAbility

PhoneTablet

为开发者提供地理围栏相关的能力，继承自ExtensionAbility。

### 属性

PhoneTablet

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [FenceExtensionContext](js-apis-app-ability-fenceextensioncontext.md) | 否 | 否 | 围栏服务上下文。 |

### onFenceStatusChange

PhoneTablet

onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void;

接收系统通知的地理围栏事件，根据围栏事件类型和数据进行相应处理。

**系统能力**：SystemCapability.Location.Location.Geofence

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | [geoLocationManager.GeofenceTransition](js-apis-geolocationmanager.md#geofencetransition12) | 是 | 地理围栏事件信息；包含地理围栏ID和具体的地理围栏事件。 |
| additions | Record<string, string> | 是 | 附加信息 |

**示例：**

```
1. import { FenceExtensionAbility, geoLocationManager } from '@kit.LocationKit';
2. import { notificationManager } from '@kit.NotificationKit';
3. import { Want, wantAgent } from '@kit.AbilityKit';

5. export class MyFenceExtensionAbility extends FenceExtensionAbility {
6. onFenceStatusChange(transition: geoLocationManager.GeofenceTransition, additions: Record<string, string>): void {
7. // 接受围栏状态变化事件，处理业务逻辑
8. console.info(`on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}`);

10. // 可以发送围栏业务通知
11. let wantAgentInfo: wantAgent.WantAgentInfo = {
12. wants: [
13. {
14. bundleName: 'com.example.myapplication',
15. abilityName: 'EntryAbility',
16. parameters:
17. {
18. "geofenceId": transition?.geofenceId,
19. "transitionEvent": transition?.transitionEvent,
20. }
21. } as Want
22. ],
23. actionType: wantAgent.OperationType.START_ABILITY,
24. requestCode: 100
25. };
26. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentMy) => {
27. let notificationRequest: notificationManager.NotificationRequest = {
28. id: 1,
29. content: {
30. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
31. normal: {
32. title: `围栏通知`,
33. text: `on geofence transition,id:${transition.geofenceId},event:${transition.transitionEvent},additions:${JSON.stringify(additions)}`,
34. }
35. },
36. notificationSlotType: notificationManager.SlotType.SOCIAL_COMMUNICATION,
37. wantAgent: wantAgentMy
38. };
39. notificationManager.publish(notificationRequest);
40. });
41. }
42. }
```

### onDestroy

PhoneTablet

onDestroy(): void;

接收FenceExtensionAbility的销毁事件并处理，会在FenceExtensionAbility销毁前回调。

**系统能力**：SystemCapability.Location.Location.Geofence

**示例：**

```
1. import { FenceExtensionAbility } from '@kit.LocationKit';

3. class MyFenceExtensionAbility extends FenceExtensionAbility {
4. onDestroy(): void {
5. // 处理ability销毁事件
6. console.info(`on ability destroy`);
7. }
8. }
```
