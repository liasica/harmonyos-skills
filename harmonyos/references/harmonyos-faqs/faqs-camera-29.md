---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-29
title: 应用已同意相机授权，点击扫一扫按钮调不起相机
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用已同意相机授权，点击扫一扫按钮调不起相机
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:828a6573a31b9b23af5fec834d3ef179c637c2edbd584c65488f6f9047ac13c4
---

## 问题现象

应用已同意相机授权，点击扫描二维码按钮，调不起相机。

## 背景知识

* [customScan.init](../harmonyos-references/scan-customscan-api.md#init)：初始化自定义界面扫码。
* [customScan.start](../harmonyos-references/scan-customscan-api.md#start)：启动扫码相机流。
* [ViewControl](../harmonyos-references/scan-customscan-api.md#viewcontrol)：相机控制参数。
  + width：XComponent组件的宽，默认使用单位为vp，支持px、lpx和vp。
  + height：XComponent组件的高，默认使用单位为vp，支持px、lpx和vp。
  + surfaceId：XComponent持有surface的ID。

## 问题定位

* 首先排查相机授权是否成功，根据"permission"、"CAMERA"搜索hilog日志，发现用户确实已经授权了相机权限弹窗。

  ```screen
  commonUI/ASP: [SPC][PermissionDialog][Ability]: caller permision: ["ohos.permission.CAMERA"].
  commonUI/ASP: [SPC][PermissionDialog][ViewModel]: group: CAMERA, title: 允许“xxxx”访问你的相机？, reason: 需要您同意使用相机，为您提供识别二维码、人脸识别、远程柜台、拍照、录像服务.
  commonUI/ASP: [SPC][PermissionDialog][Model]: handle ClickIntent, grantState: ALLOW, group: CAMERA.
  commonUI/ASP: [SPC][PermissionDialog][Model]: permission: ohos.permission.CAMERA, opt: GRANT, result: 1.
  commonUI/PrivacyCenter_permissionGrant: {"PNAMEID":"com.huawei.hmos.security.privacycenter","PVERSIONID":"5.0.20.362","BUNDLE_NAME":"com.example","PERMISSION_GROUP":"CAMERA","REQUESTED_PERMISSION":["ohos.permission.CAMERA"],"NEW_GRANT_STATE":"ALLOW"} PERMISSION_GRANT_DIALOG
  commonUI/PrivacyCenter_permissionGrant: HiSysEventUtil reportHiSysEvent PERMISSION_GRANT_DIALOG success.{"PNAMEID":"com.huawei.hmos.security.privacycenter","PVERSIONID":"5.0.20.362","BUNDLE_NAME":"com.example","PERMISSION_GROUP":"CAMERA","REQUESTED_PERMISSION":["ohos.permission.CAMERA"],"NEW_GRANT_STATE":"ALLOW"}
  commonUI/ASP: [SPC][PermissionDialog][Model]: terminate session with result, resultCode: 1, reqPerms: [ohos.permission.CAMERA], result: [0].
  ```
* 排查相机调用失败的原因，比如接口返回异常、接口调用顺序问题、参数设置问题等。继续查看日志，搜到多条1000500001的报错，该错误码是内部错误，其中报错信息"The width and height of viewcontrol do not match the width and height supported by the camera"表示传入的ViewControl宽高比例与相机分辨率不匹配。

  ```screen
  E A00001/com.example/[Scan]: callback failed, code: 1000500001, message: Internal error. The width and height of viewcontrol do not match the width and height supported by the camera.
    E A00001/com.example/[Scan]: callback failed, code: 1000500001, message: Internal error. The width and height of viewcontrol do not match the width and height supported by the camera.
  ```

## 分析结论

ViewControl的width和height需和XComponent的保持一致，start接口根据设置宽高值会匹配最接近相机分辨率，当未匹配到合适分辨率，接口会返回1000500001内部错误。如果传入的ViewControl宽高比例与相机分辨率不匹配，就会导致应用无法拉起相机实现扫一扫功能。

## 修改建议

建议ViewControl设置的宽高比例和XComponent组件的宽高保持一致。可以参考[自定义界面扫码开发步骤](../harmonyos-guides/scan-customscan.md#开发步骤)中第4步示例代码中initCamera方法对ViewControl的设置和build中对XComponent组件宽高的设置。
