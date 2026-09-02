---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-196
title: 如何保持屏幕常亮
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何保持屏幕常亮
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:af82b1a2b9780bce32a565387b7900de2a3ddf08bcd85b602535cf22a16bef61
---

获取窗口实例对象后，调用setWindowKeepScreenOn方法可设置屏幕是否常亮。

```screen
let isKeepScreenOn: boolean = true;
let windowClass: window.Window = window.findWindow("test");
try {
  windowClass.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
    const errCode: number = err.code;
    if (errCode) {
      console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(err));
      return;

    }
    console.info('Succeeded in setting the screen to be always on.');
  });
} catch (exception) {
  console.error('Failed to set the screen to be always on. Cause: ' + JSON.stringify(exception));
}
```

**参考链接**

[setWindowKeepScreenOn](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)
