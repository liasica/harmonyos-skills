---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-b112
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.1(13) Release引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:57+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:33567fd70eddfedb6ca46210cf9bdf7f4e5c6bd5af86f683aa77a7adde198bdc
---

## Tabs组件底部页签默认高度由52vp变更为48vp

**变更原因**

Tabs组件底部页签默认高度由52vp调整到48vp，优化用户体验。

**变更影响**

此变更涉及应用适配。

变更前：设置BottomTabBarStyle样式且vertical属性为false时，barHeight的默认值为52vp。

变更后：设置BottomTabBarStyle样式且vertical属性为false时，barHeight的默认值为48vp。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

barHeight

**适配指导**

若发现组件高度变化导致界面内容出现留白，可通过修改内容区高度或自适应内容区高度。

若组件高度发生变化，开发者期望保持原有高度样式。示例如下：

```
1. @Entry
2. @Component
3. struct barHeightTest {
4. build() {
5. Column() {
6. Tabs() {
7. TabContent() {
8. Column().width('100%').width('100%').height('100%').backgroundColor(Color.Pink)
9. }
10. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), "Pink"))

12. TabContent() {
13. Column().width('100%').width('100%').height('100%').backgroundColor(Color.Green)
14. }
15. .tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), "Green"))
16. }
17. .barHeight(52)
18. }
19. }
20. }
```

## 画布组件在绘制文本时设置globalCompositeOperation、fillStyle和globalAlpha属性的效果变更

**变更原因**

使用画布组件（CanvasRenderingContext2D和OffscreenCanvasRenderingContext2D）进行文本绘制时，设置globalCompositeOperation属性和pattern样式的fillStyle属性无效；设置带透明度颜色的fillStyle属性，同时设置globalAlpha属性，文本的透明度仅由globalAlpha决定，不考虑fillStyle属性的颜色透明度。导致绘制效果与W3C标准存在差异，因此需要变更绘制行为。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.1(13)时生效。

变更前：CanvasRenderingContext2D和OffscreenCanvasRenderingContext2D的globalCompositeOperation属性与fillStyle属性设置的pattern样式在绘制文本时不生效；fillStyle属性设置带透明度颜色并设置globalAlpha属性时，fillText绘制文本的透明度为globalAlpha属性值。

变更后：CanvasRenderingContext2D和OffscreenCanvasRenderingContext2D的globalCompositeOperation属性与fillStyle属性设置的pattern样式在绘制文本时生效；fillStyle属性设置带透明度颜色并设置globalAlpha属性时，fillText绘制文本的透明度为颜色透明度×globalAlpha。

| 使用场景 | 变更前 | 变更后 |
| --- | --- | --- |
| globalCompositeOperation与fillText组合使用 |  |  |
| fillStyle设置pattern样式与fillText组合使用 |  |  |
| globalAlpha设置透明度，fillStyle设置带透明度颜色，与fillText组合使用 |  |  |

**起始API Level**

8

**变更的接口/组件**

CanvasRenderingContext2D和OffscreenCanvasRenderingContext2D的fillText和strokeText接口。

**适配指导**

若希望在绘制文本时globalCompositeOperation属性保持默认值，需在fillText/strokeText方法前声明context.globalCompositeOperation = 'source-over'；若希望pattern样式在绘制文本时不生效，需在fillText方法前指定所需的fillStyle；若希望文本透明度不受fillStyle颜色透明度的影响，需将fillStyle设置为不透明颜色。

示例：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg")
8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .onReady(() =>{
14. this.context.font = '30vp sans-serif'
15. this.context.fillStyle = 'rgb(227, 248, 249)'
16. this.context.fillRect(0, 0, 150, 150)
17. this.context.fillStyle = 'rgb(39, 135, 217)'
18. this.context.globalCompositeOperation = 'xor' // 设置globalCompositeOperation为'xor'模式
19. this.context.fillText('Hello World', 50, 50) // 生效'xor'模式
20. this.context.globalCompositeOperation = 'source-over' // 设置globalCompositeOperation为默认值
21. this.context.fillText('Hello World', 50, 150) // 生效'source-over'模式
22. let pattern = this.context.createPattern(this.img, 'repeat')
23. if (pattern) {
24. this.context.fillStyle = pattern // 设置fillStyle为pattern样式
25. }
26. this.context.fillText('Hello World', 50, 250) // 生效pattern样式
27. this.context.fillStyle = '#88FF0000' // 设置fillStyle为带透明度颜色
28. this.context.globalAlpha = 0.5 // 设置画布透明度
29. this.context.fillText('Hello World', 50, 350) // 透明度为颜色透明度×globalAlpha
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

## NavDestination的Dialog模式默认支持系统动画

**变更原因**

NavDestination的Dialog模式支持系统动画。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.1(13)时生效。

变更前：NavDestination的Dialog模式，无系统默认动画。

变更后：NavDestination的Dialog模式，默认带有系统转场动画。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

9

**变更的接口/组件**

NavDestination

**适配指导**

开发者可以通过在pop与push接口中设置false关闭NavDestination的系统默认动画。

示例：

```
1. @Entry
2. @Component

4. struct NavigationDemo {
5. @State pageInfos: NavPathStack = new NavPathStack();

7. @Builder
8. pageOneTmp() {
9. NavDestination() {
10. Text("This is a sample")
11. .fontSize(50)
12. }
13. .title("PageOne")
14. .mode(NavDestinationMode.DIALOG)
15. .backgroundColor(Color.Blue)
16. }

18. @Builder
19. PageMap(name: string, param: object) {
20. if (name === 'pageOne') {
21. this.pageOneTmp()
22. }
23. }

25. build() {
26. Column({ space: 10 }) {
27. Button('Pop Dialog')
28. .onClick(() => {
29. // Set true to enable system animations, or set false to disable system animations.
30. this.pageInfos.pop(true)
31. })
32. Button('Push Dialog')
33. .onClick(() => {
34. // Set true to enable system animations, or set false to disable system animations.
35. this.pageInfos.pushPath({ name: 'pageOne' }, true)
36. })
37. Navigation(this.pageInfos) {
38. Column({ space: 10 }) {
39. Text("This is navigation").fontSize(60).align(Alignment.Center)
40. }
41. }
42. .height(500)
43. .backgroundColor(Color.Grey)
44. .navDestination(this.PageMap)
45. }.height(50)
46. }
47. }
```
