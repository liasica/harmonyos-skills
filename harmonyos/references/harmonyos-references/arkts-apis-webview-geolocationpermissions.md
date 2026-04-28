---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions
title: Class (GeolocationPermissions)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (GeolocationPermissions)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:01+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:5df3fd44ae004646d4ae68942bd4e8ee291258b72134a6bf7e9d776e9c311490
---

Web组件地理位置权限管理对象。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。
* 目前调用GeolocationPermissions下的方法，都需要先加载Web组件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## 需要权限

PhonePC/2in1TabletTVWearable

访问地理位置时需添加权限：ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION、ohos.permission.LOCATION\_IN\_BACKGROUND，具体权限说明请参考[位置服务](js-apis-geolocation.md)。

## allowGeolocation

PhonePC/2in1TabletTVWearable

static allowGeolocation(origin: string, incognito?: boolean): void

允许指定来源使用地理位置接口。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示隐私模式下允许指定来源使用地理位置，false表示正常非隐私模式下允许指定来源使用地理位置。  默认值：false。  传入null或undefined时为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. origin: string = "file:///";

11. build() {
12. Column() {
13. Button('allowGeolocation')
14. .onClick(() => {
15. try {
16. webview.GeolocationPermissions.allowGeolocation(this.origin);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## deleteGeolocation

PhonePC/2in1TabletTVWearable

static deleteGeolocation(origin: string, incognito?: boolean): void

清除指定来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示隐私模式下清除指定来源的地理位置权限状态，false表示正常非隐私模式下清除指定来源的地理位置权限状态。  默认值：false。  传入null或undefined时为false。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. origin: string = "file:///";

11. build() {
12. Column() {
13. Button('deleteGeolocation')
14. .onClick(() => {
15. try {
16. webview.GeolocationPermissions.deleteGeolocation(this.origin);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## getAccessibleGeolocation

PhonePC/2in1TabletTVWearable

static getAccessibleGeolocation(origin: string, callback: AsyncCallback<boolean>, incognito?: boolean): void

以回调方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| callback | AsyncCallback<boolean> | 是 | 返回指定源的地理位置权限状态。  获取成功，true表示已授权，false表示拒绝访问。  获取失败，表示不存在指定源的权限状态。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以回调方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以回调方式异步获取指定源的地理位置权限状态。  默认值：false。  传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. origin: string = "file:///";

11. build() {
12. Column() {
13. Button('getAccessibleGeolocation')
14. .onClick(() => {
15. try {
16. webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
17. if (error) {
18. console.error(`getAccessibleGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. return;
20. }
21. console.info('getAccessibleGeolocationAsync result: ' + result);
22. });
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }
26. })
27. Web({ src: 'www.example.com', controller: this.controller })
28. }
29. }
30. }
```

## getAccessibleGeolocation

PhonePC/2in1TabletTVWearable

static getAccessibleGeolocation(origin: string, incognito?: boolean): Promise<boolean>

以Promise方式异步获取指定源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以Promise方式异步获取指定源的地理位置权限状态，false表示正常非隐私模式下以Promise方式异步获取指定源的地理位置权限状态。  默认值：false。  传入null或undefined时会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise实例，用于获取指定源的权限状态。  获取成功，true表示已授权，false表示拒绝访问。  获取失败，表示不存在指定源的权限状态。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100011 | Invalid origin. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();
9. origin: string = "file:///";

11. build() {
12. Column() {
13. Button('getAccessibleGeolocation')
14. .onClick(() => {
15. try {
16. webview.GeolocationPermissions.getAccessibleGeolocation(this.origin)
17. .then(result => {
18. console.info('getAccessibleGeolocationPromise result: ' + result);
19. }).catch((error: BusinessError) => {
20. console.error(`getAccessibleGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
21. });
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## getStoredGeolocation

PhonePC/2in1TabletTVWearable

static getStoredGeolocation(callback: AsyncCallback<Array<string>>, incognito?: boolean): void

以回调方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<string>> | 是 | 返回已存储地理位置权限状态的所有源信息。 |
| incognito11+ | boolean | 否 | true表示隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以回调方式异步获取已存储地理位置权限状态的所有源信息。  默认值：false。  传入null或undefined时会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('getStoredGeolocation')
13. .onClick(() => {
14. try {
15. webview.GeolocationPermissions.getStoredGeolocation((error, origins) => {
16. if (error) {
17. console.error(`getStoredGeolocationAsync error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. let origins_str: string = origins.join();
21. console.info('getStoredGeolocationAsync origins: ' + origins_str);
22. });
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }
26. })
27. Web({ src: 'www.example.com', controller: this.controller })
28. }
29. }
30. }
```

## getStoredGeolocation

PhonePC/2in1TabletTVWearable

static getStoredGeolocation(incognito?: boolean): Promise<Array<string>>

以Promise方式异步获取已存储地理位置权限状态的所有源信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息，false表示正常非隐私模式下以Promise方式异步获取已存储地理位置权限状态的所有源信息。  默认值：false。  传入null或undefined时会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise实例，用于获取已存储地理位置权限状态的所有源信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('getStoredGeolocation')
13. .onClick(() => {
14. try {
15. webview.GeolocationPermissions.getStoredGeolocation()
16. .then(origins => {
17. let origins_str: string = origins.join();
18. console.info('getStoredGeolocationPromise origins: ' + origins_str);
19. }).catch((error: BusinessError) => {
20. console.error(`getStoredGeolocationPromise error, ErrorCode: ${error.code},  Message: ${error.message}`);
21. });
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## deleteAllGeolocation

PhonePC/2in1TabletTVWearable

static deleteAllGeolocation(incognito?: boolean): void

清除所有来源的地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下清除所有来源的地理位置权限状态，false表示正常非隐私模式下清除所有来源的地理位置权限状态。  默认值：false。  传入null或undefined时为false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Button('deleteAllGeolocation')
13. .onClick(() => {
14. try {
15. webview.GeolocationPermissions.deleteAllGeolocation();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```
