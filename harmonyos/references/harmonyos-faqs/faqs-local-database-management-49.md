---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-49
title: 应用每次登录都需要确认隐私协议
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 应用每次登录都需要确认隐私协议
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3940b27d67fa2ad4c6bad51e7fcd884b85afef483ebda3738280a4a7f2be52ef
---

## 问题现象

应用每次登录都需要确认隐私协议，而不是在首次登录时接受隐私协议后，后续登录时会记住选择且不会弹窗。

## 背景知识

通过用户首选项实现[数据持久化](../harmonyos-guides/data-persistence-by-preferences.md)：用户首选项（Preferences）为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。当用户有轻量级的键值型数据需要存储时，可以采用Preferences来进行存储。一般适用于保存用户的个性化设置，例如字体大小、是否开启夜间模式等。

## 问题定位

查看登录页面中用于保存“是否接受隐私协议”的状态变量是否实现了持久化。若此状态变量并未持久化，每次触发组件相关生命周期时，该变量均重新初始化，而不会记住用户的上一次选择结果。

## 分析结论

应用并未对相关的状态变量进行数据持久化，导致每次登录时，记录“是否接受隐私协议”的状态变量重新初始化，因此需要重新确认隐私协议。

## 修改建议

建议应用使用[用户首选项](../harmonyos-references/js-apis-data-preferences.md)持久化保存记录“是否接受隐私协议”的状态变量这种轻量级数据，当用户在首次登录时，记住用户的选择，在后续的登录动作中，不必再重新确认。相关示例代码如下。

```screen
import preferences from '@ohos.data.preferences';
import { PromptAction, UIContext } from '@kit.ArkUI';

const PREFERENCES_NAME = 'theme.db';
const AGREED_KEY = 'privacy_agreed';
// 全局Preferences对象
let preferencesDB: preferences.Preferences;

@Entry
@Component
struct AlertDialogExample {
  @State private isAgreed: string = '';
  uiContext: UIContext = this.getUIContext();
  promptAction: PromptAction = this.uiContext.getPromptAction();

  async aboutToAppear() {
    await this.getPreferencesFromStorage();
    this.isAgreed = preferencesDB.getSync(AGREED_KEY, 'default') as string;
  }

  async getPreferencesFromStorage() {
    let context = this.getUIContext().getHostContext() as Context;
    preferencesDB = await preferences.getPreferences(context, PREFERENCES_NAME);
  }

  build() {
    Column({ space: 5 }) {
      Button('登录')
        .onClick(() => {
          if (this.isAgreed === '是') {
            // 登录成功
            this.startMainPage();
          } else {
            // 弹出隐私政策弹窗
            this.getUIContext().showAlertDialog(
              {
                title: '隐私政策',
                subtitle: '',
                message: '我们尊重您的隐私，本应用会收集必要信息以提供服务，请您阅读并同意隐私政策。',
                autoCancel: true,
                alignment: DialogAlignment.Bottom,
                gridCount: 4,
                offset: { dx: 0, dy: -20 },
                primaryButton: {
                  value: '拒绝',
                  action: () => {
                    preferencesDB.putSync('privacy_agreed', '否');
                    preferencesDB.flush();
                    this.getUIContext().getPromptAction().showToast({
                      message: '您必须接受隐私条款才能进入应用',
                      duration: 2000,
                    });
                  }
                },
                secondaryButton: {
                  enabled: true,
                  defaultFocus: true,
                  style: DialogButtonStyle.HIGHLIGHT,
                  value: '同意',
                  action: () => {
                    preferencesDB.putSync('privacy_agreed', '是');
                    preferencesDB.flush();
                    this.startMainPage();
                  }
                }
              }
            );
          }
        }).backgroundColor(0x317aff)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  startMainPage() {
    // 这里使用即时弹窗表示登录成功
    this.promptAction.openToast({
      message: '登录成功',
      duration: 5000,
    });
  }
}
```
