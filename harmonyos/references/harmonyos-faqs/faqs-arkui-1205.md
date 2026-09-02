---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1205
title: 适老化适配问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 适老化适配问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:188941aa308bc99a5e0a3c857f2f74a25bdb7ff63dfdfc2d02df5a2bab46516b
---

## 问题现象

在实现适老化功能时，有以下经典场景：

* 场景一：标准字体大小为24px，放大六档后，字体大小是多少，是按照倍数去放大吗？
* 场景二：关怀模式调整放大倍率后，应用内组件未放大，该如何修改？
* 场景三：如何实现在系统不设置适老化场景情况下，应用内自实现适老化，只开启应用内适老化场景时，只有应用内进行统一放大显示，不影响系统和其他应用？
* 场景四：TextArea的滚动条能否隐藏？
* 场景五：在实现主题切换和适老化模式切换能力的过程中，针对每个UI组件做配置时，无法实现切换状态后实时更新UI组件的样式配置，有无简便方式实现？

## 背景知识

* [setCustomDensity](../harmonyos-references/arkts-apis-window-windowstage.md#setcustomdensity20)：支持应用主窗口自定义显示大小缩放系数，并设置已创建的子窗和系统窗口跟随主窗重新布局的生效时机。当存在同时使用该接口和[setDefaultDensityEnabled(true)](../harmonyos-references/arkts-apis-window-windowstage.md#setdefaultdensityenabled12)的情况时，以最后调用的设置效果为准。
* [BarState](../harmonyos-references/ts-appendix-enums.md#barstate)：用于设置滚动条的状态。
* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)：多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [maxFontScale](../harmonyos-references/ts-basic-components-textarea.md#maxfontscale18)：设置文本最大的字体缩放倍数。

## 解决方案

* 场景一：标准字体大小为24px，放大六档后的字体大小是放大3.2倍也就是24px \* 3.2 ≈ 76.8px，系统字体被放大后，有界面布局异常的风险，为了确保应用整体布局不出现错乱，组件不出现重叠，在适老化指南中推荐根据业务需要，限制跟随字体最大档位、改变布局来更好的适配更大字体。详情请参考官网：[支持适老化](../harmonyos-guides/arkui-support-for-aging-adaptation.md)。
* 场景二：在app.json5中添加配置项configuration，并在base文件目录下新增profile文件夹，并在此目录下新增configuration.json文件。具体可参考[应用适配适老化大字体](../harmonyos-guides/arkui-support-for-aging-adaptation.md#应用适配适老化大字体)。
* 场景三：请参考官方文档接口[setCustomDensity](../harmonyos-references/arkts-apis-window-windowstage.md#setcustomdensity20)，支持应用主窗口自定义显示大小缩放系数，并设置已创建的子窗和系统窗口跟随主窗重新布局的生效时机。
* 场景四：TextArea中的[BarState](../harmonyos-references/ts-appendix-enums.md#barstate)可以设置输入框滚动条的显示模式。
* 场景五：做两套UI样式，结合首选项去记录当前是正常模式还是长者模式，根据需要切换对应的UI样式。使用Toggle控件开启、关闭“大字号模式”，并使用dataPreferences持久化用户的设置。请参考如下示例代码：

```ts
import dataPreferences from '@ohos.data.preferences';

let preferences: dataPreferences.Preferences | null = null;
let options: dataPreferences.Options = { name: 'myStore' };

@Entry
@Component
struct AgeFriendly {
  // 获取当前组件的上下文（用于访问数据存储等系统服务）
  context: Context | undefined = this.getUIContext().getHostContext();
  @State isOn: boolean = false;
  @State customSize: string = '18vp';

  // 生命周期钩子：在组件即将显示前执行（通常用于初始化数据）
  aboutToAppear(): void {
    preferences = dataPreferences.getPreferencesSync(this.context, options);
    if (!preferences) {
      return;
    }
    // 从本地存储中读取 'customSize' 的值，若不存在则使用默认值 '18vp'
    let customSize = preferences.getSync('customSize', '18vp');
    let isOn = preferences.getSync('isOn', 'false');
    console.info('The size value is' + customSize + '| isOn: ' + isOn);
    this.isOn = JSON.parse(isOn as string);
    this.customSize = customSize.toString();
  }

  build() {
    Column() {
      Text('点击按钮切换长者模式')
        .fontSize(this.customSize)
        .fontColor(Color.Black);

      Row() {
        // Toggle 开关控件：用于开启/关闭长者模式
        Toggle({
          type: ToggleType.Switch, // type: Switch 表示显示为滑动开关样式
          isOn: this.isOn // isOn: 绑定响应式状态变量，开关状态实时同步
        })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            // 当开关状态改变时触发的回调函数
            this.isOn = isOn; // 更新本地状态变量
            this.customSize = isOn ? '28vp' : '18vp'; // 根据状态切换字体大小
            if (!preferences) {
              return;
            }
            // 根据开关状态写入新的字体大小值
            if (isOn) {
              preferences.putSync('customSize', '28vp');
              preferences.putSync('isOn', 'true');
            } else {
              preferences.putSync('customSize', '18vp');
              preferences.putSync('isOn', 'false');
            }
            // 强制将所有未写入的数据立即刷新到磁盘（确保持久化生效）
            preferences.flush();
          });
      };
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
