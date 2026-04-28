---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router
title: Class (Router)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (Router)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4418a2c70179c140c89cc0ce5fe068a734929c6a160d5193869368940002317e
---

提供通过不同的url访问不同的页面，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getRouter()](arkts-apis-uicontext-uicontext.md#getrouter)方法获取到Router对象，再通过该对象调用对应方法。

## pushUrl

PhonePC/2in1TabletTVWearable

pushUrl(options: router.RouterOptions): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 定义传递参数的类
5. class innerParams {
6. array: number[];

8. constructor(tuple: number[]) {
9. this.array = tuple;
10. }
11. }

13. class RouterParams {
14. data: innerParams;

16. constructor(tuple: number[]) {
17. this.data = new innerParams(tuple);
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. async routePage() {
25. let options: router.RouterOptions = {
26. url: 'pages/second',
27. params: new RouterParams([12, 45, 78])
28. }
29. this.getUIContext()
30. .getRouter()
31. .pushUrl(options)
32. .then(() => {
33. console.info('pushUrl success');
34. })
35. .catch((err: ESObject) => {
36. console.error(`pushUrl failed, code is ${(err as BusinessError).code}, message is ${(err as BusinessError).message}`);
37. })
38. }

40. build() {
41. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
42. Text('First Page')
43. Button('Next page')
44. .type(ButtonType.Capsule)
45. .margin({ top: 20 })
46. .onClick(() => {
47. this.routePage()
48. })
49. }
50. .width('100%')
51. .height('100%')
52. }
53. }
```

```
1. // 在second页面中接收传递过来的参数
2. class innerParams {
3. array: number[];

5. constructor(tuple: number[]) {
6. this.array = tuple;
7. }
8. }

10. class RouterParams {
11. data: innerParams;

13. constructor(tuple: number[]) {
14. this.data = new innerParams(tuple);
15. }
16. }

18. @Entry
19. @Component
20. struct Second {
21. @State data: object = (this.getUIContext().getRouter().getParams() as RouterParams).data;
22. @State secondData: string = '';

24. build() {
25. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
26. Text('Second Page')
27. Button('Back')
28. .fontSize(30)
29. .onClick(() => {
30. try {
31. this.getUIContext().getRouter().showAlertBeforeBackPage({ message: 'Are you sure to return?' })
32. } catch (error) {
33. // TODO: Implement error handling.
34. }
35. this.getUIContext().getRouter().back()
36. })
37. .margin({ top: 20 })
38. Button(`The value on the first page：${this.secondData}`)
39. .margin({ top: 20 })
40. .onClick(()=> {
41. this.secondData = (this.data['array'][1]).toString();
42. })
43. }
44. .width('100%')
45. .height('100%')
46. }
47. }
```

## pushUrl

PhonePC/2in1TabletTVWearable

pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().pushUrl({
8. url: 'pages/routerpage2',
9. params: {
10. data1: 'message',
11. data2: {
12. data3: [123, 456, 789]
13. }
14. }
15. }, (err: Error) => {
16. if (err) {
17. let message = (err as BusinessError).message;
18. let code = (err as BusinessError).code;
19. console.error(`pushUrl failed, code is ${code}, message is ${message}`);
20. return;
21. }
22. console.info('pushUrl success');
23. })
24. }

26. build() {
27. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
28. Button() {
29. Text('next page')
30. .fontSize(25)
31. .fontWeight(FontWeight.Bold)
32. }.type(ButtonType.Capsule)
33. .margin({ top: 20 })
34. .backgroundColor('#ccc')
35. .onClick(() => {
36. this.routePage();
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

## pushUrl

PhonePC/2in1TabletTVWearable

pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

跳转到应用内的指定页面，使用Promise异步回调。与[pushUrl](arkts-apis-uicontext-router.md#pushurl)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().pushUrl({
15. url: 'pages/routerpage2',
16. params: {
17. data1: 'message',
18. data2: {
19. data3: [123, 456, 789]
20. }
21. }
22. }, rtm.Standard)
23. .then(() => {
24. console.info('succeeded');
25. })
26. .catch((error: BusinessError) => {
27. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
28. })
29. }

31. build() {
32. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
33. Button() {
34. Text('next page')
35. .fontSize(25)
36. .fontWeight(FontWeight.Bold)
37. }.type(ButtonType.Capsule)
38. .margin({ top: 20 })
39. .backgroundColor('#ccc')
40. .onClick(() => {
41. this.routePage();
42. })
43. }
44. .width('100%')
45. .height('100%')
46. }
47. }
```

## pushUrl

PhonePC/2in1TabletTVWearable

pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到应用内的指定页面。使用callback异步回调。与[pushUrl](arkts-apis-uicontext-router.md#pushurl-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist. |
| 100003 | Page stack error. Too many pages are pushed. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().pushUrl({
15. url: 'pages/routerpage2',
16. params: {
17. data1: 'message',
18. data2: {
19. data3: [123, 456, 789]
20. }
21. }
22. }, rtm.Standard, (err) => {
23. if (err) {
24. let message = (err as BusinessError).message;
25. let code = (err as BusinessError).code;
26. console.error(`pushUrl failed, code is ${code}, message is ${message}`);
27. return;
28. }
29. console.info('pushUrl success');
30. })
31. }

33. build() {
34. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
35. Button() {
36. Text('next page')
37. .fontSize(25)
38. .fontWeight(FontWeight.Bold)
39. }.type(ButtonType.Capsule)
40. .margin({ top: 20 })
41. .backgroundColor('#ccc')
42. .onClick(() => {
43. this.routePage();
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

## replaceUrl

PhonePC/2in1TabletTVWearable

replaceUrl(options: router.RouterOptions): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().replaceUrl({
8. url: 'pages/detail',
9. params: {
10. data1: 'message'
11. }
12. })
13. .then(() => {
14. console.info('succeeded');
15. })
16. .catch((error: BusinessError) => {
17. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
18. })
19. }

21. build() {
22. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
23. Button() {
24. Text('next page')
25. .fontSize(25)
26. .fontWeight(FontWeight.Bold)
27. }.type(ButtonType.Capsule)
28. .margin({ top: 20 })
29. .backgroundColor('#ccc')
30. .onClick(() => {
31. this.routePage();
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

## replaceUrl

PhonePC/2in1TabletTVWearable

replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().replaceUrl({
8. url: 'pages/detail',
9. params: {
10. data1: 'message'
11. }
12. }, (err: Error) => {
13. if (err) {
14. let message = (err as BusinessError).message;
15. let code = (err as BusinessError).code;
16. console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
17. return;
18. }
19. console.info('replaceUrl success');
20. })
21. }

23. build() {
24. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
25. Button() {
26. Text('next page')
27. .fontSize(25)
28. .fontWeight(FontWeight.Bold)
29. }.type(ButtonType.Capsule)
30. .margin({ top: 20 })
31. .backgroundColor('#ccc')
32. .onClick(() => {
33. this.routePage();
34. })
35. }
36. .width('100%')
37. .height('100%')
38. }
39. }
```

## replaceUrl

PhonePC/2in1TabletTVWearable

replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>

用应用内的某个页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceUrl](arkts-apis-uicontext-router.md#replaceurl)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().replaceUrl({
15. url: 'pages/detail',
16. params: {
17. data1: 'message'
18. }
19. }, rtm.Standard)
20. .then(() => {
21. console.info('succeeded');
22. })
23. .catch((error: BusinessError) => {
24. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
25. })
26. }

28. build() {
29. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
30. Button() {
31. Text('next page')
32. .fontSize(25)
33. .fontWeight(FontWeight.Bold)
34. }.type(ButtonType.Capsule)
35. .margin({ top: 20 })
36. .backgroundColor('#ccc')
37. .onClick(() => {
38. this.routePage();
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

## replaceUrl

PhonePC/2in1TabletTVWearable

replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用应用内的某个页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceUrl](arkts-apis-uicontext-router.md#replaceurl-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 200002 | Uri error. The URI of the page to be used for replacement is incorrect or does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().replaceUrl({
15. url: 'pages/detail',
16. params: {
17. data1: 'message'
18. }
19. }, rtm.Standard, (err: Error) => {
20. if (err) {
21. let message = (err as BusinessError).message;
22. let code = (err as BusinessError).code;
23. console.error(`replaceUrl failed, code is ${code}, message is ${message}`);
24. return;
25. }
26. console.info('replaceUrl success');
27. });
28. }

30. build() {
31. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
32. Button() {
33. Text('next page')
34. .fontSize(25)
35. .fontWeight(FontWeight.Bold)
36. }.type(ButtonType.Capsule)
37. .margin({ top: 20 })
38. .backgroundColor('#ccc')
39. .onClick(() => {
40. this.routePage();
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

## pushNamedRoute

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: router.NamedRouterOptions): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().pushNamedRoute({
8. name: 'myPage',
9. params: {
10. data1: 'message',
11. data2: {
12. data3: [123, 456, 789]
13. }
14. }
15. })
16. .then(() => {
17. console.info('succeeded');
18. })
19. .catch((error: BusinessError) => {
20. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
21. })
22. }

24. build() {
25. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
26. Button() {
27. Text('next page')
28. .fontSize(25)
29. .fontWeight(FontWeight.Bold)
30. }.type(ButtonType.Capsule)
31. .margin({ top: 20 })
32. .backgroundColor('#ccc')
33. .onClick(() => {
34. this.routePage();
35. })
36. }
37. .width('100%')
38. .height('100%')
39. }
40. }
```

## pushNamedRoute

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().pushNamedRoute({
8. name: 'myPage',
9. params: {
10. data1: 'message',
11. data2: {
12. data3: [123, 456, 789]
13. }
14. }
15. }, (err: Error) => {
16. if (err) {
17. let message = (err as BusinessError).message;
18. let code = (err as BusinessError).code;
19. console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
20. return;
21. }
22. console.info('pushNamedRoute success');
23. })
24. }

26. build() {
27. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
28. Button() {
29. Text('next page')
30. .fontSize(25)
31. .fontWeight(FontWeight.Bold)
32. }.type(ButtonType.Capsule)
33. .margin({ top: 20 })
34. .backgroundColor('#ccc')
35. .onClick(() => {
36. this.routePage();
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

## pushNamedRoute

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

跳转到指定的命名路由页面，使用Promise异步回调。与[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp{
5. Standard:router.RouterMode = router.RouterMode.Standard;
6. }
7. let rtm:RouterTmp = new RouterTmp();

9. @Entry
10. @Component
11. struct Index {
12. async routePage() {
13. this.getUIContext().getRouter().pushNamedRoute({
14. name: 'myPage',
15. params: {
16. data1: 'message',
17. data2: {
18. data3: [123, 456, 789]
19. }
20. }
21. }, rtm.Standard)
22. .then(() => {
23. console.info('succeeded');
24. })
25. .catch((error: BusinessError) => {
26. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
27. })
28. }

30. build() {
31. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
32. Button() {
33. Text('next page')
34. .fontSize(25)
35. .fontWeight(FontWeight.Bold)
36. }.type(ButtonType.Capsule)
37. .margin({ top: 20 })
38. .backgroundColor('#ccc')
39. .onClick(() => {
40. this.routePage();
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

## pushNamedRoute

PhonePC/2in1TabletTVWearable

pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

跳转到指定的命名路由页面。使用callback异步回调。与[pushNamedRoute](arkts-apis-uicontext-router.md#pushnamedroute-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 跳转页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().pushNamedRoute({
15. name: 'myPage',
16. params: {
17. data1: 'message',
18. data2: {
19. data3: [123, 456, 789]
20. }
21. }
22. }, rtm.Standard, (err: Error) => {
23. if (err) {
24. let message = (err as BusinessError).message;
25. let code = (err as BusinessError).code;
26. console.error(`pushNamedRoute failed, code is ${code}, message is ${message}`);
27. return;
28. }
29. console.info('pushNamedRoute success');
30. })
31. }

33. build() {
34. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
35. Button() {
36. Text('next page')
37. .fontSize(25)
38. .fontWeight(FontWeight.Bold)
39. }.type(ButtonType.Capsule)
40. .margin({ top: 20 })
41. .backgroundColor('#ccc')
42. .onClick(() => {
43. this.routePage();
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

## replaceNamedRoute

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the number of parameters is less than 1 or the type of the url parameter is not string. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().replaceNamedRoute({
8. name: 'myPage',
9. params: {
10. data1: 'message'
11. }
12. })
13. .then(() => {
14. console.info('succeeded');
15. })
16. .catch((error: BusinessError) => {
17. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
18. })
19. }

21. build() {
22. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
23. Button() {
24. Text('next page')
25. .fontSize(25)
26. .fontWeight(FontWeight.Bold)
27. }.type(ButtonType.Capsule)
28. .margin({ top: 20 })
29. .backgroundColor('#ccc')
30. .onClick(() => {
31. this.routePage();
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

## replaceNamedRoute

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. async routePage() {
7. this.getUIContext().getRouter().replaceNamedRoute({
8. name: 'myPage',
9. params: {
10. data1: 'message'
11. }
12. }, (err: Error) => {
13. if (err) {
14. let message = (err as BusinessError).message;
15. let code = (err as BusinessError).code;
16. console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
17. return;
18. }
19. console.info('replaceNamedRoute success');
20. })
21. }

23. build() {
24. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
25. Button() {
26. Text('next page')
27. .fontSize(25)
28. .fontWeight(FontWeight.Bold)
29. }.type(ButtonType.Capsule)
30. .margin({ top: 20 })
31. .backgroundColor('#ccc')
32. .onClick(() => {
33. this.routePage();
34. })
35. }
36. .width('100%')
37. .height('100%')
38. }
39. }
```

## replaceNamedRoute

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Failed to get the delegate. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().replaceNamedRoute({
15. name: 'myPage',
16. params: {
17. data1: 'message'
18. }
19. }, rtm.Standard)
20. .then(() => {
21. console.info('succeeded');
22. })
23. .catch((error: BusinessError) => {
24. console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
25. })
26. }

28. build() {
29. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
30. Button() {
31. Text('next page')
32. .fontSize(25)
33. .fontWeight(FontWeight.Bold)
34. }.type(ButtonType.Capsule)
35. .margin({ top: 20 })
36. .backgroundColor('#ccc')
37. .onClick(() => {
38. this.routePage();
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

## replaceNamedRoute

PhonePC/2in1TabletTVWearable

replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void

用指定的命名路由页面替换当前页面，并销毁被替换的页面。使用callback异步回调。与[replaceNamedRoute](arkts-apis-uicontext-router.md#replacenamedroute-1)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.NamedRouterOptions](js-apis-router.md#namedrouteroptions10) | 是 | 替换页面描述信息。 |
| mode | [router.RouterMode](js-apis-router.md#routermode9) | 是 | 跳转页面使用的模式。 |
| callback | AsyncCallback<void> | 是 | router跳转结果回调函数。  当路由跳转成功时，error为undefined。当路由跳转失败时，error为系统返回的错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)、[页面路由错误码](errorcode-router.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the number of parameters is less than 1 or the type of the url parameter is not string. |
| 100001 | The UI execution context is not found. This error code is thrown only in the standard system. |
| 100004 | Named route error. The named route does not exist. |

**示例：**

```
1. import { router } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class RouterTmp {
5. Standard: router.RouterMode = router.RouterMode.Standard;
6. }

8. let rtm: RouterTmp = new RouterTmp();

10. @Entry
11. @Component
12. struct Index {
13. async routePage() {
14. this.getUIContext().getRouter().replaceNamedRoute({
15. name: 'myPage',
16. params: {
17. data1: 'message'
18. }
19. }, rtm.Standard, (err: Error) => {
20. if (err) {
21. let message = (err as BusinessError).message;
22. let code = (err as BusinessError).code;
23. console.error(`replaceNamedRoute failed, code is ${code}, message is ${message}`);
24. return;
25. }
26. console.info('replaceNamedRoute success');
27. })
28. }

30. build() {
31. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
32. Button() {
33. Text('next page')
34. .fontSize(25)
35. .fontWeight(FontWeight.Bold)
36. }.type(ButtonType.Capsule)
37. .margin({ top: 20 })
38. .backgroundColor('#ccc')
39. .onClick(() => {
40. this.routePage();
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

## back

PhonePC/2in1TabletTVWearable

back(options?: router.RouterOptions ): void

返回上一页面或指定的页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.RouterOptions](js-apis-router.md#routeroptions) | 否 | 返回页面描述信息，其中参数url指路由跳转时返回到指定url的页面，如果页面栈中没有对应url的页面，则不响应该操作；如果栈中存在对应url的页面，则返回至index最大的同名页面。  如果url未设置，则返回上一页，页面不会重新构建，页面栈里面的page不会回收，出栈后会被回收。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();
3. let router: Router = uiContext.getRouter();
4. router.back({url:'pages/detail'});
```

## back12+

PhonePC/2in1TabletTVWearable

back(index: number, params?: Object): void

返回指定的页面。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 跳转目标页面的索引值。  取值范围：[0, +∞) |
| params | Object | 否 | 页面返回时携带的参数。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. router.back(1);
```

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();
3. let router: Router = uiContext.getRouter();
4. router.back(1, {info:'来自Home页'}); // 携带参数返回
```

## clear

PhonePC/2in1TabletTVWearable

clear(): void

清空页面栈中的所有历史页面，仅保留当前页面作为栈顶页面。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. router.clear();
```

## getLength(deprecated)

PhonePC/2in1TabletTVWearable

getLength(): string

获取当前在页面栈内的页面数量。

说明

从API version 10开始支持，从 API version 23开始废弃，建议使用[getStackSize](arkts-apis-uicontext-router.md#getstacksize23)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 页面数量，页面栈支持最大数值是32。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. let size = router.getLength();
6. console.info('pages stack size = ' + size);
```

## getStackSize23+

PhonePC/2in1TabletTVWearable

getStackSize(): number

获取当前页面栈内的页面数量。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 页面数量，页面栈支持最大数值是32。 |

**示例：**

```
1. @Entry
2. @Component
3. struct Index {

5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button() {
8. Text('stack size')
9. .fontSize(25)
10. .fontWeight(FontWeight.Bold)
11. }.type(ButtonType.Capsule)
12. .margin({ top: 20 })
13. .backgroundColor('#ccc')
14. .onClick(() => {
15. console.info(`get stack size: ${this.getUIContext().getRouter().getStackSize()}`)
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

## getState

PhonePC/2in1TabletTVWearable

getState(): router.RouterState

获取当前页面的状态信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| router.[RouterState](js-apis-router.md#routerstate) | 页面状态信息。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. let page = router.getState();
6. if (page != undefined) {
7. console.info('current index = ' + page.index);
8. console.info('current name = ' + page.name);
9. console.info('current path = ' + page.path);
10. }
```

## getStateByIndex12+

PhonePC/2in1TabletTVWearable

getStateByIndex(index: number): router.RouterState | undefined

通过索引值获取对应页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 表示要获取的页面索引。  取值范围：[1, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| router.[RouterState](js-apis-router.md#routerstate) | undefined | 返回页面状态信息。索引不存在时返回undefined。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. let options: router.RouterState | undefined = router.getStateByIndex(1);
6. if (options != undefined) {
7. console.info('index = ' + options.index);
8. console.info('name = ' + options.name);
9. console.info('path = ' + options.path);
10. console.info('params = ' + options.params);
11. }
```

## getStateByUrl12+

PhonePC/2in1TabletTVWearable

getStateByUrl(url: string): Array<router.[RouterState](js-apis-router.md#routerstate)>

通过url获取当前页面的状态信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 表示要获取对应页面信息的url。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<router.[RouterState](js-apis-router.md#routerstate)> | 页面状态信息。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();
3. let router: Router = uiContext.getRouter();
4. let options:Array<router.RouterState> = router.getStateByUrl('pages/index');
5. for (let i: number = 0; i < options.length; i++) {
6. console.info('index = ' + options[i].index);
7. console.info('name = ' + options[i].name);
8. console.info('path = ' + options[i].path);
9. console.info('params = ' + options[i].params);
10. }
```

## showAlertBeforeBackPage

PhonePC/2in1TabletTVWearable

showAlertBeforeBackPage(options: router.EnableAlertOptions): void

开启页面返回询问对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [router.EnableAlertOptions](js-apis-router.md#enablealertoptions) | 是 | 文本弹窗信息描述。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[接口调用异常错误码](errorcode-internal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal error. |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let uiContext: UIContext = this.getUIContext();
5. let router: Router = uiContext.getRouter();
6. try {
7. router.showAlertBeforeBackPage({
8. message: 'Message Info'
9. });
10. } catch(error) {
11. let message = (error as BusinessError).message;
12. let code = (error as BusinessError).code;
13. console.error(`showAlertBeforeBackPage failed, code is ${code}, message is ${message}`);
14. }
```

## hideAlertBeforeBackPage

PhonePC/2in1TabletTVWearable

hideAlertBeforeBackPage(): void

禁用页面返回询问对话框。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();

4. let router: Router = uiContext.getRouter();
5. router.hideAlertBeforeBackPage();
```

## getParams

PhonePC/2in1TabletTVWearable

getParams(): Object

获取发起跳转的页面往当前页传入的参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 发起跳转的页面往当前页传入的参数。 |

**示例：**

完整示例请参考[PushUrl](arkts-apis-uicontext-router.md#pushurl)中的示例。

```
1. import { Router , UIContext } from '@kit.ArkUI';
2. let uiContext: UIContext = this.getUIContext();
3. let router: Router = uiContext.getRouter();
4. router.getParams();
```
