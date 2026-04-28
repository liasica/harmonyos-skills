---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/savebutton
title: 使用保存控件
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9341a7c7858111719f8ae3959f7fa2b71d212857c1da956a0a09962d97b09ebf
---

保存控件允许用户通过点击按钮临时获取存储权限，无需权限弹框确认。

集成保存控件后，当用户点击该控件时，应用会在短时间内获取访问媒体库特权接口的授权。在API version 19及之前的版本中，授权持续时间为10秒；在API version 20及之后的版本中，授权持续时间为1分钟。这适用于任何需要将文件保存到媒体库的应用场景，例如保存图片或视频等。

与需要触发系统应用并由用户选择具体保存路径的Picker不同，保存控件可以直接保存到指定的媒体库路径，使得操作更为便捷。

保存控件效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_WXgT7j4S8mRqt5kPneifg/zh-cn_image_0000002583438405.png?HW-CC-KV=V1&HW-CC-Date=20260427T234205Z&HW-CC-Expire=86400&HW-CC-Sign=720D02BBEB1FB37DE3791E20A691C4AE5B9C16A2236CF52860D9D8EAFB3B6E59)

## 约束与限制

* 当用户首次点击应用中的保存控件，系统将弹窗请求用户授权。如果用户点击“取消”，弹窗消失，应用无授权，用户再次点击保存控件时，将会重新弹窗；如果用户点击“允许”，弹窗消失，应用将被授予临时保存权限，此后点击该应用的保存控件将不会弹窗。
* 应用在点击控件触发onClick()回调到调用媒体库特权接口的时间间隔需控制在授权时间内。在API version 19及之前的版本中，授权持续时间为10秒；在API version 20及之后的版本中，授权持续时间为1分钟。
* 保存控件仅支持在[应用主窗口和子窗口](../harmonyos-references/arkts-apis-window-e.md#windowtype7)中使用，且不支持在[UIExtension](../harmonyos-references/js-apis-arkui-uiextension.md)中使用。
* 用户点击一次控件，仅获取一次授权调用。
* 为了保障用户的隐私不被恶意应用获取，应用需确保安全控件是可见的且用户能够识别的。开发者需要合理的配置控件的尺寸、颜色等属性，避免视觉混淆的情况，如果发生因控件的样式不合法导致授权失败的情况，请检查设备错误日志。
* 当开发者需要自定义保存控件的图标和文本时，需要向应用市场申请ohos.permission.CUSTOMIZE\_SAVE\_BUTTON权限。

  注意

  ohos.permission.CUSTOMIZE\_SAVE\_BUTTON受限开放，仅默认样式无法满足业务场景时可申请，申请方式请参考[申请使用受限权限](declare-permissions-in-acl.md)。

## 开发步骤

以保存对话中图片为例，应用仅需在前台期间短暂使用保存图片的特性，而不需要长时间使用。此时，可以直接使用安全控件中的保存控件，免去权限申请和请求等环节，获得临时授权，保存对应图片。

1. 导入文件和媒体库依赖。

   ```
   1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 设置图片资源并添加保存控件。

   保存控件是由图标、文本和背景组成的类似按钮的安全控件。其中，背景是必选的，图标和文本至少选择一个。图标和文本可以从已有的选项中选择，也可以通过[setIcon](../harmonyos-references/ts-security-components-savebutton.md#seticon20)和[setText](../harmonyos-references/ts-security-components-savebutton.md#settext20)自定义。在声明安全控件的接口时，有传参和不传参两种方式。不传参将默认创建一个包含图标、文本和背景的按钮；传参则根据参数创建，不包含未配置的元素。

   当前示例使用默认参数。具体请参见[SaveButton控件](../harmonyos-references/ts-security-components-savebutton.md)。此外，所有安全控件都继承了[安全控件通用属性](../harmonyos-references/ts-securitycomponent-attributes.md)，可用于定制样式。

   有关将图片保存到媒体库的详细信息，请参考[保存媒体库资源](photoaccesshelper-savebutton.md)。

   ```
   1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { promptAction } from '@kit.ArkUI';
   5. import { BusinessError } from '@kit.BasicServicesKit';

   7. async function savePhotoToGallery(context: common.UIAbilityContext) {
   8. let helper = photoAccessHelper.getPhotoAccessHelper(context);
   9. try {
   10. // onClick触发后一分钟内通过createAsset接口创建图片文件，一分钟后createAsset权限收回。
   11. let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
   12. // 使用uri打开文件，可以持续写入内容，写入过程不受时间限制。
   13. let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   14. // $r('app.media.test')需要替换为开发者所需的图像资源文件。
   15. context.resourceManager.getMediaContent($r('app.media.test').id, 0)
   16. .then(async value => {
   17. let media = value.buffer;
   18. // 写到媒体库文件中。
   19. await fileIo.write(file.fd, media);
   20. await fileIo.close(file.fd);
   21. promptAction.openToast({ message: $r('app.string.saved_in_photo') });
   22. });
   23. } catch (error) {
   24. const err: BusinessError = error as BusinessError;
   25. console.error(`Failed to save photo. Code is ${err.code}, message is ${err.message}`);
   26. }
   27. }

   29. @Entry
   30. @Component
   31. struct Index {
   32. build() {
   33. Row() {
   34. Column({ space: 10 }) {
   35. // $r('app.media.test')需要替换为开发者所需的图像资源文件。
   36. Image($r('app.media.test'))
   37. .height(400)
   38. .width('100%')

   40. SaveButton()
   41. .padding({top: 12, bottom: 12, left: 24, right: 24})
   42. .onClick((event: ClickEvent, result: SaveButtonOnClickResult) => {
   43. if (result === SaveButtonOnClickResult.SUCCESS) {
   44. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   45. // 免去权限申请和权限请求等环节，获得临时授权，保存对应图片。
   46. savePhotoToGallery(context);
   47. } else {
   48. promptAction.openToast({ message: $r('app.string.set_permission_failed') });
   49. }
   50. })
   51. }
   52. .width('100%')
   53. }
   54. .height('100%')
   55. .backgroundColor(0xf1f3f5)
   56. }
   57. }
   ```

   [Save.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/SecurityComponent/entry/src/main/ets/securitycomponent/pages/Save.ets#L16-L73)
