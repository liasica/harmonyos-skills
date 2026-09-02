---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-27
title: 如何使用代码设置和连接Wi-Fi热点
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何使用代码设置和连接Wi-Fi热点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e4bb10a1e6dbcbe49b21a5051b6f690d243f191c49f6849039224f657650e81
---

## 问题现象

* 问题一：如何在代码中设置并开启自定义名称和密码的Wi-Fi热点？
* 问题二：如何通过代码搜索到Wi-Fi列表，连接上指定的Wi-Fi？

## 解决方案

* **问题一**：除系统应用外，其他应用不支持通过代码开启自定义名称和密码的Wi-Fi热点，可在应用中跳转至系统设置页来开启热点。

  ```screen
  import { common, Want } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    build() {
      Column() {
        Button('Go to Settings')
          .margin({ top: 300 })
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let want: Want = {
              bundleName: 'com.huawei.hmos.settings',
              abilityName: 'com.huawei.hmos.settings.MainAbility',
              uri: 'hotspot_data_settings',
              parameters: {
                // 传对应应用的包名
                pushParams: 'com.example.myapplication'
              }
            };
            context.startAbility(want);
          })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
* **问题二**：可以使用接口[wifiManager.getCandidateConfigs](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetcandidateconfigs)获取候选网络配置，再使用接口[wifiManager.connectToCandidateConfig](../harmonyos-references/js-apis-wifimanager.md#wifimanagerconnecttocandidateconfig)连接到自己添加的候选网络即可。
