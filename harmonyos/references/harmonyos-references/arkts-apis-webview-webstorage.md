---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webstorage
title: Class (WebStorage)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebStorage)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:09+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:8451f9ccd5ca263cda67a4727df097c4fb36f51ae9c45d1e15b417cd1124ac15
---

通过WebStorage可管理Web SQL数据库接口和HTML5 Web存储接口，每个应用中的所有Web组件共享一个WebStorage。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。
* 目前调用WebStorage下的方法，都需要先加载Web组件。
* 本Class下的接口在ArkWeb内核升级到M132版本后因内核废弃Web SQL，对Web SQL数据库的管理失效。ArkWeb内核版本参考ArkWeb简介[约束与限制](../harmonyos-guides/web-component-overview.md#约束与限制)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## deleteOrigin

PhonePC/2in1TabletTVWearable

static deleteOrigin(origin: string): void

清除指定源所使用的存储。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引，来自于[getOrigins](arkts-apis-webview-webstorage.md#getorigins)。 |

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
9. origin: string = "resource://rawfile/";

11. build() {
12. Column() {
13. Button('deleteOrigin')
14. .onClick(() => {
15. try {
16. webview.WebStorage.deleteOrigin(this.origin);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }

21. })
22. Web({ src: $rawfile('index.html'), controller: this.controller })
23. }
24. }
25. }
```

加载的html文件。

```
1. <!-- index.html -->
2. <!DOCTYPE html>
3. <html>
4. <head>
5. <meta charset="UTF-8">
6. <title>test</title>
7. <script type="text/javascript">

9. // 打开或创建数据库
10. var request = indexedDB.open('myDatabase', 1);

12. // 如果数据库版本变化或首次创建时触发
13. request.onupgradeneeded = function(event) {
14. var db = event.target.result;

16. // 创建对象存储（表），设置主键为‘id’
17. var objectStore = db.createObjectStore('customers', { keyPath: 'id' });

19. // 为‘name’创建索引
20. objectStore.createIndex('name', 'name', { unique: false });
21. };

23. // 打开数据库成功时的回调
24. request.onsuccess = function(event) {
25. var db = event.target.result;

27. const customerData = [
28. {id: 1, name: 'John Doe', email: 'john@example.com'},
29. {id: 2, name: 'John Doe', email: 'john@example.com'},
30. ]

32. // 插入数据
33. var transaction = db.transaction('customers', 'readwrite');
34. var objectStore = transaction.objectStore('customers');

36. customerData.forEach((customer) => {
37. objectStore.add(customer);
38. });

40. transaction.oncomplete = function () {
41. console.info('Transaction completed: data added');
42. }

44. transaction.onerror = function (event) {
45. console.error("Transaction failed", event);
46. }

48. // 查询数据
49. var queryTransaction = db.transaction(['customers']);
50. var queryObjectStore = queryTransaction.objectStore('customers');
51. var query = queryObjectStore.get(2);

53. query.onsuccess = function (event) {
54. console.info('query succ');
55. console.info('Customer:', event.target.result);
56. console.info('Customer id:', event.target.result.id);
57. console.info('Customer name:', event.target.result.name);
58. console.info('Customer email:', event.target.result.email);
59. };

61. queryObjectStore.openCursor().onsuccess = (event) => {
62. const cursor = event.target.result;
63. if (cursor) {
64. var msg = "<p>查询记录：" + cursor.key + "</p>";
65. document.querySelector("#status").innerHTML += msg;
66. var msg = "<p><b>" + cursor.value.name + "</b></p>";
67. document.querySelector("#status").innerHTML += msg;
68. console.info(`SSN ${cursor.key} 对应的名字是 ${cursor.value.name}`);
69. cursor.continue();
70. } else {
71. console.info("没有更多记录了")
72. }
73. }
74. };

76. // 错误处理
77. request.onerror = function(event) {
78. console.error('Database error:', event.target.error);
79. };

81. </script>
82. </head>
83. <body>
84. <div id="status" name="status">状态信息</div>
85. </body>
86. </html>
```

## getOrigins

PhonePC/2in1TabletTVWearable

static getOrigins(callback: AsyncCallback<Array<WebStorageOrigin>>): void

以回调方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[WebStorageOrigin](arkts-apis-webview-i.md#webstorageorigin)>> | 是 | 以数组方式返回源的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100012 | Invalid web storage origin. |
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
12. Button('getOrigins')
13. .onClick(() => {
14. try {
15. webview.WebStorage.getOrigins((error, origins) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. for (let i = 0; i < origins.length; i++) {
21. console.info('origin: ' + origins[i].origin);
22. console.info('usage: ' + origins[i].usage);
23. console.info('quota: ' + origins[i].quota);
24. }
25. })
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }

30. })
31. Web({ src: $rawfile('index.html'), controller: this.controller })
32. }
33. }
34. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOrigins

PhonePC/2in1TabletTVWearable

static getOrigins(): Promise<Array<WebStorageOrigin>>

以Promise方式异步获取当前使用Web SQL数据库和HTML5支持的Web存储API的所有源的信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WebStorageOrigin](arkts-apis-webview-i.md#webstorageorigin)>> | Promise实例，用于获取当前所有源的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100012 | Invalid web storage origin. |
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
12. Button('getOrigins')
13. .onClick(() => {
14. try {
15. webview.WebStorage.getOrigins()
16. .then(origins => {
17. for (let i = 0; i < origins.length; i++) {
18. console.info('origin: ' + origins[i].origin);
19. console.info('usage: ' + origins[i].usage);
20. console.info('quota: ' + origins[i].quota);
21. }
22. })
23. .catch((e: BusinessError) => {
24. console.error('error: ' + JSON.stringify(e));
25. })
26. } catch (error) {
27. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
28. }

30. })
31. Web({ src: $rawfile('index.html'), controller: this.controller })
32. }
33. }
34. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginQuota

PhonePC/2in1TabletTVWearable

static getOriginQuota(origin: string, callback: AsyncCallback<number>): void

使用callback回调异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引。 |
| callback | AsyncCallback<number> | 是 | 指定源的存储配额。  number是long型整数，范围为[-2147483648, 2147483647]。  单位：byte。 |

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
9. origin: string = "resource://rawfile/";

11. build() {
12. Column() {
13. Button('getOriginQuota')
14. .onClick(() => {
15. try {
16. webview.WebStorage.getOriginQuota(this.origin, (error, quota) => {
17. if (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. return;
20. }
21. console.info('quota: ' + quota);
22. })
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }

27. })
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. }
30. }
31. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginQuota

PhonePC/2in1TabletTVWearable

static getOriginQuota(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储配额，配额以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise实例，用于获取指定源的存储配额。  单位：byte。 |

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
9. origin: string = "resource://rawfile/";

11. build() {
12. Column() {
13. Button('getOriginQuota')
14. .onClick(() => {
15. try {
16. webview.WebStorage.getOriginQuota(this.origin)
17. .then(quota => {
18. console.info('quota: ' + quota);
19. })
20. .catch((e: BusinessError) => {
21. console.error('error: ' + JSON.stringify(e));
22. })
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }

27. })
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. }
30. }
31. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginUsage

PhonePC/2in1TabletTVWearable

static getOriginUsage(origin: string, callback: AsyncCallback<number>): void

以回调方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |
| callback | AsyncCallback<number> | 是 | 指定源的存储量。  单位：byte。 |

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
9. origin: string = "resource://rawfile/";

11. build() {
12. Column() {
13. Button('getOriginUsage')
14. .onClick(() => {
15. try {
16. webview.WebStorage.getOriginUsage(this.origin, (error, usage) => {
17. if (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. return;
20. }
21. console.info('usage: ' + usage);
22. })
23. } catch (error) {
24. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
25. }

27. })
28. Web({ src: $rawfile('index.html'), controller: this.controller })
29. }
30. }
31. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## getOriginUsage

PhonePC/2in1TabletTVWearable

static getOriginUsage(origin: string): Promise<number>

以Promise方式异步获取指定源的Web SQL数据库和HTML5支持的Web存储API的存储量，存储量以字节为单位。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| origin | string | 是 | 指定源的字符串索引 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise实例，用于获取指定源的存储量。  单位：byte。 |

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
9. origin: string = "resource://rawfile/";

11. build() {
12. Column() {
13. Button('getOriginUsage')
14. .onClick(() => {
15. try {
16. webview.WebStorage.getOriginUsage(this.origin)
17. .then(usage => {
18. console.info('usage: ' + usage);
19. }).catch((e: BusinessError) => {
20. console.error('error: ' + JSON.stringify(e));
21. })
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: $rawfile('index.html'), controller: this.controller })
27. }
28. }
29. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下的html文件。

## deleteAllData

PhonePC/2in1TabletTVWearable

static deleteAllData(incognito?: boolean): void

清除被JavaScript存储API使用的所有存储数据，这包括Web SQL数据库和HTML5支持的Web存储API。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示删除所有隐私模式下内存中的web数据，false表示删除正常非隐私模式下Web的SQL数据库当前使用的所有存储。  默认值：false。  传入undefined或null时为false。 |

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
12. Button('deleteAllData')
13. .onClick(() => {
14. try {
15. webview.WebStorage.deleteAllData();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: $rawfile('index.html'), controller: this.controller })
21. }
22. }
23. }
```

加载的html文件，请参考[deleteOrigin](arkts-apis-webview-webstorage.md#deleteorigin)接口下加载的html文件。
