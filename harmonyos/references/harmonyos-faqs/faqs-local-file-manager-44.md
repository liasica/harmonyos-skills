---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-44
title: 如何读取指定文件内容，并转为具体对象
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何读取指定文件内容，并转为具体对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:99f7246b4849f9a186531791bf4c8b203d1f38c0d3a34b695785f5f775d81e07
---

可以使用[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)方法，参考代码如下：

```ts
import { Context } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private context: Context | undefined = this.getUIContext().getHostContext();
  private str: string = '';

  getRawFile(): ESObject {
    //Call the getRawFileContent interface to retrieve the content of a JSON file and read it as a string
    this.getUIContext().getHostContext()!.resourceManager.getRawFileContent('test.json', (err, data) => {
      try {
        this.str = buffer.from(data.buffer).toString();
        console.info(JSON.stringify(this.str));
      } catch (e) {
        console.info(JSON.stringify(e));
      }
    })
    //You can also call the getRawFileContentSync interface to retrieve the content of the JSON file and read it as a string
    try {
      let data: Uint8Array = this.context!.resourceManager.getRawFileContentSync('test.json');
      this.str = buffer.from(data.buffer).toString();
    } catch (e) {
      console.info(JSON.stringify(e));
    }
    // Convert string to ESObject
    let obj: ESObject = JSON.parse(this.str);
    console.info('ESObject', JSON.stringify(obj));
    return obj;
  }

  build() {
    Column() {
      Button('get')
        .onClick(() => {
          this.getRawFile();
        })
    }.width('100%')
  }
}
```
