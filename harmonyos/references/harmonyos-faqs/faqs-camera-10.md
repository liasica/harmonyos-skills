---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-10
title: 预览流黑屏但无报错信息该怎么解决
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 预览流黑屏但无报错信息该怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:478358db42171a3c3611130abff9079e52a350b20ce20acbc1b5806d900ff569
---

## 可能原因

* 未正确获取相机权限的情况下，进行相机初始化和相机输入流获取等操作。
* 应用切换到后台再返回时，相机资源被回收，未重新获取权限并开启预览导致。
* 配置的预览流尺寸不被支持。

## 解决措施

* 确保在初始化相机和获取相机输入流之前，先正确获取相机权限。
  1. 首先在module.json5文件中申请需要的权限（地理位置权限可以根据需要申请，非必选）；

     ```ts
     "requestPermissions": [
       {
         "name": "ohos.permission.CAMERA",
         "usedScene": {
           "abilities": [
             "FormAbility"
           ],
           "when": "always"
         },
         "reason": "$string:Camera_Permission_Request"
       },
       {
         "name": "ohos.permission.MICROPHONE",
         "usedScene": {
           "abilities": [
             "FormAbility"
           ],
           "when": "always"
         },
         "reason": "$string:Camera_Permission_Request"
       },
       // The geographical location permission can be applied for as required. This parameter is optional.
       {
         "name": "ohos.permission.MEDIA_LOCATION",
         "usedScene": {
         "abilities": [
             "FormAbility"
         ],
         "when": "always"
         },
         "reason": "$string:Camera_Permission_Request"
       }
     ],
     ```
  2. 接着在EntryAbility.ets中onWindowStageCreate中使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法获取权限。

     ```ts
     onWindowStageCreate(windowStage: window.WindowStage): void {
       let atManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(this.context,
         [
           'ohos.permission.CAMERA',
           'ohos.permission.MICROPHONE',
           'ohos.permission.MEDIA_LOCATION'
         ]
       ).then((data) => {
         console.info('data:' + JSON.stringify(data));
         console.info('data permissions:' + data.permissions);
         console.info('data authResults:' + data.authResults);
         // Main window is created, set main page for this ability
         hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

         windowStage.loadContent('pages/CameraPreviewFlow', (err, data) => {
           if (err.code) {
             hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
             return;
           }
           hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
         });
       }).catch((err: BusinessError) => {
         console.info('data:' + JSON.stringify(err));
       });
     }
     ```
* 当应用被切换到后台后，相机资源会被全部回收，所以为了避免出现前后台切换时预览流黑屏的问题，需在onPageShow中进行重新创建会话、配置会话、启动等操作，并在onPageHide中对相机资源进行释放。

  ```ts
  async onPageShow() {
    let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
    await this.initCamera(baseContext, this.surfaceId);
  }

  async onPageHide() {
    await this.releaseCamera();
  }
  ```
* 获取相机设备支持的输出流能力，确定支持的预览尺寸。

  ```ts
  // Obtain the output stream capability supported by the camera device
  let cameraOutputCap: camera.CameraOutputCapability =
    cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
  if (!cameraOutputCap) {
    console.error(TAG, "cameraManager.getSupportedOutputCapability error");
    return;
  }
  console.info(TAG, "outputCapability: " +
  JSON.stringify(cameraOutputCap));  //The aspect ratio of the preview stream and the video output stream resolution should be consistent
  let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
  let position: number = 0;
  if (previewProfilesArray != null) {
    previewProfilesArray.forEach((value: camera.Profile,
      index: number) => { // View supported preview sizes
      console.info(TAG,
        `Supported preview sizes: [${value.size.width},${value.size.height},${value.size.width / value.size.height}]`);
      if (value.size.width === 2592 && value.size.height === 1200) {
        position = index;
      }
    })
  } else {
    console.error(TAG, "createOutput photoProfilesArray == null || undefined");
  }
  ```
