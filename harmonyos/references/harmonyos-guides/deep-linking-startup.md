---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup
title: 使用Deep Linking实现应用间跳转
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > 应用间跳转 > 拉起指定应用 > 使用Deep Linking实现应用间跳转
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:00953dc1e9ad8ee9a6357ba0db41a9ff0b355a2a03897c30ef91421940e479c7
---

采用Deep Linking进行跳转时，系统会根据接口中传入的uri信息，在本地已安装的应用中寻找到符合条件的应用并进行拉起。当匹配到多个应用时，会拉起应用选择框。

## 实现原理

Deep Linking基于隐式Want匹配机制中的uri匹配来查询、拉起目标应用。隐式Want的uri匹配规则详见[uri匹配规则](explicit-implicit-want-mappings.md#uri匹配规则)。

## 目标应用操作指导

### 配置module.json5文件

为了能够支持被其他应用访问，目标应用需要在[module.json5配置文件](module-configuration-file.md)中配置[skills标签](module-configuration-file.md#skills标签)。

**说明** 

skills标签下默认包含一个skill对象，用于标识应用入口。应用跳转链接不能在该skill对象中配置，需要创建独立的skill对象。如果存在多个跳转场景，需要在skills标签下创建不同的skill对象，否则会导致配置无法生效。

配置示例如下：

```json5
{
  "module": {
    // ···
    "abilities": [
    // ···
      {
        // ···
        "skills": [
          {
            "entities": [
              "entity.system.home"
            ],
            "actions": [
              "ohos.want.action.home"
            ]
          },
          {
            "actions": [
              // actions不能为空，actions为空会造成目标方匹配失败。
              "ohos.want.action.viewData"
            ],
            "uris": [
              {
                // scheme必选，可以自定义，以link为例，需要替换为实际的scheme
                "scheme": "link",
                "host": "www.example.com"
              }
            ]
          } // 新增一个skill对象，用于跳转场景。如果存在多个跳转场景，需配置多个skill对象。
        ]
      },
    // ···
    ],
    // ···
  }
}
```

### 获取并解析拉起方传入的应用链接

在目标应用的UIAbility的[onCreate()](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或者[onNewWant()](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)生命周期回调中，获取、解析拉起方传入的应用链接。

```typescript
// 以DeepAbility.ets为例
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { url } from '@kit.ArkTS';

const DOMAIN = 0x0000;

export default class DeepAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    // 从want中获取传入的链接信息。
    // 如传入的url为：link://www.example.com/programs?action=showall
    let uri = want?.uri;
    if (uri) {
      // 从链接中解析query参数，拿到参数后，开发者可根据自己的业务需求进行后续的处理。
      let urlObject = url.URL.parseURL(want?.uri);
      let action = urlObject.params.get('action');
      // 例如，当action为showall时，展示所有的节目。
      if (action === 'showall') {
        // ···
      }
    }
  }
// ···
}
```

## 拉起方应用实现应用跳转

下面通过三个案例，分别介绍如何使用[openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)与[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口实现应用跳转，以及如何在[Web组件](../harmonyos-references/arkts-basic-components-web.md)中实现应用跳转。

### 使用openLink实现应用跳转

在[openLink()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)接口的link字段中传入目标应用的URL信息，并将options字段中的[appLinkingOnly](../harmonyos-references/js-apis-app-ability-openlinkoptions.md#openlinkoptions)配置为false。

示例代码如下：

```typescript
import { common, OpenLinkOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct DeepOpenLinkIndex {
  build() {
    Button('start link', { type: ButtonType.Capsule, stateEffect: true })
      .width('87%')
      .height('5%')
      .margin({ bottom: '12vp' })
      .onClick(() => {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let link: string = 'link://www.example.com'; // 此处为实际应用链接
        let openLinkOptions: OpenLinkOptions = {
          appLinkingOnly: false
        };

        try {
          context.openLink(link, openLinkOptions)
            .then(() => {
              hilog.info(DOMAIN_NUMBER, TAG, 'openLink success.');
            }).catch((err: BusinessError) => {
            hilog.error(DOMAIN_NUMBER, TAG, `openLink failed. Code is ${err.code}, message is ${err.message}`);
          });
        } catch (paramError) {
          hilog.error(DOMAIN_NUMBER, TAG, `Failed to start link. Code is ${paramError.code}, message is ${paramError.message}`);
        }
      })
  }
}
```

### 使用startAbility实现应用跳转

[startAbility()](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口是将应用链接放入Want中，通过调用[隐式Want匹配](explicit-implicit-want-mappings.md#隐式want匹配原理)的方法触发应用跳转。

示例代码如下：

```typescript
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[UIAbilityComponentsOpenLink]';
const DOMAIN_NUMBER: number = 0xFF00;

@Entry
@Component
struct DeepStartIndex {
  build() {
    Button('start ability', { type: ButtonType.Capsule, stateEffect: true })
      .width('87%')
      .height('5%')
      .margin({ bottom: '12vp' })
      .onClick(() => {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let want: Want = {
          uri: 'link://www.example.com' // 此处为实际应用链接
        };

        try {
          context.startAbility(want).then(() => {
            hilog.info(DOMAIN_NUMBER, TAG, 'startAbility success.');
          }).catch((err: BusinessError) => {
            hilog.error(DOMAIN_NUMBER, TAG, `startAbility failed. Code is ${err.code}, message is ${err.message}`);
          });
        } catch (paramError) {
          hilog.error(DOMAIN_NUMBER, TAG, `Failed to start ability. Code is ${paramError.code}, message is ${paramError.message}`);
        }
      })
  }
}
```

### 使用Web组件实现应用跳转

Web组件可以在[onLoadIntercept()](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)的回调函数中实现应用跳转。

示例代码如下：

```typescript
// DeepWebIndex.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN_NUMBER = 0xF811;
const TAG = '[Sample_PullLinking]';

@Entry
@Component
struct DeepWebIndex {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onLoadIntercept((event) => {
          const url: string = event.data.getRequestUrl();
          if (url === 'link://www.example.com') {
            (this.getUIContext().getHostContext() as common.UIAbilityContext).openLink(url)
              .then(() => {
                hilog.info(DOMAIN_NUMBER, TAG, 'openLink success.');
              }).catch((err: BusinessError) => {
              hilog.error(DOMAIN_NUMBER, TAG, `openLink failed, err: ${JSON.stringify(err)}.`);
            });
            return true;
          }
          // 返回true表示阻止此次加载，否则允许此次加载
          return false;
        })
    }
  }
}
```

前端页面代码：

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
<h1>Hello World</h1>
<!--方式一、通过绑定事件window.open方法实现跳转-->
<button class="doOpenLink" onclick="doOpenLink()">跳转其他应用一</button>
<!--方式二、通过超链接实现跳转-->
<a href="link://www.example.com">跳转其他应用二</a>
</body>
</html>
<script>
    function doOpenLink() {
        window.open("link://www.example.com")
    }
</script>
```
