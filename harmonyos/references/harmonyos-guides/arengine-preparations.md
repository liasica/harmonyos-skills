---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations
title: 开发准备
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0f7801660fca9f2a5cb970ac60783b4e3474b1e7b2284d79d5c49d9a8f0a94c8
---

## 硬件要求

开发者可根据实际的开发语言，选择对应接口判断当前设备是否支持AR Engine。接口的调用参考如下方式：

ArkTS（[arViewController.isARTypeSupported](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)）：

```
1. import { arEngine, arViewController } from '@kit.AREngine';

3. let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
```

C/C++（[HMS\_AREngine\_CheckSupported](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_checksupported)）：

```
1. #include "ar/ar_engine_core.h"

3. auto ret = HMS_AREngine_CheckSupported(ARENGINE_FEATURE_TYPE_FACE);
```

若对应接口返回错误码为801或ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED，则表示AR Engine不支持当前设备。

## 环境搭建

请参考[应用开发准备](application-dev-overview.md)完成基本准备工作。

## 申请权限

在开发AR应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限，需要的权限如下表。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。

* 使用相机拍摄前，需要申请**ohos.permission.CAMERA**相机权限。
* 当需要使用加速计感知设备运动状态时，需要申请**ohos.permission.ACCELEROMETER**加速计权限。
* 当需要陀螺仪感知设备位姿信息时，需要申请**ohos.permission.GYROSCOPE**陀螺仪权限。

## 前置准备

推荐使用[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)作为页面路由，使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的[页面生命周期](arkts-navigation-navigation.md#页面生命周期)所示方法。

开发者需先创建首页，通过首页选择进入AR Engine场景。

1. 导入所需模块。

   ```
   1. import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建一个基础的页面，具体可参考[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

   ```
   1. @Entry
   2. @Component
   3. struct Selector {
   4. pageInfo: NavPathStack = new NavPathStack();

   6. build(): void {
   7. Navigation(this.pageInfo) {

   9. }
   10. .mode(NavigationMode.Stack)
   11. .hideTitleBar(true)
   12. .hideBackButton(true)
   13. .hideToolBar(true)
   14. }
   15. }
   ```
3. 创建sampleButton，封装Button及权限校验功能，使用@Builder装饰，并配置routerMap进行页面跳转。

   ```
   1. @Entry
   2. @Component
   3. struct Selector {
   4. pageInfo: NavPathStack = new NavPathStack();
   5. private hasPermission: boolean = false;
   6. @State context: Context = this.getUIContext().getHostContext() as Context;

   8. build(): void {
   9. // ...
   10. }

   12. @Builder
   13. sampleButton(sampleName: string): void {
   14. Button(sampleName, { type: ButtonType.Normal, stateEffect: true })
   15. .borderRadius(8)
   16. .width('50%')
   17. .height('5%')
   18. .onClick(async () => {
   19. if (!this.hasPermission) {
   20. this.hasPermission = await requestPermissionOnSetting(this.context);
   21. if (!this.hasPermission) {
   22. return;
   23. }
   24. }
   25. this.pageInfo.clear();
   26. this.pageInfo.pushDestinationByName(sampleName, null).catch((error: BusinessError) => {
   27. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
   28. });
   29. })
   30. }
   31. }
   ```
4. 创建requestPermissionOnSetting方法用于校验在进入AR场景时是否已经获取相机权限。

   ```
   1. struct Selector {
   2. // ...
   3. }

   5. async function requestPermissionOnSetting(context: Context): Promise<boolean> {
   6. let requestResult: boolean = false;
   7. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   8. await atManager.requestPermissionOnSetting(context, ['ohos.permission.CAMERA'])
   9. .then((data: abilityAccessCtrl.GrantStatus[]) => {
   10. console.info('data:' + JSON.stringify(data));
   11. if (data[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
   12. requestResult = true;
   13. }
   14. })
   15. .catch((err: BusinessError) => {
   16. console.error('data:' + JSON.stringify(err));
   17. })
   18. return requestResult;
   19. }
   ```
5. 在页面上创建按钮，用于进入AR场景。

   ```
   1. build(): void {
   2. Navigation(this.pageInfo) {
   3. Column() {
   4. this.sampleButton('ARWorld'); // 进入ARWorld场景
   5. }
   6. .justifyContent(FlexAlign.SpaceEvenly)
   7. .width('100%')
   8. .height('100%')
   9. }
   10. .mode(NavigationMode.Stack)
   11. .hideTitleBar(true)
   12. .hideBackButton(true)
   13. .hideToolBar(true)
   14. }
   ```
6. 在onAppear中配置应用首次启动时的权限校验方法requestPermissionOnFirstStartup。

   ```
   1. struct Selector {
   2. // ...
   3. build(): void {
   4. Navigation(this.pageInfo) {
   5. Column() {
   6. this.sampleButton('ARWorld');
   7. }
   8. .justifyContent(FlexAlign.SpaceEvenly)
   9. .width('100%')
   10. .height('100%')
   11. }
   12. .onAppear(() => {
   13. this.requestPermissionOnFirstStartup();
   14. })
   15. .mode(NavigationMode.Stack)
   16. .hideTitleBar(true)
   17. .hideBackButton(true)
   18. .hideToolBar(true)
   19. }

   21. @Builder
   22. sampleButton(sampleName: string): void {
   23. // ...
   24. }

   26. private requestPermissionOnFirstStartup(): void {
   27. abilityAccessCtrl.createAtManager()
   28. .requestPermissionsFromUser(this.context, ['ohos.permission.CAMERA'])
   29. .then((data: PermissionRequestResult) => {
   30. let grantStatus: number[] = data.authResults;
   31. if (grantStatus[0] === 0) {
   32. this.hasPermission = true;
   33. console.info('Succeeded in getting requestPermission.');
   34. } else {
   35. this.hasPermission = false;
   36. console.error('Failed to get requestPermission, user rejected.');
   37. }
   38. })
   39. .catch((err: BusinessError) => {
   40. console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}.`);
   41. })
   42. }
   43. }
   ```
