---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-352
title: 如何避免Badge在数量显示切换时的Image闪烁问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何避免Badge在数量显示切换时的Image闪烁问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:75206e149c193bfccdebb21940e0a02a318bef10806fe2b87c5a04bcb704148f
---

在 onComplete 回调事件中处理 Badge 数量的逻辑，图片数据加载成功和解码成功时均触发该回调。示例代码如下：

```
1. @Entry
2. @Component
3. struct BadgeDemo {
4. @State message: string = 'Hello World';
5. @State sizes: string = '0';
6. @State showCountBadge: boolean = false;

8. build() {
9. Row() {
10. Text(this.message)
11. .fontSize(50)
12. .fontWeight(FontWeight.Bold)
13. .onClick(() => {
14. this.showCountBadge = !this.showCountBadge; // change show status
15. })
16. Stack() {
17. Badge({
18. value: '',
19. position: {
20. x: 40,
21. y: 0
22. },
23. style: {
24. badgeSize: 15,
25. badgeColor: Color.Red
26. }
27. }) {
28. Image($r('app.media.startIcon'))
29. .width(50)
30. .height(50)
31. }
32. .visibility(this.showCountBadge ? Visibility.Visible : Visibility.None)

35. Badge({
36. count: 98,
37. maxCount: 99,
38. position: { x: 30, y: 0 },
39. style: {
40. fontSize: 15,
41. badgeSize: 15,
42. badgeColor: Color.Red
43. }
44. }) {
45. Image($r('app.media.startIcon'))
46. .width(50)
47. .height(50)
48. }
49. .visibility(this.showCountBadge ? Visibility.None : Visibility.Visible)
50. }
51. }
52. .height('100%')
53. }
54. }
```

[BadgeDoesNotFlash.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BadgeDoesNotFlash.ets#L21-L75)
