---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-incognito-mode
title: 使用隐私模式
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 设置基本属性和事件 > 使用隐私模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:21cd02d4e1ae04b517ef7579a5ddefa79a2588709f80a7842d000e5b89c9d283
---

开发者在创建Web组件时，可以将可选参数[incognitoMode](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)设置为true，来开启Web组件的隐私模式。使用隐私模式浏览网页时，Cookie、缓存等数据不会写入本地持久化存储；隐私模式的Web组件销毁后，这些数据将被清除，不会保留。

* 创建隐私模式的[Web组件](../harmonyos-references/arkts-basic-components-web.md)。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct WebComponent {
  6. controller: webview.WebviewController = new webview.WebviewController();

  8. build() {
  9. Column() {
  10. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  11. }
  12. }
  13. }
  ```

  [IncognitoMode\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/IncognitoMode_one.ets#L16-L30)
* 通过[isIncognitoMode](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#isincognitomode11) 判断当前Web组件是否是隐私模式。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Button('isIncognitoMode')
  12. .onClick(() => {
  13. try {
  14. let result = this.controller.isIncognitoMode();
  15. console.info('isIncognitoMode' + result);
  16. } catch (error) {
  17. console.error(
  18. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  19. }
  20. })
  21. Web({ src: 'www.example.com', controller: this.controller });
  22. }
  23. }
  24. }
  ```

  [IncognitoMode\_two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/IncognitoMode_two.ets#L16-L41)

隐私模式提供了一系列接口，用于操作地理位置、Cookie以及Cache Data。

* 通过[allowGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#allowgeolocation)设置隐私模式下的Web组件允许指定来源使用地理位置。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();
  8. origin: string = 'file:///';

  10. build() {
  11. Column() {
  12. Button('allowGeolocation')
  13. .onClick(() => {
  14. try {
  15. // allowGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，允许指定来源使用地理位置。
  16. webview.GeolocationPermissions.allowGeolocation(this.origin, true);
  17. } catch (error) {
  18. console.error(
  19. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  20. }
  21. })
  22. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  23. }
  24. }
  25. }
  ```

  [AllowGeolocation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/AllowGeolocation.ets#L16-L42)
* 通过[deleteGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#deletegeolocation)清除隐私模式下指定来源的地理位置权限状态。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();
  8. origin: string = 'file:///';

  10. build() {
  11. Column() {
  12. Button('deleteGeolocation')
  13. .onClick(() => {
  14. try {
  15. // deleteGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，清除指定来源的地理位置权限状态。
  16. webview.GeolocationPermissions.deleteGeolocation(this.origin, true);
  17. } catch (error) {
  18. console.error(
  19. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  20. }
  21. })
  22. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  23. }
  24. }
  25. }
  ```

  [DeleteGeolocation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/DeleteGeolocation.ets#L16-L42)
* 通过[getAccessibleGeolocation](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md#getaccessiblegeolocation)以回调方式异步获取隐私模式下指定源的地理位置权限状态。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();
  8. origin: string = 'file:///';

  10. build() {
  11. Column() {
  12. Button('getAccessibleGeolocation')
  13. .onClick(() => {
  14. try {
  15. // getAccessibleGeolocation第三个参数表示隐私模式（true）或非隐私模式（false）下
  16. // 以回调方式异步获取指定源的地理位置权限状态。
  17. webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
  18. if (error) {
  19. console.error(`getAccessibleGeolocationAsync error: + Code: ${error.code}, message: ${error.message}`);
  20. return;
  21. }
  22. console.info('getAccessibleGeolocationAsync result: ' + result);
  23. }, true);
  24. } catch (error) {
  25. console.error(
  26. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  27. }
  28. })
  29. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  30. }
  31. }
  32. }
  ```

  [GetAccessibleGeolocation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/GetAccessibleGeolocation.ets#L16-L49)
* 通过[deleteAllData](../harmonyos-references/arkts-apis-webview-webstorage.md#deletealldata)清除隐私模式下Web SQL当前使用的所有存储。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Button('deleteAllData')
  12. .onClick(() => {
  13. try {
  14. // deleteAllData参数表示删除所有隐私模式（true）或非隐私模式（false）下，内存中的web数据。
  15. webview.WebStorage.deleteAllData(true);
  16. } catch (error) {
  17. console.error(
  18. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  19. }
  20. })
  21. Web({ src: $rawfile('index.html'), controller: this.controller, incognitoMode: true })
  22. .databaseAccess(true)
  23. }
  24. }
  25. }
  ```

  [DeleteAllData.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/DeleteAllData.ets#L16-L42)

  加载的html文件。

  ```
  1. <!-- index.html -->
  2. <!DOCTYPE html>
  3. <html>
  4. <head>
  5. <meta charset="UTF-8">
  6. <title>test</title>
  7. <script type="text/javascript">

  9. var db = openDatabase('mydb','1.0','Test DB',2 * 1024 * 1024);
  10. var msg;

  12. db.transaction(function(tx){
  13. tx.executeSql('INSERT INTO LOGS (id,log) VALUES(1,"test1")');
  14. tx.executeSql('INSERT INTO LOGS (id,log) VALUES(2,"test2")');
  15. msg = '<p>数据表已创建,且插入了两条数据。</p>';

  17. document.querySelector('#status').innerHTML = msg;
  18. });

  20. db.transaction(function(tx){
  21. tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
  22. var len = results.rows.length,i;
  23. msg = "<p>查询记录条数：" + len + "</p>";

  25. document.querySelector('#status').innerHTML += msg;

  27. for(i = 0; i < len; i++){
  28. msg = "<p><b>" + results.rows.item(i).log + "</b></p>";

  30. document.querySelector('#status').innerHTML += msg;
  31. }
  32. },null);
  33. });

  35. </script>
  36. </head>
  37. <body>
  38. <div id="status" name="status">状态信息</div>
  39. </body>
  40. </html>
  ```
* 通过[fetchCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#fetchcookiesync11)获取隐私模式下指定url对应cookie的值。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Button('fetchCookieSync')
  12. .onClick(() => {
  13. try {
  14. // fetchCookieSync第二个参数表示获取隐私模式（true）或非隐私模式（false）下，webview的内存cookies。
  15. let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com', true);
  16. console.info('fetchCookieSync cookie = ' + value);
  17. } catch (error) {
  18. console.error(
  19. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  20. }
  21. })
  22. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  23. }
  24. }
  25. }
  ```

  [FetchCookieSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/FetchCookieSync.ets#L16-L42)
* 通过[configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)设置隐私模式下指定url的单个cookie的值。

  ```
  1. import { webview } from '@kit.ArkWeb';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. @Entry
  5. @Component
  6. struct WebComponent {
  7. controller: webview.WebviewController = new webview.WebviewController();

  9. build() {
  10. Column() {
  11. Button('configCookieSync')
  12. .onClick(() => {
  13. try {
  14. // configCookieSync第三个参数表示设置隐私模式（true）或非隐私模式（false）下，对应url的cookies。
  15. webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', true);
  16. } catch (error) {
  17. console.error(
  18. `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
  19. }
  20. })
  21. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  22. }
  23. }
  24. }
  ```

  [ConfigCookieSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/ConfigCookieSync.ets#L16-L41)
* 通过[existCookie](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#existcookie)查询隐私模式下是否存在cookie。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct WebComponent {
  6. controller: webview.WebviewController = new webview.WebviewController();

  8. build() {
  9. Column() {
  10. Button('existCookie')
  11. .onClick(() => {
  12. // existCookie参数表示隐私模式（true）或非隐私模式（false）下，查询是否存在cookies。
  13. let result = webview.WebCookieManager.existCookie(true);
  14. console.info('result: ' + result);
  15. })
  16. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  17. }
  18. }
  19. }
  ```

  [ExistCookie.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/ExistCookie.ets#L16-L36)
* 通过[clearAllCookiesSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#clearallcookiessync11)清除隐私模式下所有cookie。

  ```
  1. import { webview } from '@kit.ArkWeb';

  3. @Entry
  4. @Component
  5. struct WebComponent {
  6. controller: webview.WebviewController = new webview.WebviewController();

  8. build() {
  9. Column() {
  10. Button('clearAllCookiesSync')
  11. .onClick(() => {
  12. // clearAllCookiesSync参数表示清除隐私模式（true）或非隐私模式（false）下，webview的所有内存cookies。
  13. webview.WebCookieManager.clearAllCookiesSync(true);
  14. })
  15. Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
  16. }
  17. }
  18. }
  ```

  [ClearAllCookiesSync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/SetBasicAttrsEvts/SetBasicAttrsEvtsOne/entry/src/main/ets/pages/ClearAllCookiesSync.ets#L16-L35)
