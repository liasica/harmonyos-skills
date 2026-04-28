---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-16
title: 注册的自定义字体在webview中无效
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 注册的自定义字体在webview中无效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4e5307a6e36462bdf4c08c348b51709a2a24fbb58095a6fb814ab51a256c6b6c
---

**问题现象**

通过@ohos.font.registerFont接口注册的自定义字体在webview中设置对应的family无法正确显示。在webview H5中设置DOM style font-family也无效。

**解决措施**

将字体文件放置在工程的rawfile目录下，在H5代码中使用@font-face指定自定义字体用于显示文本。在需要应用自定义字体的元素中，配置font-family属性。

H5侧：

```
1. <!DOCTYPE html>
2. <html lang="en">
3. <head>
4. <meta charset="UTF-8"/>
5. <meta http-equiv="X-UA-Compatible" content="IE=edge"/>
6. <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
7. <title>Document</title>
8. <style>
9. @font-face {
10. font-family: 'MaoKenWangXingYuan';src: url('./MaoKenWangXingYuan.ttf');
11. }
12. #title {
13. font-family: 'MaoKenWangXingYuan';
14. }
15. </style>
16. </head>
17. <body>
18. <h1 id="title">猫啃忘形圆</h1>
19. </body>
20. </html>
```

[registerFont.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/registerFont.txt#L6-L25)
