---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-appinfo-use
title: 实现应用图标动态切换
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 图标管理服务 > 实现应用图标动态切换
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c9fc73c0628e2ec2a455d77e707d3498729785033d4ebcb66cb82c90affadcbb
---

AppGallery Kit为使用动态图标的应用客户端提供查询动态图标信息、切换动态图标、恢复默认图标功能。

说明

从版本5.0.3(15)开始，支持实现应用图标动态切换。

## 场景介绍

* 查询动态图标信息

  应用内查询可选的动态图标信息。
* 切换动态图标

  用户点击切换可选的动态图标，系统切换对应的动态图标。
* 恢复默认图标

  用于停止已选择的动态图标，系统切换默认图标。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/JdFBHtm2T-i5o-Ej3oyylA/zh-cn_image_0000002583438839.png?HW-CC-KV=V1&HW-CC-Date=20260427T234820Z&HW-CC-Expire=86400&HW-CC-Sign=F6CCC0A6E2CB4643C4439F2D2AA554552D420AC6A2167D716E66F41770969477)

### 查询动态图标信息

1. 用户查询可选的动态图标信息。
2. 调用接口queryDynamicIcons获取动态图标信息。
3. 接口返回动态图标信息给应用。
4. 应用返回结果给用户。

### 切换动态图标

1. 用户需要切换动态图标。
2. 调用接口selectDynamicIcon切换动态图标。
3. 接口返回选择结果给应用。
4. 应用返回结果给用户。

### 恢复默认图标

1. 用户需要恢复默认图标。
2. 调用接口disableDynamicIcon禁用动态图标。
3. 接口返回禁用结果给应用。
4. 应用返回结果给用户。

## 约束与限制

* 图标管理服务不支持模拟器，请使用真机调试。
* 图标管理服务支持Phone、Tablet、PC/2in1设备。并且从5.1.1(18)版本开始，新增支持Wearable设备，从5.1.1(19)版本开始，新增支持TV设备。

## 接口说明

图标管理服务提供以下接口，具体API说明详见[接口文档](../harmonyos-references/appgallery-appinfomanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [queryDynamicIcons](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerquerydynamicicons)(): Promise<[DynamicIconInfo](../harmonyos-references/appgallery-appinfomanager.md#dynamiciconinfo)[]> | 查询动态图标信息接口，用于查询动态图标信息。 |
| [selectDynamicIcon](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerselectdynamicicon)(iconId: string): Promise<void> | 切换动态图标接口，用于切换动态图标。 |
| [disableDynamicIcon](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerdisabledynamicicon)(): Promise<void> | 禁用动态图标接口，用于停止动态图标，恢复默认图标。 |

说明

从版本6.0.0(20)开始，切换动态图标接口支持返回1006800013错误码。

## 开发步骤

### 查询动态图标信息

1. 导入appInfoManager模块及相关公共模块。

   ```
   1. import { appInfoManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[queryDynamicIcons](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerquerydynamicicons)方法查询动态图标信息。

   ```
   1. try {
   2. appInfoManager.queryDynamicIcons()
   3. .then((queryResult: appInfoManager.DynamicIconInfo[]) => {
   4. hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo size = " + queryResult.length);
   5. for (let i = 0; i < queryResult.length; i++) {
   6. hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo iconUrl = " + queryResult[i]["iconUrl"] + ", iconId = " + queryResult[i]["iconId"] + ", enabled = "+queryResult[i]["enabled"]);
   7. }
   8. }).catch((error: BusinessError) => {
   9. hilog.error(0, 'TAG', "queryDynamicIcons failed, code: " + error.code + ", exception message: " + error.message);
   10. });
   11. } catch (error) {
   12. hilog.error(0, 'TAG', "queryDynamicIcons exception code: " + error.code + ", exception message: " + error.message);
   13. }
   ```

### 切换动态图标

1. 导入appInfoManager模块及相关公共模块。

   ```
   1. import { appInfoManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[selectDynamicIcon](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerselectdynamicicon)方法切换动态图标。

   ```
   1. try {
   2. let iconId: string = 'iconId';
   3. appInfoManager.selectDynamicIcon(iconId).then(() => {
   4. hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
   5. }).catch((error: BusinessError) => {
   6. hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
   7. });
   8. } catch (error) {
   9. hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
   10. }
   ```

### 恢复默认图标

1. 导入appInfoManager模块及相关公共模块。

   ```
   1. import { appInfoManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[disableDynamicIcon](../harmonyos-references/appgallery-appinfomanager.md#appinfomanagerdisabledynamicicon)方法恢复默认图标。

   ```
   1. try {
   2. appInfoManager.disableDynamicIcon().then(() => {
   3. hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
   4. }).catch((error: BusinessError) => {
   5. hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
   6. });
   7. } catch (error) {
   8. hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
   9. }
   ```
