---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-113
title: 如何在ArkTS使用Reflect正确绑定this指针
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在ArkTS使用Reflect正确绑定this指针
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:14+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:0e45d9cf28d619f64c42f0756d3da45b60a8fe30082df03a120bbd28b290ebab
---

参考以下示例代码，注意只有对象的get/set方法才能绑定this指针。

```
1. class ReflectClass {
2. private a = 'a';

4. get getA() {
5. return () => {
6. return this.a;
7. };
8. }

10. set setA(a: string) {
11. this.a = a;
12. }
13. }

15. function testInvoke() {
16. const reflectClass = new ReflectClass();
17. const fn: Function = Reflect.get(reflectClass, 'getA', reflectClass);
18. console.info(fn());
19. }

21. @Entry
22. @Component
23. struct ReflectBoundThis {
24. aboutToAppear(): void {
25. testInvoke();
26. }

28. build() {
29. }
30. }
```

[ReflectBoundThis.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ReflectBoundThis.ets#L21-L51)
