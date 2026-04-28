---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-142
title: 如何在调用处实现接口中的方法
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在调用处实现接口中的方法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:83e2f0de108fcdd3cc769c66100dbfcc295d81fbef116a4526e2c00b48b325ed
---

示例代码如下：

```
1. // The custom interface is as follows:
2. export interface OnTrustListener {
3. OnSuccess: (data: string) => void;
4. OnError: (error: string) => void;
5. }

7. @Component
8. export struct InterfaceUse {
9. private listener: OnTrustListener = {
10. OnSuccess: (data: string) => {
11. console.info('data is:' + data);
12. },
13. OnError: (error: string) => {
14. console.info('error is:' + error);
15. }
16. };

18. build() {
19. Column() {
20. Button('click me')
21. .onClick((event: ClickEvent) => {
22. this.listener.OnSuccess('success');
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

[CallInterface.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CallInterface.ets#L21-L48)
