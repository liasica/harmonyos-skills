---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-206
title: 如何进行页面横竖屏切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何进行页面横竖屏切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d2e1eb4b2bebc2d09287d1fef25000045a0f872c4444bf6abb9b00d3cd2c5f5
---

设置方法：setPreferredOrientation(orientation: Orientation, callback: AsyncCallback<void>): void。Orientation取值为AUTO\_ROTATION，表示传感器自动旋转模式。参考代码如下：

```screen
let orientation = window.Orientation.AUTO_ROTATION;
try{
  windowClass.setPreferredOrientation(orientation, (err) => {
    if(err.code){
      console.error('Failed to set window orientation. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in setting window orientation.');
  });
}catch (exception) {
  console.error('Failed to set window orientation. Cause: ' + JSON.stringify(exception));
}
```

**参考链接**

[setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)
