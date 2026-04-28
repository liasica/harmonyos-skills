---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-334
title: List控件加载的数据如何判断是否超过一屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List控件加载的数据如何判断是否超过一屏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f2c5b8a49a6b96370989dece566ecfeac5ea971a9497283df519d88888f3f1bd
---

1.通过行高计算。

```
1. @Entry
2. @Component
3. struct AllListItemHeight {
4. private itemHeightArr = [100, 150, 200, 130, 120, 110.130];
5. private listHeight = 700;
6. scroller = new ListScroller();

9. build() {
10. Column() {
11. Button('Is it more than one screen')
12. .height(50)
13. .width('100%')
14. .onClick(() => {
15. let result = 0;
16. for (let i = 0; i < this.itemHeightArr.length; i++) {
17. result += this.itemHeightArr[i];
18. }
19. console.info(result > this.listHeight ? 'More than one screen' : 'Not exceeding one screen');
20. })
21. List({ scroller: this.scroller }) {
22. ForEach(this.itemHeightArr, (_: number, index: number) => {
23. ListItem() {
24. Text(index.toString())
25. .width('100%')
26. .textAlign(TextAlign.Center)
27. }
28. .height(this.itemHeightArr[index])
29. .align(Alignment.Center)
30. }, (item: number) => JSON.stringify(item))
31. }
32. .height(this.listHeight)
33. .width('100%')
34. }
35. }
36. }
```

[DetermineWhetherTheListDataExceedsOneScreen\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DetermineWhetherTheListDataExceedsOneScreen_One.ets#L21-L56)

2.通过getItemRect(index: number): RectResult获取子组件的大小位置，可以获取最后一个ListItem的位置大小信息进行计算。

```
1. @Entry
2. @Component
3. struct GetLastItem {
4. private itemHeightArr = [100, 150, 200, 130, 120, 110.130];
5. private listHeight = 700;
6. // Scroll controller for obtaining the position information of list items
7. scroller = new ListScroller();

10. build() {
11. Column() {
12. Button('Is it more than one screen')
13. .height(50)
14. .width('100%')
15. .onClick(() => {
16. let result = this.scroller.getItemRect(this.itemHeightArr.length - 1);
17. let flag = result.y + result.height > this.listHeight;
18. console.info(flag ? 'More than one screen' : 'Not exceeding one screen')
19. })
20. List({ scroller: this.scroller }) {
21. ForEach(this.itemHeightArr, (_: number, index: number) => {
22. ListItem() {
23. Text(index.toString())
24. .width('100%')
25. .textAlign(TextAlign.Center)
26. }
27. .height(this.itemHeightArr[index])
28. .align(Alignment.Center)
29. }, (item: number) => JSON.stringify(item))
30. }
31. .height(this.listHeight)
32. .width('100%')
33. }
34. }
35. }
```

[DetermineWhetherTheListDataExceedsOneScreen\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DetermineWhetherTheListDataExceedsOneScreen_Two.ets#L21-L55)

3.通过getItemRectInGroup(index: number, indexInGroup: number): RectResult，获取最后一个ListItemGroup中的最后一个ListItem的大小和相对于List的位置进行计算

```
1. @Entry
2. @Component
3. struct GetLastGroup {
4. private groupItemHeightArr =
5. [[30, 50, 60, 40, 90, 80.60],
6. [50, 40, 50, 55, 77, 88.44],];
7. private listHeight = 700;
8. // Scroll controller for obtaining the position information of list items
9. scroller = new ListScroller();

11. build() {
12. Column() {
13. Button('Is it more than one screen')
14. .height(50)
15. .width('100%')
16. .onClick(() => {
17. let lastGroupIndex = this.groupItemHeightArr.length - 1;
18. let lastItemIndex = this.groupItemHeightArr[lastGroupIndex].length - 1;
19. let result = this.scroller.getItemRectInGroup(lastGroupIndex, lastItemIndex);
20. let flag = result.y + result.height > this.listHeight;
21. console.info(flag ? 'More than one screen' : 'Not exceeding one screen')
22. })
23. List({ scroller: this.scroller }) {
24. ForEach(this.groupItemHeightArr, (itemHeight: number[], index: number) => {
25. ListItemGroup() {
26. ForEach(itemHeight, (height: number) => {
27. ListItem() {
28. Text(index.toString())
29. .width('100%')
30. .textAlign(TextAlign.Center)
31. }
32. .height(height)
33. .align(Alignment.Center)
34. }, (item: number, index: number) => JSON.stringify(item) + index)
35. }
36. }, (item: number[]) => JSON.stringify(item))
37. }
38. .height(this.listHeight)
39. .width('100%')
40. }
41. }
42. }
```

[DetermineWhetherTheListDataExceedsOneScreen\_Three.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DetermineWhetherTheListDataExceedsOneScreen_Three.ets#L21-L63)
