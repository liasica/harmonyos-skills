---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdatabase
title: Class (WebDataBase)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (WebDataBase)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:04+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c628afc47c42adf72c9926a1c2afea1833866b073bb2d76fdb7811b0b12993e8
---

Web组件数据库管理对象。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 9开始支持。
* 示例效果请以真机运行为准。
* 目前调用WebDataBase下的方法，都需要先加载Web组件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## getHttpAuthCredentials

PhonePC/2in1TabletTVWearable

static getHttpAuthCredentials(host: string, realm: string): Array<string>

检索给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | HTTP身份验证凭据应用的主机。 |
| realm | string | 是 | HTTP身份验证凭据应用的域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 包含用户名和密码的数组，检索失败返回空数组。 |

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
9. host: string = "www.spincast.org";
10. realm: string = "protected example";
11. username_password: string[] = [];

13. build() {
14. Column() {
15. Button('getHttpAuthCredentials')
16. .onClick(() => {
17. try {
18. this.username_password = webview.WebDataBase.getHttpAuthCredentials(this.host, this.realm);
19. console.info('num: ' + this.username_password.length);
20. } catch (error) {
21. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
22. }
23. })
24. Web({ src: 'www.example.com', controller: this.controller })
25. }
26. }
27. }
```

## saveHttpAuthCredentials

PhonePC/2in1TabletTVWearable

static saveHttpAuthCredentials(host: string, realm: string, username: string, password: string): void

保存给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| host | string | 是 | HTTP身份验证凭据应用的主机。 |
| realm | string | 是 | HTTP身份验证凭据应用的域。 |
| username | string | 是 | 用户名。 |
| password | string | 是 | 密码。 |

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
9. host: string = "www.spincast.org";
10. realm: string = "protected example";

12. build() {
13. Column() {
14. Button('saveHttpAuthCredentials')
15. .onClick(() => {
16. try {
17. webview.WebDataBase.saveHttpAuthCredentials(this.host, this.realm, "Stromgol", "Laroche");
18. } catch (error) {
19. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
20. }
21. })
22. Web({ src: 'www.example.com', controller: this.controller })
23. }
24. }
25. }
```

## existHttpAuthCredentials

PhonePC/2in1TabletTVWearable

static existHttpAuthCredentials(): boolean

判断是否存在任何已保存的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否存在任何已保存的HTTP身份验证凭据。  存在返回true，不存在返回false。 |

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
12. Button('existHttpAuthCredentials')
13. .onClick(() => {
14. try {
15. let result = webview.WebDataBase.existHttpAuthCredentials();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```

## deleteHttpAuthCredentials

PhonePC/2in1TabletTVWearable

static deleteHttpAuthCredentials(): void

清除所有已保存的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

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
12. Button('deleteHttpAuthCredentials')
13. .onClick(() => {
14. try {
15. webview.WebDataBase.deleteHttpAuthCredentials();
16. } catch (error) {
17. console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
18. }
19. })
20. Web({ src: 'www.example.com', controller: this.controller })
21. }
22. }
23. }
```
