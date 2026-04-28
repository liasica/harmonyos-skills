---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-image-update
title: 刷新本地图片和网络图片
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面刷新 > 刷新本地图片和网络图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:29+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:eda24be19a33cb2e1b94887a76480e1bf044971847389d56c5333a369574c4c9
---

在卡片上需要展示本地图片或从网络上下载的图片，获取本地图片和网络图片需要通过FormExtensionAbility来实现，如下示例代码介绍了如何在卡片上显示本地图片和网络图片。

1. 下载网络图片需要使用到网络能力，需要申请ohos.permission.INTERNET权限，配置方式请参见[声明权限](declare-permissions.md)。
2. 在WgtImgUpdateEntryFormAbility.ts文件中导入相关模块。

   ```
   1. // entry/src/main/ets/wgtimgupdateentryformability/WgtImgUpdateEntryFormAbility.ts
   2. import { Want } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { formBindingData, FormExtensionAbility, formInfo, formProvider } from '@kit.FormKit';
   6. import { hilog } from '@kit.PerformanceAnalysisKit';
   7. import { http } from '@kit.NetworkKit';
   ```
3. 在EntryFormAbility中的onAddForm生命周期回调中实现本地文件的刷新。

   ```
   1. // entry/src/main/ets/wgtimgupdateentryformability/WgtImgUpdateEntryFormAbility.ts
   2. const TAG: string = 'WgtImgUpdateEntryFormAbility';
   3. const DOMAIN_NUMBER: number = 0xFF00;
   4. // ...

   6. export default class WgtImgUpdateEntryFormAbility extends FormExtensionAbility {
   7. // 在添加卡片时，打开一个本地图片并将图片内容传递给卡片页面显示
   8. onAddForm(want: Want): formBindingData.FormBindingData {
   9. // 假设在当前卡片应用的tmp目录下有一个本地图片：head.PNG
   10. let tempDir = this.context.getApplicationContext().tempDir;
   11. hilog.info(DOMAIN_NUMBER, TAG, `tempDir: ${tempDir}`);
   12. let imgMap: Record<string, number> = {};
   13. try {
   14. // 打开本地图片并获取其打开后的fd, FormExtensionAbility进程销毁时释放
   15. let file = fileIo.openSync(tempDir + '/' + 'head.PNG');
   16. imgMap['imgBear'] = file.fd;
   17. } catch (e) {
   18. hilog.error(DOMAIN_NUMBER, TAG, `openSync failed: ${JSON.stringify(e as BusinessError)}`);
   19. }

   21. class FormDataClass {
   22. text: string = 'Image: Bear';
   23. loaded: boolean = true;
   24. // 卡片需要显示图片场景,必须和下列字段formImages中的key 'imgBear'相同。
   25. imgName: string = 'imgBear';
   26. // 卡片需要显示图片场景,必填字段(formImages不可缺省或改名), 'imgBear'对应fd
   27. formImages: Record<string, number> = imgMap;
   28. }

   30. let formData = new FormDataClass();
   31. // 将fd封装在formData中并返回至卡片页面
   32. return formBindingData.createFormBindingData(formData);
   33. }

   35. // ...
   36. }
   ```
4. 在EntryFormAbility中的onFormEvent生命周期回调中实现网络文件的刷新。

   ```
   1. // entry/src/main/ets/wgtimgupdateentryformability/WgtImgUpdateEntryFormAbility.ts
   2. const TAG: string = 'WgtImgUpdateEntryFormAbility';
   3. const DOMAIN_NUMBER: number = 0xFF00;
   4. const TEXT1: string = '刷新中...'
   5. const TEXT2: string = '刷新失败'

   8. export default class WgtImgUpdateEntryFormAbility extends FormExtensionAbility {
   9. // ...
   10. async onFormEvent(formId: string, message: string): Promise<void> {
   11. let param: Record<string, string> = {
   12. 'text': TEXT1
   13. };
   14. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
   15. formProvider.updateForm(formId, formInfo);

   17. // 注意：FormExtensionAbility在触发生命周期回调时被拉起，仅能在后台存在5秒
   18. // 建议下载能快速下载完成的小文件，如在5秒内未下载完成，则此次网络图片无法刷新至卡片页面上
   19. let netFile =
   20. 'https://cn-assets.gitee.com/assets/mini_app-e5eee5a21c552b69ae6bf2cf87406b59.jpg';
   21. // 需要在此处使用真实的网络图片下载链接
   22. let tempDir = this.context.getApplicationContext().tempDir;
   23. let fileName = 'file' + Date.now();
   24. let tmpFile = tempDir + '/' + fileName;
   25. let imgMap: Record<string, number> = {};

   27. class FormDataClass {
   28. text: string = 'Image: Bear' + fileName;
   29. loaded: boolean = true;
   30. // 卡片需要显示图片场景,必须和下列字段formImages中的key fileName相同。
   31. imgName: string = fileName;
   32. // 卡片需要显示图片场景,必填字段(formImages不可缺省或改名), fileName对应fd
   33. formImages: Record<string, number> = imgMap;
   34. }

   36. let httpRequest = http.createHttp()
   37. let data = await httpRequest.request(netFile);
   38. if (data?.responseCode == http.ResponseCode.OK) {
   39. try {
   40. let imgFile = fileIo.openSync(tmpFile, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   41. imgMap[fileName] = imgFile.fd;
   42. try {
   43. let writeLen: number = await fileIo.write(imgFile.fd, data.result as ArrayBuffer);
   44. hilog.info(DOMAIN_NUMBER, TAG, "write data to file succeed and size is:" + writeLen);
   45. hilog.info(DOMAIN_NUMBER, TAG, 'ArkTSCard download complete: %{public}s', tmpFile);
   46. try {
   47. let formData = new FormDataClass();
   48. let formInfo = formBindingData.createFormBindingData(formData);
   49. await formProvider.updateForm(formId, formInfo);
   50. hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'FormAbility updateForm success.');
   51. } catch (error) {
   52. hilog.error(DOMAIN_NUMBER, TAG, `FormAbility updateForm failed: ${JSON.stringify(error)}`);
   53. }
   54. } catch (err) {
   55. hilog.error(DOMAIN_NUMBER, TAG,
   56. "write data to file failed with error message: " + err.message + ", error code: " + err.code);
   57. } finally {
   58. fileIo.closeSync(imgFile);
   59. }
   60. } catch (e) {
   61. hilog.error(DOMAIN_NUMBER, TAG, `openSync failed: ${JSON.stringify(e as BusinessError)}`);
   62. }

   64. } else {
   65. hilog.error(DOMAIN_NUMBER, TAG, `ArkTSCard download task failed`);
   66. let param: Record<string, string> = {
   67. 'text': TEXT2
   68. };
   69. let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
   70. formProvider.updateForm(formId, formInfo);
   71. }
   72. httpRequest.destroy();
   73. }

   75. onAcquireFormState(want: Want): formInfo.FormState {
   76. // 卡片使用方查询卡片状态时触发该回调，默认返回初始状态。
   77. return formInfo.FormState.READY;
   78. }

   80. }
   ```
5. 在卡片页面通过backgroundImage属性展示EntryFormAbility传递过来的卡片内容。

   ```
   1. // entry/src/main/ets/widgetimageupdate/pages/WidgetImageUpdateCard.ets
   2. let storageWidgetImageUpdate = new LocalStorage();

   4. @Entry(storageWidgetImageUpdate)
   5. @Component
   6. struct WidgetImageUpdateCard {
   7. // $r('app.string.loading')需要替换为开发者所需的资源文件
   8. @LocalStorageProp('text') text: ResourceStr = $r('app.string.loading');
   9. @LocalStorageProp('loaded') loaded: boolean = false;
   10. // $r('app.string.imgName')需要替换为开发者所需的资源文件
   11. @LocalStorageProp('imgName') imgName: ResourceStr = $r('app.string.imgName');

   13. build() {
   14. Column() {
   15. Column() {
   16. Text(this.text)
   17. .fontColor('#FFFFFF')
   18. .opacity(0.9)
   19. .fontSize(12)
   20. .textOverflow({ overflow: TextOverflow.Ellipsis })
   21. .maxLines(1)
   22. .margin({ top: '8%', left: '10%' })
   23. }.width('100%').height('50%')
   24. .alignItems(HorizontalAlign.Start)

   26. Row() {
   27. Button() {
   28. // $r('app.string.update')需要替换为开发者所需的资源文件
   29. Text($r('app.string.update'))
   30. .fontColor('#45A6F4')
   31. .fontSize(12)
   32. }
   33. .width(120)
   34. .height(32)
   35. .margin({ top: '30%', bottom: '10%' })
   36. .backgroundColor('#FFFFFF')
   37. .borderRadius(16)
   38. .onClick(() => {
   39. postCardAction(this, {
   40. action: 'message',
   41. params: {
   42. info: 'refreshImage'
   43. }
   44. });
   45. })
   46. }.width('100%').height('40%')
   47. .justifyContent(FlexAlign.Center)
   48. }
   49. .width('100%').height('100%')
   50. // $r('app.media.ImageDisp')需要替换为开发者所需的资源文件
   51. .backgroundImage(this.loaded ? 'memory://' + this.imgName : $r('app.media.ImageDisp'))
   52. .backgroundImageSize(ImageSize.Cover)
   53. }
   54. }
   ```

说明

* Image组件入参格式为memory://fileName时表示进行远端内存图片显示，fileName来自EntryFormAbility传递对象('formImages': {key: fd})中的key。
* Image组件通过传入的参数是否有变化来决定是否刷新图片，因此EntryFormAbility每次传递过来的imgName都需要不同，连续传递两个相同的imgName时，图片不会刷新。
