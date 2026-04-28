---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalbutton
title: FunctionalButton（Button组件）
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > FunctionalButton（Button组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fdf9ab967d659fa842f2e01ff4c05549ee4e29235b39539e051f19b21c961a62
---

本模块提供FunctionalButton组件，为开发者提供场景化开发能力，包括：快速验证手机号、实时验证手机号、选择头像、打开授权设置页、打开App、选择收货地址、选择发票抬头、打开地图选点、实名信息校验、人脸核身、实况窗订阅、权限设置、服务动态授权码、元服务分享、反馈与投诉和获取手机号和风险等级。

FunctionalButton需要配合[functionalButtonComponentManager](scenario-fusion-functionalbuttoncomponentmanager.md)一起使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
```

## FunctionalButton

PhonePC/2in1TabletTV

场景化Button组件。

本模块提供FunctionalButton场景化Button组件，HarmonyOS应用和元服务通过集成Button组件完成相应功能。

Button组件需要[functionalButtonComponentManager](scenario-fusion-functionalbuttoncomponentmanager.md)配合一起使用，完成相应功能。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| params | functionalButtonComponentManager.[FunctionalButtonParams](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttonparams) | 是 | @Prop | FunctionalButton组件参数。 |
| controller | functionalButtonComponentManager.[FunctionalButtonController](scenario-fusion-functionalbuttoncomponentmanager.md#functionalbuttoncontroller) | 是 | - | FunctionalButton组件控制器，用来接收组件的点击事件。 |

### build

PhonePC/2in1TabletTV

build(): void

用于创建FunctionalButton对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 4.1.0(11)

**示例：**

```
1. import { FunctionalButton, functionalButtonComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Row() {
9. Column() {
10. // 构建FunctionalButton组件实例。
11. FunctionalButton({
12. params: {
13. // OpenType.GET_PHONE_NUMBER表示该按钮用于快速验证手机号码。
14. openType: functionalButtonComponentManager.OpenType.GET_PHONE_NUMBER,
15. label: '快速验证手机号',
16. // 调整按钮样式。
17. styleOption: {
18. bgColor:functionalButtonComponentManager.ColorType.DEFAULT,
19. size: functionalButtonComponentManager.SizeType.DEFAULT,
20. plain: false,
21. disabled:false,
22. loading: false,
23. hoverClass: functionalButtonComponentManager.HoverClassType.HOVER_CLASS,
24. hoverStartTime: 0,
25. hoverStayTime: 0,
26. styleConfig: new functionalButtonComponentManager.ButtonConfig()
27. .fontSize(20)
28. },
29. },
30. // 当OpenType为GET_PHONE_NUMBER时，回调必须为onGetPhoneNumber。
31. controller: new functionalButtonComponentManager.FunctionalButtonController()
32. .onGetPhoneNumber((err, data) => {
33. if (err) {
34. // 错误日志处理。
35. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
36. return;
37. }
38. // 成功日志处理。
39. hilog.info(0x0000, "testTag", "succeeded in authenticating");
40. // 获取授权码。
41. let authorizationCode = data.code;
42. })
43. })
44. }.width('100%')
45. }.height('100%')
46. }
47. }
```
