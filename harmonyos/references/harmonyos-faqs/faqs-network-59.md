---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-59
title: 如何将Axios获取GBK格式的网络数据转换UTF-8格式
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何将Axios获取GBK格式的网络数据转换UTF-8格式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d2e70b9d3493bdffd8156fe5f0f5097800a90f72071fb3500b0faa25e7bfdef9
---

通过[@ohos.util (util工具函数)](../harmonyos-references/js-apis-util.md)实现GBK转换UTF-8格式，实现思路如下：

1. 引入axios和util。

2. 使用axios获取网络数据，并将数据类型设置为ARRAY\_BUFFER。

3. 使用util.TextDecoder方法进行解码。

4. 将解码后的数据通过LazyForEach循环显示在列表中。

参考代码如下：

```
1. import { util } from '@kit.ArkTS';
2. import axios, { AxiosResponse } from '@ohos/axios';

4. const URL: string = 'xxx';

6. @Entry
7. @Component
8. struct FriendsBook {

10. build() {
11. }

13. aboutToAppear() {
14. axios<string, AxiosResponse<string>, null>({
15. method: 'get',
16. url: URL,
17. // When using the util.TextDecoder method, the encoding and decoding formats must be consistent,
18. // so the data type needs to be set to ARRAY_BUFFER when retrieving, otherwise garbled characters will appear.
19. responseType: 'ARRAY_BUFFER'
20. })
21. .then((res: AxiosResponse) => {
22. // First, use create to construct a TextDecoder instance and set the encoding format to gbk.
23. const textDecoder = util.TextDecoder.create('gbk', { ignoreBOM: true });
24. // Next, use the decodeWithStream method to decode the input parameters and output the corresponding UTF-8 formatted text string.
25. // The parameters passed in must be in Uint8Array format, so the obtained data needs to be converted to an array type using the Uint8Array method.
26. const result = new Uint8Array(res.data);
27. const resultString = textDecoder.decodeToString(result, { stream: false });
28. // Parse JSON strings.
29. const jsonResult = JSON.parse(resultString) as string;
30. })
31. }
32. }
```

[GetAxiosUTF.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/GetAxiosUTF.ets#L21-L52)
