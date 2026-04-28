---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-adsblockmanager
title: Class (AdsBlockManager)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (AdsBlockManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:00+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:dbe6c6cd4958cefb024ac8631376d56ba6659bbabfadeaa2c4f591ddfe8d3f73
---

通过AdsBlockManager可以向Web组件中设置自定义的广告过滤配置、关闭特定网站的广告过滤功能，其中每个应用中的所有Web组件都共享一个AdsBlockManager实例。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。
* 静态方法必须在用户界面（UI）线程上使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { webview } from '@kit.ArkWeb';
```

## setAdsBlockRules12+

PhonePC/2in1TabletTVWearable

static setAdsBlockRules(rulesFile: string, replace: boolean): void

向Web组件中设置自定义的符合通用easylist语法规则的广告过滤配置文件。

说明

此接口设置的广告过滤规则，内部解析成功后会持久化存储，应用重启后不需要重复设置。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rulesFile | string | 是 | 指定了符合easylist通用语法的规则文件路径，应用需要有此文件的读权限。 |
| replace | boolean | 是 | true表示强制替换掉内置的默认规则，false表示设置的自定义规则将与内置规则共同工作。 |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';
3. import { picker, fileUri } from '@kit.CoreFileKit';

5. // 演示点击按钮，通过filepicker打开一个easylist规则文件并设置到Web组件中
6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Row() {
13. Flex() {
14. Button({ type: ButtonType.Capsule }) {
15. Text("setAdsBlockRules")
16. }
17. .onClick(() => {
18. try {
19. let documentSelectionOptions: ESObject = new picker.DocumentSelectOptions();
20. let documentPicker: ESObject = new picker.DocumentViewPicker();
21. documentPicker.select(documentSelectionOptions).then((documentSelectResult: ESObject) => {
22. if (documentSelectResult && documentSelectResult.length > 0) {
23. let fileRealPath = new fileUri.FileUri(documentSelectResult[0]);
24. console.info('DocumentViewPicker.select successfully, uri: ' + fileRealPath);
25. webview.AdsBlockManager.setAdsBlockRules(fileRealPath.path, true);
26. }
27. })
28. } catch (err) {
29. console.error('DocumentViewPicker.select failed with err:' + err);
30. }
31. })
32. }
33. }
34. }
35. }
```

## addAdsBlockDisallowedList12+

PhonePC/2in1TabletTVWearable

static addAdsBlockDisallowedList(domainSuffixes: Array<string>): void

向AdsBlockManager的DisallowedList中添加一组域名。广告过滤功能开启时，将禁用这些网站的广告过滤功能。

说明

此接口设置的域名不会持久化，应用重启需要重新设置。

广告过滤特性会使用后缀匹配的方式判断domainSuffix和当前站点的url是否能匹配，例如，当前Web组件打开的网站是https://www.example.com，设置的DisallowedList中有'example.com'或者'www.example.com'，后缀匹配成功，此网站将禁用广告过滤，访问'https://m.example.com'也将禁用广告过滤。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
5. @Entry
6. @Component
7. struct WebComponent {
8. main_url: string = 'https://www.example.com';
9. text_input_controller: TextInputController = new TextInputController();
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id("input_url")
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text("Go") }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text("addAdsBlockDisallowedList") }
32. .onClick(() => {
33. let arrDomainSuffixes = new Array<string>();
34. arrDomainSuffixes.push('example.com');
35. arrDomainSuffixes.push('abcdefg.cn');
36. webview.AdsBlockManager.addAdsBlockDisallowedList(arrDomainSuffixes);
37. })
38. }
39. }
40. Web({ src: this.main_url, controller: this.controller })
41. .onControllerAttached(()=>{
42. this.controller.enableAdsBlock(true);
43. })
44. }
45. }
46. }
```

## removeAdsBlockDisallowedList12+

PhonePC/2in1TabletTVWearable

static removeAdsBlockDisallowedList(domainSuffixes: Array<string>): void

从AdsBlockManager的DisallowedList中删除一组域名。

说明

AdsBlockManager的DisallowedList不会持久化，应用重启需要重新设置。删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 演示通过一个按钮的点击从AdsBlockManager的DisallowedList中删除域名元素
5. @Entry
6. @Component
7. struct WebComponent {
8. main_url: string = 'https://www.example.com';
9. text_input_controller: TextInputController = new TextInputController();
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id("input_url")
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text("Go") }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text("removeAdsBlockDisallowedList") }
32. .onClick(() => {
33. let arrDomainSuffixes = new Array<string>();
34. arrDomainSuffixes.push('example.com');
35. arrDomainSuffixes.push('abcdefg.cn');
36. webview.AdsBlockManager.removeAdsBlockDisallowedList(arrDomainSuffixes);
37. })
38. }
39. }
40. Web({ src: this.main_url, controller: this.controller })
41. .onControllerAttached(()=>{
42. this.controller.enableAdsBlock(true);
43. })
44. }
45. }
46. }
```

## clearAdsBlockDisallowedList12+

PhonePC/2in1TabletTVWearable

static clearAdsBlockDisallowedList(): void

清空AdsBlockManager的DisallowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. main_url: string = 'https://www.example.com';
8. text_input_controller: TextInputController = new TextInputController();
9. controller: webview.WebviewController = new webview.WebviewController();
10. @State input_text: string = 'https://www.example.com';

12. build() {
13. Column() {
14. Row() {
15. Flex() {
16. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
17. .id("input_url")
18. .height(40)
19. .margin(5)
20. .borderColor(Color.Blue)
21. .onChange((value: string) => {
22. this.input_text = value;
23. })

25. Button({type: ButtonType.Capsule}) { Text("Go") }
26. .onClick(() => {
27. this.controller.loadUrl(this.input_text);
28. })

30. Button({type: ButtonType.Capsule}) { Text("clearAdsBlockDisallowedList") }
31. .onClick(() => {
32. webview.AdsBlockManager.clearAdsBlockDisallowedList();
33. })
34. }
35. }
36. Web({ src: this.main_url, controller: this.controller })
37. .onControllerAttached(()=>{
38. this.controller.enableAdsBlock(true);
39. })
40. }
41. }
42. }
```

## addAdsBlockAllowedList12+

PhonePC/2in1TabletTVWearable

static addAdsBlockAllowedList(domainSuffixes: Array<string>): void

向AdsBlockManager的AllowedList中添加一组域名，主要用于重新开启DisallowedList中的部分网站的广告过滤。

说明

此接口设置的域名不会持久化，应用重启需要重新设置。

AllowedList的优先级比DisallowedList高，例如，DisallowedList中配置了['example.com']，禁用了所有example.com域名下的网页，此时如果需要开启'news.example.com'下的广告过滤，可以使用addAdsBlockAllowedList(['news.example.com'])。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
5. @Entry
6. @Component
7. struct WebComponent {
8. main_url: string = 'https://www.example.com';
9. text_input_controller: TextInputController = new TextInputController();
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id("input_url")
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text("Go") }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text("addAdsBlockAllowedList") }
32. .onClick(() => {
33. let arrDisallowDomainSuffixes = new Array<string>();
34. arrDisallowDomainSuffixes.push('example.com');
35. webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);

37. let arrAllowedDomainSuffixes = new Array<string>();
38. arrAllowedDomainSuffixes.push('news.example.com');
39. webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
40. })
41. }
42. }
43. Web({ src: this.main_url, controller: this.controller })
44. .onControllerAttached(()=>{
45. this.controller.enableAdsBlock(true)
46. })
47. }
48. }
49. }
```

## removeAdsBlockAllowedList12+

PhonePC/2in1TabletTVWearable

static removeAdsBlockAllowedList(domainSuffixes: Array<string>): void

从AdsBlockManager的AllowedList中删除一组域名。

说明

AdsBlockManager的AllowedList不会持久化，应用重启需要重新设置。删除不存在的条目不会触发异常。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domainSuffixes | Array<string> | 是 | 一组域名列表，例如['example.com', 'abcd.efg.com'] |

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 演示通过一个按钮的点击从AdsBlockManager的AllowedList中删除域名元素
5. @Entry
6. @Component
7. struct WebComponent {
8. main_url: string = 'https://www.example.com';
9. text_input_controller: TextInputController = new TextInputController();
10. controller: webview.WebviewController = new webview.WebviewController();
11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id("input_url")
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text("Go") }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text("removeAdsBlockAllowedList") }
32. .onClick(() => {
33. let arrDomainSuffixes = new Array<string>();
34. arrDomainSuffixes.push('example.com');
35. arrDomainSuffixes.push('abcdefg.cn');
36. webview.AdsBlockManager.removeAdsBlockAllowedList(arrDomainSuffixes);
37. })
38. }
39. }
40. Web({ src: this.main_url, controller: this.controller })
41. .onControllerAttached(()=>{
42. this.controller.enableAdsBlock(true);
43. })
44. }
45. }
46. }
```

## clearAdsBlockAllowedList12+

PhonePC/2in1TabletTVWearable

static clearAdsBlockAllowedList(): void

清空AdsBlockManager的AllowedList。

**系统能力：** SystemCapability.Web.Webview.Core

**错误码：**

说明

从API version 18开始，在不支持广告过滤功能的设备上调用该API会抛出801异常。

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

**示例：**

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. main_url: string = 'https://www.example.com';
8. text_input_controller: TextInputController = new TextInputController();
9. controller: webview.WebviewController = new webview.WebviewController();
10. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id("input_url")
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text("Go") }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text("clearAdsBlockAllowedList") }
32. .onClick(() => {
33. webview.AdsBlockManager.clearAdsBlockAllowedList();
34. })
35. }
36. }
37. Web({ src: this.main_url, controller: this.controller })
38. .onControllerAttached(()=>{
39. this.controller.enableAdsBlock(true);
40. })
41. }
42. }
43. }
```
