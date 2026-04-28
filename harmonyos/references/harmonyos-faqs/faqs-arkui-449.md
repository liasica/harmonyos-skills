---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-449
title: 如何针对UI组件属性做API版本兼容性判断
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何针对UI组件属性做API版本兼容性判断
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e2933e59dddaf7798409d648f188e46d42c84c48f393ac3eafb86f62863d5d97
---

**问题描述**

在使用了高版本才支持的UI属性后，如果在低API版本的系统上可能会运行出错，出现闪退。

**解决措施**

针对上述问题，开发者需要做低版本API适配或者兼容性判断，例如某个组件属性A是API 15新增的，但是项目的最低支持设备API版本是API 12，针对这种情况下，可以使用AttributeModifier做版本判断进行适配。

假设要使用列表List组件的backToTop属性，需要做兼容性判断的实现方案，示例代码如下：

```
1. import { deviceInfo } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct ComponentAttributeCompatibilityJudgment {
6. modifier: MyListModifier = new MyListModifier();

8. build() {
9. List() {
10. // List content
11. }
12. .height('100%')
13. .width('100%')
14. .attributeModifier(this.modifier)
15. }
16. }

18. class MyListModifier implements AttributeModifier<ListAttribute> {
19. applyNormalAttribute(instance: ListAttribute): void {
20. // Determine based on the API version information of deviceInfo
21. if (deviceInfo.sdkApiVersion > 14) {
22. // The property to be adapted is the backToTop attribute of the List component
23. // The instance is an attribute object of the List, and its properties can be modified through the instance
24. instance.backToTop(true);
25. }
26. }
27. }
```

[ComponentAttributeCompatibilityJudgment.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentAttributeCompatibilityJudgment.ets#L21-L48)

**参考链接**

[AttributeModifier](../harmonyos-guides/arkts-user-defined-modifier.md#attributemodifier)
