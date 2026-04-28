---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-474
title: Tabs导航页签栏如何根据Tabbar数均匀设置宽度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs导航页签栏如何根据Tabbar数均匀设置宽度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:46825dd8371e32b8f7c170fc89eec91c3ded9f6107883ca7bccf1e5552def6fa
---

可以通过设置TabBar布局模式枚举中的BarMode.Fixed来动态均分Tab导航栏宽度，示例代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State fontColor: string = '#182431'
5. @State selectedFontColor: string = '#007DFF'
6. @State currentIndex: number = 0
7. @State selectedIndex: number = 0
8. private controller: TabsController = new TabsController()

10. @Builder
11. TabBuilder(index: number, name: string) {
12. Column() {
13. Text(name)
14. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
15. .fontSize(16)
16. .fontWeight(this.selectedIndex === index ? 500 : 400)
17. .lineHeight(22)
18. .margin({ top: 17, bottom: 7 })
19. }.width('100%')
20. }

22. build() {
23. Column() {
24. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
25. TabContent() {
26. Column().width('100%').height('100%').backgroundColor('#FFBF00')
27. }.tabBar(this.TabBuilder(0, 'green'))

29. TabContent() {
30. Column().width('100%').height('100%').backgroundColor('#007DFF')
31. }.tabBar(this.TabBuilder(1, 'blue'))

33. TabContent() {
34. Column().width('100%').height('100%').backgroundColor('#FFBF00')
35. }.tabBar(this.TabBuilder(2, 'yellow'))

37. TabContent() {
38. Column().width('100%').height('100%').backgroundColor('#E67C92')
39. }.tabBar(this.TabBuilder(3, 'pink'))
40. }
41. .vertical(false)
42. .barMode(BarMode.Fixed)
43. .barWidth(360)
44. .barHeight(56)
45. .animationDuration(400)
46. .onChange((index: number) => {
47. // currentIndex controls TabContent to display tabs
48. this.currentIndex = index
49. this.selectedIndex = index
50. })
51. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
52. if (index === targetIndex) {
53. return
54. }
55. // selectedIndex controls the color switching between Image and Text within the custom TabBar
56. this.selectedIndex = targetIndex
57. })
58. .width(360)
59. .height(296)
60. .margin({ top: 52 })
61. .backgroundColor('#F1F3F5')
62. }
63. .width('100%')
64. }
65. }
```

[TabsSetWidth.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsSetWidth.ets#L21-L86)
