---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-reactnative
title: React Native框架+H5接入智能填充
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 智能填充服务 > 三方框架+H5接入智能填充 > React Native框架+H5接入智能填充
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:01+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:423437ad8c6d4464e7d39ef462cb7742acf312b2f82a146d074ec01ccefe1b02
---

**说明** 

目前仅支持已适配HarmonyOS的三方框架应用使用。

HarmonyOS版React Native环境搭建请参考官方文档[React Native环境搭建指导](https://gitcode.com/openharmony-sig/ohos_react_native?source_module=search_result_repo)。

## 前提条件

* 设备智能填充开关必须处于打开状态，请前往“设置 > 隐私和安全 > 智能填充”页面开启开关。
* 设备已连接互联网并且登录华为账号。
* 该应用需已接入[智能填充服务](scenario-fusion-introduction-to-smart-fill.md#申请接入智能填充服务)。

## 开发准备

配置React Native已适配HarmonyOS的工程。

## React Native输入框效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/LMiUG2v3T0qMuKHUzoSgpg/zh-cn_image_0000002706675248.png)

## 示例代码

在React Native输入框TextInput需要配置[textContentType](scenario-fusion-mappingrelationship.md#react-native-textcontenttype和harmonyos的contenttype的映射关系)属性来支持智能填充，代码如下：

```tsx
import React from 'react';
import { Text, TextInput, View, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  default: {
    borderWidth: StyleSheet.hairlineWidth,
    borderColor: '#0f0f0f',
    flex: 1,
    fontSize: 13,
    padding: 4,
    height: 80,
    width: 160,
  },
  labelContainer: {
    flexDirection: 'row',
    marginVertical: 2,
  },
  label: {
    width: 140,
    textAlign: 'right',
    marginRight: 10,
    paddingTop: 2,
    fontSize: 15,
  },
  inputContainer: {
    flex: 1,
  }
});
class WithLabel extends React.Component<$FlowFixMeProps> {
  render(): React.Node {
    return (
      <View style={styles.labelContainer}>
        <Text style={styles.label}>{this.props.label}</Text>
        <View style={styles.inputContainer}>{this.props.children}</View>
      </View>
    );
  }
}
const RNTesterApp = () : React.ReactNode=> {
  return (
    <View style={{width: '100%', height: '100%', paddingTop: 40}}>
      <WithLabel label="昵称">
        <TextInput textContentType="nickname" style={styles.default} />
      </WithLabel>
      <WithLabel label="姓名">
        <TextInput textContentType="name" style={styles.default} />
      </WithLabel>
      <WithLabel label="手机号">
        <TextInput textContentType="telephoneNumber" style={styles.default} />
      </WithLabel>
      <WithLabel label="邮件">
        <TextInput textContentType="emailAddress" style={styles.default} />
      </WithLabel>
      <WithLabel label="身份证号">
        <TextInput textContentType="idCardNumber" style={styles.default} />
      </WithLabel>
      <WithLabel label="全部地址">
        <TextInput textContentType="formatAddress" style={styles.default} />
      </WithLabel>
      <WithLabel label="带街道的详细地址">
        <TextInput textContentType="fullStreetAddress" style={styles.default}  />
      </WithLabel>
      <WithLabel label="不带街道的详细地址">
        <TextInput textContentType="detailInfoWithoutStreet" style={styles.default} />
      </WithLabel>
    </View>
  );
};
export default RNTesterApp;
```

## React Native框架中加载的H5页面效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nXHeF3unQ3yJ5NiwSy5HYw/zh-cn_image_0000002736434337.png)

React Native框架加载H5页面场景，通过给form表单的input输入框（form表单的子节点）配置[autocomplete](scenario-fusion-mappingrelationship.md#h5-autocomplete和harmonyos的contenttype的映射关系)属性来支持智能填充，代码如下：

```tsx
import React,{ useEffect } from 'react';
import { View } from 'react-native';
import { WebView } from 'react-native-webview';
// ...

const RNTesterAppH5 = () : React.ReactNode => {
// ...

  return (
// ...
      <View style={{width: '100%', height: '100%', paddingTop: 40}}>
        <WebView
          source={require('./autofill_h5.html')}
          style={{flex: 1, paddingTop: 50}}
        />
      </View>
// ...
  );
};

export default RNTesterAppH5;
```

autofill\_h5.html实现参考[示例代码二](scenario-fusion-h5.md#示例代码二)。
