---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-194
title: 如何锁定设备竖屏，使得窗口不随屏幕旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何锁定设备竖屏，使得窗口不随屏幕旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e0946ad5f9a6afb83f48233c54883fcb95964563b8431b908e9f0a4218bcff70
---

使用setPreferredOrientation方法锁定竖屏，设置orientation为window.Orientation.PORTRAIT。参考代码如下：

```ts
//1.Get the window instance object, use the createWindow method to create a new window, and use the findWindow method to obtain an existing window
let windowClass: window.Window | undefined = undefined;
let config: window.Configuration = {
  name: "alertWindow",
  windowType: window.WindowType.TYPE_SYSTEM_ALERT,
  ctx: this.context
};
try {
  let promise = window.createWindow(config);
  promise.then((data)=> {
    windowClass = data;
    console.info('Succeeded in creating the window. Data:' + JSON.stringify(data));
  }).catch((err: BusinessError)=>{
    console.error('Failed to create the Window. Cause:' + JSON.stringify(err));
  });} catch (exception) {
  console.error('Failed to create the window. Cause: ' + JSON.stringify(exception));
}
//2.The window instance uses the setPreferred Orientation method to set the display orientation of the window. PORTRAIT is a fixed vertical screen, and other orientations can refer to the reference link
let orientation = window.Orientation.PORTRAIT;
try {
  let windowClass: window.Window = window.findWindow("test");
  windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in setting window orientation.');
  });
} catch (exception) {
  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
}
```

**参考链接**

[Orientation](../harmonyos-references/js-apis-display.md#orientation10)
