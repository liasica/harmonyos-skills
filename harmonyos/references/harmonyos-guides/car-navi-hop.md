---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-navi-hop
title: 导航流转至车机
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 实现车机导航流转 > 导航流转至车机
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:395f0a3c3a6ded74e5ba136aa7a755bd6cb20990e5b0c021e7fcca145fc85187
---

## 场景介绍

导航流转至车机包含如下几个常见使用场景：

* 碰一碰导航流转：用户在手机地图的指定页面中（地图选点页面、规划路线页面、驾车导航页面），与车机中控屏指定区域碰一碰后，将手机上的导航数据流转至车机。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/RJ_RdQvBTdGVs6iId_yQlw/zh-cn_image_0000002583478467.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=3647FDFB19A27FAA59245834E90260E18A2DA8FB10EB9DA703D90A706BE4491B)
* 上车导航自动流转：用户使用手机地图应用发起驾车导航后上车，手机上的导航数据会自动流转至车机。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/s4vYEt4HSYKP1_6ewqoaMA/zh-cn_image_0000002552798818.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=6EB0EEF6FBF769CED7097D71A6A759017CACB4FB4348D67479B1591761DE22B2)
* 车内导航自动流转：用户在车内，使用手机地图应用发起驾车导航，手机上的导航数据会自动流转至车机。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/r8vo6R-nStOSYR1uNjAi5g/zh-cn_image_0000002583438513.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=EBC7971316EBA656EC9CF4902993D36739426F2ABBF59812593FF147A34C158A)

## 接口说明

导航流转至车机使用接口如下：

| 接口名 | 描述 |
| --- | --- |
| [registerSystemNavigationListener](../harmonyos-references/car-navigationinfomgr.md#registersystemnavigationlistener) | 注册监听系统导航信息和指令。 |
| [on('smartMobilityEvent')](../harmonyos-references/car-smartmobilitycommon.md#onsmartmobilityevent) | 注册智慧出行业务的事件监听。 |
| [updateNavigationStatus](../harmonyos-references/car-navigationinfomgr.md#updatenavigationstatus) | 设置导航状态，包含地图状态、导航类型、导航目的地、导航途经点、路线和主题等。 |
| [unregisterSystemNavigationListener](../harmonyos-references/car-navigationinfomgr.md#unregistersystemnavigationlistener) | 取消注册监听系统导航信息和指令。 |
| [off('smartMobilityEvent')](../harmonyos-references/car-smartmobilitycommon.md#offsmartmobilityevent) | 取消注册智慧出行业务的事件监听。 |

### SmartMobilityEvent事件名说明

SmartMobilityEvent事件名（eventName）取值如下：

| 事件名 | 描述 |
| --- | --- |
| hopSucceeded | 流转成功事件。 |

## 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/GinNdQ7GQlWTSQMaeLmoUw/zh-cn_image_0000002552958468.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=3F693744E2842BF8212DA3837A303465D3E1105043EEE2435E365C7F2BE9B5CE)

## 开发步骤

1. 能力配置。

   请参考[配置能力](car-preparations.md#配置能力)进行配置。导航流转至车机场景下，metadata的name取值为carHopCapability。对应的value值根据不同的使用场景取值如下：

   * 碰一碰导航流转场景下，value取值为**carHopNavi**。
   * 上车导航自动流转场景下，value取值为**getOnCarNavi**。
   * 车内导航自动流转场景下，value取值为**insideCarNavi**。
2. 导入相关模块。

   ```
   1. import { navigationInfoMgr, smartMobilityCommon } from '@kit.CarKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 监听系统导航信息和指令。

   从5.1.0(18)开始，新增searchPOI指令，用于搜索POI信息。

   在打开地图应用时，地图应用需要注册监听系统导航信息和指令，方便地图接收系统指令（如：停止导航）用于对应的业务逻辑处理。

   ```
   1. // 实现SystemNavigationListener接口
   2. class Listener implements navigationInfoMgr.SystemNavigationListener {
   3. // 实现onQueryNavigationInfo方法
   4. onQueryNavigationInfo(query: navigationInfoMgr.QueryType, args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
   5. // 返回导航信息给系统
   6. return new Promise(resolve => {
   7. let ret: navigationInfoMgr.ResultData = {
   8. code: 1001,
   9. message: 'message test1',
   10. data: args
   11. }
   12. resolve(ret);
   13. })
   14. }

   16. // 实现onReceiveNavigationCmd方法
   17. onReceiveNavigationCmd(command: navigationInfoMgr.CommandType, args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
   18. // 接收并处理系统导航指令
   19. return new Promise(resolve => {
   20. let ret: navigationInfoMgr.ResultData = {
   21. code: 1002,
   22. message: 'message test2',
   23. data: args
   24. }
   25. resolve(ret);
   26. })
   27. }
   28. }

   30. try {
   31. // 获取NavigationController实例
   32. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   33. // 注册监听系统导航信息和指令
   34. navInfoController.registerSystemNavigationListener(new Listener());
   35. } catch (e) {
   36. // 捕获接口调用异常时的错误码并做相应处理
   37. hilog.error(0x0000, 'testTag', `register system navigation listener error, error code: ${e?.code}`);
   38. }
   ```
4. （可选）监听智慧出行业务事件。

   地图应用在监听系统导航信息和指令的同时，还可以注册智慧出行业务的事件监听，方便地图应用接收智慧出行业务发送的事件通知（如：流转成功事件），用于对应的业务逻辑处理。

   ```
   1. // 智慧出行业务的事件回调函数
   2. const callBack = (event: smartMobilityCommon.SmartMobilityEvent) => {
   3. hilog.info(0x0000, 'testTag', 'Received smart mobility event: ', JSON.stringify(event));
   4. if (event.eventName === 'hopSucceeded' && event.type === smartMobilityCommon.SmartMobilityType.CAR_HOP) {
   5. // 地图应用处理流转成功事件（如退出导航等）
   6. // ...
   7. }
   8. };

   10. try {
   11. // 业务类型
   12. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
   13. // 获取SmartMobilityAwareness实例
   14. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
   15. // 注册智慧出行业务的事件监听
   16. awareness.on('smartMobilityEvent', types, callBack);
   17. } catch (e) {
   18. // 捕获接口调用异常时的错误码并做相应处理
   19. hilog.error(0x0000, 'testTag', `register smart mobility event listener error, error code: ${e?.code}`);
   20. }
   ```
5. 设置系统导航状态。

   用户在地图上每次选择目的地、途经点或者变更导航信息时，地图应用都需要设置导航状态，将当前最新的导航状态保存到Car Kit中，系统会将最新的导航状态数据流转到车机上。

   ```
   1. // 设置目的地
   2. let location: navigationInfoMgr.Location = {
   3. name: 'location',
   4. coordType: navigationInfoMgr.LocationCoordType.GCJ02,
   5. longitude: 0.000000000000001,
   6. latitude: 1.000000000000001,
   7. altitude: 2.000000000000001,
   8. };
   9. // 设置途经点（可选）
   10. let passPoint0: navigationInfoMgr.Location = {
   11. name: 'passPoint0',
   12. coordType: navigationInfoMgr.LocationCoordType.GCJ02,
   13. longitude: 29.53851890563965,
   14. latitude: 16.50643920898438,
   15. altitude: 3.00015949516846,
   16. };
   17. let passPoint1: navigationInfoMgr.Location = {
   18. name: 'passPoint1',
   19. coordType: navigationInfoMgr.LocationCoordType.WGS84,
   20. longitude: 4.4445874651238,
   21. latitude: 5.55565329843751,
   22. altitude: 6.66641578943265,
   23. };
   24. // 设置导航状态属性
   25. let navigationStatus: navigationInfoMgr.NavigationStatus = {
   26. status: navigationInfoMgr.MapStatus.NAVIGATION,
   27. naviType: navigationInfoMgr.NaviType.DRIVING,
   28. destLocation: location,
   29. passPoint: [passPoint0, passPoint1],
   30. routeIndex: 101,
   31. customData: "customData",
   32. routePreference: [
   33. navigationInfoMgr.RoutePreference.TIME_FIRST,
   34. navigationInfoMgr.RoutePreference.MAIN_ROAD_FIRST
   35. ],
   36. theme: navigationInfoMgr.ThemeType.LIGHT
   37. };

   39. try {
   40. // 获取 NavigationController
   41. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   42. navInfoController.updateNavigationStatus(navigationStatus);
   43. } catch (e) {
   44. // 捕获接口调用异常时的错误码并做相应处理
   45. hilog.error(0x0000, 'testTag', `update navigation status error, error code: ${e?.code}`);
   46. }
   ```
6. 取消监听。

   在地图应用退出时，需要取消之前注册的监听，减少系统不必要的资源消耗。

   取消注册监听系统导航信息和指令：

   ```
   1. try {
   2. // 获取NavigationController实例
   3. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   4. // 取消注册监听系统导航信息和指令
   5. navInfoController.unregisterSystemNavigationListener();
   6. } catch (e) {
   7. // 捕获接口调用异常时的错误码并做相应处理
   8. hilog.error(0x0000, 'testTag', `unregister system navigation listener error, error code: ${e?.code}`);
   9. }
   ```

   取消注册智慧出行业务的事件监听，可以选择下面2种方法中的一种：

   **方法1**：**不传入callback（可选参数），会取消该type下的所有监听。**

   示例代码：

   ```
   1. try {
   2. // 业务类型
   3. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
   4. // 获取SmartMobilityAwareness实例
   5. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
   6. // 解注册智慧出行业务的事件监听
   7. awareness.off('smartMobilityEvent', types);
   8. } catch (e) {
   9. // 捕获接口调用异常时的错误码并做相应处理
   10. hilog.error(0x0000, 'testTag', `unregister smart mobility event listener error, error code: ${e?.code}`);
   11. }
   ```

   **方法2：传入callback（可选参数），会取消指定的监听。**

   示例代码：

   ```
   1. try {
   2. // 业务类型
   3. let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.CAR_HOP];
   4. // 获取SmartMobilityAwareness实例
   5. let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
   6. // 解注册智慧出行业务的事件监听，callback为步骤4中定义的callback
   7. awareness.off('smartMobilityEvent', types, callBack);
   8. } catch (e) {
   9. // 捕获接口调用异常时的错误码并做相应处理
   10. hilog.error(0x0000, 'testTag', `unregister smart mobility event listener error, error code: ${e?.code}`);
   11. }
   ```
