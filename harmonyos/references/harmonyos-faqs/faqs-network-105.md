---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-105
title: 应用拉起系统浏览器时，如何指定浏览器通过Wi-Fi网络加载网页
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 应用拉起系统浏览器时，如何指定浏览器通过Wi-Fi网络加载网页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb9b495856f8c894aa93692b8af08f5d855af0dd9cd5c24e2974b746b5bbe4f9
---

## 问题现象

手机开启移动网络，并连接到Wi-Fi网络后，当三方应用拉起系统浏览器时，如何指定浏览器通过Wi-Fi网络加载网页。

## 背景知识

* 通过[connection.getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets)方法可获取所有处于连接状态的网络列表。
* 通过[Want](../harmonyos-references/js-apis-inner-ability-want.md)跳转拉起应用时，可通过parameters参数传递数据。

## 解决方案

1. 在module.json5文件中申请允许应用获取数据网络信息的权限：[ohos.permission.GET\_NETWORK\_INFO](../harmonyos-guides/permissions-for-all.md#ohospermissionget_network_info)。
2. 使用[connection.getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets)方法获取连接状态的网络列表，并使用[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)方法判断是否有Wi-Fi的netId，若存在Wi-Fi的netId，在应用拉起系统浏览器时，可通过parameters参数传递Wi-Fi网络的netId，并设置action，entities及abilityName参数，传递的uri为探测地址。

```screen
import { common, Want } from '@kit.AbilityKit';
import { connection } from '@kit.NetworkKit';

@Entry
@Component
struct NetPage {
  build() {
    RelativeContainer() {
      Button('拉起浏览器')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          middle: { anchor: '__container__', align: HorizontalAlign.Center },
          center: { anchor: '__container__', align: VerticalAlign.Center }
        })
        .onClick(() => {
          let netId = 0;
          // 获取已连接的网络列表
          let netHandle = connection.getAllNetsSync();
          netHandle.forEach(item => {
            // 判断是否为Wi-Fi网络
            if (connection.getNetCapabilitiesSync(item).bearerTypes[0] === 1) {
              netId = item.netId;
            }
          });

          try {
            let want: Want = {
              // action设置为ohos.want.action.awc或ohos.want.action.viewData
              action: 'ohos.want.action.awc',
              bundleName: 'com.huawei.hmos.browser',
              entities: ['entity.browser.hbct'],
              abilityName: 'CustomTabAbility',
              // 此处地址实际使用过程中替换为真实地址
              uri: 'xx.xx.xx',
              // 传递netId
              parameters: {
                'netId': netId
              }
            };
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            context.startAbility(want);
            console.info(`explicit start ability succeed`);
          } catch (error) {
            console.error(`explicit start ability failed with ${error.code}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 常见FAQ

Q：如何指定拉起系统浏览器时打开的网页？

A：Want对象的uri属性即要打开的网页链接。
