---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-230
title: Component如何监听应用前后台切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Component如何监听应用前后台切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eff0629a9ab4ecf41487549c0d460b75fbebef8fc1bc20fc33a53e70d4694103
---

应用的前后台生命周期与页面和组件无关，组件仅能感知aboutToAppear和aboutToDisappear事件。若组件需要感知应用的前后台切换，可以使用[ApplicationContext.on('applicationStateChange')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)注册对当前应用前后台状态变化的监听。也可以设置一个应用前后台状态的变量。在UIAbility中对应的生命周期函数中更改此变量，并在组件中监听AppStorage状态变量的变化，执行相应的逻辑。

参考代码如下：

```ts
// EntryAbility中
export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    AppStorage.setOrCreate<boolean>('isOnForeground', undefined);
  }

  onForeground(): void {
    AppStorage.set<boolean>('isOnForeground', true);
  }

  onBackground(): void {
    AppStorage.set<boolean>('isOnForeground', false);
  }
}
```

```typescript
@Entry
@Component
struct ComponentListenFrontAndBack {
  @State message: string = 'Hello World';
  @StorageLink('isOnForeground') isOnForeground: boolean = true;

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        ForegroundAwareComponent({ isOnForeground: this.isOnForeground })
      }
      .width('100%')
    }
    .height('100%')
  }
}

@Component
struct ForegroundAwareComponent {
  @Watch('change') @Link isOnForeground: boolean;
  @State message: string = 'video';

  build() {
    Text('message')
      .fontSize(50)
      .fontWeight(FontWeight.Bold)
      .onClick(() => {
        this.message += this.isOnForeground;
        console.info('' + this.isOnForeground);
      })
  }

  change() {
    if (this.isOnForeground) {
      console.info('The component is on foreground.');
    } else {
      console.info('The component is on background.');
    }
  }
}
```
