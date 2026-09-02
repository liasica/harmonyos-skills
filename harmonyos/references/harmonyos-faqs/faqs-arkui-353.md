---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-353
title: Toggle组件响应点击后会立即渲染并回调。如何实现点击后延迟改变状态并时回调
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Toggle组件响应点击后会立即渲染并回调。如何实现点击后延迟改变状态并时回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cb704c2d5f03e2d17059e1cde6e4934809ce5dd213824409d4bb7865d53aa9d7
---

使用hitTestBehavior和setTimeout解决。示例代码如下：

```ts
@Entry
@Component
struct ToggleDemo {
  @State isDarkMode: boolean = false;
  private timeoutID?: number;

  aboutToDisappear(): void {
    clearTimeout(this.timeoutID);
  }

  build() {
    Column() {
      Column() {
        Toggle({ type: ToggleType.Switch, isOn: $$this.isDarkMode })
          .onChange((isOn: boolean) => {
            console.info('Toggle.onChange:isOn' + isOn);
            this.isDarkMode = isOn;
            this.getUIContext().getHostContext()!.getApplicationContext().setColorMode(this.isDarkMode ? 0 : 1);
          })
      }
      // Set hitTestBehavior property to HitTestMode.Block to block Toggle component's event response.
      .hitTestBehavior(HitTestMode.Block)
      .onClick(() => {
        this.timeoutID = setTimeout(() => {
          this.isDarkMode = !this.isDarkMode;
        }, 1500);
      })
    }
    .width('100%')
    .height('100%')
    .padding(32)
  }
}
```
