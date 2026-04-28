---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-5
title: 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:374f88ac8c37b2e4bb4a695b3902c704cdfc5128836a72bdb9e16c46684ae878
---

先将URL设置为空，再改回原来的值，示例代码如下：

```
1. @Component
2. export struct VideoErrorReload {
3. @State url: string = 'https://******';

5. build() {
6. Column({ space: 20 }) {
7. Video({ src: this.url })
8. .height(300)

10. Button('重新url')
11. .onClick(() => {
12. let temp = this.url;
13. this.url = '';
14. setTimeout(() => {
15. this.url = temp;
16. }, 100);
17. })
18. }
19. }
20. }
```

[VideoErrorReload.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AudioKit/entry/src/main/ets/pages/VideoErrorReload.ets#L6-L25)
