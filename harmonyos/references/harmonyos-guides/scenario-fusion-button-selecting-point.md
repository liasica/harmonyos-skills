---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-selecting-point
title: 地图选点Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 地图选点Button
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:40761cb3b1e65f4e3d4fff183933687311b92372c722bfedd0acef1f3f924cca
---

## 场景介绍

地图选点Button功能可以帮助开发者调用Button组件拉起Map Kit的地图选点页面，用户在地图中选择位置后，位置相关信息返回Button页面。

运行示例代码单击“地图选点”按钮拉起地图选点页面。

## 约束与限制

地图选点Button支持Phone和Tablet设备，并且从5.0.1(13)版本开始，新增支持PC/2in1设备。

## 前提条件

参见[开发准备](map-config-agc.md)。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```typescript
   @Entry
   @Component
   struct Index {
     build() {
       Row() {
         Column() {
           // 构建FunctionalButton组件实例。
           FunctionalButton({
             params: {
               // OpenType.CHOOSE_LOCATION表示该按钮用于在地图上选择位置。
               openType: functionalButtonComponentManager.OpenType.CHOOSE_LOCATION,
               label: '地图选点',
               // 调整按钮样式。
               styleOption: {
                 bgColor: functionalButtonComponentManager.ColorType.DEFAULT,
                 size: functionalButtonComponentManager.SizeType.DEFAULT,
                 plain: false,
                 disabled: false,
                 loading: false,
                 hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
                 hoverStartTime: 0,
                 hoverStayTime: 0,
                 styleConfig: new functionalButtonComponentManager.ButtonConfig()
                   .fontSize(20)
               }
             },
             // 当OpenType设置为CHOOSE_LOCATION时，回调必须为onChooseLocation。
             controller: new functionalButtonComponentManager.FunctionalButtonController()
               .onChooseLocation((err, data) => {
                 if (err) {
                   // 错误日志处理。
                   hilog.error(0x0000, 'testTag', 'Failed to choose location, error: %{public}d %{public}s', err.code, err.message);
                   return;
                 }
                 // 成功日志处理。
                 hilog.info(0x0000, 'testTag', 'succeeded in choosing location');
                 let name: string = data.name;
                 let address: string = data.address;
                 let longitude: number = data.longitude;
                 let latitude: number = data.latitude;
               })
           })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   **说明** 

   * openType参数填写"functionalButtonComponentManager.OpenType.CHOOSE\_LOCATION"指定Button为打开地图选点类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onChooseLocation"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
