---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-307
title: 如何查看触摸热区范围
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何查看触摸热区范围
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:58fa849097e46cea8affc884c77cc33a7d412db04529fe53964e4e390d9d0c89
---

通过自定义方式设置responseRegion属性值，参考代码如下：

```
1. @Entry
2. @Component
3. struct TouchTargetExample {
4. @State text: string = '';
5. @State x: number = 0;
6. @State y: number = 0;
7. @State regWidth: string = '50%';
8. @State regHeight: string = '100%';

10. build() {
11. Column({ space: 20 }) {
12. Text(`{x:0,y:0,width:'50%',height:'100%'}`)
13. // The width of the hot zone is half of the button, and there is no response when clicking on the right side
14. Button('button1')
15. .responseRegion({
16. x: this.x,
17. y: this.y,
18. width: this.regWidth,
19. height: this.regHeight
20. })
21. .onClick(() => {
22. this.text = 'button1 clicked';
23. console.info('button1 clicked: ' + this.x + ' ' + this.y + ' ' + this.regWidth + ' ' + this.regHeight);
24. })

26. Text(this.text)
27. .margin({ top: 10 })
28. }
29. .width('100%')
30. .margin({ top: 100 })
31. }
32. }
```

[ViewRangeOfTouchHotspots.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ViewRangeOfTouchHotspots.ets#L21-L53)

**参考链接**

[responseRegion](../harmonyos-references/ts-universal-attributes-touch-target.md#responseregion)
