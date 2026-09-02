---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-41
title: 在Web组件的H5页面中，如何使用a标签实现打开各种页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 在Web组件的H5页面中，如何使用a标签实现打开各种页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0638271045b8250c773a2a4dee4aafab8068e647ff76b24f8e29cc68d28001a1
---

情况一：跳转本应用的ArkTS页面

实现逻辑是使用Web组件的onLoadIntercept方法来监听Web组件加载的URL，然后通过回调结果判断是否需要跳转到本地ArkTS页面。如果需要跳转，使用router进行跳转。

通过获取URL并进行字符串操作来获取参数。

ArkTS页面一：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Column() {
        Web({ src: $rawfile('hello.html'), controller: this.controller })
          .onLoadIntercept((event) => {
            if(event){
              let url = event.data.getRequestUrl();
              console.log(url);
              if(url.indexOf('native://') === 0){
                this.getUIContext().getRouter().pushUrl({ url : url.substring(9)})
                return true;
              }
            }
            return false;
          })
          .width('100%')
          .height('100%')
      }
      .layoutWeight(1)
    }
  }
}
```

ArkTS页面二：

```ts
@Entry
@Component
struct Second {
  build() {
    Column() {
      Text('This is the second page of this application')
    }
  }
}
```

H5侧

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Document</title>
</head>
<body>
<div id="bg">
    hello world!<br>
    <a href="native://pages/Second">Jump to the second ads page of this application</a>
</div>
</body>
</html>
```

情况二：跳转本应用的H5页面

使用相对路径定位第二个H5页面。

H5侧页面一：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Document</title>
</head>
<body>
<div id="bg">
    hello world!<br>
    <a href="Second.html">Jump to the second H5 page of this application</a>
</div>
</body>
</html>
```

H5侧页面二：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Document</title>
</head>
<body>
<div id="bg">
    hello world
    <br>
    <br>
    I am the second H5 page of this application
</div>
</body>
</html>
```

情况三：跳转至系统应用页面

实现逻辑是在a标签的URL中存储系统应用的URL，然后使用startAbility打开系统应用，完成跳转。

ArkTS页面：

```ts
import { webview } from '@kit.ArkWeb'
import { common } from '@kit.AbilityKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function startSettingsInfo(context: common.UIAbilityContext,uri : string): void {
  let want: Want = {
    bundleName: 'com.huawei.hmos.settings',
    abilityName: 'com.huawei.hmos.settings.MainAbility',
    uri: uri
  };
  context.startAbility(want)
    .then(() => {
      // ...
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    });
}
@Entry
@Component
struct WebComponent {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Column() {
        Web({ src: $rawfile('hello.html'), controller: this.controller })
          .onLoadIntercept((event) => {
            if(event){
              let url = event.data.getRequestUrl();
              console.log(url);
              if(url.indexOf('hmos://') === 0){
                startSettingsInfo(this.context,url.substring(7))
                return true;
              }
            }
            return false;
          })
          .width('100%')
          .height('100%')
      }
      .layoutWeight(1)
    }
  }
}
```

H5侧：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>Document</title>

</head>
<body>
<div id="bg">
    hello world!<br>
    <a href="hmos://volume_settings">Jump to system application (taking sound and vibration as examples)</a>
</div>
</body>
</html>
```

情况四：跳转至三方应用页面

实现逻辑为：使用Web组件的[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)方法监测Web组件加载的URL，获取URL并判断是否需要跳转到三方应用，然后通过startAbility方法打开三方应用，完成跳转。

ArkTS页面

```ts
import { webview } from '@kit.ArkWeb'
import { common } from '@kit.AbilityKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Column() {
        Web({ src: $rawfile('hello.html'), controller: this.controller })
          .onLoadIntercept((event) => {
            let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            let want: Want = {
              deviceId: '', // An empty DeviceId indicates that this device
              bundleName: '***', // BundleName of the third-party application you want to jump to
              moduleName: 'entry', // ModuleName is not mandatory
              abilityName: 'EntryAbility',
              parameters: {
                // Customize parameters to transmit page information
                router: 'index'
              }
            }
            context.startAbility(want).then(() => {
              console.log('success')
            }).catch((err: BusinessError) => {
              console.log('error:' + JSON.stringify(err))
            });
            return false;
          })
      }
      .layoutWeight(1)
    }

  }
}
```

H5侧：

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<a  href="">Jump to third-party applications</a>
</body>
</html>
```
