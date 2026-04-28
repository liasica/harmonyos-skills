---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-97
title: 如何自定义Video组件控制栏样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何自定义Video组件控制栏样式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dc8a25b1fd7f7bcb10d8ea28c7a68a612fde47bbd013f3ebc9babd92b75ad6c8
---

1. 通过设置属性controls为false关闭默认控制栏。
2. 设置Video组件的controller。
3. 通过ArkTS实现自定义的控制栏，并通过VideoController控制视频播放。

   ```
   1. @Entry
   2. @Component
   3. struct VideoCreateComponent {
   4. @State videoSrc: Resource = $rawfile('xxx.mp4')
   5. @State previewUri: Resource = $r('app.media.xxx')
   6. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X
   7. @State isAutoPlay: boolean = false
   8. @State showControls: boolean = true
   9. controller: VideoController = new VideoController()

   11. build() {
   12. Column() {
   13. Video({
   14. src: this.videoSrc,
   15. previewUri: this.previewUri,
   16. currentProgressRate: this.curRate,
   17. controller: this.controller
   18. })
   19. .width('100%')
   20. .height(600)
   21. .autoPlay(this.isAutoPlay)
   22. .controls(this.showControls)
   23. .onStart(() => {
   24. console.info('onStart')
   25. })
   26. .onPause(() => {
   27. console.info('onPause')
   28. })
   29. .onFinish(() => {
   30. console.info('onFinish')
   31. })
   32. .onError(() => {
   33. console.info('onError')
   34. })
   35. .onPrepared((e) => {
   36. console.info('onPrepared is ' + e.duration)
   37. })
   38. .onSeeking((e) => {
   39. console.info('onSeeking is ' + e.time)
   40. })
   41. .onSeeked((e) => {
   42. console.info('onSeeked is ' + e.time)
   43. })
   44. .onUpdate((e) => {
   45. console.info('onUpdate is ' + e.time)
   46. })
   47. Row() {
   48. Button('src').onClick(() => {
   49. this.videoSrc = $rawfile('xxx.mp4') // Switch video source
   50. }).margin(5)
   51. Button('previewUri').onClick(() => {
   52. this.previewUri = $r('app.media.xxx') // Switch video preview poster
   53. }).margin(5)

   55. Button('controls').onClick(() => {
   56. this.showControls = !this.showControls // Switch whether to display the video control bar
   57. }).margin(5)
   58. }

   60. Row() {
   61. Button('start').onClick(() => {
   62. this.controller.start() // 开始播放
   63. }).margin(5)
   64. Button('pause').onClick(() => {
   65. this.controller.pause() // 暂停播放
   66. }).margin(5)
   67. Button('stop').onClick(() => {
   68. this.controller.stop() // 结束播放
   69. }).margin(5)
   70. Button('setTime').onClick(() => {
   71. this.controller.setCurrentTime(10, SeekMode.Accurate) // Accurately jump to the 10s position of the video
   72. }).margin(5)
   73. }

   75. Row() {
   76. Button('rate 0.75').onClick(() => {
   77. this.curRate = PlaybackSpeed.Speed_Forward_0_75_X // 0.75 times playback speed
   78. }).margin(5)
   79. Button('rate 1').onClick(() => {
   80. this.curRate = PlaybackSpeed.Speed_Forward_1_00_X // Original speed playback
   81. }).margin(5)
   82. Button('rate 2').onClick(() => {
   83. this.curRate = PlaybackSpeed.Speed_Forward_2_00_X // Play at 2x speed
   84. }).margin(5)
   85. }
   86. }
   87. }
   88. }
   ```

   [CustomizeVideoStyles.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CustomizeVideoStyles.ets#L21-L108)

**参考链接**

[Video](../harmonyos-guides/arkts-common-components-video-player.md)
