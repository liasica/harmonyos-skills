---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-190
title: 如何获取窗口的宽高信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取窗口的宽高信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:03d558b8af6b4accc908a0fae5431320e5271d9fea3056b4977073aa316316ec
---

获取指定窗口对象Window后，在该对象上使用[getWindowProperties()](../harmonyos-references/arkts-apis-window-window.md#getwindowproperties9)获取窗口各个属性，在属性windowRect中获取窗口宽高信息。如果要在页面中获取窗口宽高信息，需要注意获取的正确时机。页面生命周期[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)阶段，不代表此时窗口可见，仅代表当前组件已创建，此时获取到的窗口尺寸信息（windowRect）可能有误。建议在页面生命周期[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)阶段获取，该阶段会在窗口可见后调用，此时可以拿到窗口正确的宽高信息。参考代码如下：

```ts
//If you need to get the window width and height information in the page, it is recommended to put the following code in the onPageShow stage of the page life cycle, rather than calling it in the aboutToAppear stage of the page life cycle
let windowClass: window.Window | undefined = undefined;
try {
  let promise = window.getLastWindow(this.context);
  promise.then((data) => {
    //Get window object
    windowClass = data;
    try {
      //Get window properties
      let properties = windowClass.getWindowProperties();
      let rect = properties.windowRect;
      //rect.width: Window Width, rect.height: Window height
    } catch (exception) {
      console.error('Failed to obtain the window properties. Cause: ' + JSON.stringify(exception));
    }
    console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
  });
} catch (exception) {
  console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
}
```
