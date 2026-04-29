---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-button-annotation
title: 按钮标注场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 按钮标注场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:31405d5f3c5e54c8aec7a5f6250b9ecef6f3685839b4c5f703dc216ca434eb06
---

## 设计场景

对于用户可点击等操作的任何按钮，如果不是文本类控件，则须通过给出标注信息，包括用户自定义的控件中的虚拟按钮区域，否则可能会导致屏幕朗读用户无法完成对应的功能。此类控件在进行标注时，标注文本不要包含控件类型、“单指双击即可打开”之类的字符串，此部分指引由屏幕朗读根据控件类型、控件状态，并结合用户是否开启了“新手指引”自动追加朗读。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/2WekUmQHSNizYdjOFLy08w/zh-cn_image_0000002589243815.png?HW-CC-KV=V1&HW-CC-Date=20260429T052608Z&HW-CC-Expire=86400&HW-CC-Sign=4F307AA943F33DAF7043E20AA122ED4C41864A52D59A4553A2E7D92A25A33D06)

## 开发实例

在下面的代码片段中，您可以看到Image组件（它实际上是一个播放/暂停按钮），通过设置accessibilityText属性提供标注信息：

```
1. const RESOURCE_STR_PLAY = $r('app.media.play')
2. const RESOURCE_STR_PAUSE = $r('app.media.pause')

4. @Entry
5. @Component
6. export struct Rule_2_1_5 {
7. title: string = 'Rule 2.1.5'
8. @State isPlaying: boolean = false
9. play() {
10. // play audio file
11. }

13. pause() {
14. // pause playing of audio file
15. }

17. build() {
18. NavDestination() {
19. Column() {
20. Flex({
21. direction: FlexDirection.Column,
22. alignItems: ItemAlign.Center,
23. justifyContent: FlexAlign.Center,
24. }) {
25. Row() {
26. Image(this.isPlaying ? RESOURCE_STR_PAUSE : RESOURCE_STR_PLAY)
27. .width(50)
28. .height(50)
29. .onClick(() => {
30. this.isPlaying = !this.isPlaying
31. if (this.isPlaying) {
32. this.play()
33. } else {
34. this.pause()
35. }
36. })
37. .accessibilityRole(BUTTON_TYPE)
38. .accessibilityText(this.isPlaying ? 'Pause' : 'Play') // 设置注释信息
39. Text('Good_morning.mp3')
40. .margin({
41. left: 10
42. })
43. }
44. }
45. .width('100%')
46. .height('100%')
47. .backgroundColor(Color.White)
48. }
49. }
50. .title(this.title)
51. }
52. }
```
