---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-350
title: bindPopup适配Web组件长按菜单功能，设置offset控制弹窗的偏移
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > bindPopup适配Web组件长按菜单功能，设置offset控制弹窗的偏移
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:57a08ad71c446e01f0a786aa267447817d2429b3a09aa9525f5dfbba51f320c0
---

由于WebView组件本身不支持直接绑定Popup，需在同层添加透明占位组件作为Popup载体，可以在 WebView 组件前（同层）添加一个大小为 0 的组件来承载 bindPopup。根据当前 UX 规范，弹出菜单的边距左右各为 7vp，以确保其在屏幕范围内。具体代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct BindPopupOffset {
  controller: webview.WebviewController = new webview.WebviewController();
  private result: WebContextMenuResult | undefined = undefined;
  @State linkUrl: string = '';
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State showMenu: boolean = false;

  @Builder
  menuBuilder() {
    Menu() {
      MenuItem({
        content: 'copy picture',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: 'cut'
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
    }
    .width(150)
    .backgroundColor('#eeeeee')
  }

  build() {
    Column() {
      Row()
        .width(0)
        .height(0)
        .position({ x: 0, y: 0 })
        .bindPopup(this.showMenu,
          {
            builder: this.menuBuilder(),
            enableArrow: false,
            placement: Placement.LeftTop,
            targetSpace: 0,
            shadow: {
              radius: 0
            },
            offset: {
              x: this.offsetX - 7,
              y: this.offsetY
            },
            mask: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.showMenu = false;
                this.result?.closeContextMenu();
              }
            }
          })

      // index.html It should include elements that trigger the contextmenu event.
      Web({ src: $rawfile('index.html'), controller: this.controller })//Trigger custom pop ups
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result;
            this.showMenu = true;
            this.offsetX = Math.max(this.getUIContext().px2vp(event?.param.x() ?? 0) - 0, 0);
            this.offsetY = Math.max(this.getUIContext().px2vp(event?.param.y() ?? 0) - 0, 0);
          }
          return true;
        })
    }
  }
}
```
