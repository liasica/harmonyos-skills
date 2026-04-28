---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-component-status-change
title: 控件状态变化场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 控件状态变化场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d1d2fe7d16eeb3e9df033c6fa61a2a2eb1df2f04e434d2eb1145947269d9ac67
---

## 开发实例

例如下图，播放暂停按钮对应着两种状态，在状态切换时需要实时变化对应的标注信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/mX1gZsT2QoKOtwbDSj8-yg/zh-cn_image_0000002552957518.png?HW-CC-KV=V1&HW-CC-Date=20260427T233807Z&HW-CC-Expire=86400&HW-CC-Sign=E05883CB0B3E09C8B8506110B270F8AA6166679BC4142E29A9F9DDCC77032BDB)

```
1. import { PromptAction } from "@kit.ArkUI"

3. const RESOURCE_STR_PLAY = $r('app.media.play') // 此处为图片资源，请替换为本地图片
4. const RESOURCE_STR_PAUSE = $r('app.media.pause') // 此处为图片资源，请替换为本地图片

6. @Entry
7. @Component
8. export struct Rule_2_1_11 {
9. title: string = 'Rule 2.1.8'
10. @State isPlaying: boolean = true
11. uiContext: UIContext = this.getUIContext();
12. promptAction: PromptAction = this.uiContext.getPromptAction();
13. play() {
14. // play audio file
15. }

17. pause() {
18. // pause playing of audio file
19. }

21. build() {
22. NavDestination() {
23. Column() {
24. Flex({
25. direction: FlexDirection.Column,
26. alignItems: ItemAlign.Center,
27. justifyContent: FlexAlign.Center,
28. }) {
29. Row() {

31. Image(this.isPlaying ? RESOURCE_STR_PAUSE : RESOURCE_STR_PLAY)
32. .width(50)
33. .height(50)
34. .onClick(() => {
35. this.promptAction.showToast({
36. message :this.isPlaying ? "Play" : "Pause"
37. })
38. this.isPlaying = !this.isPlaying
39. if (this.isPlaying) {
40. this.play()
41. } else {
42. this.pause()
43. }
44. })
45. .accessibilityText(this.isPlaying ? 'Pause' : 'Play') // 设置可访问性框架的注释信息
46. }
47. }
48. .width('100%')
49. .height('100%')
50. .backgroundColor(Color.White)
51. }
52. }.title(this.title)
53. }
54. }
```
