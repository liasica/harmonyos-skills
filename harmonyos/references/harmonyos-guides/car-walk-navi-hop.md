---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-walk-navi-hop
title: 下车步行导航流转
breadcrumb: 指南 > 系统 > 硬件 > Car Kit（车服务） > 实现车机导航流转 > 下车步行导航流转
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9d839c212aa825390e08dc1c1e258cedad6e85729a36dbeb1b25ffbf7d7693a9
---

支持将车机指定的地图应用的步行导航数据流转至手机。

## 场景介绍

下车步行导航流转：用户下车前，车机地图应用导航还未结束，下车后可将车机上的导航数据流转至手机，发起步行导航。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/zMuhnnpsQaa_GuDZY0iPJg/zh-cn_image_0000002552798820.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=539D56F20D5B2B23FB5275A0FAC2569A4F27D744A2DEE31D62784E2CE53C1CC7)

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [registerSystemNavigationListener](../harmonyos-references/car-navigationinfomgr.md#registersystemnavigationlistener) | 注册监听系统导航信息和指令。 |
| [unregisterSystemNavigationListener](../harmonyos-references/car-navigationinfomgr.md#unregistersystemnavigationlistener) | 取消注册监听系统导航信息和指令。 |

## 开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8x1uwnaFQcmtZ1ZAlVsGXg/zh-cn_image_0000002583438515.png?HW-CC-KV=V1&HW-CC-Date=20260427T234434Z&HW-CC-Expire=86400&HW-CC-Sign=C4D91750AF2A4A55158781AB3FC6A227057260389FA0B4773A6353770DFCF697)

## 开发步骤

1. 能力配置。

   请参考[配置能力](car-preparations.md#配置能力)进行配置。下车步行导航流转场景下，metadata的name取值为carHopCapability，value取值应为**getOffCarNavi**。示例代码如下所示：

   ```
   1. "metadata": [
   2. {
   3. "name": "carHopCapability",
   4. "value": "getOffCarNavi"
   5. }
   6. ]
   ```
2. 导入相关模块。

   ```
   1. import { navigationInfoMgr } from '@kit.CarKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
3. 监听系统导航信息和指令。

   地图应用需要注册监听系统导航信息和指令，方便地图应用接收系统指令。用户下车后，系统会给地图应用发送START\_NAVIGATION指令，地图应用在收到指令后即可开启步行导航任务。

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
   18. if (command == navigationInfoMgr.CommandType.START_NAVIGATION) {
   19. // 地图应用处理下车后自动开启步行导航的逻辑
   20. if (args !== undefined && args !== null) {
   21. // 获取导航类型
   22. let naviType: navigationInfoMgr.NaviType = args['naviType'] as navigationInfoMgr.NaviType;
   23. // 如果是步行导航
   24. if (naviType === navigationInfoMgr.NaviType.WALKING) {
   25. let destPoi: string = args['destPoi'] as string;
   26. // 获取目的地名
   27. let destLocationName: string = args['destName'] as string;
   28. // 获取目的地纬度
   29. let destLatitude: string = destPoi?.split(',')[0].toString();
   30. // 获取目的地经度
   31. let destLongitude: string = destPoi?.split(',')[1].toString();
   32. // 开发者根据destLocationName、destLatitude、destLongitude发起步行导航
   33. // ...
   34. }
   35. }
   36. }
   37. return new Promise(resolve => {
   38. let ret: navigationInfoMgr.ResultData = {
   39. code: 1002,
   40. message: 'message test2',
   41. data: args
   42. }
   43. resolve(ret);
   44. })
   45. }
   46. }

   48. try {
   49. // 获取NavigationController实例
   50. let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
   51. // 注册监听系统导航信息和指令
   52. navInfoController.registerSystemNavigationListener(new Listener());
   53. } catch (e) {
   54. // 捕获接口调用异常时的错误码并做相应处理
   55. hilog.error(0x0000, 'testTag', `register system navigation listener, error code: ${e?.code}`);
   56. }
   ```
4. 取消监听。

   在地图应用退出时，需要取消之前注册的监听，减少手机系统不必要的资源消耗。

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
