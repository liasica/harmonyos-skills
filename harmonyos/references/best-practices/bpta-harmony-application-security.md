---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-harmony-application-security
title: 应用安全编码实践
breadcrumb: 最佳实践 > 应用安全 > 应用安全编码实践
category: best-practices
scraped_at: 2026-04-28T08:22:16+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:83fe9b2b1ce6e71817e58bd81edfddb84c2528d8bf195af6d8ccbdf01ac4fbc3
---

## 通用组件安全

### 不涉及对外交互的应用组件应设置exported属性为false

应用程序内部使用的组件必须设置为不可见，以防止其他应用程序调用。

不对外交互的应用组件应显式设置exported属性为false，防止遗漏和错误配置。这可避免内部接口被恶意应用利用，导致信息泄露、功能异常或应用拒绝服务等问题。

说明

当应用组件的exported属性设置为false时，使用DevEco Studio启动调试或运行应用/服务，或通过命令行拉起时，会出现安装HAP错误，提示“error: failed to start ability. error: ability visible false deny request”。系统安全权限不允许拉起exported属性设置为false的应用/服务。建议在调试阶段将exported属性设置为true，正式上架发布时再设置为false。

**错误示例：**

```
1. // module.json5
2. "abilities": [
3. {
4. "name": "PrivacyAbility",
5. "srcEntry": "./ets/privacyability/PrivacyAbility.ts",
6. "description": "$string:PrivacyAbility_desc",
7. "exported": true
8. }
9. ]
```

PrivacyAbility 是一个不对外交互的组件，但设置exported属性为true后，任何应用都能访问该组件。

**正确示例：**

```
1. // module.json5
2. "abilities": [
3. {
4. "name": "PrivacyAbility",
5. "srcEntry": "./ets/privacyability/PrivacyAbility.ts",
6. "description": "$string:PrivacyAbility_desc",
7. "exported": false
8. }
9. ]
```

### 对外交互的应用组件应设置合理的访问权限

应用程序组件不仅在内部使用，还需要与外部进行交互。以下情况表明组件是对外交互的：

* module.json5文件中显式设置exported属性为true，则表明该Ability允许对外交互的；

程序内应用组件如果允许对外交互，数据会跨越信任边界，若被恶意应用程序利用，可能导致信息泄露、功能异常或应用拒绝服务等问题。因此，应使用`permissions`属性为对外交互的应用组件设置访问权限。

敏感功能和对外提供的Ability存在利用风险，建议相关组件设置权限进行保护。

1）未经用户操作确认，系统即可执行关键操作，例如发送短信、拨打电话、拍照、录音、录屏、截屏和定位等。

2）导致个人数据和敏感数据泄露的关键操作，例如：读取短信、读取联系人和读取设备标识符等。

3）导致权限提升，例如：可以执行原本需要system权限的操作。

**例外情况：**必须对外提供且无利用风险的应用组件，可以不设置权限。

**错误示例：**

```
1. // module.json5
2. "abilities": [
3. {
4. "name": "ContactDataAbility",
5. "srcEntry": "./ets/DataAbility/DataAbility.ts",
6. "description": "$string: DataAbility_desc",
7. "exported": true
8. }
9. ]
```

任意外部应用都可以访问此ContactDataAbility，恶意应用可能利用该组件获取联系人数据。

**正确示例：**

```
1. // module.json5
2. "abilities": [
3. {
4. "name": "ContactDataAbility",
5. "srcEntry": "./ets/DataAbility/DataAbility.ts",
6. "description": "$string: DataAbility_desc",
7. "exported": true,
8. "permissions": ["ohos.permission.READ_CONTACTS"]
9. }
10. ]
```

### 建议隐式启动应用组件时避免携带个人数据

隐式want是通过action条件匹配的方式来筛选组件，凡是满足条件的应用组件都有被启动的可能。如果携带个人数据，则恶意应用有可能劫持携带的个人数据。应用程序如果要携带个人数据，需要显式指定目标应用组件（bundle名、ability名）或者将个人数据匿名化。示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

**错误示例:**

```
1. import { Want } from '@kit.AbilityKit';
2. // ...
3. let wantInfo:Want = {
4. deviceId: '',
5. action: 'ability.want.test',
6. parameters: {
7. 'password': 'xxxxxxxx'
8. }
9. };
10. try{
11. let data = this.context.startAbility(wantInfo);
12. hilog.info(0x0000, 'privacy', 'startAbility success ' + JSON.stringify(data));
13. } catch (err) {
14. hilog.error(0x0000, 'privacy', 'startAbility  with error message: ' + err.message + ', error code: ' + err.code);
15. }
```

[NoInfoJumpTo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/NoInfoJumpTo.ets#L22-L46)

通过示例代码中的action："ability.want.test" 可以隐式启动组件。如果恶意应用也声明了相同的action，隐式调用时将显示一个列表供用户选择。如果用户选择了恶意应用，该应用可能会获取传递的敏感信息。

**正确示例:**

```
1. import { Want } from '@kit.AbilityKit';
2. // ...
3. let wantInfo:Want = {
4. deviceId: '',
5. action: 'ability.want.test',
6. bundleName:'com.example.myapplication10',
7. abilityName:'MainAbility1',
8. parameters: {
9. 'password': 'xxxxxxxx'
10. }
11. }
12. try{
13. let data = this.context.startAbility(wantInfo);
14. hilog.info(0x0000, 'privacy', 'startAbility success ' + JSON.stringify(data));
15. } catch (err) {
16. hilog.error(0x0000, 'privacy', 'startAbility  with error message: ' + err.message + ', error code: ' + err.code);
17. }
```

[NoInfoJumpTo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/NoInfoJumpTo.ets#L22-L48)

这里显式指定了需要拉起的应用组件的bundleName和abilityName，只会拉起指定的目标组件。

### 避免涉及口令输入的应用界面可以被截屏或录屏

口令输入界面包含账号密码输入框和输入法弹出框。在用户输入口令时，应禁止截屏或录屏操作。如果恶意软件获得授权，窃取用户账号和密码，便可能在其他设备上登录，导致用户隐私泄露。

**实施指导：**

在需要保护的Page页面调用setWindowPrivacyMode()方法，禁止截屏和录屏。

注意：使用此接口前，需申请ohos.permission.PRIVACY\_WINDOW权限。

**正确示例:**

在口令输入、转账支付页面中设置隐私属性，防止截屏/录屏：

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'Hello World';

10. onPageShow(): void {
11. window.getLastWindow(this.getUIContext().getHostContext()).then((windowStage: window.Window) => {
12. windowStage.setWindowPrivacyMode(true);
13. }).catch((error: BusinessError) => {
14. hilog.error(0x0000, 'PrivacyMode', `getLastWindow error code ${error.code}`)
15. });
16. }
17. onPageHide(): void {
18. window.getLastWindow(this.getUIContext().getHostContext()).then((windowStage: window.Window) => {
19. windowStage.setWindowPrivacyMode(false);
20. }).catch((error: BusinessError) => {
21. hilog.error(0x0000, 'PrivacyMode', `getLastWindow error code ${error.code}`)
22. });
23. }
24. build() {
25. Row() {
26. Column() {
27. Text(this.message)
28. .fontSize(50)
29. .fontWeight(FontWeight.Bold)
30. Button('click to start Succ Page')
31. .onClick(async () => {
32. this.getUIContext().getRouter().pushUrl({ url: 'pages/loginSuccPage' });
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[PrivacyMode.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/PrivacyMode.ets#L21-L59)

## 公共事件安全

### 避免使用携带个人数据未设置权限的动态公共事件

不同应用程序可以通过公共事件进行进程间通信。如果公共事件的发送权限设置不当，并且携带个人数据，任何应用都可能读取这些个人数据，导致用户数据泄露。

对于携带个人数据的公共事件，需设置发送权限或加密个人数据。

**错误示例:**

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. function publishEventWithData() {
5. let options: commonEventManager.CommonEventPublishData = {
6. code: 1,
7. data: 'ContactData', // Sending sensitive data
8. }
9. commonEventManager.publish('MyCommonEvent', options, (err) => {
10. if (err.code) {
11. hilog.error(0x0000, 'privacy', `publish event error: ${err.code} ${err.message} ${err.name} ${err.stack}`);
12. } else {
13. hilog.info(0x0000, 'privacy', 'publish event with data Succeeded');
14. }
15. })
16. }
```

[PublicSafeInfo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/PublicSafeInfo.ets#L22-L37)

发送了一个包含联系人数据的公共事件，但未设置接收方所需的权限。

**正确示例:**

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. function publishEventWithData() {
5. let options: commonEventManager.CommonEventPublishData = {
6. code: 1,
7. data: 'ContactData', // Sending sensitive data
8. subscriberPermissions: ['ohos.permission.READ_CONTACTS'], // Set the permission
9. }
10. commonEventManager.publish('MyCommonEvent', options, (err) => {
11. if (err.code) {
12. hilog.error(0x0000, 'privacy', `publish event error: ${err.code} ${err.message} ${err.name} ${err.stack}`);
13. } else {
14. hilog.info(0x0000, 'privacy', 'publish event with data Succeeded');
15. }
16. })
17. }
```

[PublicSafeInfo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/PublicSafeInfo.ets#L22-L38)

通过subscriberPermissions字段设置接收权限，发布者要求订阅者具有“ohos.permission.READ\_CONTACTS”权限，才能接收携带联系人数据的公共事件。

### 建议对涉及敏感功能的公共事件进行访问权限控制

应用支持订阅自定义公共事件，并在接收到事件后执行相应功能。订阅公共事件时，需通过publisherPermission设置接收权限。若未设置权限，任意应用可发送同名自定义公共事件，可能导致接收应用拒绝服务或敏感功能泄露。

对于涉及敏感数据或操作的公共事件，订阅方必须设置足够高的权限。

**错误示例:**

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let subscriber: commonEventManager.CommonEventSubscriber;
5. //Subscriber information
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event']
8. };

10. // Create a subscriber
11. try {
12. commonEventManager.createSubscriber(subscribeInfo, (err, commonEventSubscriber) => {
13. if (!err) {
14. hilog.info(0x0000, 'privacy', 'createSubscriber Succeed');
15. subscriber = commonEventSubscriber;
16. //Subscribe to public events
17. try {
18. commonEventManager.subscribe(subscriber, (err, data) => {
19. if (err) {
20. hilog.error(0x0000, 'privacy', `subscribe failed, code is ${err.code}, message is ${err.message}`);
21. } else {
22. //Event processing after receiving public events
23. // doSomeDangerousThing(data)
24. }
25. });
26. } catch (err) {
27. hilog.error(0x0000, 'privacy', `subscribe failed, code is ${err.code}, message is ${err.message}`);
28. }
29. } else {
30. hilog.error(0x0000, 'privacy', `createSubscriber failed, code is ${err.code}, message is ${err.message}`);
31. }
32. });
33. } catch (err) {
34. hilog.error(0x0000, 'privacy', `createSubscriber failed, code is ${err.code}, message is ${err.message}`);
35. }
```

[PublicSensitive.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/PublicSensitive.ets#L22-L56)

**正确示例:**

```
1. import { commonEventManager } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let subscriber: commonEventManager.CommonEventSubscriber;
5. //Subscriber information
6. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
7. events: ['event'],
8. publisherPermission: 'ohos.permission.publisherPermission1', // Set the subscription permission
9. };

11. // Create a subscriber
12. try {
13. commonEventManager.createSubscriber(subscribeInfo, (err, commonEventSubscriber) => {
14. if (!err) {
15. hilog.info(0x0000, 'privacy', 'createSubscriber');
16. subscriber = commonEventSubscriber;
17. //Subscribe to public events
18. try {
19. commonEventManager.subscribe(subscriber, (err, data) => {
20. if (err) {
21. hilog.error(0x0000, 'privacy', `subscribe failed, code is ${err.code}, message is ${err.message}`);
22. } else {
23. //Event processing after receiving public events
24. // doSomeDangerousThing(data)
25. }
26. });
27. } catch (err) {
28. hilog.error(0x0000, 'privacy', `subscribe failed, code is ${err.code}, message is ${err.message}`);
29. }
30. } else {
31. hilog.error(0x0000, 'privacy', `createSubscriber failed, code is ${err.code}, message is ${err.message}`);
32. }
33. });
34. } catch (err) {
35. hilog.error(0x0000, 'privacy', `createSubscriber failed, code is ${err.code}, message is ${err.message}`);
36. }
```

[PublicSensitive.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/PublicSensitive.ets#L22-L57)

常见敏感功能和对外提供的公共事件存在利用风险。建议对涉及这些情况的公共事件设置权限保护。

1）未经用户确认，系统可执行关键操作，如发送短信、拨打电话、拍照、录音、录屏、截屏、定位等。

2）导致个人数据和敏感数据泄露的关键操作包括：读取短信、读取联系人、读取设备标识符等。

3）导致权限提升，例如：进行原本需要system权限的操作。

**例外情况：**必须对外提供且无利用风险的应用公共事件，可以不设置权限。

## WebView安全

### 避免加载不安全的URL或页面

Web组件或WebController均可以加载URL或页面。如果加载的URL或页面被攻击者控制，可能会加载恶意JS代码，从而调用ArkTS开放的敏感JS接口，获取用户个人数据或对应用进行攻击。

需要在加载URL之前，通过Web组件的onLoadIntercept()方法拦截URL，获取并校验其字段值是否在业务预置的白名单内。

**正确示例：**

```
1. import { uri } from '@kit.ArkTS';
2. import { webview } from '@kit.ArkWeb';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // Check function
6. function checkUrl(str: string): boolean {
7. let tmpUri = new uri.URI(str);
8. let res =
9. tmpUri.normalize(); // Note that you need to normalize tmpUri first. Otherwise, security verification will be bypassed
10. hilog.info(0x0000, 'privacy', 'res.scheme:' + res.scheme); // Protocol
11. hilog.info(0x0000, 'privacy', 'res.host:' + res.host); // domain name
12. hilog.info(0x0000, 'privacy', 'res.port:' + res.port); // Ports
13. hilog.info(0x0000, 'privacy', 'res.path:' + res.path); // Path
14. hilog.info(0x0000, 'privacy', 'res.ssp:' + res.ssp);
15. // After obtaining the values of scheme, host, port, and path, perform security verification based on the actual service
16. // Omit the part here. Perform the verification based on service requirements
17. if ('校验成功') {
18. return true;
19. }
20. return false;
21. }

23. @Entry
24. @Component
25. struct WebComponent {
26. controller: webview.WebviewController = new webview.WebviewController();

28. build() {
29. Column() {
30. Button('loadUrl')
31. .onClick(() => {
32. this.controller.loadUrl('www.huawei.com');
33. })
34. .margin({ top: 50 })
35. Web({ src: 'www.huawei.com', controller: this.controller })
36. .onLoadIntercept((event) => {
37. hilog.info(0x0000, 'privacy', 'onLoadIntercept:' + event.data.toString());
38. let tempUrl = event.data.toString();
39. return checkUrl(tempUrl); // Return true to block the load, otherwise allow the load
40. })
41. }
42. }
43. }
```

[WebUrlSafe.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/WebUrlSafe.ets#L21-L63)

**例外：**如果应用本身是提供URL加载能力的，譬如浏览器等，可以例外。但是要注意，如果应用也提供了敏感的JS接口，要注意防范可能的被恶意调用的风险。

### 避免加载不可信的JavaScript脚本

WebController提供了runJavaScript()和runJavaScriptExt()函数用于异步执行JavaScript脚本，并通过回调方式返回脚本执行的结果。以runJavaScript为例：

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .javaScriptAccess(true)
14. .onPageEnd(e => {
15. let whiteMethods = ['test()', 'test1()'];
16. let jsMethod: string = 'alert(`xss`)'; // Externally controllable fields
17. // Check the trustlist
18. if (whiteMethods.indexOf(jsMethod) === -1) {
19. hilog.error(0x0000, 'privacy', 'input method not in whiteList');
20. return;
21. }
22. this.controller.runJavaScript(jsMethod)
23. .then((result) => {
24. hilog.info(0x0000, 'privacy', 'result: ' + result);
25. })
26. .catch((error: BusinessError) => {
27. hilog.error(0x0000, 'privacy', `ErrorCode: ${error.code},  Message: ${error.message}`);
28. })
29. if (e) {
30. hilog.info(0x0000, 'privacy', 'url: ', e.url);
31. }
32. })
33. }
34. }
35. }
```

[RunJavaScriptTrustList.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/RunJavaScriptTrustList.ets#L22-L56)

加载的index.html文件内容如下：

```
1. <!DOCTYPE html>
2. <html>
3. <meta charset="utf-8">
4. <body>
5. Hello world!
6. </body>
7. <script type="text/javascript">
8. function test() {
9. console.log('Ark WebComponent')
10. return "This value is from index.html"
11. }
12. </script>
13. </html>
```

[index.html](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/resources/rawfile/index.html#L9-L21)

如果加载的脚本内容不可信，可能会导致恶意JavaScript代码的加载，引发XSS攻击。若Web组件注册了敏感的JavaScript接口，恶意代码还可能调用这些接口，进一步影响应用的安全性。

若待加载的JavaScript脚本外部可控，加载前需进行白名单校验。

**正确示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .javaScriptAccess(true)
14. .onPageEnd(e => {
15. this.controller.runJavaScript('test()')
16. .then((result) => {
17. hilog.info(0x0000, 'privacy', 'result: ' + result);
18. })
19. .catch((error: BusinessError) => {
20. hilog.error(0x0000, 'privacy', `ErrorCode: ${error.code},  Message: ${error.message}`);
21. })
22. if (e) {
23. hilog.info(0x0000, 'privacy', 'url: ', e.url);
24. }
25. })
26. }
27. }
28. }
```

[RunJavaScript.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/RunJavaScript.ets#L22-L49)

**错误示例：**

```
1. import { webview } from '@kit.ArkWeb';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct WebComponent {
8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: $rawfile('index.html'), controller: this.controller })
13. .javaScriptAccess(true)
14. .onPageEnd(e => {
15. let jsMethod: string = 'alert(`xss`)' // Externally controllable fields
16. this.controller.runJavaScript(jsMethod)
17. .then((result) => {
18. hilog.info(0x0000, 'privacy', 'result: ' + result);
19. })
20. .catch((error: BusinessError) => {
21. hilog.error(0x0000, 'privacy', `ErrorCode: ${error.code},  Message: ${error.message}`);
22. })
23. if (e) {
24. hilog.info(0x0000, 'privacy', 'url: ', e.url);
25. }
26. })
27. }
28. }
29. }
```

[RunJavaScriptTrustList.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/RunJavaScriptTrustList.ets#L22-L50)

### 避免将mixedMode属性配置成All

mixedMode设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）混合内容，默认不允许加载HTTP和HTTPS混合内容。支持三种模式，其中All是允许混合内容加载，存在中间人攻击的风险，默认不允许配置成All。

**错误示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src:'www.huawei.com', controller: this.controller })
11. .mixedMode(MixedMode.All)
12. }
13. }
14. }
```

[MixedMode.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/MixedMode.ets#L22-L35)

应该去掉此配置项，或者选择MixedMode.None模式。

**例外：**对于提供特定业务的应用可以例外，例如浏览器。

### 避免在SSL校验出错时继续加载页面

onSslErrorEventReceive()回调函数用于通知用户加载资源时发生SSL错误。

当Web组件通过SSL协议进行网络请求时，默认情况下，如果底层Web组件校验服务端返回的证书或协议出错，则应取消请求，以避免中间人攻击风险。

```
1. import { webview } from '@kit.ArkWeb';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .onSslErrorEventReceive((event) => {
13. hilog.info(0x0000, 'privacy', 'ssl check failed,error is : ' + event.error.toString());
14. event.handler.handleCancel();
15. })
16. }
17. }
18. }
```

[OnSslErrorEventReceive.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/OnSslErrorEventReceive.ets#L22-L39)

**错误示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .onSslErrorEventReceive((event) => {
12. event.handler.handleConfirm();
13. })
14. }
15. }
16. }
```

[OnSslErrorEventReceive.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/OnSslErrorEventReceive.ets#L22-L37)

如果在SSL校验出错时直接调用handleConfirm()函数，页面将忽略SSL错误并继续加载，从而导致中间人攻击等风险。

**例外：**对于浏览器等用于加载URL的应用可以例外，但需要在页面显式告知用户待加载页面存在安全风险。

### 避免在用户同意前返回位置信息

geolocationAccess开关用于配置是否开启地理位置权限，默认开启。onGeolocationShow()回调函数用于通知用户收到地理位置信息获取请求。H5页面请求获取地理位置信息时，Web组件通过上述两个API进行配置。

无使用场景时，显式禁用geolocationAccess()。存在使用场景时，需在onGeolocationShow()回调内先弹框提示用户，经用户确认和同意后才能返回位置信息，否则存在隐私泄露风险。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .geolocationAccess(true)
12. .onGeolocationShow((event) => {
13. if (event === undefined) {
14. return;
15. }
16. AlertDialog.show({
17. title: 'title',
18. message: 'text',
19. confirm: {
20. value: 'onConfirm',
21. action: () => {
22. event.geolocation.invoke(event.origin, true, true);
23. }
24. },
25. cancel: () => {
26. event.geolocation.invoke(event.origin, false, true);
27. }
28. });
29. })
30. }
31. }
32. }
```

[GeolocationAccess.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/GeolocationAccess.ets#L22-L53)

**错误示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: 'www.example.com', controller: this.controller })
11. .geolocationAccess(true)
12. .onGeolocationShow((event) => {
13. if (event === undefined) {
14. return;
15. }
16. event.geolocation.invoke(event.origin, true, true);
17. })
18. }
19. }
20. }
```

[GeolocationAccess.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/GeolocationAccess.ets#L22-L41)

在使用位置权限的场景中，不能直接返回位置信息。必须先明确告知用户并获得其同意后，才能返回位置信息。

### 避免注册返回含有全局认证凭据的JavaScriptProxy

在HarmonyOS中，可以使用Web组件加载H5等页面。同时Web组件可以通过JavaScriptProxy()方法或者通过WebController的registerJavaScriptProxy()方法向H5提供JS接口，供H5访问。

如果提供的JS接口返回敏感信息或涉及敏感操作，被恶意调用，则存在安全风险。特别是当JS接口返回用于认证用户身份的全局认证凭据ServiceToken（简称ST）或AccessToken（简称AT）时，攻击者获取这些凭据后，可以冒充用户恶意调用应用在云端的所有接口，扩大攻击影响。因此，禁止Web组件提供获取全局认证凭据ST或AT的JavaScriptProxy。

**错误示例：**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Row() {
11. Button('registerJavaScriptProxy').onClick(() => {
12. this.controller.registerJavaScriptProxy(
13. {
14. getServiceToken: () => {
15. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
16. }
17. },
18. 'objName',
19. ['getServiceToken'],
20. );
21. this.controller.refresh();
22. })
23. }

25. Web({ src: $rawfile('H5CallETS.html'), controller: this.controller })
26. .javaScriptAccess(true)
27. .javaScriptProxy({
28. object: {
29. getServiceToken: () => {
30. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
31. }
32. },
33. name: 'objName',
34. methodList: ['getServiceToken'],
35. controller: this.controller
36. })
37. }
38. }
39. }
```

[JavaScriptProxy.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/JavaScriptProxy.ets#L22-L60)

H5攻击界面：

```
1. <!DOCTYPE html>
2. <html>
3. <meta charset="utf-8">
4. <body>
5. Hello js call ets interface!
6. <br>
7. <script type="text/javascript">
8. function callJSInt() {
9. let ST = objName.getServiceToken();
10. console.log('wzz:ST = '+ ST);
11. alert(ST);
12. }
13. </script>
14. <button onclick="callJSInt()">get ST</button>
15. </body>
16. </html>
```

[H5CallETS.html](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/resources/rawfile/H5CallETS.html#L22-L37)

提供了一个ST接口，用于H5调用以获取全局认证凭据。如果H5存在漏洞，攻击者可能获取此ST并冒充用户访问云服务上的个人数据，进行恶意操作。

为了降低全局认证凭据ST或AT丢失带来的安全风险，推荐以下两种方法：

**第一种方法：**在加载URL页面前，校验当前页面的URL是否在白名单内，仅允许白名单内的URL调用。要同时校验协议、域名、PATH等，白名单范围控制的越小越安全。

校验方法可使用如下API格式化相关URL，跟预置的数据进行比较。

1. 使用URI库进行URL格式化，准确获取URL各字段值，并校验这些值是否在业务预置的白名单内。

```
1. // Index.ets
2. import { uri } from '@kit.ArkTS';
3. import { webview } from '@kit.ArkWeb';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. // Check function
7. function checkUrl(surl: string): boolean {
8. let tmpUri: uri.URI = new uri.URI(surl);
9. let res = tmpUri.normalize(); // Note that you need to normalize tmpUri first. Otherwise, security verification will be bypassed
10. hilog.info(0x0000, 'privacy', 'res.scheme:' + res.scheme); // scheme
11. hilog.info(0x0000, 'privacy', 'res.host:' + res.host); // host
12. hilog.info(0x0000, 'privacy', 'res.port:' + res.port); // port
13. hilog.info(0x0000, 'privacy', 'res.path:' + res.path); // path
14. hilog.info(0x0000, 'privacy', 'res.ssp:' + res.ssp);
15. // After obtaining the values of the scheme, host, port, and path parameters, perform security verification based on the service requirements
16. // The part is omitted here. The verification is performed based on the service requirements
17. if ('校验成功') {
18. return true;
19. }
20. return false;
21. }

23. @Entry
24. @Component
25. struct Index {
26. controller: webview.WebviewController = new webview.WebviewController();

28. build() {
29. Column() {
30. Row() {
31. Button('registerJavaScriptProxy').onClick(() => {
32. this.controller.registerJavaScriptProxy(
33. {
34. getServiceToken: () => {
35. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
36. }
37. },
38. 'objName',
39. ['getServiceToken'],
40. );
41. this.controller.refresh();
42. })
43. }

45. Web({ src: $rawfile('H5CallETS.html'), controller: this.controller })
46. .javaScriptProxy({
47. object: {
48. getServiceToken: () => {
49. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
50. }
51. },
52. name: 'objName',
53. methodList: ['getServiceToken'],
54. controller: this.controller
55. })
56. .onLoadIntercept((event) => {
57. hilog.info(0x0000, 'privacy', 'onLoadIntercept:' + event.data.toString());
58. let tempUrl = event.data.toString();
59. return checkUrl(tempUrl); // Returns true to block the load, otherwise allow the load
60. })
61. }
62. }
63. }
```

[TrustListCheck.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/TrustListCheck.ets#L22-L84)

2. 使用URL库进行URL格式化，准确获取URL各字段值并校验是否在业务预置的白名单内。

```
1. // Index.ets
2. import { url } from '@kit.ArkTS';
3. import { webview } from '@kit.ArkWeb';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. // Check Function
7. function checkUrl(surl: string): boolean {
8. let tmpUrl = url.URL.parseURL(surl);
9. hilog.info(0x0000, 'privacy', 'res.scheme:' + tmpUrl.protocol); // scheme
10. hilog.info(0x0000, 'privacy', 'res.host:' + tmpUrl.host); // host
11. hilog.info(0x0000, 'privacy', 'res.port:' + tmpUrl.port); // port
12. hilog.info(0x0000, 'privacy', 'res.path:' + tmpUrl.pathname); // path
13. hilog.info(0x0000, 'privacy', 'res.ssp:' + tmpUrl.hostname); // ssp
14. // After obtaining the values of the scheme, host, port, and path parameters, perform security verification based on the service requirements
15. // The part is omitted here. The verification is performed based on the service requirements
16. if ('校验成功') {
17. return true;
18. }
19. return false;
20. }

22. @Entry
23. @Component
24. struct Index {
25. controller: webview.WebviewController = new webview.WebviewController();

27. build() {
28. Column() {
29. Row() {
30. Button('registerJavaScriptProxy').onClick(() => {
31. this.controller.registerJavaScriptProxy(
32. {
33. getServiceToken: () => {
34. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
35. }
36. },
37. 'objName',
38. ['getServiceToken']
39. );
40. this.controller.refresh();
41. })
42. }

44. Web({ src: $rawfile('H5CallETS.html'), controller: this.controller })
45. .javaScriptAccess(true)
46. .javaScriptProxy({
47. object: {
48. getServiceToken: () => {
49. return 'DLFJSLDFJALGJLDFJSDDFISLDF323LSDJFLS212DLSFJOEV';
50. }
51. },
52. name: 'objName',
53. methodList: ['getServiceToken'],
54. controller: this.controller
55. })
56. .onLoadIntercept((event) => {
57. hilog.info(0x0000, 'privacy', 'wzz:onLoadIntercept:' + event.data.toString());
58. let tempUrl = event.data.toString();
59. return checkUrl(tempUrl); // Returns true to block the load, otherwise allow the load
60. })
61. }
62. }
63. }
```

[UrlListCheck.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/UrlListCheck.ets#L22-L84)

**第二种方法：**针对H5页面申请一个新的H5Token，并严格限定此H5Token可以调用的云服务业务接口在最小范围内。

## 数据传递安全

### 建议对跨信任边界传入的Want进行合法性判断

攻击者可能向指定应用Ability发送空的Want或携带恶意数据。如果应用接收这些Want，却没有进行合法性判断，可能会导致应用业务逻辑被篡改、数据泄露或财产损失。因此，应对外部传入的Want内容进行合法性判断。

常见的对Want的判断：

1. 在使用Want的数据属性之前，先判断其是否为null或undefined，确保访问的对象属性存在。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

4. // Check function
5. function checkWant(want: Want) {
6. if (want === null || want.parameters === null
7. || want === undefined || want.parameters === undefined) {
8. return false;
9. }
10. return true;
11. }

13. export default class EntryAbility extends UIAbility {
14. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
15. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
16. if (checkWant(want)) {
17. hilog.info(0x0000, 'privacy', 'invalid want');
18. } else {
19. hilog.info(0x0000, 'privacy', 'correct want');
20. }
21. }
22. }
```

[CheckWantOne.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/CheckWantOne.ets#L23-L44)

2. 使用Want的数据前，进行try...catch异常捕获，以防止应用崩溃，并且可以定位问题。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';

4. // Check function
5. function checkWant(want: Want) {
6. try {
7. if (want.parameters) {
8. let param = want.parameters['test'] as Want;
9. let str = param.uri;
10. hilog.info(0x0000, 'privacy', 'get uri string: ' + str);
11. }
12. } catch (e) {
13. return false;
14. }
15. return true;
16. }

18. export default class EntryAbility extends UIAbility {
19. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
21. if (checkWant(want)) {
22. hilog.info(0x0000, 'privacy', 'invalid want');
23. } else {
24. hilog.info(0x0000, 'privacy', 'correct want');
25. }
26. }
27. }
```

[CheckWantTwo.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/CheckWantTwo.ets#L22-L48)

应用获取外部不可信Want的方式有很多种，例如：

在不同场景下，获取Want的方式如下：

```
1. // Application life cycle:
2. // @ohos.application.AbilityStage.d.ts
3. onAcceptWant(want: Want): string;
4. // ability life cycle：
5. // @ohos.application.Ability.d.ts
6. onCreate(want: Want, param: AbilityConstant.LaunchParam): void;
7. onContinue(wantParam: {}): AbilityConstant.OnContinueResult;
8. onNewWant(want: Want, launchParams: AbilityConstant.LaunchParam): void;
9. // ServiceExtensionAbility life cycle：
10. // @ohos.application.ServiceExtensionAbility.d.ts
11. onCreate(want: Want): void;
12. onRequest(want: Want, startId: number): void;
13. onConnect(want: Want): rpc.RemoteObject;
14. onDisconnect(want: Want): void;
15. onReconnect(want: Want): void;
```

[WantScene.ts](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/privacy/src/main/ets/pages/WantScene.ts#L26-L40)

## 数据存储安全

### 避免直接使用不可信数据来拼接SQL语句

SQL注入是指对用户输入数据的合法性没有判断或过滤不严。攻击者可以传入特定内容，将应用事先定义好的语句变成含义完全不同的SQL语句，导致信息泄露或数据篡改。

任何外部的输入，包括用户的输入，都是不安全的，需要对外部输入的数据进行过滤处理。

HarmonyOS系统提供的关系型数据库基于SQLite组件，可以直接运行用户输入的SQL语句。如果不可信的数据用于拼接SQL语句，就存在SQL注入的风险。应使用参数化查询的方式或对不可信内容进行过滤。

HarmonyOS上querySql和executeSql会被用于拼接SQL语句的执行。

示例中的context的获取方式请参见[获取UIAbility的上下文信息](../harmonyos-guides/uiability-usage.md#获取uiability的上下文信息)。

**错误示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { relationalStore } from '@kit.ArkData'
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // ...

7. // The sql parameters are from external input
8. function exesql(sql: string) {
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: 'RdbTest.db',
11. securityLevel: relationalStore.SecurityLevel.S1
12. };
13. let store: relationalStore.RdbStore | undefined = undefined;
14. relationalStore.getRdbStore(context, STORE_CONFIG, (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
15. store = rdbStore;
16. if (err) {
17. hilog.error(0x0000, 'privacy', `Get RdbStore failed, code is ${err.code},message is ${err.message}`);
18. return;
19. }
20. hilog.info(0x0000, 'privacy', 'Get RdbStore successfully.');
21. })
22. // The external input is used to directly concatenate the SQL statement, and the verification is not performed
23. let SQL_DELETE_TABLE = 'DELETE FROM test WHERE name = ' + sql;
24. if (store != undefined) {
25. (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE, (err) => {
26. if (err) {
27. hilog.error(0x0000, 'privacy', `ExecuteSql failed, code is ${err.code},message is ${err.message}`);
28. return;
29. }
30. hilog.info(0x0000, 'privacy', 'Delete table done.');
31. })
32. }
33. }
```

[UntrustedDataToSQL.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/UntrustedDataToSQL.ets#L22-L57)

如果直接使用用户输入作为查询参数，恶意用户可以输入类似“1' OR 'a' = 'a”的字符串，导致 SQL 语句变为select \* from book where name='1' OR 'a' = 'a'，从而引发 SQL 注入攻击。因此，禁止直接使用外部输入作为查询字符串的一部分，或者在拼接 SQL 语句之前，对外部输入进行字符校验。

### 避免将个人数据存放到剪贴板中

剪贴板是指操作系统提供的一个暂存数据并提供共享的模块，也称为数据中转站。剪贴板在后台起作用，存放在内存里。

如果将个人数据放入剪贴板中是不安全的，因为任意程序都可以访问剪贴板中的内容。

将内容存放入剪贴板的方法有SystemPasteboard类中的setPasteData()方法。

**例外：**如果是用户自己主动以剪切板作为中转，拷贝数据，则不受此规则约束。

### 避免使用未校验的外部数据拼接文件路径

HarmonyOS系统对文件存储进行了沙箱隔离。内部存储的文件仅应用程序有权限读取，且仅限于本应用的内部存储目录。若需读取外部共享存储，则必须添加读取权限。

在对文件进行读、写、下载、删除等操作时，如果使用外部输入拼接文件路径，攻击者可能注入恶意字符（如../）进行跨目录攻击，导致数据泄露或应用拒绝服务等安全问题。因此，拼接路径前需校验外部输入，确保其不包含恶意字符。

```
1. // The fileName is from external
2. function readFile(fileName: string) {
3. let filePath = '/data/storage/';
4. if (fileName.indexOf('..') === -1) { // Anti-splicing verification
5. let fileAllPath: string = filePath + fileName;
6. // Service processing
7. } else {
8. hilog.info(0x0000, 'privacy', 'be attacked');
9. return;
10. }
11. }
```

[UntrustedDataToSQL.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/Privacy/PrivacyError/src/main/ets/pages/UntrustedDataToSQL.ets#L66-L76)

## 配置安全

### 建议正确设置发布版本应用调试属性

"debug"属性是为了方便开发人员对应用进行调试，但对于正式发布版本，如果应用设置为可调试模式，方便了攻击者对应用进行更深入的分析调试，不利于对应用的保护，因此要求正式版本须设置为不可调试模式。

对"debug"的设置需要在app.json5文件中进行配置。其中"debug"属性缺省值为false。

**错误示例：**

```
1. // app.json5
2. {
3. "app": {
4. "bundleName": "com.application.music",
5. "vendor": "application",
6. "versionCode": 1,
7. "versionName": "1.0",
8. "minCompatibleVersionCode": 1,
9. "minAPIVersion": 7,
10. "targetAPIVersion": 8,
11. "apiReleaseType": "Release",
12. "debug": true, // debug字段设置
13. "icon": "$media:app_icon",
14. "label": "$string:app_name",
15. "description": "$string:description_application",
16. "distributedNotificationEnabled": true,
17. "entityType": "game",
18. "car": {
19. "apiCompatibleVersion": 8
20. }
21. }
22. }
```

**正确示例：**

```
1. // app.json5
2. {
3. "app": {
4. "bundleName": "com.application.music",
5. "vendor": "application",
6. "versionCode": 1,
7. "versionName": "1.0",
8. "minCompatibleVersionCode": 1,
9. "minAPIVersion": 7,
10. "targetAPIVersion": 8,
11. "apiReleaseType": "Release",
12. "debug": false,
13. "icon": "$media:app_icon",
14. "label": "$string:app_name",
15. "description": "$string:description_application",
16. "distributedNotificationEnabled": true,
17. "entityType": "game",
18. "car": {
19. "apiCompatibleVersion": 8
20. }
21. }
22. }
```

### 建议发布的软件包进行代码混淆

鸿蒙应用软件包（HAP、HAR、HSP）可以被反编译。配置代码混淆，增加攻击者分析代码的难度。

**正确示例，开启属性混淆例子：**

```
1. # Define project specific obfuscation rules here.
2. # You can include the obfuscation configuration files in the current module's build-profile.json5.
3. #
4. # For more details, see
5. #   https://gitcode.com/openharmony/arkcompiler_ets_frontend/blob/master/arkguard/README.md

7. # Obfuscation options:
8. # -disable-obfuscation: disable all obfuscations
9. # 开启对象属性混淆
10. -enable-property-obfuscation: obfuscate the property names
11. # -enable-toplevel-obfuscation: obfuscate the names in the global scope
12. # -compact: remove unnecessary blank spaces and all line feeds
13. # -remove-log: remove all console.* statements
14. # -print-namecache: print the name cache that contains the mapping from the old names to new names
15. # -apply-namecache: reuse the given cache file

17. # Keep options:
18. # -keep-property-name: specifies property names that you want to keep
19. # -keep-global-name: specifies names that you want to keep in the global scope
```

在应用源码工程obfuscation-rules.txt文件中，按照应用业务的需求配置和开启混淆规则。

### 建议应用使用的依赖库处于最新状态

应用通常依赖外部第三方库和系统SDK来完成特定任务。及时更新这些依赖项，可增强应用的安全性。

在发布应用前，请确保所有库、SDK 和其他依赖项均为最新版本。

* 对于SDK等第一方依赖项，当前SDK已嵌入DevEco Studio中，无需额外下载配置，请使用DevEco Studio最新版本。
* 对于第三方依赖项，请检查您的应用所用库的网站，并安装所有可用的更新和安全补丁。

## 应用签名安全

### 避免正式版本应用使用debug调试签名

在HarmonyOS应用打包时，可以选择debug和release两种模式。debug模式的应用便于开发者进行调试。然而，在正式发布版本中，若应用设置为可调试模式，将增加攻击者分析调试应用的风险，不利于应用的安全保护。因此，正式发布的应用必须使用release模式并禁止使用debug签名。

注意：DevEco Studio默认编译的hap应用为debug模式，不可直接用于商用版本。

### 建议应用需保证签名完整性

应用签名是保障应用完整性的关键。若因版本更新需对应用进行资源裁剪或字节调整，修改后必须重新签名，否则会破坏签名完整性。

禁止应用破坏签名后上架或者直接预装到版本中。

### 建议应用在申请应用证书时不使用个人信息

应用签名必须申请签名证书。申请证书时需要输入开发者信息和公司信息。该证书是应用的身份标识和认证凭据。签名时，证书会嵌入到应用包，成为应用包数据结构的一部分。开发者可以通过公开的API或读取应用包数据结构获取应用证书信息。

如果在证书信息中填写了姓名、工号等个人信息，将导致信息泄露，并可能引发质疑。证书信息应填写公司或团队名称，而不是个人信息。

### 建议应用软件应包含的签名信息需要真实有效

预置应用软件必须包含真实有效的签名信息。对于非开源鸿蒙官方应用，不得使用开源鸿蒙公开证书，也不得使用与产品无关的签名信息，例如Demo等。应用开发者、公司和部门信息必须真实有效，不得为网址、乱码等无效信息。签名证书应正确标识开发者身份，包括企业名称、组织、省市和国家等信息，不得包含与主体无关的信息。

**错误示例：**

```
1. 10-11 17:51:53 WARN  - Missing parameter: outproof
2. 10-11 17:51:53 INFO  - Find Hap Signing Block success, version: 3, block count: 2
3. 10-11 17:51:54 INFO  - +++++++++++++++++++++++++++certificate #0 +++++++++++++++++++++++++++++++
4. 10-11 17:51:54 INFO  - Subject: C=CN, O=Organization, OU=Unit, CN=ide_demo_app // CN字段无法标识开发组织
5. 10-11 17:51:54 INFO  - Issuer: CN=OpenHarmony Application CA, OU=OpenHarmony Team, O=OpenHarmony, C=CN
```

**正确示例：**

```
1. 10-11 17:51:54 INFO  - Issuer: CN=OpenHarmony Application CA, OU=OpenHarmony Team, O=OpenHarmony, C=CN
2. 10-11 17:52:21 WARN  - Missing parameter: outproof
3. 10-11 17:52:21 INFO  - Find Hap Signing Block success, version: 3, block count: 2
4. 10-11 17:52:21 INFO  - +++++++++++++++++++++++++++certificate #0 +++++++++++++++++++++++++++++++
5. 10-11 17:52:21 INFO  - Subject: CN=应用名称, OU=开发者组织/公司/部门, O=开发者组织/公司/部门, C=CN // CN字段标识开发组织
```
