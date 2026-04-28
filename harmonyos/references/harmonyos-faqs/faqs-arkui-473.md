---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-473
title: Tabs如何实现预加载特定的TabContent页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs如何实现预加载特定的TabContent页
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:27fd4c09125098f2dffb794eda8a615354ab8f643fd543cb5c8fe25e82bde669
---

方案一：不论用ForEach还是LazyForEach循环渲染TabContent里面的内容都是一次渲染，故不能使用循环渲染。

由于Tabs组件自带滑动切换页面动画，所以在点击TabBar切换页面时会从当前页面滑动到目标页面，导致当前页面和目标页面的中间页面也被加载。可以使用自定义切换动画去规避Tabs组件自带的动画导致多个TabContent加载的问题。参考customContentTransition使用说明。

参考代码：

```
1. @Entry
2. @Component
3. struct TabsDemo {
4. @State currentIndex: number = 0;
5. private tabsController: TabsController = new TabsController();
6. // Set up page switching animations instead of sliding to jump to page animations
7. private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
8. (from: number, to: number) => {
9. let tabContentAnimatedTransition = {
10. timeout: 1000,
11. transition: (proxy: TabContentTransitionProxy) => {
12. this.getUIContext().animateTo({
13. duration: 0,
14. onFinish: () => {
15. proxy.finishTransition();
16. }
17. }, () => {
18. })
19. }
20. } as TabContentAnimatedTransition
21. return tabContentAnimatedTransition;
22. }

24. build() {
25. Column() {
26. Tabs({ index: this.currentIndex, controller: this.tabsController }) {
27. TabContent() {
28. MyComponent({ color: '#00CB87' })
29. }.tabBar(SubTabBarStyle.of('green'))

31. TabContent() {
32. MyComponent({ color: '#007DFF' })
33. }.tabBar(SubTabBarStyle.of('green'))

35. TabContent() {
36. MyComponent({ color: '#FFBF00' })
37. }.tabBar(SubTabBarStyle.of('green'))

39. TabContent() {
40. MyComponent({ color: '#E67C92' })
41. }.tabBar(SubTabBarStyle.of('green'))
42. }
43. .customContentTransition(this.customContentTransition)
44. .width('100%')
45. .height(296)
46. .barBackgroundColor('#F1F3F5')
47. .onChange((index: number) => {
48. this.currentIndex = index;
49. })
50. }
51. }
52. }

54. @Component
55. struct MyComponent {
56. private color: string = '';

58. aboutToAppear(): void {
59. // It can be observed by printing the log that no intermediate page has been loaded
60. console.info('aboutToAppear backgroundColor:' + this.color);
61. }

63. aboutToDisappear(): void {
64. console.info('aboutToDisappear backgroundColor:' + this.color);
65. }

67. build() {
68. Column()
69. .width('100%')
70. .height('100%')
71. .backgroundColor(this.color)
72. }
73. }
```

[TabsPreloadTabContent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsPreloadTabContent.ets#L21-L94)

方案二：若要同时规避加载中间页面，又要保留手势滑动切换页面功能，可以使用Swiper自定义实现Tabs组件。通过调用SwiperController的changeIndex方法翻至指定页面，useAnimation设置为false时没有动效。

参考代码：

```
1. class MyDataSource implements IDataSource {
2. private list: number[] = [];

4. constructor(list: number[]) {
5. this.list = list;
6. }

8. totalCount(): number {
9. return this.list.length;
10. }

12. getData(index: number): number {
13. return this.list[index];
14. }

16. registerDataChangeListener(listener: DataChangeListener): void {
17. }

19. unregisterDataChangeListener(listener: DataChangeListener): void {
20. }
21. }

24. @Entry
25. @Component
26. struct SwiperExample {
27. private swiperController: SwiperController = new SwiperController();
28. private data: MyDataSource = new MyDataSource([]);

30. aboutToAppear(): void {
31. let list: number[] = [];
32. for (let i = 0; i <= 10; i++) {
33. list.push(i);
34. }
35. this.data = new MyDataSource(list);
36. }

38. build() {
39. Column({ space: 5 }) {
40. Swiper(this.swiperController) {
41. LazyForEach(this.data, (item: string) => {
42. Text(item.toString())
43. .width('90%')
44. .height(160)
45. .backgroundColor(0XAFEEEE)
46. .textAlign(TextAlign.Center)
47. .fontSize(30)
48. }, (item: string) => item)
49. }
50. .cachedCount(2)
51. .index(1)
52. .autoPlay(true)
53. .interval(4000)
54. .loop(true)
55. .duration(1000)
56. .itemSpace(0)
57. .indicator(false)

59. Row({ space: 12 }) {
60. Button('change to index:4')
61. .onClick(() => {
62. this.swiperController.changeIndex(3, false);
63. })
64. Button('change to index:7')
65. .onClick(() => {
66. this.swiperController.changeIndex(6, false);
67. })
68. }
69. .margin(5)
70. }
71. .width('100%')
72. .margin({ top: 5 })
73. }
74. }
```

[TabsPreloadTabContentPlanTwo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsPreloadTabContentPlanTwo.ets#L21-L95)
