---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/query_and_subscribe_status
title: 状态查询与订阅
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 状态查询与订阅
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df869fa7bc02f27f43507e8709710b1d18b4158ba89f3a5d4d3d26c9fbde498c
---

说明

该接口的调用需要在开发者联盟申请设备基础信息权限与穿戴用户状态权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)），穿戴用户状态权限还需获得用户授权。

* 实时查询穿戴设备可用空间、电量状态。
* 订阅穿戴设备连接状态、低电量告警、用户心率告警。
* 查询和订阅穿戴设备充电状态、佩戴状态、设备模式。

使用该接口前，需要确保应用已申请相应权限（参见[申请接入Wear Engine服务](wearengine_apply.md)）同时向手机侧用户申请获取对应权限的授权（参见[请求用户授权](request_user_authorization.md)），否则接口将调用失败。

**表1** 申请权限：设备基础信息

| 穿戴设备状态与运动健康状态 | 查询结果 | 订阅事件的触发条件 | 订阅结果 |
| --- | --- | --- | --- |
| 连接状态 | N/A | - 2：手机连接设备成功  - 3：手机与设备断开（断开蓝牙或拉远距离） | - 2：连接成功  - 3：连接断开  - 4：连接失败  - 5：设备被删除 |
| 可用空间 | 可用存储空间，单位：KB（例如：20480） | N/A | N/A |
| 电量状态 | 电量值（例如：97） | 设备电量每减少1% （例如：由98%降到97%），且设备处于非充电状态 | 电量值（例如：97） |
| 充电状态 | - 1：设备正在充电状态  - 2：设备为非充电状态  - 3：设备正在充电，且为满电状态 | - 1：给设备进行充电  - 2：设备停止充电  - 3：设备达到充满电的状态 | - 1：充电开始  - 2：充电结束  - 3：充电完成 |
| 设备模式 | - -1：设备不支持模式切换  - 0：设备处于智能模式  - 1：设备处于超长续航模式 | - 0：设备从超长续航模式切换到智能模式  - 1：设备从智能模式切换到超长续航模式 | - 0：设备处于智能模式  - 1：设备处于超长续航模式 |

**表2** 申请权限：穿戴用户状态USER\_STATUS（仅限企业开发者）

| 穿戴设备状态与运动健康状态 | 查询结果 | 订阅事件的触发条件 | 订阅结果 |
| --- | --- | --- | --- |
| 佩戴状态 | - 1：佩戴中  - 2：未佩戴 | - 1：将穿戴设备戴在手腕上  - 2：将穿戴设备由手腕摘下 | - 1：佩戴  - 2：未佩戴 |
| 心率告警 | N/A | - 1：静态心率连续10分钟高于上限值  - 2：静态心率连续10分钟低于下限值  - 3：运动心率过高  - 4：运动心率过低  备注：打开运动健康App 设备，在应用和服务列表中，点击心率，设置相应的心率提醒。 | - 1：静态心率过高  - 2：静态心率过低  - 3：运动心率过高  - 4：运动心率过低 |

说明

* 穿戴设备侧无对应的应用，手机侧应用也可以使用该能力获取穿戴设备状态。
* 在查询或订阅穿戴设备电量、充电、佩戴、心率告警状态时，请确保穿戴设备和华为运动健康App处于连接状态。用户可进入App“设备”界面查看设备是否在线。开发者可调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)或根据返回错误码了解设备是否已连接手机，如果设备未连接则提醒用户重新连接设备。
* 查询和订阅佩戴状态、心率告警时，需要申请穿戴用户状态[USER\_STATUS](../harmonyos-references/wearengine_api.md#permission)权限。

## 查询设备状态

穿戴设备的状态可以调用[MonitorClient](../harmonyos-references/wearengine_api.md#monitorclient)对象中的[queryStatus](../harmonyos-references/wearengine_api.md#querystatus)方法获取到。一次只能查询一个状态。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getMonitorClient](../harmonyos-references/wearengine_api.md#wearenginegetmonitorclient)方法，获取[MonitorClient](../harmonyos-references/wearengine_api.md#monitorclient)对象。
4. 调用[queryStatus](../harmonyos-references/wearengine_api.md#querystatus)方法，查询指定指标状态。

   * 通过[MonitorItem](../harmonyos-references/wearengine_api.md#monitoritem)对象，查询指定指标状态。目前支持查询的状态如下：
     + “电量状态”字段：POWER\_STATUS。
     + “充电状态”字段：CHARGE\_STATUS。
     + “佩戴状态”字段：WEAR\_STATUS。
     + “设备模式”字段：POWER\_MODE。
     + “可用内存”字段：AVAILABLE\_STORAGE\_SPACE
   * 通过[MonitorData](../harmonyos-references/wearengine_api.md#monitordata)对象，返回指定指标状态的查询结果。

     ```
     1. // 步骤3 获取MonitorClient对象
     2. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

     4. // 步骤4 查询指定指标状态（以佩戴状态为例）
     5. monitorClient.queryStatus(targetDevice.randomId, wearEngine.MonitorItem.WEAR_STATUS).then((result: wearEngine.MonitorData) => {
     6. // 获取到所查状态的状态值，处理对应业务逻辑
     7. console.info(`Succeeded in querying wear status, result is ${result.code}.`);
     8. }).catch((error: BusinessError) => {
     9. // 处理调用失败时捕获到的异常
     10. console.error(`Failed to query wear status. Code is ${error.code}, message is ${error.message}.`);
     11. })
     ```

## 订阅设备状态

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接的设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getMonitorClient](../harmonyos-references/wearengine_api.md#wearenginegetmonitorclient)方法，获取[MonitorClient](../harmonyos-references/wearengine_api.md#monitorclient)对象。
4. 定义订阅任务的回调对象[Callback](../harmonyos-references/js-apis-base.md#callback)。
5. 调用[subscribeEvent](../harmonyos-references/wearengine_api.md#subscribeevent)方法，订阅指定指标状态变化的订阅。

   * 通过[MonitorEvent](../harmonyos-references/wearengine_api.md#monitorevent)对象，订阅穿戴设备与运动健康状态。目前支持的订阅状态如下：
     + “设备连接状态”字段： EVENT\_CONNECTION\_STATUS\_CHANGED。
     + “电量降低状态”字段：EVENT\_BATTERY\_LEVEL\_DROPPED。
     + “充电状态”字段： EVENT\_CHARGE\_STATUS\_CHANGED。
     + “佩戴状态”字段：EVENT\_WEAR\_STATUS\_CHANGED。
     + “心率告警”字段：EVENT\_HEART\_RATE\_ALARM。
     + “设备模式”字段：EVENT\_POWER\_MODE\_CHANGED。
   * 通过[Callback](../harmonyos-references/js-apis-base.md#callback)<[MonitorEventData](../harmonyos-references/wearengine_api.md#monitoreventdata)>对象，返回设备状态的订阅结果。

   ```
   1. // 步骤3 获取MonitorClient对象
   2. let monitorClient: wearEngine.MonitorClient = wearEngine.getMonitorClient(this.getUIContext().getHostContext());

   4. // 步骤4 定义回调函数
   5. let callback = (monitorEventData: wearEngine.MonitorEventData) => {
   6. // 处理监听到状态变化后的业务逻辑
   7. console.info(`Succeeded in listening change of ${monitorEventData.event}, the new status is ${monitorEventData.data}.`)
   8. }

   10. // 步骤5 调用订阅方法
   11. monitorClient.subscribeEvent(targetDevice.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
   12. console.info(`Succeeded in subscribing wear status.`);
   13. }).catch((error: BusinessError) => {
   14. console.error(`Failed to subscribe wear status. Code is ${error.code}, message is ${error.message}.`);
   15. })
   ```
6. 调用[unsubscribeEvent](../harmonyos-references/wearengine_api.md#unsubscribeevent)方法，解除穿戴设备状态变化的订阅。（需要传入订阅时使用的回调函数对象）

   ```
   1. // 步骤6 取消订阅，取消订阅时需要传入与订阅时相同的回调函数对象才可正常取消订阅
   2. monitorClient.unsubscribeEvent(targetDevice.randomId, wearEngine.MonitorEvent.EVENT_WEAR_STATUS_CHANGED, callback).then(() => {
   3. console.info(`Succeeded in unsubscribing wear status`);
   4. }).catch((error: BusinessError) => {
   5. console.error(`Failed to unsubscribe wear status. Code is ${error.code}, message is ${error.message}.`);
   6. })
   ```
