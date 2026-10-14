---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/basic-services-kit-faq-0001
title: API兼容性保护判断常见问题
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 常见问题 > API兼容性保护判断常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:28+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:4f821e2b70d24029e8aa5a4d4eb97d7729a6c8180dc6532828e55f37e77d04bb
---

**Q：例如，应用某个特性使用了6.0.0(20)版本的API，那么在低版本设备（如5.0.0(17)版本）上如何做兼容性保护？**

**A**：解决措施如下：

* 基于ArkTS语言进行API接口兼容性保护

  使用[@ohos.deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)模块的distributionOSApiVersion属性来获取当前设备SDK版本，然后和目标版本进行比对。

  例如，下面的示例代码使用了6.0.0(20)版本开始支持的[HdsActionBar](../harmonyos-references/ui-design-hdsactionbar.md)组件。在6.0.0(20)及以上版本时，使用HdsActionBar组件来实现操作栏组件；在6.0.0(20)以下版本时，采用Row和Button组件的组合方式来实现。

  ```ts
  NavDestination() {
    Column() {
      // Regarding the proprietary interfaces of HarmonyOS, specifically the interfaces marked as since M.F.S(N).
      // Compatibility judgment, the value corresponding to version 6.0.0(20) is 60000,
      // which is derived from the new interface's since field 6*10000 + 0*100 + 0.
      if (deviceInfo.distributionOSApiVersion >= 60000) {
        // Component that calls the API of version 6.0.0(20)
        HdsActionBar({
          startButtons: [new ActionBarButton({
            baseIcon: $r('sys.symbol.stopwatch_fill')
          })],
          endButtons: [new ActionBarButton({
            baseIcon: $r('sys.symbol.mic_fill')
          })],
          // ...
        })
      } else {
        // Downgrading plan
        Row({ space: 25 }) {
          // ...
        }
        // ...
      }
    }
    // ...
  }
  .title($r('app.string.action_bar_scene'))
  .backgroundColor($r('app.color.common_backgroundColor'))
  ```
* 基于C++语言进行API接口兼容性保护

  使用[OH\_GetDistributionOSApiVersion()](../harmonyos-references/capi-deviceinfo-h.md#oh_getdistributionosapiversion)方法获取当前设备SDK版本，然后和目标版本进行比对。

  以Native侧的Button组件使用为例。在5.1.1（19）及以上版本时，使用[ArkUI\_ButtonType](../harmonyos-references/capi-button-h.md#arkui_buttontype)枚举的ARKUI\_BUTTON\_ROUNDED\_RECTANGLE设置Button圆角效果；在5.1.1（19）以下版本时，使用ARKUI\_BUTTON\_TYPE\_CAPSULE设置Button圆角效果。

  ```
  std::shared_ptr<ArkUIBaseNode> CreateButtonExample()
  {
      auto textNode = std::make_shared<ArkUIButtonNode>();
      textNode->SetTextContent(std::string("Hello World"));
      // ...
      // Regarding the proprietary interfaces of HarmonyOS, specifically the interfaces marked as since M.F.S(N).
      // Compatibility judgment, the value corresponding to version 5.1.1(19) is 50101,
      // which is derived from the new interface's since field 5*10000 + 1*100 + 1.
      if (OH_GetDistributionOSApiVersion() >= MIN_API_VERSION_5_1_1) {
          textNode->SetButtonType(ARKUI_BUTTON_ROUNDED_RECTANGLE);
      } else {
          textNode->SetButtonType(ARKUI_BUTTON_TYPE_CAPSULE);
      }
      return textNode;
  }
  ```

  ```
  void ArkUIButtonNode::SetButtonType(int32_t buttonType)
  {
      assert(handle_);
      ArkUI_NumberValue value[] = {{.i32 = buttonType}};
      ArkUI_AttributeItem item = {value, 1};
      nativeModule_->setAttribute(handle_, NODE_BUTTON_TYPE, &item);
  }
  ```

  参考链接：[实现多API版本兼容](https://gitcode.com/harmonyos_samples/APILevelAdapt)。
