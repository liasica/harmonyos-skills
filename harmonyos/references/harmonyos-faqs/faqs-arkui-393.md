---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-393
title: Swiper如何自定义导航点高度位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Swiper如何自定义导航点高度位置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0baacb9920a290ec30b72d2a53b2418f1179f3c64c9b4069cad534d21e860440
---

**问题描述**

[Swiper](../harmonyos-references/ts-container-swiper.md)组件内置[indicator](../harmonyos-references/ts-container-swiper.md#indicator)UI样式有宽高，不支持自定义修改。

**解决措施**

方案一：可以使用自定义Indicator的方式。当前DotIndicator的规格固定存在内边距，无法满足问题需求。可以通过以下步骤实现无内边距的导航指示器效果：

1. 在Stack组件中创建Swiper轮播组件与导航点Column组件。
2. 使用[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)循环渲染Column组件，并设置合适的高度和外边距，例如在Stack组件内设置[alignContent](../harmonyos-references/ts-container-stack.md#aligncontent): Alignment.Bottom参数，表示底部对齐，也可以采用[位置设置](../harmonyos-references/ts-universal-attributes-location.md)的方式，直接指定指示器位置。
3. 将index的值与currentIndex作比较，当两者相同时，改变Column的宽度与颜色，以此实现导航点效果。

具体参考代码如下所示：

```
1. @Entry
2. @Component
3. struct SwiperExample {
4. private swiperController: SwiperController = new SwiperController();
5. @State arr: string[] = ['1', '2', '3', '4', '5', '6'];
6. @State widthLength: number = 0;
7. @State heightLength: number = 0;
8. @State currentIndex: number = 0;

10. build() {
11. Column({ space: 5 }) {
12. Stack({ alignContent: Alignment.Bottom }) {
13. Swiper(this.swiperController) {
14. ForEach(this.arr, (item: string) => {
15. Text(item)
16. .width('90%')
17. .height(200)
18. .backgroundColor(0xAFEEEE)
19. .textAlign(TextAlign.Center)
20. .fontSize(30)
21. }, (item: string) => item)
22. }
23. .cachedCount(2)
24. .index(0)
25. .indicator(false)
26. .onChange((index: number) => {
27. this.currentIndex = index;
28. })

30. Row() {
31. ForEach(this.arr, (_: string, index: number) => {
32. Column()
33. .width(this.currentIndex == index ? 15 : 5)
34. .height(5)
35. .margin(5)
36. .backgroundColor(this.currentIndex == index ? Color.Gray : Color.White)
37. }, (item: string) => item)
38. }
39. }
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

[CustomNavigationPoints.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CustomNavigationPoints.ets#L21-L65)

方案二：采用API15中Indicator组件。 Indicator组件采用的依旧是Swiper中的默认指示器样式，一样有32vp的交互高度限制，不过该组件将Swiper与指示器单独分割，可以通过Column组件单独封装指示器，再通过clip属性裁剪，控制Indicator组件高度，其它的与方案一类似，采用Stack组件封装。 实现方式如下：

```
1. @Entry
2. @Component
3. struct DotIndicatorDemo {
4. private indicatorController: IndicatorComponentController = new IndicatorComponentController();
5. private swiperController: SwiperController = new SwiperController();
6. @State list: string[] = ['1', '2', '3', '4', '5', '6'];

8. build() {
9. Stack({ alignContent: Alignment.Bottom }) {
10. Swiper(this.swiperController) {
11. ForEach(this.list, (item: string) => {
12. Text(item)
13. .width('90%')
14. .height(200)
15. .backgroundColor(0xAFEEEE)
16. .textAlign(TextAlign.Center)
17. .fontSize(30)
18. }, (item: string) => item)
19. }
20. .cachedCount(2)
21. .index(0)
22. .indicator(this.indicatorController)

24. Column() {
25. IndicatorComponent(this.indicatorController)
26. .style(
27. new DotIndicator()
28. .itemWidth(10)
29. .itemHeight(10)
30. .selectedItemWidth(20)
31. .selectedItemHeight(10)
32. .color(Color.White)
33. .selectedColor(Color.Gray)
34. )
35. }
36. .height(25)
37. .clip(true)
38. }
39. .width('100%')
40. }
41. }
```

[CustomNavigationPointsPlanTwo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/4d38726fbc68dda953def7ce5ff601f3254ee760/ArkUI/entry/src/main/ets/pages/CustomNavigationPointsPlanTwo.ets#L21-L61)

注意：若方案二指示器背景为透明，不使用clip裁剪也可。同时若背景颜色为透明，也可采用margin属性，设置底部为负值达成类似效果。
