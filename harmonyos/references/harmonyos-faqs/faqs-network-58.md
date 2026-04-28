---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-58
title: 在建立好TCPSocket之后，如何将复合类型结构转换为ArrayBuffer
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 在建立好TCPSocket之后，如何将复合类型结构转换为ArrayBuffer
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:17d4df0436274753d31a5a1779aafe6932488254fcdc435fd1020a573f55de80
---

可将复合类型结构转换为字符串后使用如下方法转为ArrayBuffer，参考代码如下：

```
1. interface ObjData {
2. A1: string,
3. B1: number,
4. C1: ObjData2
5. }
6. interface ObjData2 {
7. key1: string,
8. key2: string
9. }

11. @Entry
12. @Component
13. export  struct ObjectToArrayBuffer {
14. @State message: string = 'Object转ArrayBuffer';

16. strToArrayBuffer(str: string) {
17. let buf = new ArrayBuffer(str.length * 2);
18. let bufView = new Uint16Array(buf);
19. for (let i = 0,  strLen = str.length; i < strLen; i++) {
20. bufView[i] = str.charCodeAt(i);
21. }
22. return bufView;
23. }

25. build() {
26. Row() {
27. Column() {
28. Text(this.message)
29. .fontSize(50)
30. .fontWeight(FontWeight.Bold)
31. .onClick(() => {
32. let objData: ObjData = {
33. A1:'字符串',
34. B1: 1,
35. C1:{'key1':'FF','key2':'GG'}
36. }
37. let buf1 = this.strToArrayBuffer(JSON.stringify(objData));
38. console.info(`buf1: ${JSON.stringify(buf1 )}`);
39. })
40. }
41. .width('100%')
42. }
43. .height('100%')
44. }
45. }
```

[SetTcpSocket.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/SetTcpSocket.ets#L21-L65)
