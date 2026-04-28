---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-311
title: 绑定类型的组件和ForEach的正确连用方式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 绑定类型的组件和ForEach的正确连用方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0d131d73949b1cf803d51b90f9c4e8f3409db69224ed0c6e92ecf4afc63bca88
---

**问题现象**

bindSheet和ForEach合用的问题，$$this.isShow会弹出两次半模态，如果是this.isShow，则半模态弹出的次数是数组的长度数，如何确保ForEach中每个item的点击事件仅触发对应项的弹窗显示，而不影响其他项。

**解决措施**

给每一个弹窗都绑定一个@State修饰的变量。

参考代码如下：

```
1. @Entry
2. @Component
3. export struct BindSheetAndForEach {
4. @State isShow: boolean = false;
5. @State arr: number[] = [1, 2, 3, 4];
6. @State isSheetVisible: Array<boolean> = new Array<boolean>(this.arr.length).fill(false);

10. @Builder
11. myBuilder() {
12. Column() {
13. Button('content1')
14. .margin(10)
15. .fontSize(20)
16. }
17. .width('100%')
18. }

20. // Each array item corresponds to an independent pop-up window displaying the status, which is index bound
21. build() {
22. Column() {
23. ForEach(this.arr, (item: number, idx: number) => {
24. Row() {
25. Text('item')
26. Button('Bullet Frame')
27. .onClick(() => {
28. this.isSheetVisible[idx] = true;
29. })
30. .fontSize(15)
31. .margin(10)
32. .bindSheet(this.isSheetVisible[idx], this.myBuilder(), {
33. backgroundColor: Color.Gray,
34. height: SheetSize.MEDIUM,
35. showClose: true,
36. onWillDisappear: () => {
37. this.isSheetVisible[idx] = false;
38. }
39. })
40. Checkbox()
41. }
42. .border({ width: 1, radius: 5 })
43. })
44. }
45. .justifyContent(FlexAlign.Start)
46. .width('100%')
47. .height('100%')
48. }
49. }
```

[CorrectWayToUseForEach.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CorrectWayToUseForEach.ets#L21-L70)
