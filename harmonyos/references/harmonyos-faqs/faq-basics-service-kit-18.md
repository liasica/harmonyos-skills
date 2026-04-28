---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-18
title: 应用使用API如何在不同系统版本设备上做兼容性保护判断（ArkTS/C++）
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 应用使用API如何在不同系统版本设备上做兼容性保护判断（ArkTS/C++）
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:08852074924ed5892a0da55e5f2ffe33dc96136b87943783bd6526e03c15c5d2
---

**问题描述**

例如，应用某个特性使用了6.0.0(20)版本的API，那么在低版本设备（如5.0.0(17)版本）上如何做兼容性保护？

**解决措施**

* 基于ArkTS语言进行API接口兼容性保护

  使用[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)模块的distributionOSApiVersion属性来获取当前设备SDK版本，然后和目标版本进行比对。

  例如，下面的示例代码使用了6.0.0(20)版本开始支持的[HdsActionBar](../harmonyos-references/ui-design-hdsactionbar.md)组件。在6.0.0(20)及以上版本时，使用HdsActionBar组件来实现操作栏组件；在6.0.0(20)以下版本时，采用Row和Button组件的组合方式来实现。

  ```
  1. NavDestination() {
  2. Column() {
  3. // Regarding the proprietary interfaces of HarmonyOS, specifically the interfaces marked as since M.F.S(N).
  4. // Compatibility judgment, the value corresponding to version 6.0.0(20) is 60000,
  5. // which is derived from the new interface's since field 6*10000 + 0*100 + 0.
  6. if (deviceInfo.distributionOSApiVersion >= 60000) {
  7. // Component that calls the API of version 6.0.0(20)
  8. HdsActionBar({
  9. startButtons: [new ActionBarButton({
  10. baseIcon: $r('sys.symbol.stopwatch_fill')
  11. })],
  12. endButtons: [new ActionBarButton({
  13. baseIcon: $r('sys.symbol.mic_fill')
  14. })],
  15. // ...
  16. })
  17. } else {
  18. // Downgrading plan
  19. Row({ space: 25 }) {
  20. // ...
  21. }
  22. // ...
  23. }
  24. }
  25. // ...
  26. }
  27. .title($r('app.string.action_bar_scene'))
  28. .backgroundColor($r('app.color.common_backgroundColor'))
  ```

  [ActionBarScene.ets](https://gitcode.com/HarmonyOS_Samples/APILevelAdapt/blob/master/entry/src/main/ets/pages/ActionBarScene.ets#L34-L118)
* 基于C++语言进行API接口兼容性保护

  使用[OH\_GetDistributionOSApiVersion()](../harmonyos-references/capi-deviceinfo-h.md#oh_getdistributionosapiversion)方法获取当前设备SDK版本，然后和目标版本进行比对。

  以Native侧的Button组件使用为例。在5.1.1（19）及以上版本时，使用[ArkUI\_ButtonType](../harmonyos-references/capi-native-type-h.md#arkui_buttontype)枚举的ARKUI\_BUTTON\_ROUNDED\_RECTANGLE设置Button圆角效果；在5.1.1（19）以下版本时，使用ARKUI\_BUTTON\_TYPE\_CAPSULE设置Button圆角效果。

  ```
  1. std::shared_ptr<ArkUIBaseNode> CreateButtonExample()
  2. {
  3. auto textNode = std::make_shared<ArkUIButtonNode>();
  4. textNode->SetTextContent(std::string("Hello World"));
  5. // ...
  6. // Regarding the proprietary interfaces of HarmonyOS, specifically the interfaces marked as since M.F.S(N).
  7. // Compatibility judgment, the value corresponding to version 5.1.1(19) is 50101,
  8. // which is derived from the new interface's since field 5*10000 + 1*100 + 1.
  9. if (OH_GetDistributionOSApiVersion() >= MIN_API_VERSION_5_1_1) {
  10. textNode->SetButtonType(ARKUI_BUTTON_ROUNDED_RECTANGLE);
  11. } else {
  12. textNode->SetButtonType(ARKUI_BUTTON_TYPE_CAPSULE);
  13. }
  14. return textNode;
  15. }
  ```

  [IntegratingWithArkts.cpp](https://gitcode.com/harmonyos_samples/APILevelAdapt/blob/master/entry/src/main/cpp/function/src/IntegratingWithArkts.cpp#L66-L85)

  ```
  1. void ArkUIButtonNode::SetButtonType(int32_t buttonType)
  2. {
  3. assert(handle_);
  4. ArkUI_NumberValue value[] = {{.i32 = buttonType}};
  5. ArkUI_AttributeItem item = {value, 1};
  6. nativeModule_->setAttribute(handle_, NODE_BUTTON_TYPE, &item);
  7. }
  ```

  [ArkUIButtonNode.cpp](https://gitcode.com/harmonyos_samples/APILevelAdapt/blob/master/entry/src/main/cpp/classdef/src/ArkUIButtonNode.cpp#L55-L61)

**参考链接**

[实现多API版本兼容](https://gitcode.com/harmonyos_samples/APILevelAdapt)
