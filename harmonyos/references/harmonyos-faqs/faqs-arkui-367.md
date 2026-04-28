---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-367
title: 如何获取ArkTS状态管理框架代理前的原始对象
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取ArkTS状态管理框架代理前的原始对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:90266abb7763a897ef04e365ed8915938e8d9d415f98779658bd46ce51411ada
---

使用getTarget接口获取状态管理框架代理前的原始对象。

参考示例如下：

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Observed
4. class UserInfo {
5. name: string = 'Tom';
6. }

8. @Entry
9. @Component
10. struct GetTargetDemo {
11. @State info: UserInfo = new UserInfo();

13. build() {
14. Column() {
15. Text(`info.name: ${this.info.name}`)
16. Button('Change the properties of the proxy object')
17. .onClick(() => {
18. this.info.name = 'Alice'; // The Text component can refresh
19. })
20. Button('更改原始对象的属性')
21. .onClick(() => {
22. let rawInfo: UserInfo = UIUtils.getTarget(this.info);
23. if (rawInfo) {
24. rawInfo.name = 'Bob'; // The Text component cannot be refreshed
25. }
26. })
27. }
28. }
29. }
```

[ObtainStateManagementFramework.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ObtainStateManagementFramework.ets#L21-L50)

参考链接

[getTarget接口：获取状态管理框架代理前的原始对象](../harmonyos-guides/arkts-new-gettarget.md)
