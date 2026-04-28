---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-112
title: 如何判断对象的类型
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何判断对象的类型
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:44b16e84396dab5c90f8281ca7991d5af57c2cb784741bf2149ed2c1f9b5ca97
---

在代码开发中，如果需要对对象的类型做判断，调用不同类的方法，可以使用instanceof进行判断来得知对象的类型，参考代码如下：

```
1. class BaseClass {
2. value: number = 0;

5. printf() {
6. console.info('base value:' + this.value);
7. }

10. setValue(val: number) {
11. this.value = val;
12. }
13. }

16. class AClass extends BaseClass {
17. value: number = 1;

20. setValue(val: number) {
21. this.value = val;
22. }

25. getValue(): number {
26. return this.value;
27. }
28. }

31. class BClass extends BaseClass {
32. value: number = 2;

35. setValue(val: number) {
36. this.value = val;
37. }
38. }

41. function printValue(base: BaseClass) {
42. base.printf();
43. let flag = base instanceof AClass;
44. console.info('printValue flag:' + flag);
45. if (flag) {
46. let val = (base as AClass).getValue();
47. console.info('printValue val:' + val);
48. }
49. }

52. @Entry
53. @Component
54. struct DetermineObjectType {
55. aboutToAppear(): void {
56. printValue(new AClass());
57. printValue(new BClass());
58. }

61. build() {
62. }
63. }
```

[DetermineObjectType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DetermineObjectType.ets#L21-L83)
