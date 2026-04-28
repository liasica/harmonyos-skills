---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95
title: ArkTS是否支持多继承
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持多继承
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:95277926923703e2cf5618d6aec8016b0532e20dc42720fd1cae817771850352
---

接口支持多继承，类仅支持单继承。示例如下：

```
1. class TestClassA {
2. address: string = '';
3. }

5. class TestClassB {
6. name: string = '';
7. }

9. // report errors：Classes can only extend a single class.
10. // class TestClassC extends TestClassA, TestClassB {
11. // }

13. interface AreaSize {
14. calculateAreaSize(): number;
15. }

17. interface Cal {
18. Sub(a: number, b: number): number;
19. }

21. interface Area extends AreaSize, Cal {
22. areaName: string;
23. length: number;
24. width: number;
25. }
```

[AreaSize.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/AreaSize.ets#L21-L45)
