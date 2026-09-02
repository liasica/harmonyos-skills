---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-154
title: 如何获取Web组件的宽度
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何获取Web组件的宽度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af88afff9b8e19b7fa3f37ed1893202468f4eb2e6dae7ffcfb65a10d7938cd8d
---

## 问题现象

getPageHeight()方法用于获取当前网页的页面高度，如何获取当前Web组件的宽度？

## 背景知识

* [getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)：获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。
* [应用侧调用前端页面函数](../harmonyos-guides/web-in-app-frontend-page-function-invoking.md)：应用侧可以通过runJavaScript()和runJavaScriptExt()方法调用前端页面的JavaScript相关函数。

## 解决方案

**方案一**：获取Web组件的宽度，需要先给Web组件标记一个id，然后通过getRectangleById获取组件信息，根据组件的size.width获取宽度。因为要跟方案二中前端网页获取的宽度对齐，需要使用px2vp将像素（px）转换为视觉像素（vp）。

**方案二**：通过runJavaScript方法注入window.innerWidth方法，在回调中即可获取到Web组件的宽度，单位为vp。

两种方案示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';
import { ComponentUtils } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebGetWidth{
  controller: webview.WebviewController = new webview.WebviewController();
  @State webResult: string = '';

  build() {
    Column() {
      // 获取组件宽度
      Button('获取组件宽度').onClick(() => {
        // 获取组件信息对象，然后获取对象里的size.width取得宽度
        let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
        let obj = componentUtils.getRectangleById('1');
        console.info('width is:', this.getUIContext().px2vp(obj.size.width));
      });
      // 加载链接需要替换自己业务链接
      Web({ src: 'www.example.com', controller: this.controller })
        .id('1')
        .onPageEnd((event) => {
          if (event) {
            // 执行js获取页面宽度
            this.controller.runJavaScript(
              'function getWidth(){\n' +
                '    return window.innerWidth;\n' +
                '    }\n' +
                '    getWidth();',
              // 在回调中获取前端js结果
              (error, result) => {
                if (error) {
                  console.error(`run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                if (result) {
                  this.webResult = result;
                  console.info(`The width return value is: ${result}`);
                }
              });
          }
        })
        .domStorageAccess(true)
        .javaScriptAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .width(200);
    };
  }
}
```

访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 常见FAQ

Q：通过getWindowProperties()系统方法获取的屏幕宽为何与Web加载的H5中通过window.innerWidth方法获取的宽度不一致？

A：通过[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)系统方法获取的是当前窗口尺寸，即屏幕分辨率的宽度，单位为px。

通过window.innerWidth方法获取的是布局视口的宽度，如果在H5中给viewport的content添加width=device-width，说明当前H5已经适配当前设备尺寸，获取的宽度为Web组件的宽度，单位为vp。如果没有添加，设备上的浏览器都会把默认的viewport设为980px或1024px（这个值由设备决定），单位为px。

如果需要在H5中获取到屏幕宽度，可以使用window.screen.width获取，单位为vp。使用[vp2px](../harmonyos-references/arkts-apis-uicontext-uicontext.md#vp2px12)和[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)方法，px与vp两个单位可以相互转换。
