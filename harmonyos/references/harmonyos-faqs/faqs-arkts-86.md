---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-86
title: 如何将Map转换为JSON字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将Map转换为JSON字符串
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:781c6bd544c65685f0f7878a23f9cc62e83b3548b8bb0062f76cdef9c158540d
---

将Map转换为Record后，再通过JSON.stringify()方法转换为JSON字符串。示例如下：

```
1. let mapSource = new Map<string, string>();
2. mapSource.set('name', 'name1');
3. mapSource.set('width', '100');
4. mapSource.set('height', '50');

6. let jsonObject: Record<string, Object> = {};
7. mapSource.forEach((value, key) => {
8. if (key !== undefined && value !== undefined) {
9. jsonObject[key] = value;
10. }
11. })
12. let jsonInfo: string = JSON.stringify(jsonObject);

14. @Entry
15. @Component
16. struct Index {
17. build() {
18. Column() {
19. Button('Map to JSON')
20. .onClick(() => {
21. console.log('jsonInfo:', jsonInfo); // jsonInfo: {"name":"name1","width":"100","height":"50"}
22. })
23. }
24. }
25. }
```

[MapSource.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/MapSource.ets#L21-L45)
