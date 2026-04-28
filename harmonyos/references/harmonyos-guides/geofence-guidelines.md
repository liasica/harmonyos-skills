---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geofence-guidelines
title: 端侧GNSS围栏开发指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 地理围栏开发指导 > 端侧GNSS围栏开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e6ee7d2f58050cf6c5eed5fb5830ba82c4d90ddabbf0413beef5f1a105e1d46
---

目前端侧仅支持构建圆形围栏，并且依赖GNSS芯片的地理围栏功能，仅在室外开阔区域才能准确识别用户进出围栏事件。

应用场景举例：开发者可以使用地理围栏技术，在企业周围创建一个区域围栏，当用户进入这个区域，在移动设备上进行有针对性的提醒。

## 接口说明

地理围栏所使用的接口如下，详细说明参见：[Location Kit](../harmonyos-references/js-apis-geolocationmanager.md)。

| 接口名 | 功能描述 |
| --- | --- |
| [addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise<number>](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageraddgnssgeofence12) | 添加一个GNSS地理围栏，并订阅地理围栏事件。使用Promise异步回调。 |
| [removeGnssGeofence(geofenceId: number): Promise<void>](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerremovegnssgeofence12) | 删除一个GNSS地理围栏，并取消订阅该地理围栏事件。使用Promise异步回调。 |

## 开发步骤

1. 使用地理围栏功能，需要有权限ohos.permission.APPROXIMATELY\_LOCATION，位置权限申请的方法和步骤见[申请位置权限开发指导](location-permission-guidelines.md)。
2. 导入geoLocationManager模块、wantAgent模块和BusinessError模块。

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { notificationManager } from '@kit.NotificationKit';
   ```
3. 创建围栏。

   ```
   1. // 通过WantAgentInfo的operationType设置动作类型
   2. let geofence: geoLocationManager.Geofence = {
   3. "latitude": 34.12, "longitude": 124.11, "radius": 10000.0, "expiration": 10000.0
   4. }
   ```
4. 指定APP需要监听的地理围栏事件类型，这里表示需要监听进入围栏和退出围栏事件。

   ```
   1. let transitionStatusList: Array<geoLocationManager.GeofenceTransitionEvent> = [
   2. geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_ENTER,
   3. geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_EXIT,
   4. ];
   ```
5. 创建GEOFENCE\_TRANSITION\_EVENT\_ENTER、GEOFENCE\_TRANSITION\_EVENT\_EXIT事件对应的通知对象。

   ```
   1. // GEOFENCE_TRANSITION_EVENT_ENTER事件
   2. let notificationRequest1: notificationManager.NotificationRequest = {
   3. id: 1,
   4. content: {
   5. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   6. normal: {
   7. title: "围栏通知",
   8. text: "围栏进入",
   9. additionalText: ""
   10. }
   11. }
   12. };
   13. // 创建GEOFENCE_TRANSITION_EVENT_EXIT事件对应的通知对象
   14. let notificationRequest2: notificationManager.NotificationRequest = {
   15. id: 2,
   16. content: {
   17. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
   18. normal: {
   19. title: '围栏通知',
   20. text: '围栏退出',
   21. additionalText: ""
   22. }
   23. }
   24. };
   ```
6. 添加围栏。

   ```
   1. // 把创建的通知对象存入Array中，存入顺序与transitionStatusList一致
   2. let notificationRequestList: Array<notificationManager.NotificationRequest> =
   3. [notificationRequest1, notificationRequest2];
   4. // 构造GNSS地理围栏请求对象gnssGeofenceRequest
   5. let gnssGeofenceRequest: geoLocationManager.GnssGeofenceRequest = {
   6. // 围栏属性，包含圆心和半径等信息
   7. geofence: geofence,
   8. // 指定APP需要监听的地理围栏事件类型
   9. monitorTransitionEvents: transitionStatusList,
   10. // 地理围栏事件对应的通知对象，该参数为可选
   11. notifications: notificationRequestList,
   12. // 用于监听围栏事件的callback
   13. geofenceTransitionCallback: (err : BusinessError, transition : geoLocationManager.GeofenceTransition) => {
   14. if (err) {
   15. console.error('geofenceTransitionCallback: err=' + JSON.stringify(err));
   16. }
   17. if (transition) {
   18. console.info("GeofenceTransition: %{public}s", JSON.stringify(transition));
   19. }
   20. }
   21. }
   22. try {
   23. // 添加围栏
   24. geoLocationManager.addGnssGeofence(gnssGeofenceRequest).then((id) => {
   25. // 围栏添加成功后返回围栏ID
   26. console.info("addGnssGeofence success, fence id: " + id);
   27. let fenceId = id;
   28. }).catch((err: BusinessError) => {
   29. console.error("addGnssGeofence failed, promise errCode:" + (err as BusinessError).code +
   30. ",errMessage:" + (err as BusinessError).message);
   31. });
   32. } catch(error) {
   33. console.error("addGnssGeofence failed, err:" + JSON.stringify(error));
   34. }
   ```
7. 删除围栏。

   ```
   1. // fenceId是在geoLocationManager.addGnssGeofence执行成功后获取的
   2. let fenceId = 1;
   3. try {
   4. geoLocationManager.removeGnssGeofence(fenceId).then(() => {
   5. console.info("removeGnssGeofence success fenceId:" + fenceId);
   6. }).catch((error : BusinessError) => {
   7. console.error("removeGnssGeofence: error=" + JSON.stringify(error));
   8. });
   9. } catch(error) {
   10. console.error("removeGnssGeofence: error=" + JSON.stringify(error));
   11. }
   ```
