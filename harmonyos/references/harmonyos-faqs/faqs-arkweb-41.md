---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-41
title: 在Web组件的H5页面中，如何使用a标签实现打开各种页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 在Web组件的H5页面中，如何使用a标签实现打开各种页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c2b2cf842a401ec07656f0fb4df2e8903e02ceea22f8473bda0bb9782fed45b9
---

情况一：跳转本应用的ArkTS页面

实现逻辑是使用Web组件的onLoadIntercept方法来监听Web组件加载的URL，然后通过回调结果判断是否需要跳转到本地ArkTS页面。如果需要跳转，使用router进行跳转。

通过获取URL并进行字符串操作来获取参数。

ArkTS页面一：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();
7. build() {
8. Column() {
9. Column() {
10. Web({ src: $rawfile('hello.html'), controller: this.controller })
11. .onLoadIntercept((event) => {
12. if(event){
13. let url = event.data.getRequestUrl();
14. console.log(url);
15. if(url.indexOf('native://') === 0){
16. this.getUIContext().getRouter().pushUrl({ url : url.substring(9)})
17. return true;
18. }
19. }
20. return false;
21. })
22. .width('100%')
23. .height('100%')
24. }
25. .layoutWeight(1)
26. }
27. }
28. }
```

[UseLabelAOpenPages\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseLabelAOpenPages_One.ets#L21-L48)

ArkTS页面二：

```
1. @Entry
2. @Component
3. struct Second {
4. build() {
5. Column() {
6. Text('This is the second page of this application')
7. }
8. }
9. }
```

[UseLabelAOpenPages\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseLabelAOpenPages_Two.ets#L21-L29)

H5侧

```
1. <!DOCTYPE html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8" />
5. <meta http-equiv="X-UA-Compatible" content="IE=edge" />
6. <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
7. <title>Document</title>
8. </head>
9. <body>
10. <div id="bg">
11. hello world!<br>
12. <a href="native://pages/Second">Jump to the second ads page of this application</a>
13. </div>
14. </body>
15. </html>
```

[UseLabelAOpenPages\_Fragment\_One.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseLabelAOpenPages_Fragment_One.html#L21-L35)

情况二：跳转本应用的H5页面

使用相对路径定位第二个H5页面。

H5侧页面一：

```
1. <!DOCTYPE html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8" />
5. <meta http-equiv="X-UA-Compatible" content="IE=edge" />
6. <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
7. <title>Document</title>
8. </head>
9. <body>
10. <div id="bg">
11. hello world!<br>
12. <a href="Second.html">Jump to the second H5 page of this application</a>
13. </div>
14. </body>
15. </html>
```

[UseLabelAOpenPages\_Fragment\_Two.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseLabelAOpenPages_Fragment_Two.html#L21-L35)

H5侧页面二：

```
1. <!DOCTYPE html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8" />
5. <meta http-equiv="X-UA-Compatible" content="IE=edge" />
6. <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
7. <title>Document</title>
8. </head>
9. <body>
10. <div id="bg">
11. hello world
12. <br>
13. <br>
14. I am the second H5 page of this application
15. </div>
16. </body>
17. </html>
```

[UseLabelAOpenPages\_Fragment\_Three.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseLabelAOpenPages_Fragment_Three.html#L21-L37)

情况三：跳转至系统应用页面

实现逻辑是在a标签的URL中存储系统应用的URL，然后使用startAbility打开系统应用，完成跳转。

ArkTS页面：

```
1. import { webview } from '@kit.ArkWeb'
2. import { common } from '@kit.AbilityKit';
3. import { Want } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. function startSettingsInfo(context: common.UIAbilityContext,uri : string): void {
7. let want: Want = {
8. bundleName: 'com.huawei.hmos.settings',
9. abilityName: 'com.huawei.hmos.settings.MainAbility',
10. uri: uri
11. };
12. context.startAbility(want)
13. .then(() => {
14. // ...
15. })
16. .catch((err: BusinessError) => {
17. console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
18. });
19. }
20. @Entry
21. @Component
22. struct WebComponent {
23. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
24. controller: webview.WebviewController = new webview.WebviewController();
25. build() {
26. Column() {
27. Column() {
28. Web({ src: $rawfile('hello.html'), controller: this.controller })
29. .onLoadIntercept((event) => {
30. if(event){
31. let url = event.data.getRequestUrl();
32. console.log(url);
33. if(url.indexOf('hmos://') === 0){
34. startSettingsInfo(this.context,url.substring(7))
35. return true;
36. }
37. }
38. return false;
39. })
40. .width('100%')
41. .height('100%')
42. }
43. .layoutWeight(1)
44. }
45. }
46. }
```

[UseLabelAOpenPages\_Three.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseLabelAOpenPages_Three.ets#L21-L66)

H5侧：

```
1. <!DOCTYPE html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8" />
5. <meta http-equiv="X-UA-Compatible" content="IE=edge" />
6. <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
7. <title>Document</title>

9. </head>
10. <body>
11. <div id="bg">
12. hello world!<br>
13. <a href="hmos://volume_settings">Jump to system application (taking sound and vibration as examples)</a>
14. </div>
15. </body>
16. </html>
```

[UseLabelAOpenPages\_Fragment\_Four.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseLabelAOpenPages_Fragment_Four.html#L21-L36)

情况四：跳转至三方应用页面

实现逻辑为：使用Web组件的[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)方法监测Web组件加载的URL，获取URL并判断是否需要跳转到三方应用，然后通过startAbility方法打开三方应用，完成跳转。

ArkTS页面

```
1. import { webview } from '@kit.ArkWeb'
2. import { common } from '@kit.AbilityKit';
3. import { Want } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct WebComponent {
9. controller: webview.WebviewController = new webview.WebviewController();
10. build() {
11. Column() {
12. Column() {
13. Web({ src: $rawfile('hello.html'), controller: this.controller })
14. .onLoadIntercept((event) => {
15. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
16. let want: Want = {
17. deviceId: '', // An empty DeviceId indicates that this device
18. bundleName: '***', // BundleName of the third-party application you want to jump to
19. moduleName: 'entry', // ModuleName is not mandatory
20. abilityName: 'EntryAbility',
21. parameters: {
22. // Customize parameters to transmit page information
23. router: 'index'
24. }
25. }
26. context.startAbility(want).then(() => {
27. console.log('success')
28. }).catch((err: BusinessError) => {
29. console.log('error:' + JSON.stringify(err))
30. });
31. return false;
32. })
33. }
34. .layoutWeight(1)
35. }

37. }
38. }
```

[UseLabelAOpenPages\_Four.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UseLabelAOpenPages_Four.ets#L21-L58)

H5侧：

```
1. <!doctype html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8">
5. <meta name="viewport"
6. content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
7. <meta http-equiv="X-UA-Compatible" content="ie=edge">
8. <title>Document</title>
9. </head>
10. <body>
11. <a  href="">Jump to third-party applications</a>
12. </body>
13. </html>
```

[UseLabelAOpenPages\_Fragment\_Five.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/UseLabelAOpenPages_Fragment_Five.html#L21-L33)
