---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-58
title: 在建立好TCPSocket之后，如何将复合类型结构转换为ArrayBuffer
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 在建立好TCPSocket之后，如何将复合类型结构转换为ArrayBuffer
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b61c7dddb2a031d4eb629640014e83d61a529d9e3ea9dff7a2f661d6ba038f70
---

可将复合类型结构转换为字符串后使用如下方法转为ArrayBuffer，参考代码如下：

```typescript
interface ObjData {
  A1: string,
  B1: number,
  C1: ObjData2
}
interface ObjData2 {
  key1: string,
  key2: string
}

@Entry
@Component
export  struct ObjectToArrayBuffer {
  @State message: string = 'Object转ArrayBuffer';

  strToArrayBuffer(str: string) {
    let buf = new ArrayBuffer(str.length * 2);
    let bufView = new Uint16Array(buf);
    for (let i = 0,  strLen = str.length; i < strLen; i++) {
      bufView[i] = str.charCodeAt(i);
    }
    return bufView;
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let objData: ObjData = {
              A1:'字符串',
              B1: 1,
              C1:{'key1':'FF','key2':'GG'}
            }
            let buf1 = this.strToArrayBuffer(JSON.stringify(objData));
            console.info(`buf1: ${JSON.stringify(buf1 )}`);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
