---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-geolocation-permission
title: 管理位置权限
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > 管理位置权限
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:52+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:9adec9511025a0d39519aa3811da2b9df455c4f7d4065d9227dd3ae73a14e21c
---

从API version 9开始，支持Web组件的[GeolocationPermissions](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md)类和[onGeolocationShow](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)方法对网页进行位置权限管理。更多信息请参见[应用数据安全](../best-practices/bpta-app-data-security.md)。

Web组件根据[GeolocationPermissions](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md)类和[onGeolocationShow](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)方法的响应结果，决定是否赋予前端页面权限。用户可以获取位置信息，以便使用出行导航、天气预报等服务。

## 需要权限

使用获取位置功能，需在module.json5中配置位置权限。具体添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.LOCATION" // 精准定位
4. },
5. {
6. "name" : "ohos.permission.APPROXIMATELY_LOCATION" // 模糊定位
7. },
8. {
9. "name" : "ohos.permission.LOCATION_IN_BACKGROUND" // 后台定位
10. }
11. ]
```

## 申请位置权限

在下面的示例中，用户点击前端页面"获取位置"按钮，Web组件通过弹窗通知应用侧位置权限请求消息。

* 前端页面代码。

  ```
  1. <!DOCTYPE html>
  2. <html lang="en">
  3. <head>
  4. <meta charset="UTF-8">
  5. <meta name="viewport" content="width=device-width, initial-scale=1.0">
  6. <title>位置信息</title>
  7. </head>
  8. <body>
  9. <p id="locationInfo">位置信息</p>
  10. <button onclick="getLocation()">获取位置</button>

  12. <script>
  13. var locationInfo=document.getElementById("locationInfo");
  14. function getLocation(){
  15. if (navigator.geolocation) {
  16. // 访问设备地理位置
  17. navigator.geolocation.getCurrentPosition(showPosition);
  18. }
  19. }
  20. function showPosition(position){
  21. locationInfo.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;
  22. }
  23. </script>
  24. </body>
  25. </html>
  ```
* 应用代码。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { abilityAccessCtrl, common } from '@kit.AbilityKit';

  5. let atManager = abilityAccessCtrl.createAtManager();

  7. @Entry
  8. @Component
  9. struct WebComponent {
  10. controller: webview.WebviewController = new webview.WebviewController();
  11. uiContext: UIContext = this.getUIContext();

  13. // 组件的生命周期函数，创建组件实例后触发
  14. aboutToAppear(): void {
  15. let context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
  16. if (!context) {
  17. console.error("context is undefined");
  18. return;
  19. }
  20. // 向用户请求位置权限，对整个应用生效
  21. atManager.requestPermissionsFromUser(context, ["ohos.permission.APPROXIMATELY_LOCATION"]).then((data) => {
  22. console.info('data:' + JSON.stringify(data));
  23. console.info('data permissions:' + data.permissions);
  24. console.info('data authResults:' + data.authResults);
  25. }).catch((error: BusinessError) => {
  26. console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
  27. })
  28. }

  30. build() {
  31. Column() {
  32. // Web组件的geolocationAccess属性默认为true，可以显式配置为false以禁止Web组件获取地理位置信息
  33. Web({ src: $rawfile('getLocation.html'), controller: this.controller })
  34. .geolocationAccess(true)
  35. .onGeolocationShow((event) => {
  36. // 位置权限申请通知仅对当前Web组件生效，应用内的其他Web组件不受影响
  37. this.uiContext.showAlertDialog({
  38. title: '位置权限请求',
  39. message: '是否允许获取位置信息',
  40. primaryButton: {
  41. value: 'cancel',
  42. action: () => {
  43. if (event) {
  44. // 不允许此站点位置权限请求
  45. // 注意invoke的第3个参数表示是否记住当前选择，如果传true，则下次不再弹框
  46. event.geolocation.invoke(event.origin, false, false);
  47. }
  48. }
  49. },
  50. secondaryButton: {
  51. value: 'ok',
  52. action: () => {
  53. if (event) {
  54. // 允许此站点位置权限请求
  55. // 注意invoke的第3个参数表示是否记住当前选择，如果传true，则下次不再弹框
  56. event.geolocation.invoke(event.origin, true, false);
  57. }
  58. }
  59. },
  60. cancel: () => {
  61. if (event) {
  62. // 不允许此站点位置权限请求
  63. // 注意invoke的第3个参数表示是否记住当前选择，如果传true，则下次不再弹框
  64. event.geolocation.invoke(event.origin, false, false);
  65. }
  66. }
  67. })
  68. })
  69. }
  70. }
  71. }
  ```

## 管理位置权限

通过Web组件的[GeolocationPermissions](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md)类管理网页的位置权限，提供了新增（[allowGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#allowgeolocation)）、查看（[getAccessibleGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#getaccessiblegeolocation)）和删除（[deleteGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#deletegeolocation)）网页位置权限的方法。例如查看网页是否已申请位置权限、将网页已申请的位置权限删除。

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();
8. origin: string = "www.example.com";

10. build() {
11. Column() {
12. // 新增指定源的位置权限，再次获取位置信息时则不再触发onGeolocationShow的回调
13. Button('allowGeolocation')
14. .onClick(() => {
15. try {
16. webview.GeolocationPermissions.allowGeolocation(this.origin);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })

22. // 删除指定源的位置权限，再次获取位置信息时则触发onGeolocationShow的回调
23. Button('deleteGeolocation')
24. .onClick(() => {
25. try {
26. webview.GeolocationPermissions.deleteGeolocation(this.origin);
27. } catch (error) {
28. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
29. }
30. })

32. // 查询指定源的位置权限
33. Button('getAccessibleGeolocation')
34. .onClick(() => {
35. try {
36. webview.GeolocationPermissions.getAccessibleGeolocation(this.origin)
37. .then(result => {
38. console.info('getAccessibleGeolocationPromise result: ' + result);
39. }).catch((error: BusinessError) => {
40. console.error(`getAccessibleGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
41. });
42. } catch (error) {
43. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
44. }
45. })

47. // 注意添加网络权限ohos.permission.INTERNET
48. Web({ src: 'www.example.com', controller: this.controller })
49. }
50. }
51. }
```
