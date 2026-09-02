---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-449
title: 如何针对UI组件属性做API版本兼容性判断
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何针对UI组件属性做API版本兼容性判断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8649592876f3d47b647eadeded419a1c15766a54f267fe0b30e2430ea87fc252
---

**问题描述**

在使用了高版本才支持的UI属性后，如果在低API版本的系统上可能会运行出错，出现闪退。

**解决措施**

针对上述问题，开发者需要做低版本API适配或者兼容性判断，例如某个组件属性A是API 15新增的，但是项目的最低支持设备API版本是API 12，针对这种情况下，可以使用AttributeModifier做版本判断进行适配。

假设要使用列表List组件的backToTop属性，需要做兼容性判断的实现方案，示例代码如下：

```screen
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct ComponentAttributeCompatibilityJudgment {
  modifier: MyListModifier = new MyListModifier();

  build() {
    List() {
      // List content
    }
    .height('100%')
    .width('100%')
    .attributeModifier(this.modifier)
  }
}

class MyListModifier implements AttributeModifier<ListAttribute> {
  applyNormalAttribute(instance: ListAttribute): void {
    // Determine based on the API version information of deviceInfo
    if (deviceInfo.sdkApiVersion > 14) {
      // The property to be adapted is the backToTop attribute of the List component
      // The instance is an attribute object of the List, and its properties can be modified through the instance
      instance.backToTop(true);
    }
  }
}
```

**参考链接**

[AttributeModifier](../harmonyos-guides/arkts-user-defined-modifier.md#attributemodifier)
