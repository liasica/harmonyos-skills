---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1016
title: 如何在EntryAbility中获取Toggle组件的值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在EntryAbility中获取Toggle组件的值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c8c356f724c7bf6af168fd1f00f9c6df039d3d1e0cb72f223443616200db39f9
---

## 问题现象

通过首选项保存Toggle组件的值，应用重新启动后Toggle的值和全局变量不一致。导致EntryAbility中无法正确获取到Toggle组件的值，该如何解决？

问题代码如下：

* EntryAbility.ets中后台时执行的操作：

  ```typescript
  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
    // 判断是否销毁应用
    if (delAppValue === true) {
      // module.json5配置文件中将removeMissionAfterTerminate字段取值配置为true
      this.context.terminateSelf();
    }
  }
  ```
* 设置页：

  ```typescript
  import { preferences } from '@kit.ArkData';
  import { PromptAction } from '@kit.ArkUI';

  export let delAppValue: boolean = false; // delAppValue初始化默认值
  let preferenceDelApp: preferences.Preferences | null = null;

  @Entry
  @Component
  struct SetPage {
    @State delApp: boolean = delAppValue;
    uiContext: UIContext = this.getUIContext();
    context: Context = this.uiContext.getHostContext() as Context;
    promptAction: PromptAction = this.uiContext.getPromptAction();

    async aboutToAppear() {
      delAppValue = await this.getPreferenceDelApp(); // 获取首选项中的值，同步到全局变量
      this.promptAction.showToast({ message: String(delAppValue) });
    }

    // 获取首选项中DelApp的值
    async getPreferenceDelApp(): Promise<boolean> {
      let value: boolean = false;
      try {
        preferenceDelApp = await preferences.getPreferences(this.context, 'DelAppID');
        value = await preferenceDelApp.get('DelAppID', delAppValue) as boolean;
      } catch (error) {
        console.error('getDelAppID Failed');
      }
      return value;
    }

    // 更新首选项中DelApp的值
    async putPreferenceDelApp(value: boolean) {
      if (preferenceDelApp !== null) {
        try {
          await preferenceDelApp.put('DelAppID', value);
          await preferenceDelApp.flush();
        } catch (error) {
          console.error('putDelAppID Failed');
        }
      }
    }

    build() {
      Column({ space: 5 }) {
        Text('自动销毁后台')
          .fontSize(18);
        Toggle({ type: ToggleType.Switch, isOn: delAppValue })
          .onChange(() => {
            delAppValue = !delAppValue;
            this.putPreferenceDelApp(delAppValue); // 保存到首选项中
            this.promptAction.showToast({ message: String(delAppValue) });
          });
      }
      .width('100%')
      .height('100%')
      .padding({ top: 20 });
    }
  }
  ```

问题现象效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/fKGmNDA9QiyylHISMbqy2w/zh-cn_image_0000002658804047.png "点击放大")

## 背景知识

* [Toggle](../harmonyos-references/ts-basic-components-toggle.md)组件提供勾选框样式、状态按钮样式和开关样式，可以通过[ToggleOptions](../harmonyos-references/ts-basic-components-toggle.md#toggleoptions18对象说明)对象设置开关值（支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量）和样式。当开关状态切换时触发[onChange](../harmonyos-references/ts-basic-components-toggle.md#onchange)事件获取开关当前状态。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在其[build](../harmonyos-references/ts-custom-component-lifecycle.md#build)函数执行前调用。允许在aboutToAppear函数中改变状态变量。
* [用户首选项](../harmonyos-references/js-apis-data-preferences.md)为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

## 问题定位

当首选项中获取到的值为true时，onBackground中得到的全局变量的值和开关显示的值不一致。

## 分析结论

开关没有使用状态变量，且组件在初始化时采用了默认值false。由于非状态变量发生改变时不会让组件刷新渲染，当首选项值为true时会出现全局变量和开关显示的值不一致的情况。

## 修改建议

1. 将全局变量delAppValue前的export去掉，改为导出的get方法获取值（如果需要外部修改可以添加set方法并导出）。保证EntryAbility文件中调用get方法可以随时获取delAppValue值。

   ```typescript
   let delAppValue: boolean = false; // delAppValue初始化默认值

   // 用于让EntryAbility文件获取delAppValue
   export function getDelAppValue() {
     return delAppValue;
   }
   ```
2. 开关中的值改为状态变量，在aboutToAppear函数中获取到首选项的值后同步修改状态变量。

   ```typescript
   async aboutToAppear() {
     delAppValue = await this.getPreferenceDelApp(); // 获取首选项中的值，同步到全局变量
     this.delApp = delAppValue; // 全局变量和开关的值保存一致
     this.promptAction.showToast({ message: String(delAppValue) });
   }
   ```
3. 当开关值发生变化时，通过Toggle组件的onChange事件获取开关当前值，同步给全局变量。让EntryAbility中通过getDelAppValue方法获取到的值和开关一致，根据true和false来判断应用是后台还是直接关闭。

   ```typescript
   Toggle({ type: ToggleType.Switch, isOn: $$this.delApp })
     .onChange((isOn: boolean) => {
       delAppValue = isOn; // 开关值发生变化时全局变量同步更新
       this.putPreferenceDelApp(delAppValue); // 保存到首选项中
       this.promptAction.showToast({ message: String(delAppValue) });
     });
   ```

   ```typescript
   onBackground(): void {
     // Ability has back to background
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
     // 判断是否销毁应用
     if (getDelAppValue() === true) {
       // module.json5配置文件中将removeMissionAfterTerminate字段取值配置为true
       this.context.terminateSelf();
     }
   }
   ```

完整代码如下：

```typescript
import { preferences } from '@kit.ArkData';
import { PromptAction } from '@kit.ArkUI';

let preferenceDelApp: preferences.Preferences | null = null;
let delAppValue: boolean = false; // delAppValue初始化默认值

// 用于让EntryAbility文件获取delAppValue
export function getDelAppValue() {
  return delAppValue;
}

@Entry
@Component
struct SetPage {
  @State delApp: boolean = false; // 开关，DelApp初始化默认值
  uiContext: UIContext = this.getUIContext();
  context: Context = this.uiContext.getHostContext() as Context;
  promptAction: PromptAction = this.uiContext.getPromptAction();

  async aboutToAppear() {
    delAppValue = await this.getPreferenceDelApp(); // 获取首选项中的值，同步到全局变量
    this.delApp = delAppValue; // 全局变量和开关的值保存一致
    this.promptAction.showToast({ message: String(delAppValue) });
  }

  // 获取首选项中DelApp的值
  async getPreferenceDelApp(): Promise<boolean> {
    let value: boolean = false;
    try {
      preferenceDelApp = await preferences.getPreferences(this.context, 'DelAppID');
      value = await preferenceDelApp.get('DelAppID', delAppValue) as boolean;
    } catch (error) {
      console.error('getDelAppID Failed');
    }
    return value;
  }

  // 更新首选项中DelApp的值
  async putPreferenceDelApp(value: boolean) {
    if (preferenceDelApp !== null) {
      try {
        await preferenceDelApp.put('DelAppID', value);
        await preferenceDelApp.flush();
      } catch (error) {
        console.error('putDelAppID Failed');
      }
    }
  }

  build() {
    Column({ space: 5 }) {
      Text('自动销毁后台')
        .fontSize(18);
      Toggle({ type: ToggleType.Switch, isOn: $$this.delApp })
        .onChange((isOn: boolean) => {
          delAppValue = isOn; // 开关值发生变化时全局变量同步更新
          this.putPreferenceDelApp(delAppValue); // 保存到首选项中
          this.promptAction.showToast({ message: String(delAppValue) });
        });
    }
    .width('100%')
    .height('100%')
    .padding({ top: 20 });
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/FGPpFZTzQ6CLaWvZ_-APKQ/zh-cn_image_0000002628404778.png "点击放大")
