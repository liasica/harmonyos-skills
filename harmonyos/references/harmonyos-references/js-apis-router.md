---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router
title: @ohos.router (页面路由)(不推荐)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.router (页面路由)(不推荐)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad7c71f919aa4cda3f36f396849df4842feea3544f00f0de14b5944cd6dcf5d3
---

本模块提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。

推荐使用[Navigation组件](../harmonyos-guides/arkts-navigation-architecture.md)作为应用路由框架。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 页面路由需要在页面渲染完成之后才能调用，在onInit和onReady生命周期中页面还处于渲染阶段，禁止调用页面路由方法。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 如果使用传入callback形式的[pushUrl](arkts-apis-uicontext-router.md#pushurl-1)或[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-1)接口，callback中通过[getLength](arkts-apis-uicontext-router.md#getlengthdeprecated)等接口获取的栈信息为中间态的栈信息，可能与栈操作完全结束后，再通过[getLength](arkts-apis-uicontext-router.md#getlengthdeprecated)等接口获取的栈信息不一致。

## 导入模块

PhonePC/2in1TabletTVWearableLite Wearable

```
1. import { router } from '@kit.ArkUI';
```

## router.pushUrl(deprecated)

PhonePC/2in1TabletTVWearable

pushUrl(options: RouterOptions): Promise<void>

跳转到应用内的指定页面。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](arkts-apis-uicontext-router.md#pushurl)替代。pushUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class innerParams {
4. data3: number[];

6. constructor(tuple: number[]) {
7. this.data3 = tuple;
8. }
9. }

11. class RouterParams {
12. data1: string;
13. data2: innerParams;

15. constructor(str: string, tuple: number[]) {
16. this.data1 = str;
17. this.data2 = new innerParams(tuple);
18. }
19. }

21. router.pushUrl({
22. url: 'pages/routerpage2',
23. params: new RouterParams('message', [123, 456, 789])
24. })
25. .then(() => {
26. console.error(`pushUrl finish`);
27. })
28. .catch((err: ESObject) => {
29. console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
30. })
```

## router.pushUrl(deprecated)

PhonePC/2in1TabletTVWearable

pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](arkts-apis-uicontext-router.md#pushurl-1)替代。pushUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. class innerParams {
2. data3: number[];

4. constructor(tuple: number[]) {
5. this.data3 = tuple;
6. }
7. }

9. class RouterParams {
10. data1: string;
11. data2: innerParams;

13. constructor(str: string, tuple: number[]) {
14. this.data1 = str;
15. this.data2 = new innerParams(tuple);
16. }
17. }

19. router.pushUrl({
20. url: 'pages/routerpage2',
21. params: new RouterParams('message', [123, 456, 789])
22. }, (err) => {
23. if (err) {
24. console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
25. return;
26. }
27. console.info('pushUrl success');
28. })
```

## router.pushUrl(deprecated)

PhonePC/2in1TabletTVWearable

pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>

跳转到应用内的指定页面。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](arkts-apis-uicontext-router.md#pushurl-2)替代。pushUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class innerParams {
4. data3: number[];

6. constructor(tuple: number[]) {
7. this.data3 = tuple;
8. }
9. }

11. class RouterParams {
12. data1: string;
13. data2: innerParams;

15. constructor(str: string, tuple: number[]) {
16. this.data1 = str;
17. this.data2 = new innerParams(tuple);
18. }
19. }

21. router.pushUrl({
22. url: 'pages/routerpage2',
23. params: new RouterParams('message', [123, 456, 789])
24. }, router.RouterMode.Standard)
25. .then(() => {
26. console.error(`pushUrl finish`);
27. })
28. .catch((err: ESObject) => {
29. console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
30. })
```

## router.pushUrl(deprecated)

PhonePC/2in1TabletTVWearable

pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[pushUrl](arkts-apis-uicontext-router.md#pushurl-3)替代。pushUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. class innerParams {
2. data3: number[];

4. constructor(tuple: number[]) {
5. this.data3 = tuple;
6. }
7. }

9. class RouterParams {
10. data1: string;
11. data2: innerParams;

13. constructor(str: string, tuple: number[]) {
14. this.data1 = str;
15. this.data2 = new innerParams(tuple);
16. }
17. }

19. router.pushUrl({
20. url: 'pages/routerpage2',
21. params: new RouterParams('message', [123, 456, 789])
22. }, router.RouterMode.Standard, (err) => {
23. if (err) {
24. console.error(`pushUrl failed, code is ${err.code}, message is ${err.message}`);
25. return;
26. }
27. console.info('pushUrl success');
28. })
```

## router.replaceUrl(deprecated)

PhonePC/2in1TabletTVWearableLite Wearable

replaceUrl(options: RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../harmonyos-guides/arkts-navigation-architecture.md)。

说明

* 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](arkts-apis-uicontext-router.md#replaceurl)替代。replaceUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class RouterParams {
4. data1: string;

6. constructor(str: string) {
7. this.data1 = str;
8. }
9. }

11. router.replaceUrl({
12. url: 'pages/detail',
13. params: new RouterParams('message')
14. })
15. .then(() => {
16. console.error(`replaceUrl finish`);
17. })
18. .catch((err: ESObject) => {
19. console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
20. })
```

## router.replaceUrl(deprecated)

PhonePC/2in1TabletTVWearableLite Wearable

replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](arkts-apis-uicontext-router.md#replaceurl-1)替代。replaceUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. class RouterParams {
2. data1: string;

4. constructor(str: string) {
5. this.data1 = str;
6. }
7. }

9. router.replaceUrl({
10. url: 'pages/detail',
11. params: new RouterParams('message')
12. }, (err) => {
13. if (err) {
14. console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
15. return;
16. }
17. console.info('replaceUrl success');
18. })
```

## router.replaceUrl(deprecated)

PhonePC/2in1TabletTVWearableLite Wearable

replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](arkts-apis-uicontext-router.md#replaceurl-2)替代。replaceUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class RouterParams {
4. data1:string;

6. constructor(str:string) {
7. this.data1 = str;
8. }
9. }

11. router.replaceUrl({
12. url: 'pages/detail',
13. params: new RouterParams('message')
14. }, router.RouterMode.Standard)
15. .then(() => {
16. console.error(`replaceUrl finish`);
17. })
18. .catch((err: ESObject) => {
19. console.error(`replaceUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
20. })
```

## router.replaceUrl(deprecated)

PhonePC/2in1TabletTVWearableLite Wearable

replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用[replaceUrl](arkts-apis-uicontext-router.md#replaceurl-3)替代。replaceUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. class RouterParams {
2. data1: string;

4. constructor(str: string) {
5. this.data1 = str;
6. }
7. }

9. router.replaceUrl({
10. url: 'pages/detail',
11. params: new RouterParams('message')
12. }, router.RouterMode.Standard, (err) => {
13. if (err) {
14. console.error(`replaceUrl failed, code is ${err.code}, message is ${err.message}`);
15. return;
16. }
17. console.info('replaceUrl success');
18. });
```

## router.pushNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute)替代。pushNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class innerParams {
4. data3: number[];

6. constructor(tuple: number[]) {
7. this.data3 = tuple;
8. }
9. }

11. class RouterParams {
12. data1: string;
13. data2: innerParams;

15. constructor(str: string, tuple: number[]) {
16. this.data1 = str;
17. this.data2 = new innerParams(tuple);
18. }
19. }

21. router.pushNamedRoute({
22. name: 'myPage',
23. params: new RouterParams('message', [123, 456, 789])
24. })
25. .then(() => {
26. console.error(`pushNamedRoute finish`);
27. })
28. .catch((err: ESObject) => {
29. console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
30. })
```

详细示例请参考：[UI开发-命名路由](../harmonyos-guides/arkts-routing.md#命名路由)

## router.pushNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-1)替代。pushNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. class innerParams {
2. data3: number[];

4. constructor(tuple: number[]) {
5. this.data3 = tuple;
6. }
7. }

9. class RouterParams {
10. data1: string;
11. data2: innerParams;

13. constructor(str: string, tuple: number[]) {
14. this.data1 = str;
15. this.data2 = new innerParams(tuple);
16. }
17. }

19. router.pushNamedRoute({
20. name: 'myPage',
21. params: new RouterParams('message', [123, 456, 789])
22. }, (err) => {
23. if (err) {
24. console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
25. return;
26. }
27. console.info('pushNamedRoute success');
28. })
```

## router.pushNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

跳转到指定的命名路由页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-2)替代。pushNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class innerParams {
4. data3: number[];

6. constructor(tuple: number[]) {
7. this.data3 = tuple;
8. }
9. }

11. class RouterParams {
12. data1: string;
13. data2: innerParams;

15. constructor(str: string, tuple: number[]) {
16. this.data1 = str
17. this.data2 = new innerParams(tuple)
18. }
19. }

21. router.pushNamedRoute({
22. name: 'myPage',
23. params: new RouterParams('message', [123, 456, 789])
24. }, router.RouterMode.Standard)
25. .then(() => {
26. console.error(`pushNamedRoute finish`);
27. })
28. .catch((err: ESObject) => {
29. console.error(`pushNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
30. })
```

## router.pushNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-3)替代。pushNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. class innerParams {
2. data3: number[];

4. constructor(tuple: number[]) {
5. this.data3 = tuple;
6. }
7. }

9. class RouterParams {
10. data1: string;
11. data2: innerParams;

13. constructor(str: string, tuple: number[]) {
14. this.data1 = str;
15. this.data2 = new innerParams(tuple);
16. }
17. }

19. router.pushNamedRoute({
20. name: 'myPage',
21. params: new RouterParams('message', [123, 456, 789])
22. }, router.RouterMode.Standard, (err) => {
23. if (err) {
24. console.error(`pushNamedRoute failed, code is ${err.code}, message is ${err.message}`);
25. return;
26. }
27. console.info('pushNamedRoute success');
28. })
```

## router.replaceNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute)替代。replaceNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class RouterParams {
4. data1: string;

6. constructor(str: string) {
7. this.data1 = str;
8. }
9. }

11. router.replaceNamedRoute({
12. name: 'myPage',
13. params: new RouterParams('message')
14. })
15. .then(() => {
16. console.error(`replaceNamedRoute finish`);
17. })
18. .catch((err: ESObject) => {
19. console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
20. })
```

## router.replaceNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute-1)替代。replaceNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. class RouterParams {
2. data1: string;

4. constructor(str: string) {
5. this.data1 = str;
6. }
7. }

9. router.replaceNamedRoute({
10. name: 'myPage',
11. params: new RouterParams('message')
12. }, (err) => {
13. if (err) {
14. console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
15. return;
16. }
17. console.info('replaceNamedRoute success');
18. })
```

## router.replaceNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute-2)替代。replaceNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 异常返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class RouterParams {
4. data1: string;

6. constructor(str: string) {
7. this.data1 = str;
8. }
9. }

11. router.replaceNamedRoute({
12. name: 'myPage',
13. params: new RouterParams('message')
14. }, router.RouterMode.Standard)
15. .then(() => {
16. console.error(`replaceNamedRoute finish`);
17. })
18. .catch((err: ESObject) => {
19. console.error(`replaceNamedRoute failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
20. })
```

## router.replaceNamedRoute(deprecated)

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute-3)替代。replaceNamedRoute需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | 异常响应回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

说明

该接口返回的以下错误码均为string类型。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. class RouterParams {
2. data1: string;

4. constructor(str: string) {
5. this.data1 = str;
6. }
7. }

9. router.replaceNamedRoute({
10. name: 'myPage',
11. params: new RouterParams('message')
12. }, router.RouterMode.Standard, (err) => {
13. if (err) {
14. console.error(`replaceNamedRoute failed, code is ${err.code}, message is ${err.message}`);
15. return;
16. }
17. console.info('replaceNamedRoute success');
18. });
```

## router.back(deprecated)

PhonePC/2in1TabletTVWearable

back(options?: RouterOptions ): void

返回上一页面或指定的页面，会删除当前页面与指定页面之间的所有页面。

说明

* 从API version 8开始支持，从API version 18开始废弃，建议使用[back](arkts-apis-uicontext-router.md#back)替代。back需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 否 | 返回页面描述信息，其中参数url指路由跳转时会返回到指定url的界面，如果页面栈上没有url页面，则不响应该情况。如果url未设置，则返回上一页，页面不会重新构建，页面栈里面的page不会回收，出栈后会被回收。back是返回接口，url设置为特殊值"/"不生效。如果是用命名路由的方式跳转，传入的url需是命名路由的名称。 |

**示例：**

```
1. this.getUIContext().getRouter().back({ url: 'pages/detail' });
```

## router.back(deprecated)

PhonePC/2in1TabletTVWearable

back(index: number, params?: Object): void;

返回指定的页面，会删除当前页面与指定页面之间的所有页面。

说明

* 从API version 12开始支持，从API version 18开始废弃，建议使用[back](arkts-apis-uicontext-router.md#back12)替代。back需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 跳转目标页面的索引值。 从栈底到栈顶，index从1开始递增。 |
| params | Object | 否 | 页面返回时携带的参数。 |

**示例：**

```
1. this.getUIContext().getRouter().back(1);
```

```
1. this.getUIContext().getRouter().back(1, { info: '来自Home页' }); //携带参数返回
```

## router.clear(deprecated)

PhonePC/2in1TabletTVWearable

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

说明

* 从API version 8开始支持，从API version 18开始废弃，建议使用[clear](arkts-apis-uicontext-router.md#clear)替代。clear需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. this.getUIContext().getRouter().clear();
```

## router.getLength(deprecated)

PhonePC/2in1TabletTVWearable

getLength(): string

获取当前在页面栈内的页面数量。

说明

* 从API version 8开始支持，从API version 18开始废弃，建议使用[getLength](arkts-apis-uicontext-router.md#getlengthdeprecated)替代。getLength需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

**示例：**

```
1. let size = this.getUIContext().getRouter().getLength();
2. console.info('pages stack size = ' + size);
```

## router.getState(deprecated)

PhonePC/2in1TabletTVWearable

getState(): RouterState

获取栈顶页面的状态信息。

说明

* 从API version 8开始支持，从API version 18开始废弃，建议使用[getState](arkts-apis-uicontext-router.md#getstate)替代。getLength需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RouterState](js-apis-router.md#routerstate) | 页面状态信息。 |

**示例：**

```
1. let page = this.getUIContext().getRouter().getState();
2. console.info('current index = ' + page.index);
3. console.info('current name = ' + page.name);
4. console.info('current path = ' + page.path);
```

## router.getStateByIndex(deprecated)

PhonePC/2in1TabletTVWearable

getStateByIndex(index: number): RouterState | undefined

通过索引值获取对应页面的状态信息。

说明

* 从API version 12开始支持，从API version 18开始废弃，建议使用[getStateByIndex](arkts-apis-uicontext-router.md#getstatebyindex12)替代。getStateByIndex需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 表示要获取的页面索引。从栈底到栈顶，index从1开始递增。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RouterState](js-apis-router.md#routerstate) | undefined | 返回页面状态信息。索引不存在时返回undefined。 |

**示例：**

```
1. let options: router.RouterState | undefined = router.getStateByIndex(1);
2. if (options != undefined) {
3. console.info('index = ' + options.index);
4. console.info('name = ' + options.name);
5. console.info('path = ' + options.path);
6. console.info(`params = ${JSON.stringify(options.params)}`);
7. }
```

## router.getStateByUrl(deprecated)

PhonePC/2in1TabletTVWearable

getStateByUrl(url: string): Array<RouterState>

通过url获取对应页面的状态信息。

说明

* 从API version 12开始支持，从API version 18开始废弃，建议使用[getStateByUrl](arkts-apis-uicontext-router.md#getstatebyurl12)替代。getStateByUrl需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 表示要获取对应页面信息的url。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[RouterState](js-apis-router.md#routerstate)> | 页面状态信息。 |

**示例：**

```
1. let options: Array<router.RouterState> = router.getStateByUrl('pages/index');
2. for (let i: number = 0; i < options.length; i++) {
3. console.info('index = ' + options[i].index);
4. console.info('name = ' + options[i].name);
5. console.info('path = ' + options[i].path);
6. console.info('params = ' + options[i].params);
7. }
```

## RouterState

PhonePC/2in1TabletTVWearable

页面状态信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| index | number | 否 | 否 | 表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 表示当前页面的名称，即对应文件名。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| path | string | 否 | 否 | 表示当前页面的路径。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| params12+ | Object | 否 | 否 | 表示当前页面携带的参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## router.showAlertBeforeBackPage(deprecated)

PhonePC/2in1TabletTVWearable

showAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[showAlertBeforeBackPage](arkts-apis-uicontext-router.md#showalertbeforebackpage)替代。showAlertBeforeBackPage需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EnableAlertOptions](js-apis-router.md#enablealertoptions) | 是 | 文本弹窗信息描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. this.getUIContext().getRouter().showAlertBeforeBackPage({
5. message: 'Message Info'
6. });
7. } catch (err) {
8. console.error(`showAlertBeforeBackPage failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
9. }
```

## EnableAlertOptions

PhonePC/2in1TabletTVWearable

页面返回询问对话框选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| message | string | 否 | 否 | 询问对话框内容。 |

## router.hideAlertBeforeBackPage(deprecated)

PhonePC/2in1TabletTVWearable

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。

说明

* 从API version 9开始支持，从API version 18开始废弃，建议使用[hideAlertBeforeBackPage](arkts-apis-uicontext-router.md#hidealertbeforebackpage)替代。hideAlertBeforeBackPage需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. this.getUIContext().getRouter().hideAlertBeforeBackPage();
```

## router.getParams(deprecated)

PhonePC/2in1TabletTVWearable

getParams(): Object

获取发起跳转的页面往当前页传入的参数。

说明

* 从API version 8开始支持，从API version 18开始废弃，建议使用[getParams](arkts-apis-uicontext-router.md#getparams)替代。getParams需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](arkts-apis-uicontext-router.md)实例，然后通过该实例进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的[Router](arkts-apis-uicontext-router.md)对象。

getParams只获取当前页面的参数，并不会清除页面关联的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 发起跳转的页面往当前页传入的参数。 |

**示例：**

```
1. this.getUIContext().getRouter().getParams();
```

## RouterOptions

PhonePC/2in1TabletTVWearableLite Wearable

路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 表示目标页面的url，可以用以下两种格式：  - 页面绝对路径，由配置文件中pages列表提供，例如：  - pages/index/index  - pages/detail/detail  - 特殊值，如果url的值是"/"，则跳转到首页，首页默认为页面跳转配置项src数组的第一个数据项。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| params | Object | 否 | 是 | 表示路由跳转时要同时传递到目标页面的数据，切换到其他页面时，当前接收的数据失效。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。  **说明：**  params参数只能传递可序列化的参数，不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| recoverable14+ | boolean | 否 | 是 | 表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。  **说明：**  当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)。 |

说明

页面路由栈支持的最大Page数量为32。

## RouterMode9+

PhonePC/2in1TabletTVWearable

路由跳转模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Standard | 0 | 多实例模式，也是默认情况下的跳转模式。  目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。  **说明：**  不使用路由跳转模式时，则按照默认的多实例模式进行跳转。 |
| Single | 1 | 单实例模式。  如果目标页面的url已经存在于页面栈中，则该url页面移动到栈顶。  如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。 |

## NamedRouterOptions10+

PhonePC/2in1TabletTVWearableLite Wearable

命名路由跳转选项。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 表示目标命名路由页面的name。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| params | Object | 否 | 是 | 表示路由跳转时要同时传递到目标页面的数据。跳转到目标页面后，使用router.getParams()获取传递的参数，此外，在类web范式中，参数也可以在页面中直接使用，如this.keyValue(keyValue为跳转时params参数中的key值)，如果目标页面中已有该字段，则其值会被传入的字段值覆盖。  **说明：**  params参数不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| recoverable14+ | boolean | 否 | 是 | 表示对应的页面是否可恢复，默认为true。当为true时，表示可恢复，当为false时，表示不可恢复。  **说明：**  当应用退到后台，并且在未来的某个时间点，由于系统资源限制等原因被系统杀死，如果某个页面被设置成可恢复，那么该应用再次被拉到前台后系统可以恢复出页面，详细说明请参考[UIAbility备份恢复](../harmonyos-guides/ability-recover-guideline.md)。  **系统能力：** SystemCapability.ArkUI.ArkUI.Lite |

## 完整示例

PhonePC/2in1TabletTVWearableLite Wearable

### 基于JS扩展的类Web开发范式

以下代码仅适用于javascript文件，不适用于ArkTS文件

```
1. // 在当前页面中
2. export default {
3. pushPage() {
4. router.pushUrl({
5. url: 'pages/detail/detail',
6. params: {
7. data1: 'message'
8. }
9. });
10. }
11. }
```

```
1. // 在detail页面中
2. export default {
3. onInit() {
4. console.info('showData1:' + this.getUIContext().getRouter().getParams()['data1']);
5. }
6. }
```

### 基于TS扩展的声明式开发范式

说明

直接使用router可能导致[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext获取[UIContext](arkts-apis-uicontext-uicontext.md)实例，并使用[getRouter](arkts-apis-uicontext-uicontext.md#getrouter)获取绑定实例的router。

```
1. // 通过router.pushUrl跳转至目标页携带params参数
2. import { router } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. // 定义传递参数的类
6. class innerParams {
7. array: number[];

9. constructor(tuple: number[]) {
10. this.array = tuple;
11. }
12. }

14. class RouterParams {
15. text: string;
16. data: innerParams;

18. constructor(str: string, tuple: number[]) {
19. this.text = str;
20. this.data = new innerParams(tuple);
21. }
22. }

24. @Entry
25. @Component
26. struct Index {
27. async routePage() {
28. let options: router.RouterOptions = {
29. url: 'pages/second',
30. params: new RouterParams('这是第一页的值', [12, 45, 78])
31. }
32. // 建议使用this.getUIContext().getRouter().pushUrl()
33. this.getUIContext().getRouter().pushUrl(options)
34. .then(() => {
35. console.error(`pushUrl finish`);
36. })
37. .catch((err: ESObject) => {
38. console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
39. })
40. }

42. build() {
43. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
44. Text('这是第一页')
45. .fontSize(50)
46. .fontWeight(FontWeight.Bold)
47. Button() {
48. Text('next page')
49. .fontSize(25)
50. .fontWeight(FontWeight.Bold)
51. }.type(ButtonType.Capsule)
52. .margin({ top: 20 })
53. .backgroundColor('#ccc')
54. .onClick(() => {
55. this.routePage()
56. })
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

```
1. // 在second页面中接收传递过来的参数
2. import { router } from '@kit.ArkUI';

4. class innerParams {
5. array: number[];

7. constructor(tuple: number[]) {
8. this.array = tuple;
9. }
10. }

12. class RouterParams {
13. text: string;
14. data: innerParams;

16. constructor(str: string, tuple: number[]) {
17. this.text = str;
18. this.data = new innerParams(tuple);
19. }
20. }

22. @Entry
23. @Component
24. struct Second {
25. private content: string = "这是第二页";
26. // 建议使用this.getUIContext().getRouter().getParams()
27. @State text: string = (this.getUIContext().getRouter().getParams() as RouterParams).text;
28. @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
29. @State secondData: string = '';

31. build() {
32. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
33. Text(`${this.content}`)
34. .fontSize(50)
35. .fontWeight(FontWeight.Bold)
36. Text(this.text)
37. .fontSize(30)
38. .onClick(() => {
39. this.secondData = (this.data['array'][1]).toString();
40. })
41. .margin({ top: 20 })
42. Text(`第一页传来的数值:${this.secondData}`)
43. .fontSize(20)
44. .margin({ top: 20 })
45. .backgroundColor('red')
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

## router.push(deprecated)

PhonePC/2in1TabletTVWearable

push(options: RouterOptions): void

跳转到应用内的指定页面。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[pushUrl](arkts-apis-uicontext-router.md#pushurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |

**示例：**

```
1. class innerParams {
2. data3: number[];

4. constructor(tuple: number[]) {
5. this.data3 = tuple;
6. }
7. }

9. class RouterParams {
10. data1: string;
11. data2: innerParams;

13. constructor(str: string, tuple: number[]) {
14. this.data1 = str;
15. this.data2 = new innerParams(tuple);
16. }
17. }

19. router.push({
20. url: 'pages/routerpage2',
21. params: new RouterParams('message', [123, 456, 789])
22. });
```

## router.replace(deprecated)

PhonePC/2in1TabletTVWearableLite Wearable

replace(options: RouterOptions): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[replaceUrl](arkts-apis-uicontext-router.md#replaceurl)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |

**示例：**

```
1. class RouterParams {
2. data1: string;

4. constructor(str: string) {
5. this.data1 = str;
6. }
7. }

9. router.replace({
10. url: 'pages/detail',
11. params: new RouterParams('message')
12. });
```

## router.enableAlertBeforeBackPage(deprecated)

PhonePC/2in1TabletTVWearable

enableAlertBeforeBackPage(options: EnableAlertOptions): void

开启页面返回询问对话框。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[showAlertBeforeBackPage](arkts-apis-uicontext-router.md#showalertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [EnableAlertOptions](js-apis-router.md#enablealertoptions) | 是 | 文本弹窗信息描述。 |

**示例：**

```
1. router.enableAlertBeforeBackPage({
2. message: 'Message Info'
3. });
```

## router.disableAlertBeforeBackPage(deprecated)

PhonePC/2in1TabletTVWearable

disableAlertBeforeBackPage(): void

禁用页面返回询问对话框。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[hideAlertBeforeBackPage](arkts-apis-uicontext-router.md#hidealertbeforebackpage)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. router.disableAlertBeforeBackPage();
```
