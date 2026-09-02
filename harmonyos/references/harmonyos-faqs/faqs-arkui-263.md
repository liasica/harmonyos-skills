---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-263
title: Navigation容器中，如何设置子组件的高度为100%，撑满父容器
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Navigation容器中，如何设置子组件的高度为100%，撑满父容器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0402d23006c5b9de9f75b32c05cb18521a503ee929ff11ec0dbb33fea6758080
---

参考代码如下：

```typescript
import { window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'FullNavigationSubComponent';

@Entry
@Component
struct FullNavigationSubComponent {
  context = this.getUIContext();

  onPageShow(): void {
    window.getLastWindow(this.context.getHostContext(), (err, win) => {
      if (err != null) {
        hilog.error(DOMAIN, TAG, `getLastWindow failed  code:${err.code};message:${err.message}`);
      } else {
        win.setWindowLayoutFullScreen(true);
      }
    })
  }

  build() {
    Navigation() {
      Column() {
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.Black)
    }
    .width('100%')
    .height('100%')
    .title('Personalization Settings')
    .titleMode(NavigationTitleMode.Mini)
    .backgroundColor(Color.Grey)
  }
}
```
