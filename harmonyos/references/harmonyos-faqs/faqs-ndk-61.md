---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-61
title: 传入自定义类型对象到Native侧时，index.d.ts文件如何声明
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 传入自定义类型对象到Native侧时，index.d.ts文件如何声明
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:40+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:d6045ff11556a2cddb7c124dfa034f5cc4af95470fff7d22f2138122bd26f25c
---

此处以testCb为例

```
1. class testCb {
2. testNum: number = 0;
3. testString: string = "";
4. }
```

[CustomObject.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/CustomObject.ets#L21-L24)

方法一：

在index.d.ts文件中使用object类型进行声明。

```
1. export const modifyObject: (a: object) => object;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/types/libentry/Index.d.ts#L47-L47)

方法二：

创建xx.ts文件，并在该文件中导出类。然后在index.d.ts文件中导入并使用该类。

test.ts 导出类声明。

```
1. export class testCa {
2. testNum: number = 0;
3. testString: string = "";
4. }
```

[CustomObject.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/ets/pages/interface/CustomObject.ts#L19-L22)

在index.d.ts中导入并使用。

```
1. import { testCa } from "../../../ets/pages/interface/CustomObject"
2. export const test1: (a: testCa) => void;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/entry/src/main/cpp/types/libentry/Index.d.ts#L37-L38)
