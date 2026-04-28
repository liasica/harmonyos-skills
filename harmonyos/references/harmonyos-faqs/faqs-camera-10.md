---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-10
title: 预览流黑屏但无报错信息该怎么解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 预览流黑屏但无报错信息该怎么解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4e937fde12576bf82c93ad93c898e077df8bf4d94d392624789159cc82d86d36
---

**可能原因**

* 未正确获取相机权限的情况下，进行相机初始化和相机输入流获取等操作。
* 应用切换到后台再返回时，相机资源被回收，未重新获取权限并开启预览导致。
* 配置的预览流尺寸不被支持。

**解决措施**

* 确保在初始化相机和获取相机输入流之前，先正确获取相机权限。
  1. 首先在module.json5文件中申请需要的权限（地理位置权限可以根据需要申请，非必选）；

     ```
     1. "requestPermissions": [
     2. {
     3. "name": "ohos.permission.CAMERA",
     4. "usedScene": {
     5. "abilities": [
     6. "FormAbility"
     7. ],
     8. "when": "always"
     9. },
     10. "reason": "$string:Camera_Permission_Request"
     11. },
     12. {
     13. "name": "ohos.permission.MICROPHONE",
     14. "usedScene": {
     15. "abilities": [
     16. "FormAbility"
     17. ],
     18. "when": "always"
     19. },
     20. "reason": "$string:Camera_Permission_Request"
     21. },
     22. {
     23. "name": "ohos.permission.WRITE_MEDIA",
     24. "usedScene": {
     25. "abilities": [
     26. "FormAbility"
     27. ],
     28. "when": "always"
     29. },
     30. "reason": "$string:Camera_Permission_Request"
     31. },
     32. {
     33. "name": "ohos.permission.READ_MEDIA",
     34. "usedScene": {
     35. "abilities": [
     36. "FormAbility"
     37. ],
     38. "when": "always"
     39. },
     40. "reason": "$string:Camera_Permission_Request"
     41. },
     42. // The geographical location permission can be applied for as required. This parameter is optional.
     43. {
     44. "name": "ohos.permission.MEDIA_LOCATION",
     45. "usedScene": {
     46. "abilities": [
     47. "FormAbility"
     48. ],
     49. "when": "always"
     50. },
     51. "reason": "$string:Camera_Permission_Request"
     52. }
     53. ],
     ```

     [module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/module.json5#L56-L108)
  2. 接着在EntryAbility.ets中onWindowStageCreate中使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法获取权限。

     ```
     1. onWindowStageCreate(windowStage: window.WindowStage): void {
     2. let atManager = abilityAccessCtrl.createAtManager();
     3. atManager.requestPermissionsFromUser(this.context,
     4. [
     5. 'ohos.permission.CAMERA',
     6. 'ohos.permission.MICROPHONE',
     7. 'ohos.permission.MEDIA_LOCATION',
     8. 'ohos.permission.READ_MEDIA',
     9. 'ohos.permission.WRITE_MEDIA'
     10. ]
     11. ).then((data) => {
     12. console.info('data:' + JSON.stringify(data));
     13. console.info('data permissions:' + data.permissions);
     14. console.info('data authResults:' + data.authResults);
     15. // Main window is created, set main page for this ability
     16. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     18. windowStage.loadContent('pages/CameraPreviewFlow', (err, data) => {
     19. if (err.code) {
     20. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
     21. return;
     22. }
     23. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
     24. });
     25. }).catch((err: BusinessError) => {
     26. console.info('data:' + JSON.stringify(err));
     27. });
     28. }
     ```

     [EntryAbility.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/entryability/EntryAbility.ets#L27-L54)
* 当应用被切换到后台后，相机资源会被全部回收，所以为了避免出现前后台切换时预览流黑屏的问题，需在onPageShow中进行重新创建会话、配置会话、启动等操作，并在onPageHide中对相机资源进行释放。

  ```
  1. async onPageShow() {
  2. let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
  3. await this.initCamera(baseContext, this.surfaceId);
  4. }

  6. async onPageHide() {
  7. await this.releaseCamera();
  8. }
  ```

  [ResolvePreviewStreamBlackScreenIssuePage.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/ResolvePreviewStreamBlackScreenIssuePage.ets#L28-L35)
* 获取相机设备支持的输出流能力，确定支持的预览尺寸。

  ```
  1. // Obtain the output stream capability supported by the camera device
  2. let cameraOutputCap: camera.CameraOutputCapability =
  3. cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
  4. if (!cameraOutputCap) {
  5. console.error(TAG, "cameraManager.getSupportedOutputCapability error");
  6. return;
  7. }
  8. console.info(TAG, "outputCapability: " +
  9. JSON.stringify(cameraOutputCap));  //The aspect ratio of the preview stream and the video output stream resolution should be consistent
  10. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
  11. let position: number = 0;
  12. if (previewProfilesArray != null) {
  13. previewProfilesArray.forEach((value: camera.Profile,
  14. index: number) => { // View supported preview sizes
  15. console.info(TAG,
  16. `Supported preview sizes: [${value.size.width},${value.size.height},${value.size.width / value.size.height}]`);
  17. if (value.size.width === 2592 && value.size.height === 1200) {
  18. position = index;
  19. }
  20. })
  21. } else {
  22. console.error(TAG, "createOutput photoProfilesArray == null || undefined");
  23. }
  ```

  [ResolvePreviewStreamBlackScreenIssue.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/ResolvePreviewStreamBlackScreenIssue.ets#L29-L51)
