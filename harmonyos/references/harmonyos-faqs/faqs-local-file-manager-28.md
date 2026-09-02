---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-28
title: 如何从一个二进制文件中读取其字节数组？通过fs.createStreamSync只能获取到ArrayBuffer，如何转成number[]
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何从一个二进制文件中读取其字节数组？通过fs.createStreamSync只能获取到ArrayBuffer，如何转成number[]
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fbe54207f47c706e57299c4335d2a3ecbfc23b8bf6591ace2d1d96811b7ecb9f
---

```ts
@Component
export struct ArrayBufferConversionArray {
  @State fileLength: number = 10;
  private tempData: number[] = [];

  aboutToAppear(): void {
    // Convert ArrayBuffer to a number array
    let arrayBuffer: ArrayBuffer = new ArrayBuffer(this.fileLength);
    let dataView: DataView = new DataView(arrayBuffer);
    for (let index = 0; index < this.fileLength; index++) {
      this.tempData[index] = dataView.getInt8(index);
    }
    console.info(this.tempData.toString());
  }

  build() {
    RelativeContainer() {
      Text(this.tempData.toString())
        .id('ArrayBufferHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
