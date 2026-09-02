---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-58
title: 首选项保存数据时报错：Cannot read property putSync of undefined
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 首选项保存数据时报错：Cannot read property putSync of undefined
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ee25857e92c4f4e7a28b32262905fc0f4f79e2547d85d85007b97340f1f979df
---

## 问题现象

运行问题代码后闪退，日志如下：

```screen
Pid:8619
Uid:20020045
Reason:TypeError
Error name:TypeError
Error message:Cannot read property putSync of undefined
Stacktrace:
  at saveData (entry/src/main/ets/pages/Index.ets:71:5)
  at anonymous (entry/src/main/ets/pages/Index.ets:41:11)
```

问题代码示例参考如下：

```ts
// index.ets

import Prompt from '@system.prompt';
import { UIAbility } from '@kit.AbilityKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
import preferences from '@ohos.data.preferences';

let dataPreferences:preferences.Preferences
class EntryAbility extends UIAbility{
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    dataPreferences = preferences.getPreferencesSync(this.context, options);
  }
}
@Entry
@Component
struct Index {
  @State inputText: string = '';
  @State savedText: string = '这里将显示保存的内容';

  build() {
    Column() {
      // 输入框
      TextInput({ placeholder: '请输入要保存的内容' })
        .width('90%')
        .height(60)
        .onChange((value: string) => {
          this.inputText = value;
        })

      // 保存按钮
      Button('保存数据')
        .width('90%')
        .height(60)
        .margin({ top: 20 })
        .onClick(() => {
          this.saveData();
        })

      // 显示保存内容的按钮
      Button('显示保存内容')
        .width('90%')
        .height(60)
        .margin({ top: 20 })
        .onClick(() => {
          this.loadData();
        })

      // 显示保存内容的文本区域
      Text(this.savedText)
        .width('90%')
        .margin({ top: 20 })
        .fontSize(20)
        .textAlign(TextAlign.Center)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 保存数据到Preferences
  private saveData() {
    if(this.inputText == null){
      Prompt.showToast({message: '内容为空请重试'})
      return
    }
    dataPreferences.putSync('my',this.inputText);
    dataPreferences.flush()
  }

  // 从Preferences加载数据
  private loadData() {
    let get_text = dataPreferences.getSync('my','6666')
    this.savedText = get_text.toString()
  }
}
```

## 背景知识

* [通过用户首选项实现数据持久化](../harmonyos-guides/data-persistence-by-preferences.md)：用户首选项(Preferences)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。
* 首选项实例可见[demo](https://gitee.com/harmonyos_samples/preferences)。

## 问题定位

1. 根据报错信息‘Cannot read property putSync of undefined’和报错代码行‘at saveData (entry/src/main/ets/pages/Index.ets:71:5)’，可定位至saveData()方法中的putSync属性未找到。
2. putSync是dataPreferences的方法，dataPreferences的实例化是在class文件entryAbility进行调用的。检查代码后发现主程序没有关于entryAbility的调用链，即dataPreferences未实例化。

## 分析结论

dataPreferences未实例化导致报错。

## 修改建议

在主程序中添加异步方法aboutToAppear()方法，并在里面进行Preferences实例化：

```ts
import { promptAction } from '@kit.ArkUI';
import preferences from '@ohos.data.preferences';

let dataPreferences:preferences.Preferences;

@Entry
@Component
struct Index {
  @State inputText: string = '';
  @State savedText: string = '这里将显示保存的内容';

  async aboutToAppear() {
    let context = this.getUIContext().getHostContext() as Context;
    let options: preferences.Options = { name: 'myStore' };
    dataPreferences = preferences.getPreferencesSync(context, options);
  }

  build() {
    Column() {
      // 输入框
      TextInput({ placeholder: '请输入要保存的内容' })
        .width('90%')
        .height(60)
        .onChange((value: string) => {
          this.inputText = value;
        })

      // 保存按钮
      Button('保存数据')
        .width('90%')
        .height(60)
        .margin({ top: 20 })
        .onClick(() => {
          this.saveData();
        })

      // 显示保存内容的按钮
      Button('显示保存内容')
        .width('90%')
        .height(60)
        .margin({ top: 20 })
        .onClick(() => {
          this.loadData();
        })

      // 显示保存内容的文本区域
      Text(this.savedText)
        .width('90%')
        .margin({ top: 20 })
        .fontSize(20)
        .textAlign(TextAlign.Center)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 保存数据到Preferences
  private saveData() {
    if (this.inputText == null) {
      promptAction.openToast({ message: '内容为空请重试' });
      return;
    }
    dataPreferences.putSync('my', this.inputText);
    dataPreferences.flush();
  }

  // 从Preferences加载数据
  private loadData() {
    let get_text = dataPreferences.getSync('my', '6666');
    this.savedText = get_text.toString();
  }
}
```

## 常见FAQ

Q：dataPreferences存储后的文件路径在哪里？

A：dataPreferences实际上是一个xml文件，位置放在data/app/el2/100/base/<包名>/haps/entry/preferences目录下。可以在IDE右下角，点击Device File Browser，找到文件路径。
