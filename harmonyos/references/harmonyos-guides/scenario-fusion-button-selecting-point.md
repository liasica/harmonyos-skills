---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-button-selecting-point
title: 地图选点Button
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化Button > 地图选点Button
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cc60909327455a7510659d058a7bbb507b1f32f33cc295075acb4f24251cc08
---

## 场景介绍

地图选点Button功能可以帮助开发者调用Button组件拉起Map Kit的地图选点页面，用户在地图中选择位置后，位置相关信息返回Button页面。

运行示例代码单击“地图选点”按钮拉起地图选点页面。

## 约束与限制

地图选点Button支持Phone和Tablet设备，并且从5.0.1（13）版本开始，新增支持2in1设备。

## 前提条件

参见[开发准备](map-config-agc.md)。

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在容器中声明FunctionalButton，指定Button的openType，并设置对应的回调函数，代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. Row() {
   6. Column() {
   7. // 构建FunctionalButton组件实例。
   8. FunctionalButton({
   9. params: {
   10. // OpenType.CHOOSE_LOCATION表示该按钮用于在地图上选择位置。
   11. openType: functionalButtonComponentManager.OpenType.CHOOSE_LOCATION,
   12. label: '地图选点',
   13. // 调整按钮样式。
   14. styleOption: {
   15. bgColor: functionalButtonComponentManager.ColorType.DEFAULT,
   16. size: functionalButtonComponentManager.SizeType.DEFAULT,
   17. plain: false,
   18. disabled: false,
   19. loading: false,
   20. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
   21. hoverStartTime: 0,
   22. hoverStayTime: 0,
   23. styleConfig: new functionalButtonComponentManager.ButtonConfig()
   24. .fontSize(20)
   25. },
   26. },
   27. // 当OpenType设置为CHOOSE_LOCATION时，回调必须为onChooseLocation。
   28. controller: new functionalButtonComponentManager.FunctionalButtonController()
   29. .onChooseLocation((err, data) => {
   30. if (err) {
   31. // 错误日志处理。
   32. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
   33. return;
   34. }
   35. // 成功日志处理。
   36. hilog.info(0x0000, "testTag", "succeeded in choosing location");
   37. let name: string = data.name;
   38. let address: string = data.address;
   39. let longitude: number = data.longitude;
   40. let latitude: number = data.latitude;
   41. })
   42. })
   43. }
   44. .width('100%')
   45. }
   46. .height('100%')
   47. }
   48. }
   ```

   说明

   * openType参数填写"functionalButtonComponentManager.OpenType.CHOOSE\_LOCATION"指定Button为打开地图选点类型。
   * controller参数必须对应填写"new functionalButtonComponentManager.FunctionalButtonController().onChooseLocation"。
   * 可使用自定义Modifier设置按钮样式，参考[示例](../harmonyos-references/scenario-fusion-functionalbuttoncomponentmanager.md#示例一场景化button使用自定义modifier设置按钮样式)。

   其他参数请参考：[FunctionalButton（Button组件）](../harmonyos-references/scenario-fusion-functionalbutton.md)。
