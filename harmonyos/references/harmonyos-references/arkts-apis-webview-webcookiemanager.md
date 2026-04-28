---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager
title: Class (WebCookieManager)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebCookieManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ff66a360a18bc55f4c8f3871822dd50b78acc4c551613f97a559f829e0468a02
---

通过WebCookieManager可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookieManager实例。cookie的格式遵循[RFC6265](https://www.rfc-editor.org/rfc/rfc6265)标准。当前WebCookieManager的获取cookie接口不支持partitioned cookie。使用隐私模式浏览网页时，Cookie、缓存等数据不会写入本地持久化存储；隐私模式的Web组件销毁后，这些数据将被清除，不会保留。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。
* 静态方法必须在用户界面（UI）线程上使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## fetchCookieSync11+

PhonePC/2in1TabletTVWearable

static fetchCookieSync(url: string, incognito?: boolean): string

获取指定url对应cookie的值。

说明

* 系统会自动清理过期的cookie，对于同名key的数据，新数据将会覆盖前一个数据。
* 为了获取可正常使用的cookie值，fetchCookieSync需传入完整链接。
* fetchCookieSync用于获取所有的cookie值，每条cookie值之间会通过"; "进行分隔，但无法单独获取某一条特定的cookie值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| incognito | boolean | 否 | true表示获取隐私模式下webview的内存cookies，false表示正常非隐私模式下的cookies。  默认值：false。  传入undefined或null会抛出异常错误码401。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 指定url对应的cookie的值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('fetchCookieSync')
13. .onClick(() => {
14. try {
15. let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
16. console.info("fetchCookieSync cookie = " + value);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## fetchCookie11+

PhonePC/2in1TabletTVWearable

static fetchCookie(url: string, callback: AsyncCallback<string>): void

异步callback方式获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| callback | AsyncCallback<string> | 是 | callback回调，用于获取cookie |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
12. Button('fetchCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.fetchCookie('https://www.example.com', (error, cookie) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. return;
19. }
20. if (cookie) {
21. console.info('fetchCookie cookie = ' + cookie);
22. }
23. })
24. } catch (error) {
25. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
26. }
27. })
28. Web({ src: 'www.example.com', controller: this.controller })
29. }
30. }
31. }
```

## fetchCookie11+

PhonePC/2in1TabletTVWearable

static fetchCookie(url: string): Promise<string>

以Promise方式异步获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，用于获取指定url对应的cookie值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
12. Button('fetchCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.fetchCookie('https://www.example.com')
16. .then(cookie => {
17. console.info("fetchCookie cookie = " + cookie);
18. })
19. .catch((error: BusinessError) => {
20. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
21. })
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## fetchCookie14+

PhonePC/2in1TabletTVWearable

static fetchCookie(url: string, incognito: boolean): Promise<string>

以Promise方式异步获取指定url对应cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |
| incognito | boolean | 是 | true表示获取隐私模式下webview的内存cookies，false表示正常非隐私模式下的cookies。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise实例，用于获取指定url对应的cookie值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |

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
12. Button('fetchCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.fetchCookie('https://www.example.com', false)
16. .then(cookie => {
17. console.info("fetchCookie cookie = " + cookie);
18. })
19. .catch((error: BusinessError) => {
20. console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
21. })
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## configCookieSync11+

PhonePC/2in1TabletTVWearable

static configCookieSync(url: string, value: string, incognito?: boolean): void

为指定url设置单个cookie的值。

说明

* configCookieSync中的url，可以指定域名的方式来使得页面内请求也附带上cookie。
* 同步cookie的时机建议在Web组件加载之前完成。
* cookie每30s周期性保存到磁盘中，也可以使用接口[saveCookieAsync](arkts-apis-webview-webcookiemanager.md#savecookieasync)进行强制落盘。
* value参数必须遵循Set-Cookie HTTP响应头的格式。形式为"key=value"的键值对，后面可跟随以分号分隔的cookie属性列表（例如"key=value;Max-Age=100"）。
* 若存在相同host、path和名称的cookie，将被新cookie替换。若设置的cookie已过期，则不会存储该cookie。如需设置多个cookie，应多次调用此方法。
* 若通过configCookieSync进行两次或多次设置cookie，则每次设置的cookie之间会通过"; "进行分隔。
* 如果指定的值包含"Secure"属性，则url必须使用"https://"协议。
* 如果要覆盖HttpOnly的cookies，需要在value中指定HttpOnly属性。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 否 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。  默认值：false。  传入undefined或null会抛出异常错误码401。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('configCookieSync')
13. .onClick(() => {
14. try {
15. // configCookieSync每次仅支持设置单个cookie值。
16. webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## configCookieSync14+

PhonePC/2in1TabletTVWearable

static configCookieSync(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): void

为指定url设置cookie的值。

说明

* configCookieSync中的url，可以指定域名的方式来使得页面内请求也附带上cookie。
* 同步cookie的时机建议在Web组件加载之前完成。
* cookie每30s周期性保存到磁盘中，也可以使用接口[saveCookieAsync](arkts-apis-webview-webcookiemanager.md#savecookieasync)进行强制落盘。
* value参数必须遵循Set-Cookie HTTP响应头的格式。形式为"key=value"的键值对，后面可跟随以分号分隔的cookie属性列表（例如"key=value;Max-Age=100"）。
* 若存在相同host、path和名称的cookie，将被新cookie替换。若设置的cookie已过期，则不会存储该cookie。如需设置多个cookie，应多次调用此方法。
* 若通过configCookieSync进行两次或多次设置cookie，则每次设置的cookie之间会通过"; "进行分隔。
* 如果指定的值包含"Secure"属性，则url必须使用"https://"协议。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 是 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。 |
| includeHttpOnly | boolean | 是 | true表示允许覆盖含有http-only的cookies，false表示不允许覆盖含有http-only的cookies。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('configCookieSync')
13. .onClick(() => {
14. try {
15. // 仅支持设置单个cookie值。
16. webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', false, false);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## configCookie11+

PhonePC/2in1TabletTVWearable

static configCookie(url: string, value: string, callback: AsyncCallback<void>): void

异步callback方式为指定url设置单个cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| callback | AsyncCallback<void> | 是 | callback回调，用于获取设置cookie的结果 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
12. Button('configCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.configCookie('https://www.example.com', "a=b", (error) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## configCookie11+

PhonePC/2in1TabletTVWearable

static configCookie(url: string, value: string): Promise<void>

指定url设置单个cookie的值。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取指定url设置单个cookie值是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
12. Button('configCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.configCookie('https://www.example.com', 'a=b')
16. .then(() => {
17. console.info('configCookie success!');
18. })
19. .catch((error: BusinessError) => {
20. console.info('error: ' + JSON.stringify(error));
21. })
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## configCookie14+

PhonePC/2in1TabletTVWearable

static configCookie(url: string, value: string, incognito: boolean, includeHttpOnly: boolean): Promise<void>

指定url设置单个cookie的值。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |
| incognito | boolean | 是 | true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。 |
| includeHttpOnly | boolean | 是 | true表示允许覆盖含有http-only的cookies，false表示不允许覆盖含有http-only的cookies。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取指定url设置单个cookie值是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |

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
12. Button('configCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.configCookie('https://www.example.com', 'a=b', false, false)
16. .then(() => {
17. console.info('configCookie success!');
18. })
19. .catch((error: BusinessError) => {
20. console.info('error: ' + JSON.stringify(error));
21. })
22. } catch (error) {
23. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
24. }
25. })
26. Web({ src: 'www.example.com', controller: this.controller })
27. }
28. }
29. }
```

## saveCookieSync15+

PhonePC/2in1TabletTVWearable

static saveCookieSync(): void

将当前可通过fetchCookie获取到的所有需要持久化的cookie同步保存到磁盘中。

**系统能力：** SystemCapability.Web.Webview.Core

说明

* saveCookieSync用于强制将需要持久化的cookies写入磁盘。PC/2in1和Tablet设备不会持久化session cookie，即使调用saveCookieSync，也不会将session cookie写入磁盘。
* saveCookieSync将阻塞调用者直到操作完成，期间可能会执行I/O操作。

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
12. Button('saveCookieSync')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.saveCookieSync();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## saveCookieAsync

PhonePC/2in1TabletTVWearable

static saveCookieAsync(callback: AsyncCallback<void>): void

将当前可通过fetchCookie获取到的所有需要持久化的cookie异步保存到磁盘中。

说明

* Cookie信息存储在应用沙箱路径下/proc/{pid}/root/data/storage/el2/base/cache/web/Cookies。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | callback回调，用于获取cookie是否成功保存。 |

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
12. Button('saveCookieAsync')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.saveCookieAsync((error) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## saveCookieAsync

PhonePC/2in1TabletTVWearable

static saveCookieAsync(): Promise<void>

将当前可通过fetchCookie获取到的所有需要持久化的cookie以Promise方法异步保存到磁盘中。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取cookie是否成功保存。 |

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
12. Button('saveCookieAsync')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.saveCookieAsync()
16. .then(() => {
17. console.info("saveCookieAsyncCallback success!");
18. })
19. .catch((error: BusinessError) => {
20. console.error("error: " + error);
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

## putAcceptCookieEnabled

PhonePC/2in1TabletTVWearable

static putAcceptCookieEnabled(accept: boolean): void

设置WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accept | boolean | 是 | 设置是否拥有发送和接收cookie的权限，默认为true，表示拥有发送和接收cookie的权限。false表示没有发送和接收cookie的权限。 |

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
12. Button('putAcceptCookieEnabled')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.putAcceptCookieEnabled(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## isCookieAllowed

PhonePC/2in1TabletTVWearable

static isCookieAllowed(): boolean

获取WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否拥有发送和接收cookie的权限。  true表示拥有发送和接收cookie的权限，false表示无发送和接收cookie的权限。  默认值：true。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('isCookieAllowed')
12. .onClick(() => {
13. let result = webview.WebCookieManager.isCookieAllowed();
14. console.info("result: " + result);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## putAcceptThirdPartyCookieEnabled

PhonePC/2in1TabletTVWearable

static putAcceptThirdPartyCookieEnabled(accept: boolean): void

设置WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| accept | boolean | 是 | 是否允许设置、获取第三方cookie。  true表示允许设置、获取第三方cookie，false表示不允许设置、获取第三方cookie。 |

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
12. Button('putAcceptThirdPartyCookieEnabled')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.putAcceptThirdPartyCookieEnabled(false);
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## isThirdPartyCookieAllowed

PhonePC/2in1TabletTVWearable

static isThirdPartyCookieAllowed(): boolean

获取WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否拥有发送和接收第三方cookie的权限。  true表示拥有发送和接收第三方cookie的权限，false表示无发送和接收第三方cookie的权限。  默认值：false。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('isThirdPartyCookieAllowed')
12. .onClick(() => {
13. let result = webview.WebCookieManager.isThirdPartyCookieAllowed();
14. console.info("result: " + result);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## existCookie

PhonePC/2in1TabletTVWearable

static existCookie(incognito?: boolean): boolean

获取是否存在cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito11+ | boolean | 否 | true表示隐私模式下查询是否存在cookies，false表示正常非隐私模式下查询是否存在cookies。  默认值：false。  传入undefined或null时返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示存在cookie，false表示不存在cookie。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('existCookie')
12. .onClick(() => {
13. let result = webview.WebCookieManager.existCookie();
14. console.info("result: " + result);
15. })
16. Web({ src: 'www.example.com', controller: this.controller })
17. }
18. }
19. }
```

## clearAllCookiesSync11+

PhonePC/2in1TabletTVWearable

static clearAllCookiesSync(incognito?: boolean): void

清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito | boolean | 否 | true表示清除隐私模式下Webview的所有内存cookies，false表示清除正常非隐私模式下的持久化cookies。  默认值：false。  传入undefined或null时不清除cookies。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('clearAllCookiesSync')
12. .onClick(() => {
13. webview.WebCookieManager.clearAllCookiesSync();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## clearAllCookies11+

PhonePC/2in1TabletTVWearable

static clearAllCookies(callback: AsyncCallback<void>): void

异步callback方式清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | callback回调，用于获取清除所有cookie是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('clearAllCookies')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.clearAllCookies((error) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## clearAllCookies11+

PhonePC/2in1TabletTVWearable

static clearAllCookies(): Promise<void>

清除所有cookie。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取清除所有cookie是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

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
12. Button('clearAllCookies')
13. .onClick(() => {
14. webview.WebCookieManager.clearAllCookies()
15. .then(() => {
16. console.info("clearAllCookies success!");
17. })
18. .catch((error: BusinessError) => {
19. console.error("error: " + error);
20. });
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## clearSessionCookieSync11+

PhonePC/2in1TabletTVWearable

static clearSessionCookieSync(): void

清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('clearSessionCookieSync')
12. .onClick(() => {
13. webview.WebCookieManager.clearSessionCookieSync();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## clearSessionCookie11+

PhonePC/2in1TabletTVWearable

static clearSessionCookie(callback: AsyncCallback<void>): void

异步callback方式清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | callback回调，用于获取清除所有会话cookie是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('clearSessionCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.clearSessionCookie((error) => {
16. if (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## clearSessionCookie11+

PhonePC/2in1TabletTVWearable

static clearSessionCookie(): Promise<void>

清除所有会话cookie。使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于获取清除所有会话cookie是否成功。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

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
12. Button('clearSessionCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.clearSessionCookie()
16. .then(() => {
17. console.info("clearSessionCookie success!");
18. })
19. .catch((error: BusinessError) => {
20. console.error("error: " + error);
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

## setLazyInitializeWebEngine22+

PhonePC/2in1TabletTVWearable

static setLazyInitializeWebEngine(lazy: boolean): void

设置是否延后初始化ArkWeb内核，不调用该方法时，默认不延后初始化ArkWeb内核。

说明

* 该接口为全局静态方法，须在使用ArkWeb组件和初始化ArkWeb内核前调用，否则该设置无效。
* 该接口仅适用于调用后会初始化CookieManager的接口，比如本类WebCookieManager的其他接口。调用本接口设置为true后，再调用适用的接口，会在初始化CookieManager时跳过初始化ArkWeb内核，后续需自行初始化ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lazy | boolean | 是 | 是否延后初始化ArkWeb内核，true：延后，false：不延后。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. webview.WebCookieManager.setLazyInitializeWebEngine(true);

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();

11. aboutToAppear(): void {
12. webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
13. webview.WebCookieManager.fetchCookieSync('https://www.example.com');
14. }

16. build() {
17. Column() {
18. Web({ src: 'www.example.com', controller: this.controller })
19. }
20. }
21. }
```

## fetchAllCookies23+

PhonePC/2in1TabletTVWearable

static fetchAllCookies(incognito: boolean): Promise<Array<WebHttpCookie>>

获取所有cookie，使用Promise异步回调。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| incognito | boolean | 是 | true表示获取隐私模式下webview的所有cookie，false表示正常非隐私模式下的所有cookie。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[WebHttpCookie](arkts-apis-webview-i.md#webhttpcookie23)>> | Promise对象，用于获取所有cookie及其对应的字段值。 |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController()

10. build() {
11. Row() {
12. Column() {
13. Button('Config Cookie')
14. .onClick(() => {
15. try {
16. webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b');
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })

22. Button('Get All Cookies')
23. .onClick(() => {
24. webview.WebCookieManager.fetchAllCookies(false).then((cookies) => {
25. for (let i = 0; i < cookies.length; i++) {
26. console.info('fetchAllCookies cookie[' + i + '].name = ' + cookies[i].name);
27. console.info('fetchAllCookies cookie[' + i + '].value = ' + cookies[i].value);
28. }
29. })
30. })

32. Web({ src: 'https://www.example.com', controller: this.controller})
33. }
34. }
35. }
36. }
```

## getCookie(deprecated)

PhonePC/2in1TabletTVWearable

static getCookie(url: string): string

获取指定url对应cookie的值。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[fetchCookieSync](arkts-apis-webview-webcookiemanager.md#fetchcookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要获取的cookie所属的url，建议使用完整的url。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 指定url对应的cookie的值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
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
12. Button('getCookie')
13. .onClick(() => {
14. try {
15. let value = webview.WebCookieManager.getCookie('https://www.example.com');
16. console.info("value: " + value);
17. } catch (error) {
18. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
19. }
20. })
21. Web({ src: 'www.example.com', controller: this.controller })
22. }
23. }
24. }
```

## setCookie(deprecated)

PhonePC/2in1TabletTVWearable

static setCookie(url: string, value: string): void

为指定url设置单个cookie的值。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[configCookieSync11+](arkts-apis-webview-webcookiemanager.md#configcookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 要设置的cookie所属的url，建议使用完整的url。 |
| value | string | 是 | 要设置的cookie的值。 |

**错误码：**

以下错误码的详细介绍请参见[Webview错误码](errorcode-webview.md)、[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17100002 | URL error. No valid cookie found for the specified URL. |
| 17100005 | The provided cookie value is invalid. It must follow the format specified in RFC 6265. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |

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
12. Button('setCookie')
13. .onClick(() => {
14. try {
15. webview.WebCookieManager.setCookie('https://www.example.com', 'a=b');
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## deleteEntireCookie(deprecated)

PhonePC/2in1TabletTVWearable

static deleteEntireCookie(): void

清除所有cookie。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[clearAllCookiesSync](arkts-apis-webview-webcookiemanager.md#clearallcookiessync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('deleteEntireCookie')
12. .onClick(() => {
13. webview.WebCookieManager.deleteEntireCookie();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```

## deleteSessionCookie(deprecated)

PhonePC/2in1TabletTVWearable

static deleteSessionCookie(): void

清除所有会话cookie。

说明

从API version 9开始支持，从API version 11开始废弃。建议使用[clearSessionCookieSync](arkts-apis-webview-webcookiemanager.md#clearsessioncookiesync11)替代。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Button('deleteSessionCookie')
12. .onClick(() => {
13. webview.WebCookieManager.deleteSessionCookie();
14. })
15. Web({ src: 'www.example.com', controller: this.controller })
16. }
17. }
18. }
```
