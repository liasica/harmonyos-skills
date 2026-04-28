---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/device_sensor
title: 穿戴设备传感器获取
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 穿戴设备传感器获取
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62aef3aad815a7edeb24e56df54483ce145fed258186c65b849d042b9326ecf9
---

说明

人体传感器功能仅限专业研究机构使用。

手机侧应用可以通过Wear Engine获取穿戴设备上的传感器信息，并通过打开、关闭命令控制获取传感器数据。

使用传感器相关接口前，需要向手机侧用户申请获取对应权限的授权（参见[请求用户授权](request_user_authorization.md)），否则接口将调用失败。

| 传感器类型 | 申请权限 |
| --- | --- |
| ECG、PPG、HR | [HEALTH\_SENSOR](../harmonyos-references/wearengine_api.md#permission)人体传感器 |
| ACC、GYRO、MAG | [MOTION\_SENSOR](../harmonyos-references/wearengine_api.md#permission)运动传感器 |

说明

* 穿戴设备侧无对应的应用，手机侧应用也可以使用该能力获取穿戴设备传感器。
* 请确保穿戴设备和华为运动健康App处于连接状态。用户可进入App“设备”界面查看设备是否在线。开发者可调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法了解设备是否在线，如果返回列表中不包含目标设备，则提醒用户重新连接该设备。

## 获取穿戴设备的传感器列表

说明

该接口的调用需要在开发者联盟申请运动传感器权限或人体传感器（受限开放，请参考[申请接入Wear Engine服务](wearengine_apply.md)）权限并获得用户授权。

手机侧应用可以获取穿戴设备上传感器列表，并获得这些传感器的名称、ID、上报周期等参数。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getSensorClient](../harmonyos-references/wearengine_api.md#wearenginegetsensorclient)方法，获取[SensorClient](../harmonyos-references/wearengine_api.md#sensorclient)对象。
4. 调用[getSensorList](../harmonyos-references/wearengine_api.md#getsensorlist)方法，获取指定连接设备的传感器列表。

   ```
   1. // 步骤3 获取SensorClient客户端
   2. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());

   4. // 步骤4 获取指定连接设备的传感器列表
   5. sensorClient.getSensorList(targetDevice.randomId).then((sensorList) => {
   6. console.info(`Succeeded in getting sensor list, result is ${sensorList}`);
   7. }).catch((error: BusinessError) => {
   8. console.error(`Failed to get sensor list. Code is ${error.code}, message is ${error.message}`);
   9. })
   ```

## 订阅指定传感器数据上报

说明

该接口的调用需要在开发者联盟申请运动传感器权限或人体传感器权限（受限开放，请参考[申请接入Wear Engine服务](wearengine_apply.md)）并获得用户授权。

手机侧通过[getSensorList](../harmonyos-references/wearengine_api.md#getsensorlist)方法获取传感器列表后可以通过[subscribeSensor](../harmonyos-references/wearengine_api.md#subscribesensor)方法订阅指定传感器数据上报。通过[unsubscribeSensor](../harmonyos-references/wearengine_api.md#unsubscribesensor)方法可取消订阅指定传感器的数据上报。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 参见[目标设备选择](we-device-selection.md)章节，从已连接设备列表中选定需要通信的设备。
3. 参见上一小节[获取穿戴设备的传感器列表](device_sensor.md#获取穿戴设备的传感器列表)，获取设备的传感器列表信息。
4. 核对传感器列表中是否存在目标传感器。
5. 订阅或取消订阅传感器数据上报。

   ```
   1. let sensorClient: wearEngine.SensorClient = wearEngine.getSensorClient(this.getUIContext().getHostContext());
   2. let sensorList: wearEngine.Sensor[] = await sensorClient.getSensorList(targetDevice.randomId);
   3. sensorList.forEach((sensor, idx, arr) => {
   4. if (sensor.type === wearEngine.SensorType.ACCELEROMETER) {
   5. let callback = (sensorResult: wearEngine.SensorResult) => {
   6. console.info(`Succeeded in getting sensor result, result is ${sensorResult}`);
   7. }
   8. // 订阅传感器数据上报
   9. sensorClient.subscribeSensor(targetDevice.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
   10. console.info(`Succeeded in subscribing sensor data.`);
   11. }).catch((error: BusinessError) => {
   12. console.error(`Failed to subscribe sensor data. Code is ${error.code}, message is ${error.message}`);
   13. })

   15. // 取消传感器数据上报
   16. sensorClient.unsubscribeSensor(targetDevice.randomId, wearEngine.SensorType.ACCELEROMETER, callback).then(() => {
   17. console.info(`Succeeded in unsubscribing sensor data.`);
   18. }).catch((error: BusinessError) => {
   19. console.error(`Failed to unsubscribe sensor data. Code is ${error.code}, message is ${error.message}`);
   20. })
   21. }
   22. })
   ```

   说明

   * 传感器成功打开后，会根据每个传感器的上报周期，连续不断地通过[subscribeSensor](../harmonyos-references/wearengine_api.md#subscribesensor)方法入参的回调函数上报数据，数据上报时长可由开发者通过取消订阅传感器接口自行控制。每组数据都有时间戳属性，建议开发者根据时间戳进行数据对齐。不同的传感器上报的数据格式是不同的，具体可参见：[穿戴设备传感器数据格式及样例](device_sensor.md#穿戴设备传感器数据格式及样例)。
   * 传感器分为多通道传感器，如PPG、ECG，和非多通道传感器，如ACC。对于多通道传感器上报的数据，可以通过[SensorData](../harmonyos-references/wearengine_api.md#sensordata)中的channel字段来区分通道。
   * 设备连接状态断开，设备会停止传感器数据的上报，需要开发者主动订阅设备的连接状态，设备重新连接上后主动调用[subscribeSensor](../harmonyos-references/wearengine_api.md#subscribesensor)方法订阅指定传感器数据上报。

## 穿戴设备传感器数据格式及样例

说明

数据上报数量非固定，示例中给出的是通常上报结果，实际有可能根据设备原因增加或者减少数据。

| 传感器 | 支持多通道 | 采集周期（ms） | 上报周期（ms） | 数据格式 | 数据样例 |
| --- | --- | --- | --- | --- | --- |
| ACC | No | 10 | 100 | 1次上报10组，每组3个数据，分别代表x轴、y轴、z轴加速度，共30个数据。  单位：m/s^2，4096为1个重力加速度g | [34303.0, 10753.0, 54799.0, 33023.0, 15617.0, 2576.0, 33535.0, 9729.0, 5136.0, 24063.0, 6145.0, 62479.0, 23295.0, 6145.0, 58895.0, 35071.0, 9729.0, 57359.0, 46335.0, 10497.0, 53263.0, 55039.0, 4609.0, 57359.0, 42495.0, 2305.0, 60943.0, 41471.0, 64768.0, 57359.0]  **说明：** ACC、GYRO原始数据值范围为有符号Short，目前上报后的数据值范围为无符号Short，需要开发者自行进行转换。 |
| GYRO | No | 10 | 100 | 1次上报10组，每组3个数据，分别代表x轴、y轴、z轴角速度，共30个数据。  单位：70mdps/LSB | [34303.0, 10753.0, 54799.0, 33023.0, 15617.0, 2576.0, 33535.0, 9729.0, 5136.0, 24063.0, 6145.0, 62479.0, 23295.0, 6145.0, 58895.0, 35071.0, 9729.0, 57359.0, 46335.0, 10497.0, 53263.0, 55039.0, 4609.0, 57359.0, 42495.0, 2305.0, 60943.0, 41471.0, 64768.0, 57359.0] |
| HR | No | 1000 | 1000 | 1次1个数据，代表每分钟心跳次数。  单位：次/分钟 | [80.0] |
| MAG | No | 100 | 100 | 1次上报1组，每组4个数据，分别代表x轴、y轴、z轴磁场强度，最后一个数据无实际意义，无需关注。  单位：μT | [3.9310358, 21.161278, -34.467373, 0.0] |
| PPG | Yes | 10 | 100 | 三路数据（GREEN/RED/IR） 100ms上报10包数据，每包数据4个字节。 | [758457.0, 2273675.0, 2276247.0, 2278939.0, 2281102.0, 2283411.0, 2285717.0, 2288307.0, 2290863.0, 2293297.0]（一路数据） |
| ECG | Yes | 2 | 100 | 一路数据100ms上报50包数据。不区分左右手。  单位：nV | [-5020837.0, -4742510.0, -4896082.0, -4938397.0, -4796497.0, -4886598.0, -4871642.0, -4943139.0, -5209429.0, -5294787.0, -5161278.0, -5174045.0, -5588071.0, -5323970.0, -5342938.0, -5028133.0, -5094523.0, -5240070.0, -5394008.0, -5540285.0, -5655190.0, -5589895.0, -5539920.0, -5559618.0, -5623090.0, -5501618.0, -5747845.0, -5871870.0, -5814964.0, -5885002.0, -6069946.0, -5678536.0, -5839040.0, -5903971.0, -5959417.0, -6172084.0, -6263279.0, -6029455.0, -6097669.0, -6165518.0, -6174638.0, -6284072.0, -6347544.0, -6319091.0, -6085631.0, -6143631.0, -6382198.0, -6250512.0, -6396059.0, -6424512.0] |
