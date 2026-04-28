---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-451
title: Tabs组件，自定义tabBar切换动画有延迟，Tabs页面切换完才触发tabBar切换，如何修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs组件，自定义tabBar切换动画有延迟，Tabs页面切换完才触发tabBar切换，如何修改
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ee68ecb46b327e3da73f5e96d77d3f5409c7ab1d8eea6ee9c419db6b340c1508
---

新增一个selectedIndex的索引用于标识被选择的tabBar，原来的currentIndex仍然用于TabContent页签显示的控制。然后selectedIndex在onAnimationStart事件中进行切换，就可以实现页签内容切换动画发生时，tabBar也同步切换。

需要注意的是，selectedIndex和currentIndex不能为了方便使用同一个，否则会出现页面切换没有动画的情况，当共用变量时，onAnimationStart事件中的状态更新会立即触发TabContent重绘，导致系统跳过过渡动画。

可参考如下示例：

```
1. @Component
2. struct TabsDemo {
3. @State tabArray: Array<number> = [0, 1, 2, 3];
4. @State selectedIndex: number = 0;
5. @State currentIndex: number = 0;
6. @State selectedFontColor: Color = Color.Blue;
7. @State fontColor: Color = Color.Black;
8. private controller: TabsController = new TabsController();

10. @Builder
11. tabBuilder(index: number, name: string) {
12. Column() {
13. Text(name)
14. .fontSize(16)
15. .lineHeight(22)
16. .fontWeight(this.selectedIndex === index ? 500 : 400)
17. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)

19. Divider()
20. .strokeWidth(2)
21. .color('#007DEF')
22. .opacity(this.selectedIndex === index ? 1 : 0)
23. }
24. .width('100%')
25. }

27. build() {
28. Column() {
29. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
30. ForEach(this.tabArray,(item: number, index:number) => {
31. // The system has its own tab.
32. TabContent() {
33. Text('我的内容' + item)
34. .fontSize(30)
35. }
36. .tabBar(this.tabBuilder(item, 'bar' + item))
37. })
38. }
39. .onChange((index: number) => {
40. // CurrentIndex Control TabContent Display Tab.
41. this.currentIndex = index;
42. })
43. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
44. if(index === targetIndex) {
45. return;
46. }
47. // SelectedIndex controls the color switching between Image and Text in the custom TabBar.
48. this.selectedIndex = targetIndex;
49. })
50. }
51. .width('100%')
52. }
53. }
```

[TabsDemo.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b9d6551b75b078dfbf00850327a0896f97877d23/ArkUI/entry/src/main/ets/pages/TabsDemo.ets#L21-L73)
