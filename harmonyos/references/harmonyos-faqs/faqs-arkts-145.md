---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-145
title: 如何在Index.ets中导出默认导出的对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在Index.ets中导出默认导出的对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7bbf2ef8526d5b9d105a5ed21ba7136de10a13d4ab1b171d1814e4578c4afe3b
---

**问题现象**

```
1. // src/main/ets/api/AppInterfaces.ets
2. import { DemoService } from "../service/DemoService";
3. class AppInterfaces {
4. demoService?: DemoService;
5. }
6. export default new AppInterfaces() as AppInterfaces;
7. // Index.ets
8. export AppInterfaces from './src/main/ets/api/AppInterfaces';
```

报错提示：Cannot find name 'AppInterfaces'. <ArkTSCheck>

**解决措施**

```
1. import { DemoService } from "../service/DemoService";
2. class AppInterfaces {
3. demoService?: DemoService;
4. }
5. let test = new AppInterfaces()
6. export default test;
```

[ExportDefaultObjects.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ExportDefaultObjects.ets#L5-L10)
