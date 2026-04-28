---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/movingphotoview-guidelines
title: 使用MovingPhotoView播放动态照片
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 动态照片 > 使用MovingPhotoView播放动态照片
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d3f1776f35c9f4b3da04f97314563d0d24523cc27729d5cd4ad62441e63dc5cd
---

系统提供了MovingPhotoView组件，在一些社交类、图库类应用中，可用于播放动态照片文件。

## 约束与限制

针对MovingPhotoView组件的使用，有以下约束与限制：

* 当前不支持动态属性设置。
* 当前不支持设置ArkUI通用属性[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)。
* 该组件长按触发播放时组件区域放大为1.1倍。
* 该组件使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)进行播放，同时开启的AVPlayer个数不建议超过3个，超过3个可能会出现视频播放卡顿现象。

## 开发步骤

1. 导入动态照片模块。

   说明

   * MovingPhotoViewAttribute是用于配置MovingPhotoView组件属性的关键接口。API version 21及之前版本，导入MovingPhotoView组件后需要开发者手动导入MovingPhotoViewAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入MovingPhotoView组件后，会自动导入MovingPhotoViewAttribute，无需开发者手动导入。
   * MovingPhotoViewAttribute导入后，DevEco Studio会将其显示置灰，不影响开发者使用。

   API version 21及之前版本：

   ```
   1. import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
   ```

   API version 22及之后版本：

   ```
   1. import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
   ```
2. 获取动态照片对象（[MovingPhoto](../harmonyos-references/arkts-apis-photoaccesshelper-movingphoto.md)）。

   MovingPhoto对象需要通过photoAccessHelper接口创建或获取，MovingPhotoView只接收构造完成的MovingPhoto对象。

   创建、获取的方式可参考[访问和管理动态照片资源](photoaccesshelper-movingphoto.md)。

   ```
   1. src: photoAccessHelper.MovingPhoto | undefined = undefined;
   ```
3. 创建动态照片控制器（[MovingPhotoViewController](../harmonyos-references/ohos-multimedia-movingphotoview.md#movingphotoviewcontroller)），用于控制动态照片的播放状态（如播放、停止）。

   ```
   1. controller: MovingPhotoViewController = new MovingPhotoViewController();
   ```
4. 创建动态照片组件。

   以下参数取值仅为举例，具体每个属性的取值范围，可参考API文档：[@ohos.multimedia.movingphotoview](../harmonyos-references/ohos-multimedia-movingphotoview.md)。

   ```
   1. // API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
   2. // API version 22及之后版本导入方式如下：
   3. import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State src: photoAccessHelper.MovingPhoto | undefined = undefined
   9. @State isMuted: boolean = false
   10. controller: MovingPhotoViewController = new MovingPhotoViewController();
   11. build() {
   12. Column() {
   13. MovingPhotoView({
   14. movingPhoto: this.src,
   15. controller: this.controller
   16. })
   17. // 是否静音播放，此处由按钮控制，默认值为false非静音播放。
   18. .muted(this.isMuted)
   19. // 视频显示模式，默认值为Cover。
   20. .objectFit(ImageFit.Cover)
   21. // 播放时触发。
   22. .onStart(() => {
   23. console.info('onStart');
   24. })
   25. // 播放结束触发。
   26. .onFinish(() => {
   27. console.info('onFinish');
   28. })
   29. // 播放停止触发。
   30. .onStop(() => {
   31. console.info('onStop')
   32. })
   33. // 出现错误触发。
   34. .onError(() => {
   35. console.error('onError');
   36. })

   38. Row() {
   39. // 按钮：开始播放。
   40. Button('start')
   41. .onClick(() => {
   42. this.controller.startPlayback()
   43. })
   44. .margin(5)
   45. // 按钮：停止播放。
   46. Button('stop')
   47. .onClick(() => {
   48. this.controller.stopPlayback()
   49. })
   50. .margin(5)
   51. }
   52. .alignItems(VerticalAlign.Center)
   53. .justifyContent(FlexAlign.Center)
   54. .height('15%')
   55. }
   56. }
   57. }
   ```

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/EQO02GfhTuOzkl0LcblVAg/zh-cn_image_0000002583478609.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234635Z&HW-CC-Expire=86400&HW-CC-Sign=24093A4149D771568F0EC959D1FE07C7D7DB1A1D93616955C1F6148911CA707A)
