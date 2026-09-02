---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-5
title: 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:88aeac9e95e8d2388ec82e8b2e3b7cd6dc926fb7f3251e004c36433f4ba70faf
---

先将URL设置为空，再改回原来的值，示例代码如下：

```ts
@Component
export struct VideoErrorReload {
  @State url: string = 'https://******';

  build() {
    Column({ space: 20 }) {
      Video({ src: this.url })
        .height(300)

      Button('重新url')
        .onClick(() => {
          let temp = this.url;
          this.url = '';
          setTimeout(() => {
            this.url = temp;
          }, 100);
        })
    }
  }
}
```
