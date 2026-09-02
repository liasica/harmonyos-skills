---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-16
title: 参数化配置是否支持代码读取
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 参数化配置是否支持代码读取
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:efb673e0ec8a36a0fcf9ffded068106bfe8819fb5a91324ae887bf99a6882c40
---

## 问题现象

在项目级别的oh-package.json5开启了parameterFile，是否可以在代码中读取配置中的内容？

## 背景知识

OHPM客户端在1.6.0版本开始支持[参数化配置](../harmonyos-guides/ide-oh-package-json5.md#section122411462820)。可以在项目级别的oh-package.json5文件（即项目根目录下的oh-package.json5）中添加parameterFile配置，并同时指定parameterFile文件路径。

## 解决方案

实现代码读取parameterFile文件内容，可以把parameterFile.json5文件放到rawfile文件下面，然后用[getRawFileContent](../harmonyos-references/js-apis-resource-manager.md#getrawfilecontent9)读取。

```ts
import { Context } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct Index {
  private context: Context = this.getUIContext().getHostContext()!;
  private str: string = '';

  getRawFile(): ESObject {
    // 调用getRawFileContent接口获取json文件内容，并读为string
    this.context.resourceManager.getRawFileContent('parameterFile.json5', (err, data) => {
      try {
        this.str = buffer.from(data.buffer).toString();
        let obj: ESObject = JSON.parse(this.str);
        console.info('ESObject', JSON.stringify(obj));
        return obj;
      } catch (e) {
        console.error(JSON.stringify(e));
      }
    });
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

**说明** 

parameterFile.json5内容不要添加注释。

## 常见FAQ

Q：是否可以根据不同的target动态读取parameterFile文件？

A：目前不支持不同的target动态读取parameterFile文件，但可以参考[一仓多包示例](../harmonyos-guides/ide-oh-package-json5.md#section5598132714514)根据不同target配置对应参数。
