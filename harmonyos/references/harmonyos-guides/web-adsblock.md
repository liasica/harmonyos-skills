---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-adsblock
title: 使用Web组件的广告过滤功能
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理Web组件的网络安全与隐私 > 使用Web组件的广告过滤功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c9932b9b55504afef6f80740021bfbb06d58a246da4f4eb54cf9cba2b19b457
---

ArkWeb为应用提供广告过滤功能，支持通过云端推送默认的easylist规则，或允许应用通过接口设定自定义规则文件。它在网络层拦截广告资源的下载，或在网页中注入CSS规则以隐藏特定的广告元素。

当前配置文件格式为[easylist规则](https://easylist-downloads.adblockplus.org/easylist.txt)。

## 常用easylist语法规则

| 规则类别 | 说明 | 示例 |
| --- | --- | --- |
| URL拦截规则 | 拦截所有网站中url能匹配"example.com/js/\*\_tv.js"的子资源请求。用于定义域名过滤规则，匹配特定的域名及其所有子域名。 | ||example.com/js/\*\_tv.js |
| URL拦截规则 | 拦截非alimama.com、非taobao.com域名网站中的url匹配"alimama.cn"的第三方资源。$third\_party是一种options语法，表示匹配第三方资源；域名前使用'~'表示不包括该域名。 | ||alimama.cn^$third-party,domain=~alimama.com|~taobao.com |
| 例外规则 | 关闭example.com网页内的广告过滤。@@是例外规则的语法关键字，表示不过滤。 | @@||example.com^$document |
| 例外规则 | 在域名为litv.tv的网页中，不过滤能匹配上".adserver."的子资源。 | @@.adserver.$domain=litv.tv |
| 元素隐藏规则 | 隐藏myabandonware.com和myware.com域名中所有class="i528"的元素。##用于表示元素隐藏。 | myabandonware.com, myware.com##.i528 |
| 元素隐藏例外规则 | 不隐藏sdf-event.sakura.ne.jp网站中id="ad\_1"的元素。 | sdf-event.sakura.ne.jp#@##ad\_1 |

例外规则，通常是与普通规则配合使用的，在某些特定场景下使普通规则不适用，单独应用例外规则是没有意义的。

例如先配置了一条过滤所有网站的拦截规则：||abc.com/js/123.js，如果某些网站出现误拦截或不能拦截的情况，可以针对这些网站配置新的例外规则。

## 约束与限制

* 在[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)类中，增加开启/关闭广告过滤特性的接口[enableAdsBlock()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#enableadsblock12)，支持Web实例级的特性开关。
* 新增[AdsBlockManager](../harmonyos-references/arkts-apis-webview-adsblockmanager.md)全局单例类，提供自定义广告过滤配置、控制网站级特性开关的能力。
* Web实例上提供了[onAdsBlocked()](../harmonyos-references/arkts-basic-components-web-attributes.md#onadsblocked12)回调通知方法，支持将拦截信息通知到上层应用。
* [AdsBlockManager](../harmonyos-references/arkts-apis-webview-adsblockmanager.md)接口[setAdsBlockRules()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#setadsblockrules12)接口仅能设置一份自定义配置，此配置会持久化，应用冷启动无需重新配置，可避免每次冷启动配置规则都触发广告过滤配置的编译解析。
* [AdsBlockManager](../harmonyos-references/arkts-apis-webview-adsblockmanager.md)接口[addAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)、[removeAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#removeadsblockdisallowedlist12)、[clearAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#clearadsblockdisallowedlist12)、[addAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockallowedlist12)、[removeAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#removeadsblockallowedlist12)、[clearAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#clearadsblockallowedlist12)操作的数据不会持久化，应用冷启动需要重新设置。
* 如果1个Web实例启用了广告过滤特性，但未调用[AdsBlockManager](../harmonyos-references/arkts-apis-webview-adsblockmanager.md)接口[addAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)、[removeAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#removeadsblockdisallowedlist12)、[clearAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#clearadsblockdisallowedlist12)、[addAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockallowedlist12)、[removeAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#removeadsblockallowedlist12)、[clearAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#clearadsblockallowedlist12)配置disallowedlist和allowedlist数据，则默认所有网站均启用广告过滤。
* allowedlist和disallowedlist数据共同使用时，allowedlist的优先级高于disallowedlist，即先使用allowedlist匹配，如果匹配成功就不再使用disallowedlist匹配，该网站会启用广告过滤特性。
* 如果应用未启用广告过滤特性，那么Web组件不会向服务器请求默认的内置easylist规则。
* disallowedlist和allowedlist数据采用后缀匹配，例如应用的设置的域名"xxyy.com"，可以匹配上url为"wwsstt.xxyy.com"的网站。

## 使用场景

### 开启广告过滤

应用可以通过AdsBlockManager提供的[setAdsBlockRules()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#setadsblockrules12)接口设置自定义的easylist过滤规则，并通过Web组件的[enableAdsBlock()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#enableadsblock12)接口使能广告过滤特性。

在下面的示例中，演示了一个应用通过文件选择器选择easylist规则文件，并开启广告过滤功能。

```
1. import { webview } from '@kit.ArkWeb';
2. import { picker, fileUri } from '@kit.CoreFileKit';

4. // 演示点击按钮，通过filepicker打开一个easylist规则文件并设置到Web组件中
5. @Entry
6. @Component
7. struct WebComponent {
8. main_url: string = 'https://www.example.com';
9. controller: webview.WebviewController = new webview.WebviewController();

11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. Button({type: ButtonType.Capsule}) {
18. Text('setAdsBlockRules')
19. }
20. .onClick(() => {
21. try {
22. let documentSelectionOptions: ESObject = new picker.DocumentSelectOptions();
23. let documentPicker: ESObject = new picker.DocumentViewPicker();
24. documentPicker.select(documentSelectionOptions).then((documentSelectResult: ESObject) => {
25. if (documentSelectResult && documentSelectResult.length > 0) {
26. let fileRealPath = new fileUri.FileUri(documentSelectResult[0]);
27. console.info('DocumentViewPicker.select successfully, uri: ' + fileRealPath);
28. webview.AdsBlockManager.setAdsBlockRules(fileRealPath.path, true);
29. }
30. })
31. } catch (err) {
32. console.error('DocumentViewPicker.select failed with err:' + err);
33. }
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

[EnablingAdsBlocking.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/EnablingAdsBlocking.ets#L16-L60)

如果存在内置的easylist规则文件，[setAdsBlockRules()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#setadsblockrules12)接口的replace参数可用于设置规则文件的使用策略，replace为true表示不使用内置的easylist规则文件，replace为false表示自定义规则和内置的规则将会同时工作，如果发现内置规则与自定义规则冲突，可使用replace=true禁用内置规则效果。

设置的自定义规则文件在应用进程内对所有的Web组件生效，是一个应用级全局配置文件，并将持久化，应用重启后可继续工作。

### 关闭特定域名页面的广告过滤

在Web组件的广告过滤开关开启后，应用有时候会期望关闭一些特定页面的广告过滤功能，除了可以使用自定义的easylist规则，AdsBlockManager还提供了[addAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)接口完成此功能。

```
1. import { webview } from '@kit.ArkWeb';

3. // 演示通过一个按钮的点击向Web组件设置广告过滤的域名策略
4. @Entry
5. @Component
6. struct WebComponent {
7. main_url: string = 'https://www.example.com';
8. text_input_controller: TextInputController = new TextInputController();
9. controller: webview.WebviewController = new webview.WebviewController();

11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id('input_url')
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text('Go') }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text('addAdsBlockDisallowedList') }
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

[DisAdsBlockSpecDomPages\_one.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/DisAdsBlockSpecDomPages_one.ets#L15-L62)

[addAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)接口将域名设置到AdsBlockManager的DisallowedList中，下次页面加载时会使用网页url和DisallowedList中的域名进行后缀匹配，匹配成功则不会对此页面进行广告过滤。此外，还提供了[addAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockallowedlist12)接口配合DisallowedList进行域名设置，控制是否开启广告过滤。

AdsBlockManager中缓存有2组域名列表，分别为DisallowedList和AllowedList，其中DisallowedList用于禁用网页的广告过滤，而AllowedList用于重新开启被DisallowedList关闭的广告过滤开关，其中AllowedList优先级更高。页面加载时会先使用网页url和AllowedList进行匹配，匹配成功的网页广告过滤将保持开启，否则将会继续使用DisallowedList进行匹配，匹配成功将关闭网页的广告过滤。如果访问的网页不在AllowedList和DisallowedList中，那么默认网页的广告过滤会保持开启状态。

例如，应用想要开启域名为'news.example.com'和'sport.example.com'的广告过滤，但需要关闭'example.com'的其他域名下网页的广告过滤，就可以先使用[addAdsBlockDisallowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockdisallowedlist12)接口添加'example.com'域名到DisallowedList，再使用[addAdsBlockAllowedList()](../harmonyos-references/arkts-apis-webview-adsblockmanager.md#addadsblockallowedlist12)接口添加'news.example.com'和'sport.example.com'域名。

```
1. import { webview } from '@kit.ArkWeb';

3. // 演示addAdsBlockAllowedList和addAdsBlockDisallowedList配套使用，设置网页级的广告过滤开关。
4. @Entry
5. @Component
6. struct WebComponent {
7. main_url: string = 'https://www.example.com';
8. text_input_controller: TextInputController = new TextInputController();
9. controller: webview.WebviewController = new webview.WebviewController();

11. @State input_text: string = 'https://www.example.com';

13. build() {
14. Column() {
15. Row() {
16. Flex() {
17. TextInput({ text: this.input_text, placeholder: this.main_url, controller: this.text_input_controller})
18. .id('input_url')
19. .height(40)
20. .margin(5)
21. .borderColor(Color.Blue)
22. .onChange((value: string) => {
23. this.input_text = value;
24. })

26. Button({type: ButtonType.Capsule}) { Text('Go') }
27. .onClick(() => {
28. this.controller.loadUrl(this.input_text);
29. })

31. Button({type: ButtonType.Capsule}) { Text('addAdsBlockAllowedList') }
32. .onClick(() => {
33. let arrDisallowDomainSuffixes = new Array<string>();
34. arrDisallowDomainSuffixes.push('example.com');
35. webview.AdsBlockManager.addAdsBlockDisallowedList(arrDisallowDomainSuffixes);

37. let arrAllowedDomainSuffixes = new Array<string>();
38. arrAllowedDomainSuffixes.push('news.example.com');
39. arrAllowedDomainSuffixes.push('sport.example.com');
40. webview.AdsBlockManager.addAdsBlockAllowedList(arrAllowedDomainSuffixes);
41. })
42. }
43. }
44. Web({ src: this.main_url, controller: this.controller })
45. .onControllerAttached(()=>{
46. this.controller.enableAdsBlock(true);
47. })
48. }
49. }
50. }
```

[DisAdsBlockSpecDomPages\_two.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/DisAdsBlockSpecDomPages_two.ets#L15-L66)

需要注意的是，AdsBlockManager的DisallowedList和AllowedList列表不会持久化，因此重启应用后会重置为空。

如果Web组件未通过[enableAdsBlock()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#enableadsblock12)接口开启广告过滤功能，上述接口设置在此Web组件中将不起作用。

### 收集广告过滤的信息

在Web组件的广告过滤开关开启后，访问的网页如果发生了广告过滤，会通过Web组件的[onAdsBlocked()](../harmonyos-references/arkts-basic-components-web-attributes.md#onadsblocked12)回调接口通知到应用，应用可根据需要进行过滤信息的收集和统计。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. @State totalAdsBlockCounts: number = 0;

8. controller: webview.WebviewController = new webview.WebviewController();

10. build() {
11. Column() {
12. Web({ src: 'https://www.example.com', controller: this.controller })
13. .onAdsBlocked((details: AdsBlockedDetails) => {
14. if (details) {
15. console.info(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
16. let adList: Array<string> = Array.from(new Set(details.adsBlocked));
17. this.totalAdsBlockCounts += adList.length;
18. console.info('Total blocked counts :' + this.totalAdsBlockCounts);
19. }
20. })
21. }
22. }
23. }
```

[CollectingAdsBlockingInformation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebCompSecPriv/entry/src/main/ets/pages/CollectingAdsBlockingInformation.ets#L16-L40)

由于页面可能随时发生变化并不断产生网络请求，为了减少通知频次、降低对页面加载过程的影响，仅在页面加载完成时进行首次通知，此后发生的过滤将间隔1秒钟上报，无广告过滤则无通知。
